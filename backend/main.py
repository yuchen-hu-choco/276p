from flask import Flask, request
from flask_restful import Api, Resource

import algo


class RecommendationMaker(Resource):
    def get(self):
        return {"Data": "Hello world"}

    def post(self):
        title = request.form.get("title")
        location = request.form.get("location")
        education = request.form.get("education")
        years = request.form.get("years")
        skills = request.form.get("skills")
        employment = request.form.get("employment")
        return algo.getRecommendation(title, location, education, years, skills, employment)


def main():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(RecommendationMaker, "/recommendation")
    if __name__ == '__main__':
        app.run(debug=True)

main()
