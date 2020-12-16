from flask import *
import MySQLdb.cursors
from HelpMethods import *
from flask_mysqldb import MySQL

# DATABASE BLOCK START#
app = Flask(__name__)
mysql = MySQL(app)
# DATABASE BLOCK ENDS#
#
#
#
#
ProfilePage = Blueprint('ProfilePage', __name__, static_folder='static', template_folder='templates')


@ProfilePage.route("/profile")
def main_profile():
    if 'email' in session:
        return redirect(url_for("ProfilePage.profile", user=session['email']))
    return "profile main"


@ProfilePage.route('/profile/<user>', methods=['GET', 'POST'])
def profile(user):
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    counter = 0
    if (logged):
        counter = count(getUserid(session['email']))

    try:
        if session['email'] == user and request.method == 'POST' and (
                'edit-fname' in request.form or 'edit-lname' in request.form or 'edit-phone'
                in request.form or 'edit-email' in request.form or 'edit-pw' in request.form or 'edit-adr' in request.form):
            if request.method == 'POST' and (
                    'edit-fname' in request.form or 'edit-lname' in request.form or 'edit-phone'
                    in request.form or 'edit-email' in request.form or 'edit-pw' in request.form or 'edit-adr' in request.form):
                if request.form['edit-fname'] != "":
                    fName = request.form['edit-fname']
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('UPDATE Users SET FirstName=%s WHERE Email= %s ', (fName, user,))
                    mysql.connection.commit()

                if request.form['edit-lname'] != "":
                    lName = request.form['edit-lname']
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('UPDATE Users SET LastName=%s WHERE Email= %s ', (lName, user,))
                    mysql.connection.commit()

                if request.form['edit-phone'] != "":
                    phone = request.form['edit-phone']
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('UPDATE Users SET PhoneNumber=%s WHERE Email= %s ', (phone, user,))
                    mysql.connection.commit()

                if request.form['edit-pw'] != "":
                    pw = hashfunc(request.form['edit-pw'])
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('UPDATE Users SET Password=%s WHERE Email= %s ', (pw, user,))
                    mysql.connection.commit()

                if request.form['edit-adr'] != "":
                    adr = request.form['edit-adr']
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('UPDATE Users SET Adress=%s WHERE Email= %s ', (adr, user,))
                    mysql.connection.commit()

                if request.form['edit-email'] != "":
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('SELECT * FROM Users')
                    data = cursor.fetchall()
                    print(data)
                    found = False
                    for i in data:
                        if i['Email'] == uppercase(request.form['edit-email']):
                            found = True
                            break
                    if not found:
                        print("else")
                        email = uppercase(request.form['edit-email'])
                        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                        cursor.execute('UPDATE Users SET Email=%s WHERE Email= %s ', (email, user,))
                        mysql.connection.commit()
                        session['email'] = email
                    else:
                        msg = "Email is already in database"
                        return redirect(url_for("ProfilePage.profile", msg=msg, user=session['email']))
                return redirect(url_for("ProfilePage.profile", user=session['email']))

        if session['email'] == user:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Users WHERE Email =%s', (user,))
            data = cursor.fetchone()
            fname = data['FirstName']
            lname = data['LastName']
            phonenum = data['PhoneNumber']
            email = data['Email']
            password = "*********"
            adress = data['Adress']
            admin = False
            if session['email'] == user:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                if cursor.execute('SELECT * FROM Admin WHERE Email =%s', (user,)):
                    admin = True
                else:
                    admin = False
            return render_template('profile.html', firstname=fname, lastname=lname, email=email.lower(),
                                   phonenumber=phonenum,
                                   password=password, adress=adress, admin=admin, logged=logged, counter=counter)

        return "<h1>du är inte inloggad!</h1>"
    except:
        return "<h1>du är inte inloggad!</h1>"


@ProfilePage.route("/Orders")
def Orders():
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    if logged:
        counter = count(getUserid(session['email']))
        userid = getUserid(session['email'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Orders WHERE UserID=%s', (userid,))
        orders = cursor.fetchall()

        return render_template('Orders.html', logged=logged, counter=counter, orders=orders)
    else:
        return "<h1>du är inte inloggad!</h1>"


@ProfilePage.route("/Orders/<int:OrdID>")
def OrdersDetails(OrdID):
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    if(not logged):
        return "<h1>du är inte inloggad!</h1>"
    
    if logged:
        counter = count(getUserid(session['email']))
        userid = getUserid(session['email'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Orders WHERE UserID=%s', (userid,))
        orders = cursor.fetchall()

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM OrderDetails WHERE OrderID=%s', (OrdID,))
        orderD = cursor.fetchall()

        for x in orderD:
            cursor.execute('SELECT * FROM Orders WHERE OrderID=%s', (x['OrderID'],))
            temp = cursor.fetchone()
            if temp['UserID'] != userid:
                return redirect(url_for("ProfilePage.Orders"))
                #return render_template('Shop.html', logged=logged,
                 #              message="You cannot look into orders which are not yours!",counter=counter)


        # print(orderD)
        NameLista = []
        ImgLista = []
        for temp in orderD:
            cursor.execute('SELECT * FROM Products WHERE ProductID=%s', (temp['ProductID'],))
            products = cursor.fetchall()
            # print(products)
            for pord in products:
                NameLista.append(pord['ProductName'])
                ImgLista.append(pord['imageName'])

        return render_template('Orders.html', logged=logged, counter=counter, orders=orders, orderD=orderD,
                               NameLista=NameLista, ImgLista=ImgLista)
    else:
        return "<h1>du är inte inloggad!</h1>"

@ProfilePage.route('Cancel/<orderID>')
def CancelOrder(orderID):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT OrderStatus FROM Orders WHERE OrderID=%s',(orderID,))
    orderStatus = cursor.fetchone()


    if(orderStatus['OrderStatus']!="Processing Order"):
        flash('You cannot cancel an order which is not being processed!')
        return redirect(request.referrer)

    cursor.execute('SELECT * FROM OrderDetails WHERE OrderID=%s',(orderID,))
    products = cursor.fetchall()
    
    print(products)
    for x in products:
        cursor.execute('SELECT NumberInStock FROM Products WHERE ProductID=%s',(x['ProductID'],))
        amount=cursor.fetchone()
        print(amount)
        newAmount = int(int(amount['NumberInStock'])+int(x['Amount']))
        cursor.execute('UPDATE Products SET NumberInStock=%s WHERE ProductID=%s',(newAmount, x['ProductID'],))
        mysql.connection.commit()

    cursor.execute('UPDATE Orders SET OrderStatus=%s WHERE OrderID=%s',("Canceled", orderID,))
    mysql.connection.commit()
    cursor.close()
    return redirect(request.referrer)