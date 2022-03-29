import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 8000
if len(sys.argv) == 2 and sys.argv[1].isnumeric(): PORT = int(sys.argv[1])
else:
    print('Uso: python3 pyserver.py {PUERTO}')
    print(f'>>>> por defecto asigna puerto: {PORT}')

os.chdir('.')
# Por defecto escucha puerto 8000
with HTTPServer(server_address=('', PORT), RequestHandlerClass=CGIHTTPRequestHandler) as httpd:
    print(f'\nSirviendo en puerto: {PORT}')
    # iniciar server
    httpd.serve_forever()
