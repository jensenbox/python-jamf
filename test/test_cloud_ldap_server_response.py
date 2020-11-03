# coding: utf-8

"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import jamf
from jamf.models.cloud_ldap_server_response import CloudLdapServerResponse  # noqa: E501
from jamf.rest import ApiException

class TestCloudLdapServerResponse(unittest.TestCase):
    """CloudLdapServerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CloudLdapServerResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.cloud_ldap_server_response.CloudLdapServerResponse()  # noqa: E501
        if include_optional :
            return CloudLdapServerResponse(
                id = '1001', 
                enabled = True, 
                provider_name = 'Google', 
                display_name = 'Google Secure LDAP', 
                server_url = 'ldap.google.com', 
                domain_name = 'jamf.com', 
                port = 636, 
                keystore = jamf.models.cloud_ldap_keystore.CloudLdapKeystore(
                    type = 'PKCS12', 
                    expiration_date = '2030-02-21T12:05:47.244Z', 
                    subject = 'ST=California, C=US, OU=GSuite, CN=LDAP Client, L=Mountain View, O=Google Inc.', 
                    file_name = 'keystore.p12', ), 
                connection_timeout = 15, 
                search_timeout = 60, 
                use_wildcards = True, 
                connection_type = 'LDAPS'
            )
        else :
            return CloudLdapServerResponse(
        )

    def testCloudLdapServerResponse(self):
        """Test CloudLdapServerResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
