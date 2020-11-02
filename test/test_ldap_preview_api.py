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
from openapi_client.api.ldap_preview_api import LdapPreviewApi  # noqa: E501
from openapi_client.rest import ApiException


class TestLdapPreviewApi(unittest.TestCase):
    """LdapPreviewApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.ldap_preview_api.LdapPreviewApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ldap_groups_get(self):
        """Test case for ldap_groups_get

        Retrieve the configured access groups that contain the text in the search param   # noqa: E501
        """
        pass

    def test_ldap_servers_get(self):
        """Test case for ldap_servers_get

        Retrieve all LDAP Servers including Cloud Identity Providers   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()