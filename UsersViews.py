from flask import *
from datetime import timedelta
import MySQLdb.cursors
from HelpMethods import *
from flask_sqlalchemy import SQLAlchemy  # admin
from flask_mysqldb import MySQL

UsersViews = Blueprint('UsersViews', __name__, static_folder='static', template_folder='templates')

# DATABASE BLOCK START# 
app = Flask(__name__)
mysql = MySQL(app)


# DATABASE BLOCK ENDS#


# home block start#
@UsersViews.route('/')
def home():
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Categorys')
    category = cursor.fetchall()
    print(category)
    return render_template('index.html', logged=logged, category=category)


@UsersViews.route('/shop/<category>')
def shopCategory(category):
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    counter = 0
    if(logged):
        counter = count(getUserid(session['email']))

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT CategoryID FROM Categorys WHERE CategoryName = %s', (category,))
    category = cursor.fetchone()
    if (category):  # om categorin finns i databasen
        print(category['CategoryID'])
        cursor.execute('SELECT ProductID FROM ProductsCategory WHERE CategoryID = %s',
                       (category['CategoryID'],))  # hämtar alla produkter som har med den categorin
        prodscat = cursor.fetchall()
        print("prodscat ", prodscat)

        if (prodscat):
            prods = []
            for x in prodscat:
                print(x['ProductID'])
                cursor.execute('SELECT * FROM Products WHERE ProductID = %s', (x['ProductID'],))
                prods.append(cursor.fetchone())
            print(prods)
            return render_template('Shop.html', logged=logged, prods=prods, counter=counter)
        else:
            return render_template('Shop.html', logged=logged,
                                   message="There are no products in this category! We are sorry :(", counter=counter)
    return render_template('Shop.html', logged=logged, message="404 error! Did not find this category!", counter=counter)


# home block end#
#
#
#
#
# Add To Cart start"
@UsersViews.route("/shop.<int:pro_id>", methods=["GET", "POST"])
def addToCart(pro_id):
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    if logged:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT UserID FROM Users WHERE Email = %s ', (session['email'],))
        account = cursor.fetchone()
        userid = account['UserID']
        cursor.execute('INSERT INTO Cart (UserID,ProductsID ,Amount) VALUES (%s ,%s ,%s)', (userid, pro_id, 1,))
        mysql.connection.commit()

    else:
        msg = "Please login to add items"
        returnToShop = True
        return render_template('login.html', errormsg=msg)
    return redirect(request.referrer)


# Add to Cart end#
#
#
#
#
# shop block start#
@UsersViews.route('/shop', methods=['GET', 'POST'])
def shop():
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Products')
    prods = cursor.fetchall()
    counter = 0
    if(logged):
        counter = count(getUserid(session['email']))
    return render_template('Shop.html', logged=logged, prods=prods, counter = counter)
# shop block end#