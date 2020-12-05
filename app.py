# we use Flask, render_template, url_for, request, redirect, session
from flask import *
from datetime import timedelta
import MySQLdb.cursors
from flask_admin import Admin, AdminIndexView  # admin
from flask_admin.contrib.sqla import ModelView  # admin
from flask_admin.menu import MenuLink  # admin
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy  # admin
from wtforms.validators import ValidationError
from HelpMethods import *
from UsersViews import UsersViews
from LoginPage import LoginPage
from RegisterPage import RegisterPage
from ProfilePage import ProfilePage
from shoppingbag import shoppingbag

# from flask.ext.admin.form import Select2Widget #admin för dropdown menu (kanske radera om det inte funkar)

app = Flask(__name__)


app.register_blueprint(UsersViews, url_prefix="")  # www.youtube.com/watch?v=WteIH6J9v64
app.register_blueprint(LoginPage, url_prefix="")
app.register_blueprint(RegisterPage, url_prefix="")
app.register_blueprint(ProfilePage, url_prefix="")
app.register_blueprint(shoppingbag, url_prefix="")

app.secret_key = 'thisKeyIsSoSecret'
app.permanent_session_lifetime = timedelta(minutes=500)  # session time

app.config['MYSQL_HOST'] = 'utbweb.its.ltu.se'
app.config['MYSQL_USER'] = '941227'
app.config['MYSQL_PASSWORD'] = '941227'
app.config['MYSQL_DB'] = 'db941227'

# admin

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://941227:941227@utbweb.its.ltu.se/db941227'
app.config['FLASK_ADMIN_SWATCH'] = 'Cyborg'  # http://bootswatch.com/3/ för att bälja swatches # admin panel
db = SQLAlchemy(app)
db.Model.metadata.reflect(bind=db.engine, schema='db941227')


class User(db.Model):
    # skapa en model på en befintlig tabell!!!!!!!!!!!
    __table__ = db.Model.metadata.tables['db941227.Users']

    def __repr__(self):
        return '<User %r>' % self.Username


class Categorys(db.Model):
    __table__ = db.Model.metadata.tables['db941227.Categorys']

    def __repr__(self):
        return '<User %r>' % self.CategoryName


class CategorysView(ModelView):
    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class ProductsCategory(db.Model):
    # skapa en model på en befintlig tabell!!!!!!!!!!!
    __table__ = db.Model.metadata.tables['db941227.ProductsCategory']

    # productID = db.relationship("ProductID", backref="ProductID")

    def __repr__(self):
        return '<hasdas %r>' % self.ProductID


class ProductsCategoryView(ModelView):
    column_list = ('CategoryID', 'ProductsID')
    form_columns = ['CategoryID', 'ProductsID', ]
    edit_columns = ['CategoryID', 'ProductsID', ]

    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class AdminUser(db.Model):
    # skapa en model på en befintlig tabell!!!!!!!!!!!
    __table__ = db.Model.metadata.tables['db941227.Admin']

    def __repr__(self):
        return '<User %r>' % self.Email


class Product(db.Model):
    # skapa en model på en befintlig tabell!!!!!!!!!!!
    __table__ = db.Model.metadata.tables['db941227.Products']

    def __repr__(self):
        return '<User %r>' % self.ProductID


class ProductView(ModelView):
    form_excluded_columns = ("Rating",)

    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class AdminIndexView(AdminIndexView):

    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class UserView(ModelView):
    column_searchable_list = ('Email', "FirstName", "LastName", "PhoneNumber")

    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:
            return False
        return False


class AdminUserView(ModelView):
    column_display_pk = True  # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_list = ('Email', "DateOfAdmin")
    form_excluded_columns = ("DateOfAdmin",)  # Remove the dateofadmin because its automatic in myphpadmin
    column_searchable_list = ('Email',)
    edit_columns = ["Email", ]

    def on_model_change(self, form, model, is_created):
        email = uppercase(str(form.Email.data))
        print(email)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE Email = %s', (email,))
        account = cursor.fetchone()
        if not account:
            raise ValidationError(email + " is not a user!")

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
        account = cursor.fetchone()
        if account:
            raise ValidationError(email + " is already an Admin!")
        form.Email.data = email
        return model

    def is_accessible(self):
        try:
            if session["email"]:  ## ISTÄLLER FÖR session["email"] så måste vi
                return True
        except:
            return False
        return False


#    def inaccessible_callback(self, name, **kwargs):
#       # redirect to login page if user doesn't have access
#      return redirect(url_for('home')

admin = Admin(app, name="NOUELI", template_mode="bootstrap3", index_view=AdminIndexView())
# print("ADMIN ENDPOINT: "+ str(db.Model.__tablename__))
admin.add_view(UserView(User, db.session))
admin.add_view(AdminUserView(AdminUser, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(CategorysView(Categorys, db.session))
admin.add_view(ProductsCategoryView(ProductsCategory, db.session))
admin.add_link(MenuLink(name='Profile', category='', url="/profile"))
admin.add_link(MenuLink(name='Logout', category='', url="/logout"))
# END ADMIN

mysql = MySQL(app)


@app.route("/verify")
def verify():
    return render_template("verify.html")


if __name__ == '__main__':
    app.run(debug=True)
