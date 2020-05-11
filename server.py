from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import socketserver

class Server:
    def __init__(self, port=8000, address=""):
        self.address = address
        self.port = port
        self.handler = SimpleHTTPRequestHandler

    def run(self, server_class=HTTPServer):
        # server_address = (self.address, self.port)
        # httpd = server_class(server_address, BaseHTTPRequestHandler)
        # httpd.serve_forever()
        with socketserver.TCPServer((self.address, self.port), self.handler) as httpd:
            httpd.serve_forever()

#http://localhost:8000
if __name__ == "__main__":
    server = Server()
    server.run()