# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from models import GameState, Player
from game_engine import scavenge_event, hatch_event

app = Flask(__name__)
app.secret_key = 'nukevault_secret'

game = GameState()

@app.route('/')
def index():
    return render_template('game.html', game=game)

@app.route('/setup', methods=['POST'])
def setup():
    names = request.form.getlist('player_names')
    abilities = request.form.getlist('abilities')
    game.players = [Player(name, ab) for name, ab in zip(names, abilities)]
    return redirect(url_for('index'))

@app.route('/action/<player_name>/<action>')
def player_action(player_name, action):
    player = next(p for p in game.players if p.name == player_name)
    if action == "scavenge":
        result = scavenge_event(player, game.shelter)
        game.shelter.event_log.append(result)
    elif action == "hatch":
        result = hatch_event(game.shelter)
        game.shelter.event_log.append(result)
    return redirect(url_for('index'))

@app.route('/next_day')
def next_day():
    game.shelter.days_survived += 1
    for player in game.players:
        if player.status == "alive":
            player.mental_state -= 5
            player.health -= 5
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
