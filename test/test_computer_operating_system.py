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
from jamf.models.computer_operating_system import ComputerOperatingSystem  # noqa: E501
from jamf.rest import ApiException

class TestComputerOperatingSystem(unittest.TestCase):
    """ComputerOperatingSystem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComputerOperatingSystem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.computer_operating_system.ComputerOperatingSystem()  # noqa: E501
        if include_optional :
            return ComputerOperatingSystem(
                name = 'Mac OS X', 
                version = '10.9.5', 
                build = '13A603', 
                active_directory_status = 'Not Bound', 
                master_password_set = True, 
                file_vault2_status = 'ALL_ENCRYPTED', 
                extension_attributes = [
                    jamf.models.computer_extension_attribute.ComputerExtensionAttribute(
                        definition_id = '23', 
                        name = 'Some Attribute', 
                        description = 'Some Attribute defines how much Foo impacts Bar.', 
                        enabled = True, 
                        multi_value = True, 
                        values = ["foo","bar"], 
                        data_type = 'STRING', 
                        options = ["foo","bar"], 
                        input_type = 'TEXT', )
                    ]
            )
        else :
            return ComputerOperatingSystem(
        )

    def testComputerOperatingSystem(self):
        """Test ComputerOperatingSystem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
