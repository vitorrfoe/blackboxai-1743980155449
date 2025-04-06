from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
import time

locations = {}

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        
        if parsed.path == '/update-location':
            code = query.get('code', [''])[0]
            lat = float(query.get('lat', [0])[0])
            lng = float(query.get('lng', [0])[0])
            
            locations[code] = {
                'lat': lat,
                'lng': lng,
                'timestamp': time.time()
            }
            
            self.send_response(200)
            self.end_headers()
            
        elif parsed.path == '/get-location':
            code = query.get('code', [''])[0]
            location = locations.get(code, {})
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(location).encode())
            
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting location server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()