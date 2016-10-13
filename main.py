"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
# import pygal
app = Flask(__name__)
from flask import request
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
from flask import render_template

@app.route('/')
def home():
	return render_template("home.html")


@app.route('/', methods=['POST'])
def calculate():
    beers_per_week = float(request.form['beers_per_week'])
    cost_per_beer = float(request.form['cost_per_beer'])
    weekly_spend = float(beers_per_week) * float(cost_per_beer)
    monthly_spend = float(weekly_spend * 4)
    yearly_spend = float(monthly_spend * 12)
    cost_per_20l_homebrew = float(request.form['cost_per_20l_homebrew'])
    cost_per_homebrew = cost_per_20l_homebrew / 40
    homebrew_yearly_spend = float(((cost_per_homebrew * beers_per_week) * 4 ) * 12)
    homebrew_yearly_savings = yearly_spend - homebrew_yearly_spend
    tweet_text = "Does homebrewing save money? Find out with #brew_cash"
    

    return render_template("results.html",
    	beers_per_week = int(beers_per_week),
    	cost_per_beer = float(cost_per_beer),
    	weekly_spend = float(weekly_spend),
    	monthly_spend = float(monthly_spend),
    	yearly_spend = float(yearly_spend),
    	homebrew_yearly_spend = float(homebrew_yearly_spend),
    	homebrew_yearly_savings = float(homebrew_yearly_savings),
        tweet_text = tweet_text
    	)

    

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Damn it. Something went wrong.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
