from .app import db
class Auteur(db.Model):
    idA = db.Column( db.Integer, primary_key=True )
    Nom = db.Column( db.String(100) )

    def __init__(self, Nom):
        self.Nom = Nom
    
    def __repr__ (self ):
        return "<Auteur (%d) %s>" % (self.idA , self.Nom)


class Livre(db.Model):
    idL = db.Column( db.Integer, primary_key=True )
    prix = db.Column( db.Integer)
    Titre = db.Column( db.String(255) )
    url = db.Column(db.String(255))
    img = db.Column(db.String(255))

    auteur_id = db.Column (db.Integer , db.ForeignKey ("auteur.idA") )
    auteur = db.relationship ("Auteur", backref =db.backref ("livres", lazy="dynamic") )

    def __init__(self,Titre):
        self.Titre = Titre

    def __repr__ (self ):
        return "<Livre (%d) %s>" % (self.idL , self.Titre)  
        
