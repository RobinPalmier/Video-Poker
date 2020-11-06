from flask import Flask, render_template, url_for, request, session, redirect, escape
import pandas as pd
import random
import sys
sys.path.insert(0, '/functions')
from functions import f
from threading import Timer
from deck import deck

app = Flask(__name__)
Timer(1, f.open_browser).start();
app.secret_key = "AZERTY1234"

@app.route('/')
def home():
    return render_template('Home/home.html')

@app.route('/game')
def bankroll():
    return render_template('InitGame/initGame.html')

@app.route('/game', methods=['POST'])
def u_bankroll():
    session["bankroll"] = request.form['bankroll']
    session["username"] = request.form['username']
    return redirect(url_for('table_game'))

@app.route('/table')
def table_game():
    return render_template('Table/table.html')

@app.route('/table', methods=['POST'])
def machine_premier_tirage():
    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    session["mise_joueur"] = request.form['mise_joueur']
    session['error'] = False
    if int(session["bankroll"]) < int(session["mise_joueur"]):
        session['error'] = "Votre mise est supérieur à votre bankroll"
        return render_template('Table/table.html')

    session["bankroll"] = int(session["bankroll"]) - int(session["mise_joueur"])
    tirage1, deck = f.premier_tirage(deck)
    session['premier_tirage'] = tirage1
    session['u_deck'] = deck
    return redirect(url_for('table_first'))

@app.route('/table-first')
def table_first():
    return render_template('TableFirst/tableFirst.html')

@app.route('/table-first', methods=['POST'])
def machine_second_tirage():
    hand = []
    for key in request.form:
        hand.append(escape(key))
    hand, deck = f.second_tirage(session['u_deck'], 5 - len(hand), hand)
    
    g, resultat, success = f.gain(hand, int(session["mise_joueur"]))
    session["bankroll"] = session["bankroll"] + int(g)
    session["message"] = resultat
    session["success"] = success

    if int(session["bankroll"]) == 0:
        session["success"] = False

    return  render_template('TableSecond/tableSecond.html', second_tirage=hand)