from flask import Flask, redirect, render_template, request
import json
import requests
import re

app = Flask(__name__)
"""
def form_data_is_valid(form_data):
    # Perform validation checks on form data
    username = form_data.get('newUsername')
    email = form_data.get('newEmail')
    password = form_data.get('newPassword')
    confirm_password = form_data.get('confirmPassword')

    # Check for specific validation criteria
    if not username or len(username) < 3:
        return False

    if not email or not is_valid_email(email):
        return False

    if not password or len(password) < 8:
        return False

    if password != confirm_password:
        return False

    # If all checks pass, the data is valid
    return True

def is_valid_email(email):
    # Define a regular expression pattern for a valid email address
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Use the re.match function to check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False
    
"""
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
