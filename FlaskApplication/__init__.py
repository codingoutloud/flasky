from flask import Flask
from datetime import *
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    text = { 'content': 'Welcome to this lovely looking flask application !' } 
    return render_template("home.html",
        title = 'Flasky Home',
        text = text)


app.debug = True
if __name__ == "__main__":
    app.run()
