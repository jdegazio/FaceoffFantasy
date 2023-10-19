from flask import Flask, redirect, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/createaccount')
def createaccount():
    return render_template('createaccount.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/standings')
def standings():
    return render_template('standings.html')

@app.route('/livescoring')
def livescoring():
    return render_template('livescoring.html')

@app.route('/draftroom')
def draftroom():
    return render_template('draftroom.html')

@app.route('/trading')
def trading():
    return render_template('trading.html')

'''@app.route('/redirect', methods=['GET'])
def redirect_to_team():
    team_name = request.args.get('teamName', '')
    
    return redirect('/teams', team_name)'''

@app.route('/myteam')
def myteam():
    #testteam = 'TOR'
    #api_url = 'https://api.sportsdata.io/v3/nhl/scores/json/PlayersBasic/' + testteam + '?key=e47db9561f7641f3b9a98b107c6bd71e'
    
    #try:
    #    response = requests.get(api_url)
    #    data = response.json()
    #except Exception as e:
    #    data = {}  # Handle errors gracefully

    with open('toronto.txt', 'r') as json_file:
        data = json.load(json_file)

    players = []
    for player in data:
        if str(player['Status']) == 'Active':
            player['BirthDate'] = player['BirthDate'][:10]
            players.append(player)

    return render_template('myteam.html', data=players)

if __name__ == '__main__':
    app.run(debug=True)