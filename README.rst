certstore
=========

Platform independent access to system certificate store.


Installation
------------

``certstore`` is available on PyPI.::

    $ pip install certstore

Usage
-----

Access and use system certificate bundle::

    >>> import certstore
    >>> import requests

    >>> certstore.ca_bundle
    '/path/to/system/store/ca.pem'

    >>> requests.get('https://some.domain.com', verify=certstore.ca_bundle)
