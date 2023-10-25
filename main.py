from flask import Flask, redirect, render_template, request
import json
import requests
import re

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
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

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submit_create_account', methods=['POST'])
def submit_create_account():
    # Process the form data here and perform any necessary validation
    # You can access form data using request.form
    # Redirect or render a response as needed

    # Example: Validate and redirect to the success page
    if form_data_is_valid(request.form):
        # Perform account creation logic here
        return redirect('/success')
    else:
        return render_template('createaccount.html', error_message='Invalid data')


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
