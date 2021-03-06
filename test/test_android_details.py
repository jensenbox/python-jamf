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
from jamf.models.android_details import AndroidDetails  # noqa: E501
from jamf.rest import ApiException

class TestAndroidDetails(unittest.TestCase):
    """AndroidDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AndroidDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.android_details.AndroidDetails()  # noqa: E501
        if include_optional :
            return AndroidDetails(
                os_name = 'Black Licorice', 
                manufacturer = 'Google', 
                model = 'Pixel 2', 
                internal_capacity_mb = 30000, 
                internal_available_mb = 20000, 
                internal_percent_used = 67, 
                external_capacity_mb = 20000, 
                external_available_mb = 10000, 
                external_percent_used = 50, 
                battery_level = 100, 
                last_backup_timestamp = '2018-10-15T16:39:56.307Z', 
                api_version = 1, 
                computer = jamf.models.android_details_computer.AndroidDetails_computer(
                    name = 'Ginny's Computer', 
                    id = 1, ), 
                security = jamf.models.security.Security(
                    is_data_protected = False, 
                    is_block_level_encryption_capable = True, 
                    is_file_level_encryption_capable = True, 
                    is_passcode_present = False, 
                    is_passcode_compliant = True, 
                    is_passcode_compliant_with_profile = True, 
                    hardware_encryption = 3, 
                    is_activation_lock_enabled = False, 
                    is_jail_break_detected = False, )
            )
        else :
            return AndroidDetails(
        )

    def testAndroidDetails(self):
        """Test AndroidDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
