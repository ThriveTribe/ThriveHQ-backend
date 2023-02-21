# from http.server import BaseHTTPRequestHandler
# from urllib import parse
# import requests
#
#
# class handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         s = self.path
#         url = "https://zenquotes.io/api/today"
#         r = requests.get(url)
#         data = r.json()
#         print(data)
#
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#
#         self.wfile.write(message.encode())
#
#         return
