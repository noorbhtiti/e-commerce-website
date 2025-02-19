# TODO:
# 1. fixa att t.ex adress inte kan bli null, då det inte funkar att lägga in null i orders.adress
# 2. fixa att man inte kan ha chars i telefon nummer då det inte funkar att lägga in str i orders.phone
# 3.


from flask import *
import MySQLdb.cursors
from HelpMethods import *
from flask_mysqldb import MySQL
import time

# DATABASE BLOCK START#
app = Flask(__name__)
mysql = MySQL(app)
# DATABASE BLOCK ENDS#
#
#
#
#
PlaceOrderPage = Blueprint('PlaceOrderPage', __name__, static_folder='static', template_folder='templates')


@PlaceOrderPage.route('/Check-out', methods=["GET", "POST"])
def checkOut():
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    message = ""
    counter = 0
    price = 0
    shippingCost = 0
    adressNotBlank = False

    if logged:
        counter = count(getUserid(session['email']))
    else:
        return "<h1>Du är inte inloggad!</h1>"
    if request.method == "POST":
        if logged:
            # gör en if request.methods==post här innan man kör allting!
            userid = getUserid(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Cart WHERE UserID = %s', (userid,))
            prods = cursor.fetchall()
            price = 0
            for x in prods:  # räkna pris
                cursor.execute('SELECT * FROM Products WHERE ProductID= %s ', (x['ProductsID'],))
                getprodsviaip = cursor.fetchall()
                price += getprodsviaip[0]['ProductPrice']

            if price > 0:
                price += 25

            if prods:  # om det finns produkter
                # skapa en Order

                # kolla om ändrat i form
                userid = getUserid(session['email'])
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM Users WHERE UserID = %s', (userid,))
                user = cursor.fetchone()
                firstName = user['FirstName']
                lastName = user['LastName']
                phoneNumber = user['PhoneNumber']
                email = user['Email']
                adress = user['Adress']
                print(adress)

                lista = [firstName, lastName, email, phoneNumber, adress]
                i = 0
                for key, value in request.form.items():
                    if request.form[key] != "":
                        lista[i] = value
                    i += 1

                outOfStock = []

                cursor.execute('START TRANSACTION;')
                mysql.connection.commit()
                try:
                    ##########################################################################################
                    ##########################################################################################
                    # Hitta nästa auto_increment på OrderID
                    #cursor.execute(
                    #    'SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE (TABLE_NAME = "Orders");')
                    #nextID = cursor.fetchone()

                    # Skapa en ny Order

                    cursor.execute(
                        'INSERT INTO `Orders`(`UserID`, `Amount`, `OrderStatus`,`FirstName`, `LastName`,`ShippingAdress`, `OrderPhoneNumber`, `OrderEmail`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
                        (userid, price, "Processing Order", lista[0], lista[1], lista[4], lista[3], lista[2],))

                    # Hitta nästa auto_increment på OrderID
                    nextID = cursor.lastrowid
                    print(nextID)
                    print("################################################")
                    for x in prods:  # kopiera över allt från cart till orderdetails
                        cursor.execute('SELECT * FROM Products WHERE ProductID= %s ', (x['ProductsID'],))
                        a = cursor.fetchone()
                        if int(a['NumberInStock']) >= x['Amount']:
                            cursor.execute('UPDATE Products SET NumberInStock=%s WHERE ProductID= %s ',
                                            (int(a['NumberInStock']) - (int(x['Amount'])), x['ProductsID'],))
                        else:
                            if a not in outOfStock:
                                outOfStock.append(a)
                        cursor.execute(
                            'INSERT INTO `OrderDetails`( `OrderID`, `ProductID`,`BuyingPrice` ,`Amount`) VALUES (%s,%s,%s,%s)',
                            (nextID, x['ProductsID'], a['ProductPrice'], 1,))
                        cursor.execute('DELETE FROM Cart WHERE UserID =%s and ProductsID = %s',
                                        (userid, x['ProductsID'],))
                        #raise
                    if len(outOfStock) == 0:
                        mysql.connection.commit()
                    else:
                        message = "Den/Dessa varor har vi ont om i lagret: "
                        for i, x in enumerate(outOfStock):
                            if i == 0 and len(outOfStock) > 1:
                                message += x['ProductName']
                                message += " och "
                            else:
                                message += x['ProductName']
                        session['orderMsg'] = message

                    url = "/place-order." + str(nextID)
                    return redirect(url, code=302)
                except:
                    flash("Något fel hände :( Testa gärna igen!")
                    mysql.connection.rollback()
                finally:
                    cursor.close()
            else:
                return "<h1>Din cart är tom</h1>"

    if logged and counter > 0:
        userid = getUserid(session['email'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE UserID = %s', (userid,))
        user = cursor.fetchone()
        firstName = user['FirstName']
        lastName = user['LastName']
        phoneNumber = user['PhoneNumber']
        email = user['Email']
        adress = user['Adress']
        lista = [firstName, lastName, phoneNumber, email, adress]

        if adress != "":
            adressNotBlank = True
        else:
            adressNotBlank = False

        # räkna pris
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT ProductsID  FROM Cart WHERE UserID = %s', (userid,))
        prods = cursor.fetchall()
        price = 0
        for x in prods:  # räkna pris
            cursor.execute('SELECT * FROM Products WHERE ProductID= %s ', (x['ProductsID'],))
            getprodsviaip = cursor.fetchall()
            price += getprodsviaip[0]['ProductPrice']

        if price:
            shippingCost = 25
        return render_template('Check-out.html', lista=lista, logged=logged, counter=counter, price=price,
                               shippingCost=shippingCost, adressNotBlank=adressNotBlank)

    else:
        return redirect(request.referrer)


@PlaceOrderPage.route("/place-order.<orderid>", methods=["GET", "POST"])
def order(orderid):
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    counter = 0
    if logged:
        counter = count(getUserid(session['email']))

    msg = ""
    try:
        msg = session['orderMsg']
        session.pop('orderMsg', None)
        orderid = ""
    except:
        pass

    if msg == "":
        return render_template('Shop.html', logged=logged,
                               message="Order Number is: ", orderid=orderid, counter=counter)
    return render_template('Shop.html', logged=logged,
                           message=msg, orderid=orderid, counter=counter)
