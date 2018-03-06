from flask import render_template, flash, redirect, url_for
from app import app

#@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/easter_egg')
def easter_egg():
    return render_template('index_template.html')

    
@app.route('/ejemplos')
def ejemplos():
    return render_template('ejemplos.html')

@app.route('/normas')
def normas():
    return render_template('normas.html')

@app.route('/materiales')
def materiales():
    return render_template('materiales.html')

