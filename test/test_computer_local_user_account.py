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
from jamf.models.computer_local_user_account import ComputerLocalUserAccount  # noqa: E501
from jamf.rest import ApiException

class TestComputerLocalUserAccount(unittest.TestCase):
    """ComputerLocalUserAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComputerLocalUserAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.computer_local_user_account.ComputerLocalUserAccount()  # noqa: E501
        if include_optional :
            return ComputerLocalUserAccount(
                uid = '501', 
                username = 'jamf', 
                full_name = 'John Jamf', 
                admin = True, 
                home_directory = '/Users/jamf', 
                home_directory_size_mb = 131072, 
                file_vault2_enabled = True, 
                user_account_type = 'LOCAL', 
                password_min_length = 4, 
                password_max_age = 5, 
                password_min_complex_characters = 5, 
                password_history_depth = 5, 
                password_require_alphanumeric = True, 
                computer_azure_active_directory_id = '1', 
                user_azure_active_directory_id = '1', 
                azure_active_directory_id = 'ACTIVATED'
            )
        else :
            return ComputerLocalUserAccount(
        )

    def testComputerLocalUserAccount(self):
        """Test ComputerLocalUserAccount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
