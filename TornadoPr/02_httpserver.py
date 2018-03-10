#coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hell ,tornado!")

if __name__=='__main__':
    app=tornado.web.Application([(r"/",IndexHandler),])
    #修改绑定端口部分app.listen(8000)
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()