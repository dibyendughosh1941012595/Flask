
"""
Created on Tue Apr 13 22:54:54 2021

@author: HP
"""

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login' ,methods = ["POST"])
def login():
    if request.method == "POST":
        user1 = request.form["nm"]
        user2 = request.form["age"]
        user3 = request.form["qua"]
        return render_template('index.html',x=user1,y=user2,z=user3)

if __name__ == ('__main__'):
    app.run(debug = True)
