from datetime import *
from os import *
from flask import Flask
from flask import render_template
import logging

app = Flask(__name__)

logging.basicConfig(filename='flasky.log',level=logging.DEBUG)
logging.debug('LOG FILE ENABLED as file %s' % log_file)

@app.route('/')
def home():
    #logging.info('home page visit at %s UTC [currently running on COMPUTERNAME
        #(datetime.utcnow(), getenv('COMPUTERNAME', '<i>unknown</i>')))
    text = { 'content': 'Welcome to this lovely looking flask application !' } 
    return render_template('home.html',
        title = 'Flasky Home',
        text = text)

app.debug = True
if __name__ == "__main__":
    app.run()


