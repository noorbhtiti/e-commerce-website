from flask import *
import MySQLdb.cursors
from flask_mysqldb import MySQL

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
        cursor.execute('SELECT UserID FROM Users WHERE Email = %s ', (session['email'],))
        getuserid = cursor.fetchone()
        #################################################################################
        userid = getuserid['UserID']
        cursor.execute('SELECT ProductsID FROM Cart WHERE  UserID= %s ', (userid,))
        getprodids = cursor.fetchall()
        print(getprodids)
        #################################################################################
        lista = []
        for x in getprodids:
            cursor.execute('SELECT * FROM Products WHERE ProductID= %s ', (x['ProductsID'],))
            getprodsviaip = cursor.fetchall()
            lista.append(getprodsviaip)

        return render_template('shoppingbag.html', lista=lista)

    else:
        msg = "Please login to see cart"
        return render_template('login.html', errormsg=msg)
