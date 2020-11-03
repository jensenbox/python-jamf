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
from jamf.models.cloud_ldap_configuration_response import CloudLdapConfigurationResponse  # noqa: E501
from jamf.rest import ApiException

class TestCloudLdapConfigurationResponse(unittest.TestCase):
    """CloudLdapConfigurationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CloudLdapConfigurationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.cloud_ldap_configuration_response.CloudLdapConfigurationResponse()  # noqa: E501
        if include_optional :
            return CloudLdapConfigurationResponse(
                id = '1001', 
                server = jamf.models.cloud_ldap_server_response.CloudLdapServerResponse(
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
                    connection_type = 'LDAPS', ), 
                mappings = jamf.models.cloud_ldap_mappings_response.CloudLdapMappingsResponse(
                    user_mappings = jamf.models.user_mappings.UserMappings(
                        object_class_limitation = 'ANY_OBJECT_CLASSES', 
                        object_classes = 'inetOrgPerson', 
                        search_base = 'ou=Users', 
                        search_scope = 'ALL_SUBTREES', 
                        additional_search_base = '0', 
                        user_id = 'mail', 
                        username = 'uid', 
                        real_name = 'displayName', 
                        email_address = 'mail', 
                        department = 'departmentNumber', 
                        building = '0', 
                        room = '0', 
                        phone = '0', 
                        position = 'title', 
                        user_uuid = 'uid', ), 
                    group_mappings = jamf.models.group_mappings.GroupMappings(
                        object_class_limitation = 'ANY_OBJECT_CLASSES', 
                        object_classes = 'groupOfNames', 
                        search_base = 'ou=Groups', 
                        search_scope = 'ALL_SUBTREES', 
                        group_id = 'cn', 
                        group_name = 'cn', 
                        group_uuid = 'gidNumber', ), 
                    membership_mappings = jamf.models.membership_mappings.MembershipMappings(
                        group_membership_mapping = 'memberOf', ), )
            )
        else :
            return CloudLdapConfigurationResponse(
                id = '1001',
                server = jamf.models.cloud_ldap_server_response.CloudLdapServerResponse(
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
                    connection_type = 'LDAPS', ),
        )

    def testCloudLdapConfigurationResponse(self):
        """Test CloudLdapConfigurationResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
