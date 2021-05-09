from flask import Flask
import mysql.connector

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="0612AnLu+",
    database="jogoteca",
    auth_plugin='mysql_native_password'
)


from views import *


if __name__ == '__main__':
    app.run(debug=True)
