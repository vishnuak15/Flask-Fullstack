from flask import Flask

app = Flask(__name__)#special variable to identify the current application or module that is being rendered or passed to flask

from application import routes

