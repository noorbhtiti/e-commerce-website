from flask import *
from datetime import timedelta
import MySQLdb.cursors
from HelpMethods import *
from flask_sqlalchemy import SQLAlchemy  # admin
from flask_mysqldb import MySQL

# DATABASE BLOCK START#
app = Flask(__name__)
mysql = MySQL(app)
# DATABASE BLOCK ENDS#
#
#
#
#
RegisterPage = Blueprint('RegisterPage', __name__, static_folder='static', template_folder='templates')


@RegisterPage.route('/register', methods=['GET', 'POST'])
def register():
    regMsg = ''
    if request.method == 'POST' and 'fName' in request.form and 'lName' in request.form and 'phone' in request.form and 'email' in request.form and 'pw' in request.form:
        fName = request.form['fName']
        lName = request.form['lName']
        phone = request.form['phone']
        email = uppercase(request.form['email'])
        pw = hashfunc(request.form['pw'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE Email = %s', (email,))
        account = cursor.fetchone()
        if account:
            regMsg = 'Account Already exists'
        else:
            cursor.execute(
                'INSERT INTO Users (FirstName, LastName, PhoneNumber, Email, Password) VALUES (%s , %s, %s, %s, %s)',
                (fName, lName, phone, email, pw,))
            mysql.connection.commit()
            regMsg = 'Successfully registered!\n You can login now!'
            # here we should send the user to verify instead of login
            return render_template('login.html', errormsg=regMsg)
    return render_template('Register.html', regMsg=regMsg)
