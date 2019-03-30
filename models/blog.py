from tortoise import Model
from tortoise import fields

class Post(Model):
    class Meta:
        table = 'posts'
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=160)
    author_id = fields.IntField()
    summary = fields.CharField(max_length=160)
    created_time = fields.DatetimeField(auto_now_add=True)
    view = fields.IntField()



