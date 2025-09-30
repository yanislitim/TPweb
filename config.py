# import random, string, os
# "".join([random.choice(string.printable) for _ in os.urandom(24) ] )
SECRET_KEY = "889b8c68-2a09-4c7e-84a0-c620a19ceaff"

ABOUT = "Bienvenue sur la page à propos de Flask !"

CONTACT = "Bienvenue sur l'autre page la"

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')

BOOTSTRAP_SERVE_LOCAL = True