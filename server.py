from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import socketserver
from template import Template

class RequestHandler(SimpleHTTPRequestHandler, object):
    def do_GET(self):
        template = Template()
        template.render()
        self.path = 'jinja2_test'
        super(RequestHandler, self).do_GET()

class Server:
    def __init__(self, port=8000, address="", handler = SimpleHTTPRequestHandler):
        self.address = address
        self.port = port
        self.handler = handler

    #def run(self, server_class=HTTPServer):
    def run(self):
        # server_address = (self.address, self.port)
        # httpd = server_class(server_address, BaseHTTPRequestHandler)
        # httpd.serve_forever()
        with socketserver.TCPServer((self.address, self.port), self.handler) as httpd:
            httpd.serve_forever()

#http://localhost:8000
if __name__ == "__main__":
    server = Server(handler = RequestHandler)
    server.run()