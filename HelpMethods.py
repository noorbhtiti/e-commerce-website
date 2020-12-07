import hashlib
import MySQLdb.cursors
from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


# HASHING METHOD

def hashfunc(password):
    temp = hashlib.sha256(password.encode('utf-8'))
    return temp.hexdigest()


# end of HASHING METHOD

# start of uppercase function#
def uppercase(email):
    return email.upper()


# end of uppercase function


#start of get User ID#

def getUserid(email):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT UserID FROM Users WHERE Email = %s ', (email,))
    getuserid = cursor.fetchone()
    userid = getuserid['UserID']
    return userid

#end of user ID#

# start of counting things in Cart #
def count(UserID):
    counter = 0
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Cart WHERE UserID=%s', (UserID,))
    get = cursor.fetchall()
    for x in get:
        counter += 1
    return counter

# end of counting things in Cart
