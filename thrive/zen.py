import requests
# Make a GET request to the ZenQuotes API
response = requests.get("https://zenquotes.io/api/today/")
# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response to extract the quote
    data = response.json()[0]
    quote = data["q"]
    author = data["a"]
    print(f"{quote} - {author}")
else:
    print("Error: Unable to retrieve quote")






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
