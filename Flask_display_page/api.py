from flask import Flask
from flask_restful import Resource, Api
import jsonify
from flask import Flask, jsonify, make_response, request, abort, render_template, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
api = Api(app)
bootstrap = Bootstrap(app)

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


@app.route('/job_listings_get_api', methods=['GET'])
def getjobs():
	return jsonify({'jobs': jobs})

@app.route('/test')
def test():
	return render_template('test.html')



# @app.route('/todo/api/addTask', methods=['POST'])
# def add_task():
# 	if request.json['title'] == "":
# 		abort(400)
# 	task = {
# 		'id' : tasks[-1]['id'] + 1,
# 		'title': request.json['title'],
# 		'description' : request.json.get('description', ""),
# 		'done' : False
# 	}
# 	tasks.append(task)
# 	return jsonify({'tasks': tasks}), 201

# @app.route('/todo/api/deleteTask', methods=['POST'])
# def delete_task():
# 	task_id = request.json['id']
# 	for task in tasks:
# 		if task['id'] == task_id:
# 			tasks.remove(task)
# 			return jsonify({'tasks': tasks}), 201


# #404
# @app.errorhandler(404)
# def not_found(error):
# 	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
