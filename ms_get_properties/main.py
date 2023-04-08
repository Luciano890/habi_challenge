"""Main module for ms_get_properties."""
from config.server import httpd
from config.db import cnx, cursor

try:
    print(
        f'Server started at http://{httpd.server_name}:{httpd.server_port}'
          '; close with (Ctrl + C)'
    )
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Server stopped by user')
    cursor.close()
    cnx.close()
    httpd.server_close()
