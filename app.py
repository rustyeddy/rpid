from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Mobile Robot I/O")

@app.route('/hello')
def hello_world():
    return render_template('index.html')

@app.route('/routes')
def display_routes():
    print(url_for('index'))
    print(url_for('login'))
