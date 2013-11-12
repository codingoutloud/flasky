from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home():
    text = { 'content': 'Welcome to this somewhat respectable looking flask application !' } 
    return render_template("home.html",
        title = 'Home away from home',
        text = text)


app.debug = True
if __name__ == "__main__":
    app.run()
