import tornado.ioloop
import tornado.httpserver
import config
from views import index
from application import Applicatioin

if __name__ == "__main__":
    app = Applicatioin()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options["port"])
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()