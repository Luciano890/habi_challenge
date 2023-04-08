"""Server for the ms_get_properties."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from common.enums import HTTPStatus
from core.urls import router
from settings import PORT, HOST


def load_views(params: dict[str, str], /) -> None:
    """Load views.
    
    Parameters:
        * params (dict[str, str]): Parameters to load the views.
    """
    for path, view in router.views.items():
        types = view.__annotations__
        params = {param: types[param](value) for param, value in params.items()}
        router.saved_responses[path] = {
            "full_path": \
                f"{path}?"
                f"{'&'.join([f'{key}={value}' for key, value in params.items()])}",
            "response": view(**params)
        }


class APIHandler(BaseHTTPRequestHandler):
    """Handler for the ms_get_properties."""
    def do_GET(self):
        """Handle GET requests."""
        try:
            params = self.path.split("?")[1].split("&")
            params_data = {}
            for param in params:
                if "=" in param:
                    key, value = param.split('=')
                    params_data[key] = value
                else:
                    params_data[param] = None
        except IndexError:
            params_data = {}
        load_views(params_data)
        message = router.saved_responses.get(self.path.split("?")[0], {})
        self.send_response(
            HTTPStatus.HTTP_200_OK.value if message else HTTPStatus.HTTP_404_NOT_FOUND.value
        )
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(
            bytes(
                json.dumps(message.get("response") or {"message": "Not Found."}),
                "utf8"
            )
        )

server_address = (HOST, PORT)
httpd = HTTPServer(server_address, APIHandler)
