# Tornado server to access WT chat client

import os
import tornado.web
import tornado.ioloop

SERVER_PORT = 8880

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('web/tekton_client_webpage.html')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
        ]
        settings = {
            "debug": True,
            "static_path": os.path.join(os.path.dirname(__file__), "web")
        }
        tornado.web.Application.__init__(self, handlers, **settings)


http_server = tornado.httpserver.HTTPServer(Application())
http_server.listen(SERVER_PORT)
tornado.ioloop.IOLoop.instance().start()
tornado.ioloop.IOLoop.current().start()
