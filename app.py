import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

class RH(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		message = ['test1' + 'Client: ' + self.address_string() + '<br>',
					'Server: ' + IP + ' aka ' + hostname + '<br>',
					'Date: ' + self.date_time_string() + '<br>' + '\n']
		for i in message:
			print(i)
			self.wfile.write(bytes(i, "utf8"))
		return

def run():
	server_address = (IP, 8080)
	httpd = HTTPServer(server_address, RH)
	httpd.serve_forever()
run()
