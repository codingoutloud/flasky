from flask import Flask
from datetime import *
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    text = { 'content': 'Welcome to this lovely looking flask application !' } 
    return render_template("home.html",
        title = 'Home away from home',
        text = text)
    print("home page visit at %s (currently running on COMPUTERNAME = %s)" %
          (datetime.utcnow(), os.getenv('COMPUTERNAME', '<i>unknown</i>'))


app.debug = True
if __name__ == "__main__":
    app.run()
