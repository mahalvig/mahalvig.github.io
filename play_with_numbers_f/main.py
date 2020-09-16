
import sys
import os
from random import random, randrange, choice
# external package imports
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return flask.render_template('home.html')

@app.route('/random', methods=['GET'])
def _random():
    return str(random())

@app.route('/random/<limit>', methods=['GET'])
def random_with_limit(limit):
    _limit = int(limit)
    return str(randrange(_limit))

@app.route('/roll-a-dice', methods=['GET'])
def roll_a_dice():
    allowed = list(range(1,13))
    allowed = [str(n) for n in allowed]
    return choice(allowed)

@app.route('/roll-a-dhayam', methods=['GET'])
def roll_a_dhayam():
    allowed = ['1', '2', '3', '4', '5','6', '12']
    return choice(allowed)

app.run()
