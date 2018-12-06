import json
from datetime import date
from typing import Dict

from sunlight import use_sunlight_windows
from sunlight.definitions import exceptions
from sunlight.delivery.aws_lambda import util


def handler(event: Dict, context: Dict) -> Dict:
    try:
        on_date = date.fromisoformat(event['queryStringParameters']['on_date'])
        iana_timezone = event['queryStringParameters']['iana_timezone']
    except (KeyError, ValueError):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Bad request'})
        }

    sunlight_context = util.create_default_context()

    try:
        sunlight_window = use_sunlight_windows.get_sunlight_window(
            sunlight_context,
            iana_timezone,
            on_date
        )
    except exceptions.InvalidIanaTimezoneError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': str(e)})
        }

    body = json.dumps(sunlight_window._asdict(), default=lambda v: v.isoformat())
    return {
        'statusCode': 200,
        'body': body
    }
