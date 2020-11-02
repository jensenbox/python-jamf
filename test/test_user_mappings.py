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
from openapi_client.models.user_mappings import UserMappings  # noqa: E501
from openapi_client.rest import ApiException

class TestUserMappings(unittest.TestCase):
    """UserMappings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserMappings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.user_mappings.UserMappings()  # noqa: E501
        if include_optional :
            return UserMappings(
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
                user_uuid = 'uid'
            )
        else :
            return UserMappings(
                object_class_limitation = 'ANY_OBJECT_CLASSES',
                object_classes = 'inetOrgPerson',
                search_base = 'ou=Users',
                search_scope = 'ALL_SUBTREES',
                user_id = 'mail',
                username = 'uid',
                real_name = 'displayName',
                email_address = 'mail',
                department = 'departmentNumber',
                building = '0',
                room = '0',
                phone = '0',
                position = 'title',
                user_uuid = 'uid',
        )

    def testUserMappings(self):
        """Test UserMappings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
