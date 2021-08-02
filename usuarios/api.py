from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/usarios.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.config["JWT_SECRET_KEY"] = "secret-jwt"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

jwt = JWTManager(app)
api = Api(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)



class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "username")


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserListResource(Resource):
    @jwt_required()
    def get(self):
        posts = User.query.all()
        return users_schema.dump(posts)
    @jwt_required()
    def post(self):
        new_user = User(
            username=request.json['username'],
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)


class UserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)



api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', ssl_context='adhoc')