import http

#Create an HTTP server to handle responses */
http.server(request, response)
response.writeHead(200, {"Content-Type": "text/plain"});
response.write("Hello World");
response.end()
respose.listen(8888)