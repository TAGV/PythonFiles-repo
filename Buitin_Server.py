# Python has a HTTP server built into the
# standard library. This is super handy for
# previewing websites.
import http.server
import socketserver



PORT = 8000
handler = http.server.SimpleHTTPRequestHandler



# http://127.0.0.1:8000/
# http://0.0.0.0:8000/
with socketserver.TCPServer(("",PORT),handler) as httpd:
    print("Port available at : ",PORT)
    httpd.serve_forever()