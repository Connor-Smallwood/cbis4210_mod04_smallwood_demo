from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/adoptions')
def adoptions():
    return render_template('adoptions.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/services.html')
def services():
    return render_template('services.html')

@app.route('/help')
def help():
    return render_template('help.html')

