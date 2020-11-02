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
from openapi_client.models.authorization_v1 import AuthorizationV1  # noqa: E501
from openapi_client.rest import ApiException

class TestAuthorizationV1(unittest.TestCase):
    """AuthorizationV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthorizationV1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.authorization_v1.AuthorizationV1()  # noqa: E501
        if include_optional :
            return AuthorizationV1(
                account = openapi_client.models.auth_account_v1.AuthAccountV1(
                    id = '1', 
                    username = 'admin', 
                    real_name = 'IT Bob', 
                    email = 'ITBob@Jamf.com', 
                    preferences = openapi_client.models.account_preferences_v1.AccountPreferencesV1(
                        language = 'en', 
                        date_format = 'MM/dd/yyyy', 
                        region = 'Europe', 
                        timezone = 'Etc/GMT', 
                        disable_relative_dates = False, ), 
                    multi_site_admin = True, 
                    access_level = 'FullAccess', 
                    privilege_set = 'CUSTOM', 
                    privileges_by_site = {"1":["Read SSO Settings","Delete eBooks"]}, 
                    group_ids = [1,3], 
                    current_site_id = '1', ), 
                account_groups = [
                    openapi_client.models.account_group.AccountGroup(
                        access_level = 'FullAccess', 
                        privilege_set = 'CUSTOM', 
                        site_id = 1, 
                        privileges = Read SSO Settings, 
                        member_user_ids = [1,3], )
                    ], 
                sites = [
                    openapi_client.models.v1_site.V1Site(
                        id = '1', 
                        name = 'Eau Claire', )
                    ], 
                authentication_type = 'JSS'
            )
        else :
            return AuthorizationV1(
        )

    def testAuthorizationV1(self):
        """Test AuthorizationV1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()