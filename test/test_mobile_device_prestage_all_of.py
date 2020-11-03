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
from jamf.models.mobile_device_prestage_all_of import MobileDevicePrestageAllOf  # noqa: E501
from jamf.rest import ApiException

class TestMobileDevicePrestageAllOf(unittest.TestCase):
    """MobileDevicePrestageAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MobileDevicePrestageAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.mobile_device_prestage_all_of.MobileDevicePrestageAllOf()  # noqa: E501
        if include_optional :
            return MobileDevicePrestageAllOf(
                is_allow_pairing = True, 
                is_multi_user = True, 
                is_supervised = True, 
                maximum_shared_accounts = 10, 
                is_auto_advance_setup = True, 
                is_configure_device_before_setup_assistant = True, 
                language = 'en', 
                region = 'US', 
                names = jamf.models.mobile_device_prestage_names.MobileDevicePrestageNames(
                    assign_names_using = 'List of Names', 
                    prestage_device_names = [
                        jamf.models.mobile_device_prestage_name.MobileDevicePrestageName(
                            id = 1, 
                            device_name = 'iPad', 
                            is_used = False, )
                        ], 
                    device_name_prefix = 'prefix', 
                    device_name_suffix = 'suffix', 
                    single_device_name = 'name', 
                    is_manage_names = True, 
                    is_device_naming_configured = True, )
            )
        else :
            return MobileDevicePrestageAllOf(
                is_allow_pairing = True,
                is_multi_user = True,
                is_supervised = True,
                maximum_shared_accounts = 10,
                is_auto_advance_setup = True,
                is_configure_device_before_setup_assistant = True,
        )

    def testMobileDevicePrestageAllOf(self):
        """Test MobileDevicePrestageAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
