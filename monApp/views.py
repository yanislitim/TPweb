from .app import app
from flask import render_template, request
from monApp.models import Auteur, Livre

@app.route('/')
@app.route('/index/')
def index():
    # si pas de paramètres
    if len(request.args)==0:
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name="Cricri")
    else :
        param_name = request.args.get('name')
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name=param_name)

@app.route('/auteurs/')
def getAuteurs():
    lesAuteurs = Auteur.query.all()
    return render_template('auteurs_list.html', title="R3.01 Dev Web avec Flask", auteurs=lesAuteurs)

@app.route("/about/")
def about():
    return render_template("about.html",title ="R3.01 Dev Web avec Flask",name="yanis r")


@app.route("/contact/")
def contact():
    return render_template("contact.html", title = "R3.01 Dev Web avec Flask",name = "yanis er")

@app.route('/livres/')
def getLivres():
    lesLivres = Livre.query.all()
    return render_template("livres_list.html", title="Liste des livres", livres=lesLivres)


if __name__== "__main__" :
    app.run()