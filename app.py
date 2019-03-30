import asyncio

import aiomcache
import aioredis
from sanic import Sanic
from sanic.response import text
from sanic.exceptions import NotFound
from sanic_session import Session, MemcacheSessionInterface

from config import config
from db import context, mako, init_db
from views.index import index

app = Sanic(__name__)
app.config.from_object(config)
app.static('/static', './static')
mako.init_app(app, context_processors={})
session = Session()
redis = None
client = None
app.blueprint(index)


@app.exception(NotFound)
async def ignore_404s(request, exception):
    return text("Oops, That page couldn't found.")


async def server_error_handler(request, exception) -> text:
    print(exception)
    return text("Oops, server error", status=500)

# app.error_handler.add(Exception, server_error_handler)


@app.listener('before_server_start')
async def set_db(app, loop):
    global client
    await init_db()
    client = aiomcache.Client(config.MEMCACHED_HOST,
                              config.MEMCACHED_PORT, loop=loop)
    session.init_app(app, interface=MemcacheSessionInterface(client))
    loop.set_task_factory(context.task_factory)


@app.middleware("request")
async def setup_context(request):
    global redis
    loop = asyncio.get_event_loop()
    if redis is None:
        redis = await aioredis.create_pool(
            config.REDIS_URL, minsize=5, maxsize=20, loop=loop)
    context.set('redis', redis)
    context.set('memcache', client)


if __name__ == '__main__':
    app.run(debug=True)




