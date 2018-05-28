# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:22:52 2017

@author: mustafa
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/')
def about():
    return "<h1>This is my about page<h1>"
if __name__ ==  "__main__":
    app.run()
