import json
import os
from datetime import date
from typing import Dict

from aws_xray_sdk.core import patch

import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

from sunlight import use_sunlight_windows
from sunlight.definitions import exceptions
from sunlight.delivery.aws_lambda import util


if os.environ.get('AWS_EXECUTION_ENV'):
    # setup sentry
    sentry_sdk.init(
        dsn="https://e29ca6959f374a3d8381fc6e15316caa@sentry.io/1357226",
        integrations=[AwsLambdaIntegration()]
    )

    # setup xray patching
    libraries = ('requests',)
    patch(libraries)


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
