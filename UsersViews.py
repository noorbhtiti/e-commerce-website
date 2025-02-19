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

    counter = 0
    if (logged):
        counter = count(getUserid(session['email']))

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Categorys')
    category = cursor.fetchall()
    # print(category)
    return render_template('index.html', logged=logged, category=category, counter=counter)


@UsersViews.route('/shop/<category>')
def shopCategory(category):
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    counter = 0
    if (logged):
        counter = count(getUserid(session['email']))

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT CategoryID FROM Categorys WHERE CategoryName = %s', (category,))
    category = cursor.fetchone()
    if (category):  # om categorin finns i databasen
        # print(category['CategoryID'])
        cursor.execute('SELECT ProductID FROM ProductsCategory WHERE CategoryID = %s',
                       (category['CategoryID'],))  # hämtar alla produkter som har med den categorin
        prodscat = cursor.fetchall()
        # print("prodscat ", prodscat)

        if prodscat:
            prods = []
            for x in prodscat:
                # print(x['ProductID'])
                cursor.execute('SELECT * FROM Products WHERE ProductID = %s', (x['ProductID'],))
                prods.append(cursor.fetchone())
            # print(prods)
            return render_template('Shop.html', logged=logged, prods=prods, counter=counter)
        else:
            return render_template('Shop.html', logged=logged,
                                   message="There are no products in this category! We are sorry :(", counter=counter)
    return render_template('Shop.html', logged=logged, message="404 error! Did not find this category!",
                           counter=counter)


# home block end#
#
#
#
#
# Add To Cart start"
# /shop/product.{{prod['ProductID']}}
@UsersViews.route("/shop/product.<int:pro_id>", methods=["GET", "POST"])
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
    if logged:
        counter = count(getUserid(session['email']))
    return render_template('Shop.html', logged=logged, prods=prods, counter=counter)


# shop block end#

def updateRating(prodid):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT Rating FROM UserReviews where ProductID = %s', (prodid,))
    ratings = cursor.fetchall()
    totalRating = 0
    for x in ratings:
        totalRating += x['Rating']
    totalRating=int(round(totalRating/len(ratings)))
    cursor.execute('UPDATE Products SET Rating=%s WHERE ProductID=%s',(totalRating,prodid,))
    mysql.connection.commit()
    #print(totalRating)


    #'UPDATE UserReviews SET Review=%s,Rating=%s WHERE UserID=%s and ProductID=%s',
                          # (comments, rate, getUserid(session['email']), Proid,))

@UsersViews.route("/shop/product-<Proid>", methods=['GET', 'POST'])
def productSida(Proid):
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    counter = 0
    if logged:
        counter = count(getUserid(session['email']))

    userid = 0
    try:
        if logged:
            userid = getUserid(session['email'])
    except:
        userid

    msg = ""

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Products where ProductID = %s', (Proid,))
    prods = cursor.fetchone()
    cursor.execute('SELECT * FROM UserReviews where ProductID = %s', (Proid,))
    reviews = cursor.fetchall()

    lista = []
    for review in reviews:
        user = review['UserID']
        cursor.execute('SELECT FirstName FROM Users where UserID = %s', (user,))
        users = cursor.fetchall()
        for x in users:
            lista.append(x['FirstName'])

    if logged:
        userid = getUserid(session['email'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM UserReviews WHERE ProductID=%s and UserID=%s', (Proid, userid,))
        theId = cursor.fetchone()
        #print(theId)
        if theId is None and request.method == "POST":
            try:
                rate = request.form['rate']
            except:
                rate = 1
            comments = request.form['comments']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO UserReviews (UserID,ProductID ,Review,Rating) VALUES (%s ,%s ,%s,%s)',
                           (userid, Proid, comments, rate,))
            mysql.connection.commit()
            updateRating(Proid)
            return redirect(request.referrer)
        elif request.method == "POST":
            #print("Update")
            try:
                rate = request.form['rate']
            except:
                rate = 1
            comments = request.form['comments']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE UserReviews SET Review=%s,Rating=%s WHERE UserID=%s and ProductID=%s',
                           (comments, rate, getUserid(session['email']), Proid,))
            mysql.connection.commit()
            updateRating(Proid)
            return redirect(request.referrer)

    if not logged:
        if request.method == "POST":
            msg = "Please log in to leave a review"
            return render_template("Product-page.html", prods=prods, logged=logged, counter=counter, reviews=reviews,
                                   msg=msg, lista=lista)

    return render_template("Product-page.html", prods=prods, logged=logged, counter=counter, reviews=reviews,
                           lista=lista, userid=userid)


@UsersViews.route("/shop/product-<Proid>/<ReviewID>")
def deletereview(Proid, ReviewID):
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    counter = 0
    if logged:
        counter = count(getUserid(session['email']))

    if logged:
        userid = getUserid(session['email'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM UserReviews WHERE ProductID=%s and UserID=%s and ReviewID=%s',
                       (Proid, userid, ReviewID))
        mysql.connection.commit()
        return redirect(request.referrer)

    else:
        return redirect(request.referrer)
