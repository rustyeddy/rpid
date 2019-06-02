#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import Response

# from multiprocessing import Process
# from multiprocessing import Queue
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Mobile Robot I/O")

@app.route('/hello')
def hello_world():
    return render_template('index.html')


app.run(host="0.0.0.0", debug=True, port=5001)

