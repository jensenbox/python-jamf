# coding: utf-8

"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.jamf_pro_initialization_preview_api import JamfProInitializationPreviewApi  # noqa: E501
from openapi_client.rest import ApiException


class TestJamfProInitializationPreviewApi(unittest.TestCase):
    """JamfProInitializationPreviewApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.jamf_pro_initialization_preview_api.JamfProInitializationPreviewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_system_initialize_database_connection_post(self):
        """Test case for system_initialize_database_connection_post

        Provide Database Password during startup   # noqa: E501
        """
        pass

    def test_system_initialize_post(self):
        """Test case for system_initialize_post

        Set up fresh installed Jamf Pro Server   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()