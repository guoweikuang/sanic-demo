import aiotask_context as context
from tortoise import Tortoise
from sanic_mako import SanicMako

from config import config

mako = SanicMako()


async def init_db(create_db=False):
    await Tortoise.init(
        db_url=config.DB_URL,
        modules={'models': ['models']},
        _create_db=create_db,
    )