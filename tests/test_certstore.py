"""pytests for certstore package."""
import os

import certstore


def test_bundle_exists():
    assert os.path.isfile(certstore.ca_bundle)
