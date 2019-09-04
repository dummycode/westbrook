import os

from http.server import BaseHTTPRequestHandler, HTTPServer
from stats import isAveragingTripleDouble

class MyHTTPServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """ GET """
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # A simple "Is he?"
        content = str(isAveragingTripleDouble())
        # Write content as utf-8 data
        self.wfile.write(bytes(content, "utf8"))

        return

# Server settings
__server_address__ = ('127.0.0.1', int(os.environ.get("PORT", 17995)))
__httpd__ = HTTPServer(__server_address__, MyHTTPServerRequestHandler)
__httpd__.serve_forever()
