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
from openapi_client.api.sso_settings_api import SsoSettingsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestSsoSettingsApi(unittest.TestCase):
    """SsoSettingsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.sso_settings_api.SsoSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_sso_dependencies_get(self):
        """Test case for v1_sso_dependencies_get

        Retrieve the list of Enrollment Customizations using SSO   # noqa: E501
        """
        pass

    def test_v1_sso_disable_post(self):
        """Test case for v1_sso_disable_post

        Disable SSO   # noqa: E501
        """
        pass

    def test_v1_sso_get(self):
        """Test case for v1_sso_get

        Retrieve the current Single Sign On configuration settings   # noqa: E501
        """
        pass

    def test_v1_sso_history_get(self):
        """Test case for v1_sso_history_get

        Get SSO history object   # noqa: E501
        """
        pass

    def test_v1_sso_history_post(self):
        """Test case for v1_sso_history_post

        Add SSO history object notes   # noqa: E501
        """
        pass

    def test_v1_sso_metadata_download_get(self):
        """Test case for v1_sso_metadata_download_get

        Download the Jamf Pro SAML metadata file   # noqa: E501
        """
        pass

    def test_v1_sso_put(self):
        """Test case for v1_sso_put

        Updates the current Single Sign On configuration settings   # noqa: E501
        """
        pass

    def test_v1_sso_validate_post(self):
        """Test case for v1_sso_validate_post

        Endpoint for validation of a saml metadata url   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()