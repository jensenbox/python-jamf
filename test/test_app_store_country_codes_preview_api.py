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
from jamf.api.app_store_country_codes_preview_api import AppStoreCountryCodesPreviewApi  # noqa: E501
from jamf.rest import ApiException


class TestAppStoreCountryCodesPreviewApi(unittest.TestCase):
    """AppStoreCountryCodesPreviewApi unit test stubs"""

    def setUp(self):
        self.api = jamf.api.app_store_country_codes_preview_api.AppStoreCountryCodesPreviewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_app_store_country_codes_get(self):
        """Test case for v1_app_store_country_codes_get

        Return a list of Countries and the associated Codes   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
