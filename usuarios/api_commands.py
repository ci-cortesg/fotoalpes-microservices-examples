from base import app, api, ma, db, User, user_schema, users_schema, q, Resource, Flask, request
from sender import send_user

class UserListResource(Resource):
    def post(self):
        new_user = User(
            username=request.json['username'],
        )
        db.session.add(new_user)
        db.session.commit()
        q.enqueue(send_user, user_schema.dump(new_user))
        return user_schema.dump(new_user)



api.add_resource(UserListResource, '/api-commands/users')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
