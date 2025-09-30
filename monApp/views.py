from .app import app
from flask import render_template
@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html",title ="R3.01 Dev Web avec Flask",name="yanis")

@app.route("/about/")
def about():
    return render_template("about.html",title ="R3.01 Dev Web avec Flask",name="yanis r")


@app.route("/contact/")
def contact():
    return render_template("contact.html", title = "R3.01 Dev Web avec Flask",name = "yanis er")

if __name__== "__main__" :
    app.run()