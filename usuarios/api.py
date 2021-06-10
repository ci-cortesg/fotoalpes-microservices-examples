from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from redis import Redis
from rq import Queue
from sender import send_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/usarios.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

q = Queue(connection=Redis(host='redis', port=6379, db=0))


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
        q.enqueue(send_user, user_schema.dump(new_user))
        return user_schema.dump(new_user)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)



api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
