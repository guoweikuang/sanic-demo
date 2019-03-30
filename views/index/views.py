from . import index
from db import mako

from config import config
from models import Post
from common.utils import Pagination


@index.route('/')
async def index(request):
    posts = await _posts(request)
    return posts


@mako.template('index.html')
async def _posts(request, page=1):
    start = (page -1) * config.PER_PAGE
    posts = await Post.all()
    page_posts = posts[start: start+config.PER_PAGE]
    pagination = Pagination(page, config.PER_PAGE,
                            len(posts), page_posts)
    return {'paginatior': pagination}

