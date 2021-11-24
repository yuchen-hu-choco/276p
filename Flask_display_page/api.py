from flask import Flask
from flask_restful import Resource, Api
import jsonify
from flask import Flask, jsonify, make_response, request, abort, render_template, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
api = Api(app)
bootstrap = Bootstrap(app)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
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

# @app.route('/todo/api/tasks', methods=['GET'])
# def getTasks():
# 	return jsonify({'tasks': tasks})

# #POST方法API，添加数据项
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

# #POST方法API，删除数据项
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
