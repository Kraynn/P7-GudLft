import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime


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
        flash('Invalid email - Try again with a registered email')
        return redirect(url_for('index'))


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        if datetime.strptime(foundCompetition['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
            flash("Competition closed - Try another one")
            return render_template('welcome.html', club=foundClub, competitions=competitions)
        else:
            return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong - Please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    points_available = int(club['points'])
    placesRequired = int(request.form['places'])
    if placesRequired <= 12 and int(competition['numberOfPlaces']) > 0:
        if placesRequired <= points_available:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
            flash('Great - Booking complete ')
            if competition['numberOfPlaces'] >= 0 and placesRequired <= points_available:
                club['points'] = points_available - placesRequired
                flash('You have reserved {} places.'.format(placesRequired))
        else:
            flash('Booking incomplete - Not enough places in your wallet ')
    else:
        if competition['numberOfPlaces'] > 0:
            flash('Booking incomplete - 12 places maximum allowed ')
        else:
            flash('Booking incomplete - The competition is full ')    
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/displayClubs')
def displayClubs():
    return render_template('clubs.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))