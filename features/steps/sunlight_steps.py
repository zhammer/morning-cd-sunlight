import json
from datetime import date

from behave import given, then, when

from sunlight.delivery.aws_lambda.get_sunlight_window import handler as sunlight_handler


@given('I live in new york')  # noqa: F811
def step_impl(context):
    context.iana_timezone = 'America/New_York'


@given('today\'s date is November 24th, 2018')  # noqa: F811
def step_impl(context):
    context.todays_date = date(2018, 11, 24)


@given('sunrise is at "{sunrise_utc}" utc')  # noqa: F811
def step_impl(context, sunrise_utc: str):
    context.sunrise_utc = sunrise_utc


@given('sunset is at "{sunset_utc}" utc')  # noqa: F811
def step_impl(context, sunset_utc: str):
    context.sunset_utc = sunset_utc


@when('I request today\'s sunlight window')  # noqa: F811
def step_impl(context):
    event = {
        'queryStringParameters': {
            'on_date': context.todays_date.isoformat(),
            'iana_timezone': context.iana_timezone
        }
    }

    # this will actually send a request to sunrise-sunset api
    context.response = sunlight_handler(event, {})


@then('I get a sunlight window with the values')  # noqa: F811
def step_impl(context):
    expected_sunrise_utc = context.table[0][0]
    expected_sunset_utc = context.table[0][1]

    expected_sunlight_window_response = {
        'sunrise_utc': expected_sunrise_utc,
        'sunset_utc': expected_sunset_utc
    }

    body = json.loads(context.response['body'])
    assert body == expected_sunlight_window_response
