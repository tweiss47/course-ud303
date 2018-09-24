#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First determine the response body
        body = "Hello, HTTP!\n".encode()

        # Send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()

        # Now, write the response body.
        self.wfile.write(body)

if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
