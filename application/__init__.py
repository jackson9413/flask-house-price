from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '123hdchfuhudhfnfggsojkdjhunjnckjkdfhbapqowomdncioi99090kmcnjdh?!&~'

db = SQLAlchemy(app)

app.app_context().push()

from application import routes