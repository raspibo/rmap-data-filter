#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
PORT_NUMBER = 9999


class SummariesJSON(BaseHTTPRequestHandler):
    def do_GET(self):
        print('GET %s' % self.path)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        if self.path in ('/index.html', '/'):
            with open("index.html", 'r') as fd:
                self.wfile.write(fd.read())
        elif self.path.startswith('/summaries'):
            # emulates http://rmap.cc/borinud/api/v1/dbajson/*/*/*/*/*/*/summaries
            with open("summaries.json", 'r') as fd:
                self.wfile.write(fd.read())
        return

server = HTTPServer(('', PORT_NUMBER), SummariesJSON)
print('Started server on http://localhost:%d' % PORT_NUMBER)
server.serve_forever()
