import os
import bottle
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

app = bottle.Bottle()
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
database_url = os.environ["DATABASE_URL"]

Base = declarative_base()
engine = create_engine(database_url, echo=True)

plugin = sqlalchemy.Plugin(
        engine,
        Base.metadata,
        keyword='db',
        create=True,
        commit=True,
        use_kwargs=False
)

app.install(plugin)

db = sqlalchemy(app)

@route("/")
def hello_world():
    return "Hello, World!"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
