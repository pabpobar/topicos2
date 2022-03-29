from http import server
from logging import Handler
import os, sys, http.server
import socketserver
#from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 8000
if len(sys.argv) == 2:
    if sys.argv[1].isnumeric(): PORT = int(sys.argv[1])
else:
    print('Uso: python3 pyserver.py {PUERTO}')
    print(f'>>>> por defecto asigna puerto: {PORT}')

os.chdir('.')
# Por defecto escucha puerto 8000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'\nSirviendo en puerto: {PORT}')
    httpd.serve_forever()
