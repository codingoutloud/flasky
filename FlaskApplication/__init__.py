from datetime import *
from os import *
from logging import *
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    Logger.warning('helllllloo')
    Logger.error('danger Will Robinson')
    print('home page visit at %s UTC [currently running on COMPUTERNAME = %s]' % 
            (datetime.utcnow(), getenv('COMPUTERNAME', '<i>unknown</i>')))
    text = { 'content': 'Welcome to this lovely looking flask application !' } 
    return render_template('home.html',
        title = 'Flasky Home',
        text = text)



app.debug = True
if __name__ == "__main__":
    app.run()


