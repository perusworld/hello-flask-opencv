"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from app import app
from flask import request
import numpy as np
import cv2

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.')

@app.route('/api-test', methods = ['POST'])
def api_test():
    return "Hi There"

@app.route('/process-image', methods = ['POST'])
def process_image():
    if str(request.headers.get('content-type')) == 'application/octet-stream':
        img = cv2.imdecode(np.frombuffer(request.data, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        return 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
    else:
        return "Unsupported"