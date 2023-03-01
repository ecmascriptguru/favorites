import requests
from atexit import register
from functools import singledispatch
from ratelimit import limits, sleep_and_retry


FIFTEEN_MINUTES = 900


@sleep_and_retry
@limits(calls=15, period=FIFTEEN_MINUTES)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    return response


def run():
    pass


@register
def terminate():
    run()
    print("Goodbye!")


@singledispatch
def fun(arg):
    print("Called with a single argument")


@fun.register(int)
def _(arg):
    print("Called with an integer")


@fun.register(list)
def _(arg):
    print("Called with a list")


if __name__ == '__main__':
    pass
