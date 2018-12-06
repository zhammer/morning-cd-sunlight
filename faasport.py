import json
from typing import Dict

from faaspact_verifier import faasport, provider_state  # noqa: F401
from faaspact_verifier.definitions import Request, Response

from sunlight.delivery.aws_lambda.get_sunlight_window import handler


@faasport
def port(request: Request) -> Response:
    event = _build_aws_event(request)
    aws_response = handler(event, {})
    return _pluck_response(aws_response)


def _pluck_response(aws_response: Dict) -> Response:
    if 'body' in aws_response:
        body = json.loads(aws_response['body'])
    else:
        body = None

    return Response(
        headers=aws_response.get('headers', {}),
        status=aws_response['statusCode'],
        body=body
    )


def _build_aws_event(request: Request) -> Dict:
    return {
        'headers': request.headers,
        'path': request.path,
        'httpMethod': request.method,
        'body': request.body,
        'queryStringParameters': {field: value[0] for field, value in request.query.items()}
    }
