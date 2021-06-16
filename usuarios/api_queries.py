from base import app, api, ma, db, User, user_schema, users_schema, q, Resource, Flask, request
from sender import send_user

class UserListResource(Resource):
    def get(self):
        posts = User.query.all()
        return users_schema.dump(posts)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)



api.add_resource(UserListResource, '/api-queries/users')
api.add_resource(UserResource, '/api-queries/users/<int:user_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
