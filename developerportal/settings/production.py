from urllib.parse import urlparse

from .base import *  # noqa

DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = []

if BASE_URL:
    # This is the URL that Wagtail's CMS runs on.
    ALLOWED_HOSTS.append(urlparse(BASE_URL).hostname)

if CDN_URL:
    # This is the URL the CDNed site will be served from.
    # It is different from the BASE_URL (where Wagtail is running).
    ALLOWED_HOSTS.append(urlparse(CDN_URL).hostname)

if SUPPLEMENTARY_URL:
    # This is the URL of an additional CDN/hostname to front the site,
    # useful for domain switchover
    # It is different from the BASE_URL (where Wagtail is running) and the CDN_URL
    ALLOWED_HOSTS.append(urlparse(SUPPLEMENTARY_URL).hostname)

try:
    from .local import *  # noqa
except ImportError:
    pass
