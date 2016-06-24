certstore
=========

Platform independent access to OS certificate store.


Installation
------------

``certstore`` is available on PyPI.::

    $ pip install certstore

Usage
-----

Access and use OS certificate bundle::

    >>> import certstore
    >>> import requests

    >>> certstore.ca_bundle
    '/usr/local/lib/python2.7/site-packages/certifi/cacert.pem'

    >>> requests.get('https://github.com', verify=certstore.ca_bundle)
