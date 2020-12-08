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

@PlaceOrderPage.route("/place-order")
def order():
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    if(logged):
        #gör en if request.methods==post här innan man kör allting!
        userid = getUserid(session['email'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT ProductsID  FROM Cart WHERE UserID = %s' , (userid,))
        prods = cursor.fetchall()
        price = 0
        for x in prods: #räkna pris
            cursor.execute('SELECT * FROM Products WHERE ProductID= %s ', (x['ProductsID'],))
            getprodsviaip = cursor.fetchall()
            price += getprodsviaip[0]['ProductPrice']
        if(price>0):
            price+=25


        if(prods): #om det finns produkter
            #skapa en Order
            cursor.execute('SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE (TABLE_NAME = "Orders");')
            nextID = cursor.fetchone()
            ################################ JAG HÅRDKODADE RADEN UNDER MED RANDOM INFO!!!!!!! ##############################
            cursor.execute('INSERT INTO `Orders`(`UserID`, `Amount`, `OrderStatus`, `ShippingAdress`, `OrderPhoneNumber`, `OrderEmail`) VALUES (%s,%s,%s,%s,%s,%s)',(userid, price,"Processing Order", "Luleå", 112, session['email'],))
            #################################################################################################################
            mysql.connection.commit()
            print(nextID)
            for x in prods: #kopiera över allt från cart till orderdetails
                cursor.execute('SELECT * FROM Products WHERE ProductID= %s ', (x['ProductsID'],))
                a = cursor.fetchone()
                print(a)
                cursor.execute('INSERT INTO `OrderDetails`( `OrderID`, `ProductID`,`BuyingPrice` ,`Amount`) VALUES (%s,%s,%s,%s)',(nextID['AUTO_INCREMENT'],x['ProductsID'],a['ProductPrice'],1,))
                cursor.execute('DELETE FROM Cart WHERE UserID =%s and ProductsID = %s', (userid, x['ProductsID'],))
                mysql.connection.commit()
            return "<h1>Din order har placerats!</h1>"
        else:
            return "<h1>Din cart är tom</h1>"
        
    return "<h1>Du är inte inloggad!</h1>"


    return str(price)