#coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define,options
from tornado.web import RequestHandler,url

tornado.options.define("port",type=int ,default=8000,help="server port")

class IndexHandler(RequestHandler):
    def get(self):
        query_args=self.get_query_arguments("q")
        self.write(str(query_args))

if __name__=='__main__':
    tornado.options.parse_command_line()
    app=tornado.web.Application(
        [(r"/",IndexHandler),
        ],
        debug=True
    )

    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()