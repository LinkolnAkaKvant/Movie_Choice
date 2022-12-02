from flask_restx import Resource, Namespace
from flask import request

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('user')


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        result = UserSchema().dump(user)
        return result, 200

    def put(self, uid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = uid

        user_service.update(request_json)
        return "", 204

