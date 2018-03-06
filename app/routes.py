from flask import render_template, flash, redirect, url_for
from app import app

#@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/ejemplos')
def ejemplos():
    return render_template('ejemplos.html')
