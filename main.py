#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Test con [Tornado](http://www.tornadoweb.org)
http://stackoverflow.com/questions/5375220/how-do-i-stop-tornado-web-server
Incapsulo l'intero web server in un thread separato

Luca Bacchi <bacchilu@gmail.com> - http://www.lucabacchi.it
"""

import tornado.ioloop
import tornado.web


class Handler(tornado.web.RequestHandler):

    c = 0

    def get(self, d):
        Handler.c += 1
        print d, Handler.c
        self.write('OK\n')


class TornadoWebServer(object):

    @staticmethod
    def _startTornado():
        application = tornado.web.Application([(r'/(.*)', Handler)])
        application.listen(13100)
        tornado.ioloop.IOLoop.instance().start()

    @staticmethod
    def start():
        import threading
        TornadoWebServer.t = \
            threading.Thread(target=TornadoWebServer._startTornado)
        TornadoWebServer.t.setDaemon(True)
        TornadoWebServer.t.start()

    @staticmethod
    def stop():
        tornado.ioloop.IOLoop.instance().stop()
        TornadoWebServer.t.join()


if __name__ == '__main__':
    import time

    TornadoWebServer.start()

    print 'Your web server will self destruct in 1 minute'
    time.sleep(60)

    TornadoWebServer.stop()
