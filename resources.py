from flask_restful import Resource, reqparse

from models import BlogModel

blog_parser = reqparse.RequestParser()
blog_parser.add_argument('user_id', help='This field cannot be blank', required=True)
blog_parser.add_argument('title', help='This field cannot be blank', required=True)
blog_parser.add_argument('body', help='This field cannot be blank', required=True)
blog_parser.add_argument('total_views', help='This field cannot be blank', required=False)


class CreateBlog(Resource):
    def post(self):
        data = blog_parser.parse_args()

        total_views = 0
        if 'total_views' in data:
            total_views = data['total_views']
        print(data)
        new_blog = BlogModel(
            user_id=data['user_id'],
            title=data['title'],
            body=data['body'],
            total_views=total_views
        )
        try:
            new_blog.save_to_db()
            return {
                'message': 'New Blog {} was created'.format(data['title'])
            }
        except:
            return {'message': 'Something went wrong'}, 500
        return data


class RetrieveBlogs(Resource):
    def get(self, user_id):
        try:
            return BlogModel.find_by_user_id(user_id)
        except:
            return {'message': 'Something went wrong'}, 500


class AllBlogs(Resource):
    def get(self):
        return BlogModel.return_all()

    def delete(self):
        return BlogModel.delete_all()
