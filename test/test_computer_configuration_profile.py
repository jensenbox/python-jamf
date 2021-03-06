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
from jamf.models.computer_configuration_profile import ComputerConfigurationProfile  # noqa: E501
from jamf.rest import ApiException

class TestComputerConfigurationProfile(unittest.TestCase):
    """ComputerConfigurationProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComputerConfigurationProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.computer_configuration_profile.ComputerConfigurationProfile()  # noqa: E501
        if include_optional :
            return ComputerConfigurationProfile(
                id = '1', 
                username = 'username', 
                last_installed = '2018-10-31T18:04:13Z', 
                removable = True, 
                display_name = 'Displayed profile', 
                profile_identifier = '0ae590fe-9b30-11ea-bb37-0242ac130002'
            )
        else :
            return ComputerConfigurationProfile(
        )

    def testComputerConfigurationProfile(self):
        """Test ComputerConfigurationProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
