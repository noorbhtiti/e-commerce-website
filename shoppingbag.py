from flask import *
import MySQLdb.cursors
from flask_mysqldb import MySQL
from HelpMethods import *
# DATABASE BLOCK START#
app = Flask(__name__)
mysql = MySQL(app)
# DATABASE BLOCK ENDS#
#
#
#
#
shoppingbag = Blueprint('shoppingbag', __name__, static_folder='static', template_folder='templates')


@shoppingbag.route('/cart')
def cart():
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    if logged:
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        userid = getUserid(session['email'])
        cursor.execute('SELECT ProductsID FROM Cart WHERE UserID= %s ', (userid,))
        getprodids = cursor.fetchall()
        # print(getprodids)
        #################################################################################
        cartDict = {}
        lista = []
        counter = 0
        price = 0
        shippingCost = 0
        print(getprodids)
        for x in getprodids:
            cursor.execute('SELECT * FROM Products WHERE ProductID= %s ', (x['ProductsID'],))
            getprodsviaip = cursor.fetchall()
            price += getprodsviaip[0]['ProductPrice']
            if x['ProductsID'] in cartDict:
                cartDict[x['ProductsID']] += 1
            else:
                cartDict[x['ProductsID']] = 1
                lista.append(getprodsviaip)
            counter = count(getUserid(session['email']))
            session['counter'] = counter
        if(price>0):
            shippingCost = 25
        else:
            shippingCost = 0
        return render_template('shoppingbag.html', lista=lista, cartDict=cartDict, logged=logged, counter=counter, price=price, shippingCost=shippingCost)

    else:
        msg = "Please login to see cart"
        return render_template('login.html', errormsg=msg)


@shoppingbag.route("/cart.<int:idt>")
def removeFromCart(idt):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT UserID FROM Users WHERE Email = %s ', (session['email'],))
    getuserid = cursor.fetchone()
    cursor.execute('DELETE FROM Cart WHERE UserID =%s and ProductsID = %s', (getuserid['UserID'], idt,))
    mysql.connection.commit()
    return redirect(url_for('shoppingbag.cart'))
