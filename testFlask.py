# -*- coding:utf-8 -*-
'''
Created on 2016年3月24日

@author: zxj
'''

from flask import Flask,redirect,abort,url_for,render_template,request
from flask.helpers import url_for

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return redirect(url_for('other'))
    #return "Hello Flask"

@app.route('/route')
def other():
    #abort(404)
    return render_template('index.html')
    #return "route"
    
@app.errorhandler(404)
def page_not_found(error):
    return "404 Error",404

if __name__ == "__main__":
    app.run()