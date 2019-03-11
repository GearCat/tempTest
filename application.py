import tornado.web
from views import index
import config


class Applicatioin(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/home', index.HomeHandler),
            (r'/func', index.FuncHandler),
            (r'/trans', index.TransHandler),
            (r'/cart', index.CartHandler),
        ]
        super(Applicatioin, self).__init__(handlers, **config.settings)