from run import DB


class BlogModel(DB.Model):
    __tablename__ = 'blogs'

    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.Integer, nullable=False)
    total_views = DB.Column(DB.Integer, default=0)
    title = DB.Column(DB.Text, nullable=False)
    body = DB.Column(DB.Text, nullable=False)

    def save_to_db(self):
        DB.session.add(self)
        DB.session.commit()

    @staticmethod
    def to_json(x):
        return {
            'blog_id': x.id,
            'user_id': x.user_id,
            'title': x.title,
            'body': x.body,
            'total_views': x.total_views
        }

    @classmethod
    def get_blog(cls, user_id, blog_id):
        return cls.query.filter_by(user_id=user_id, id=blog_id).first()

    def delete_from_db(self):
        # deleting the record and updating the DB
        blog_id = self.id
        DB.session.delete(self)
        DB.session.commit()
        return blog_id

    @classmethod
    def find_by_user_id(cls, user_id):
        return {'blogs': list(map(lambda x: BlogModel.to_json(x), cls.query.filter_by(user_id=user_id)))}

    @classmethod
    def return_all(cls):
        return {'blogs': list(map(lambda x: BlogModel.to_json(x), BlogModel.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = DB.session.query(cls).delete()
            DB.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}
