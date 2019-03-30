from tortoise import Tortoise
from config import config


async def init_db(create_db=False):
    await Tortoise.init(
        db_url=config.DB_URL,
        modules={'models': ['models']},
        _create_db=create_db,
    )