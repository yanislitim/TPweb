from .app import app
from flask import render_template
@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html",title ="R3.01 Dev Web avec Flask",name="yanis gros looser")

@app.route("/about/")
def about():
    return render_template("index2.html",title ="R3.01 Dev Web avec Flask",name="yanis gros gros looser")


@app.route("/contact/")
def contact():
    return app.config["CONTACT"]

if __name__== "__main__" :
    app.run()