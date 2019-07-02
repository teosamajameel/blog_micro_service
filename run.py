from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
API = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///APP.DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
DB = SQLAlchemy(app)
ENCRYPT_RESPONSE = False
# import views
import resources


@app.before_first_request
def create_tables():
    DB.create_all()


API.add_resource(resources.CreateBlog, '/create_blog')
API.add_resource(resources.RetrieveBlogs, '/retrieve_blog/<int:user_id>')
API.add_resource(resources.AllBlogs, '/blogs')

# API.add_resource(resources.UserLogin, '/login')
# API.add_resource(resources.UserLogoutAccess, '/logout/access')
# API.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
# API.add_resource(resources.TokenRefresh, '/token/refresh')

# API.add_resource(resources.CreateTeacher, '/create_teacher')
# API.add_resource(resources.RetrieveTeacher, '/retrieve_teacher')
# API.add_resource(resources.UpdateTeacher, '/update_teacher')
# API.add_resource(resources.DeleteTeacher, '/delete_teacher')
