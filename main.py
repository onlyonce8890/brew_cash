"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
app = Flask(__name__)
from flask import request
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
from flask import render_template

@app.route('/')
def home():
	return render_template("home.html")


@app.route('/', methods=['POST'])
def my_form_post():
    beers_per_week = float(request.form['beers_per_week'])
    cost_per_beer = request.form['cost_per_beer']
    weekly_spend = float(beers_per_week) * float(cost_per_beer)
    monthly_spend = float(weekly_spend * 4)
    yearly_spend = float(monthly_spend * 12)
    cost_per_20l_homebrew = float(request.form['cost_per_20l_homebrew'])
    cost_per_homebrew = cost_per_20l_homebrew / 40
    homebrew_yearly_spend = float(((cost_per_homebrew * beers_per_week) * 4 ) * 12)
    print type(yearly_spend)
    print type(homebrew_yearly_spend)
    homebrew_yearly_savings = yearly_spend - homebrew_yearly_spend
    return render_template("results.html",
    	beers_per_week = int(beers_per_week),
    	cost_per_beer = int(cost_per_beer),
    	weekly_spend = int(weekly_spend),
    	monthly_spend = int(monthly_spend),
    	yearly_spend = int(yearly_spend),
    	homebrew_yearly_spend = int(homebrew_yearly_spend),
    	homebrew_yearly_savings = int(homebrew_yearly_savings)

    	)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Damn it. Something went wrong.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
