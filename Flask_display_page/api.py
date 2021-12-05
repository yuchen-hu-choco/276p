import re
from flask import Flask
from flask_restful import Resource, Api
import jsonify
from flask import Flask, jsonify, make_response, request, abort, render_template, url_for
from flask_bootstrap import Bootstrap
import algo

app = Flask(__name__)
api = Api(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/job_listing')
def jobListing():
	return render_template('job_listing.html')


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/job_listings_get_api', methods=['POST'])
def post():
    print(request.form)
    title = request.form.get("title")
    if title is None:
        title = "Software Engineer"
    location = request.form.get("location")
    if location is None:
        location = " "
    education = request.form.get("education")
    years = request.form.get("years")
    skills = request.form.get("skills")
    if skills is None:
        skills = " "
    employment = request.form.get("employment")
    result = algo.getRecommendation(title, location, education, years, skills, employment)
    print(result)
    return render_template('job_listing.html', list = result)


if __name__ == '__main__':
    app.run(debug=True)


jobs = [
    {
        'img': "1",
        'title': 'Software Engineer',
        'company': 'Galaxy Systems, Inc.',
        'location': 'Mountain View, CA, United States'
    },
    {
        'img': "2",
        'title': 'Software Engineer',
        'company': 'Genesis10',
        'location': 'Frankfurt, Germany'
    },
    {
        'img': "3",
        'title': 'Site Reliability Engineer',
        'company': 'Digital Intelligence Systems, LLC',
        'location': 'Singapore'
    },
    {
        'img': "4",
        'title': 'Software Engineer',
        'company': 'Tellus Solutions',
        'location': 'Sunnyvale, CA, United States'
    },
    {
        'img': "5",
        'title': 'Software Engineer',
        'company': 'TransTech LLC',
        'location': 'Sunnyvale, CA, United States'
    },
    {
        'img': "6",
        'title': 'Site Reliability Engineer',
        'company': 'Noble1',
        'location': 'San Francisco, CA, United States'
    },
    {
        'img': "7",
        'title': 'QA Engineer',
        'company': 'Maxonic, Inc.',
        'location': 'Seattle, WA, United States'
    },
    {
        'img': "8",
        'title': 'Software Engineer',
        'company': 'VanderHouwen & Associates, Inc.',
        'location': 'Paris, France'
    },
    {
        'img': "9",
        'title': 'Software Engineer',
        'company': 'Eastridge Workforce Solutions',
        'location': 'Gurugram, India'
    },
    {
        'img': "10",
        'title': 'Software Engineer',
        'company': 'Collabera',
        'location': 'New York, NY, United States'
    },
]