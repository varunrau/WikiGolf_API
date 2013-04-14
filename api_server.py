import os
from bottle import *
import bottle
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
import json

app = bottle.Bottle()
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

class Path(Base):
    __tablename__ = "path"
    id = Column(Integer, Sequence("id_seq"), primary_key=True)
    start_node = Column(String)
    end_node = Column(String)
    path = Column(String)

    def __init__(self, start_node, end_node, path):
        self.start_node = start_node
        self.end_node = end_node
        self.path = path

    def __repr__(self):
        return "<Path(id: '%d', start_node: '%s', end_node: '%s', path: '%s')>" & (self.id, self.start_node, self.end_node, self.path)

@app.get("/get", db)
def node_value(db):
    node = "face"
    start_path = db.query(Path).filter_by(start_node=node)
    end_path = db.query(Path).filter_by(end_node=node)
    if start_path and end_path:
        data = start_node
        data.append(end_path)
    if start_path:
        return start_node
    if end_path:
        return end_path
    else:
        return "ERROR"


@route("/")
def hello_world():
    return "Hello, World!"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
