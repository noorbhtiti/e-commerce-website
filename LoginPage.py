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
LoginPage = Blueprint('LoginPage', __name__, static_folder='static', template_folder='templates')


#
@LoginPage.route('/login', methods=['GET', 'POST'])
def login():
    errormsg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = uppercase(request.form['email'])
        password = hashfunc(request.form['password'])
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE Email = %s and Password =%s', (email, password,))
        account = cursor.fetchone()
        if account:
            session['email'] = email
            return redirect(url_for('ProfilePage.profile', user=email))
            # return redirect(request.referrer)
        else:
            errormsg = 'Incorrect Email/Password!'
    else:
        if 'email' in session:
            return redirect(url_for("ProfilePage.profile", user=session['email']))
    return render_template('login.html', errormsg=errormsg)


@LoginPage.route('/logout')
def logout():
    if "email" in session:
        session.pop("email", None)
    return redirect(url_for("UsersViews.home"))
