# coding: utf-8

"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import jamf
from jamf.api.cache_settings_api import CacheSettingsApi  # noqa: E501
from jamf.rest import ApiException


class TestCacheSettingsApi(unittest.TestCase):
    """CacheSettingsApi unit test stubs"""

    def setUp(self):
        self.api = jamf.api.cache_settings_api.CacheSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_cache_settings_get(self):
        """Test case for v1_cache_settings_get

        Get Cache Settings   # noqa: E501
        """
        pass

    def test_v1_cache_settings_put(self):
        """Test case for v1_cache_settings_put

        Update Cache Settings   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
