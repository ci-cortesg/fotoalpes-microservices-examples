from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/usarios.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
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
    def get(self):
        posts = User.query.all()
        return users_schema.dump(posts)

    def post(self):
        new_user = User(
            username=request.json['username'],
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)



api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')