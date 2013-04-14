import os
import bottle
from bottle.ext import sqlalchemy
import sqlalchemy

app = bottle.Bottle()
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db = sqlalchemy(app)

@route("/")
def hello_world():
    return "Hello, World!"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
