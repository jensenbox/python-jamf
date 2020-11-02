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

import openapi_client
from openapi_client.models.ldap_group_search_results import LdapGroupSearchResults  # noqa: E501
from openapi_client.rest import ApiException

class TestLdapGroupSearchResults(unittest.TestCase):
    """LdapGroupSearchResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LdapGroupSearchResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.ldap_group_search_results.LdapGroupSearchResults()  # noqa: E501
        if include_optional :
            return LdapGroupSearchResults(
                total_count = 3, 
                results = [
                    openapi_client.models.ldap_group.LdapGroup(
                        id = '1', 
                        uuid = '89AF33FC-123C-1231-AEFD-9C3ED123AFCC', 
                        ldap_server_id = 1, 
                        name = 'Grade School Teachers', 
                        distinguished_name = 'Grade School Teachers', )
                    ]
            )
        else :
            return LdapGroupSearchResults(
        )

    def testLdapGroupSearchResults(self):
        """Test LdapGroupSearchResults"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
