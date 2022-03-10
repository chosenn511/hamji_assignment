from urllib.parse import urljoin

from django.conf import settings


def absolutify(url, host, scheme=settings.DEFAULT_HTTP_SCHEME):
    return urljoin("{scheme}://{host}".format(scheme=scheme, host=host), url)


def restify(url):
    return absolutify('/_api{}'.format(url), settings.API_HOST)
