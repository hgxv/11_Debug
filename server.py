import json
from datetime import datetime
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)
    
    except IndexError:
        error = "Mail was not found"
        return render_template('index.html', error=error)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    competition_date = datetime.strptime(foundCompetition["date"], "%Y-%m-%d %H:%M:%S")
    date = datetime.now()
    if foundClub and foundCompetition and competition_date > date:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    
    elif competition_date < date:
        flash("You cannot book in a past competition !")
        return render_template('welcome.html', club=foundClub, competitions=competitions)

    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=foundClub, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    if placesRequired > 12:
        error = "You cannot book more than 12 places."
        return render_template('booking.html', club=club, competition=competition, error=error)
    
    elif placesRequired < 1:
        error = "Please enter a number between 1 and 12 to book places."
        return render_template('booking.html', club=club, competition=competition, error=error)

    else:
        if placesRequired <= int(club['points']):
            club['points'] = int(club['points']) - placesRequired
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)
        
        else:
            error = "You do not have enough points to do that."
            return render_template('booking.html', club=club, competition=competition, error=error)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))