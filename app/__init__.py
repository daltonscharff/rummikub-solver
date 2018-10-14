from flask import Flask

app = Flask(__name__)
from rummikub_solver import views