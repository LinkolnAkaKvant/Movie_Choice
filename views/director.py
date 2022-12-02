from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        director = director_service.get_all()
        result = DirectorSchema(many=True).dump(director)
        return result, 200


@directors_ns.route("/<int:did>")
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_by_id(did)
        result = DirectorSchema().dump(director)
        return result, 200
