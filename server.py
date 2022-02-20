from os import environ
from flask import Flask

app = Flask(_name_)
app.run(environ.get('PORT'))