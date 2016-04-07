import sys
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import json
import urllib

class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        mpath,margs = urllib.splitquery(self.path)
        data = {'addr':mpath,'args':margs}
        r_str = str(data)
        enc="UTF-8"
        encoded = ''.join(r_str).encode(enc)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
    
    def de_POST(self):
        mpath,margs = urllib.splitquery(self.path)
        postData = self.rfile.read(self.headers['content-length'])
        data = {'addr':mpath,'args':margs,'postData':postData}
        r_str = str(data)
        enc="UTF-8"
        encoded = ''.join(r_str).encode(enc)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
        
httpd = HTTPServer(('',8000),MyHttpRequestHandler)
print("Server started on 127.0.0.1,port 8000...")
httpd.serve_forever()
