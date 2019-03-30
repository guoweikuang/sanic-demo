import math


class Pagination(object):
    """分页模块
    # ref: http://flask.pocoo.org/snippets/44/
    """
    def __init__(self, page, per_page, total, items):
        self.page = page
        self.per_page = per_page
        self.total = total
        self.items = items

    @property
    def pages(self):
        if self.per_page == 0 or not self.total:
            pages = 0
        else:
            pages = int(math.ceil(self.total / float(self.per_page)))
        return pages

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    @property
    def prev_num(self):
        return self.page - 1 if self.has_prev else None

    @property
    def next_num(self):
        return self.page + 1 if self.has_next else None

    def iter_pages(self, left_edge=2, left_current=2,
                  right_current=5, right_edge=2):
        last = 0
        for num in range(1, self.pages + 1):
            if (
                num <= left_edge or
                self.page - left_current - 1 < num < self.page + right_current or
                num > self.pages - right_edge
            ):
                if last + 1 != num:
                    yield None
                yield num
                last = num