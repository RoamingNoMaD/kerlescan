from http.client import responses

from connexion.lifecycle import ConnexionRequest, ConnexionResponse
from connexion.problem import problem


def handle_http_error(request: ConnexionRequest, error) -> ConnexionResponse:
    return problem(
        title=responses[error.status_code],
        detail=error.message,
        status=error.status_code,
    )
