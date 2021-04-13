# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#from flask import Flask
#app=Flask(__name__)

#@app.route('/hello')
#def hello_world():
   # return "Hello World am Deek"
   
#@app.route('/hello/<name>')
#def hello_world(name):
    #return "hello %s" %name

#@app.route('/user/<int:value>')
#def user(value):
    #return "number %d" %value
    
    
    
from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/admin')
def hello_admin():
    return "hello admin"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "hello %s guest" %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))
if __name__ == '__main__':
    #app.run()
    app.run(debug = True)
    
