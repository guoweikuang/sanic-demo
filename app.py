from sanic import Sanic
from sanic import request
from sanic.response import text
from sanic.exceptions import NotFound

from config import config
from db import init_db

app = Sanic(__name__)
app.config.from_object(config)


@app.exception(NotFound)
async def ignore_404s(request, exception):
    return text("Oops, That page couldn't found.")


async def server_error_handler(request, exception) -> text:
    return text("Oops, server error", status=500)

app.error_handler.add(Exception, server_error_handler)


@app.listener('before_server_start')
async def set_db(app, loop):
    await init_db()


if __name__ == '__main__':
    app.run()




