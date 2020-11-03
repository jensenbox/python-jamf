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
from jamf.models.current_account import CurrentAccount  # noqa: E501
from jamf.rest import ApiException

class TestCurrentAccount(unittest.TestCase):
    """CurrentAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CurrentAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.current_account.CurrentAccount()  # noqa: E501
        if include_optional :
            return CurrentAccount(
                id = 1, 
                username = 'admin', 
                real_name = 'IT Bob', 
                email = 'ITBob@Jamf.com', 
                preferences = jamf.models.account_preferences.AccountPreferences(
                    language = 'en', 
                    date_format = 'MM/dd/yyyy', 
                    region = 'Europe', 
                    timezone = 'Etc/GMT', 
                    is_disable_relative_dates = False, ), 
                is_multi_site_admin = True, 
                access_level = 'FullAccess', 
                privilege_set = 'CUSTOM', 
                privileges = ["Read SSO Settings","Delete eBooks"], 
                group_ids = [1,3], 
                current_site_id = 1
            )
        else :
            return CurrentAccount(
        )

    def testCurrentAccount(self):
        """Test CurrentAccount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
