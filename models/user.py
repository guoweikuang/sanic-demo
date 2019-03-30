from tortoise import Model
from tortoise import fields
from werkzeug.security import generate_password_hash, check_password_hash


class User(Model):
    class Meta:
        table = 'users'

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    email = fields.CharField(max_length=100)
    password_hash = fields.TextField()

    def _get_password(self):
       raise AttributeError("Password not allow to reading")

    def _set_password(self, password):
       self.password_hash = generate_password_hash(password)

    password = property(_get_password, _set_password)


async def create_user(**kwargs):
    """create user

    :param kwargs:
    :return:
    """
    kwargs['password_hash'] = generate_password_hash(kwargs.pop('password'))
    kwargs['username'] = kwargs.pop('name')
    user = await User.create(**kwargs)
    return user