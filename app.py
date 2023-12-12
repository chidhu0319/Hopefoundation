# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from ast import Continue
from flask import Flask, render_template, request, redirect, session , url_for , send_file
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)


app.secret_key = 'a'
  
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)


#HOME--PAGE

@app.route("/")
def home():
    return render_template("signup.html")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/python")
def python():
    return render_template("python.html")


@app.route("/html")
def html():
    pdf_path = 'html\HTML mock QA Set-1.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/css")
def css():
   pdf_path = 'html\CSS mock QA Set-1 .pdf'
   return send_file(pdf_path, mimetype='application/pdf')
@app.route("/sql")
def sql():
    pdf_path = 'sql\800+ SQL Interview Questions.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/L")
def L():
    pdf_path = 'python\Ch1Introduction & Installation.pptx.pdf'
    return send_file(pdf_path, mimetype='application/pdf')

@app.route("/A")
def A():
    pdf_path = 'python\datatypes_py.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/B")
def B():
    pdf_path = 'python\FILE HANDLING.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/C")
def C():
    pdf_path = 'python\web-servers.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/D")
def D():
    pdf_path = 'python\Obj_Orient_python.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/E")
def E():
    pdf_path = 'python\Algorithms__DS.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/F")
def F():
    pdf_path = 'python\Python Module.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/G")
def G():
    pdf_path = 'python\Libraries in Python.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/H")
def H():
    pdf_path = 'python\Python GUI.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/I")
def I():
    pdf_path = 'python\ch3Python Functions.pptx.pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/J")
def J():
    pdf_path = 'python\Django REST API - CRUD with DRF .pdf'
    return send_file(pdf_path, mimetype='application/pdf')
@app.route("/K")
def K():
    pdf_path = 'python\Django REST API - CRUD with DRF .pdf'
    return send_file(pdf_path, mimetype='application/pdf')





#SIGN--UP--OR--REGISTER


@app.route("/signup")
def signup():
    return render_template("signup.html")



@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM register WHERE username = % s', (username, ))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute('INSERT INTO register VALUES (NULL, % s, % s, % s)', (username, email,password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            return render_template('signup.html', msg = msg)
        
        
 
        
 #LOGIN--PAGE
    
@app.route("/signin")
def signin():
    return render_template("login.html")

        
@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM register WHERE username = % s AND password = % s', (username, password ),)
        account = cursor.fetchone()
        print (account)
        
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid=  account[0]
            session['username'] = account[1]
           
            return redirect('/index')
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)




       






#log-out

@app.route('/logout')

def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return render_template('login.html')

             

if __name__ == "__main__":
    app.run(debug=True)