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
from jamf.models.mobile_device_group import MobileDeviceGroup  # noqa: E501
from jamf.rest import ApiException

class TestMobileDeviceGroup(unittest.TestCase):
    """MobileDeviceGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MobileDeviceGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.mobile_device_group.MobileDeviceGroup()  # noqa: E501
        if include_optional :
            return MobileDeviceGroup(
                id = 1, 
                name = 'All Managed iPads', 
                is_smart_group = True
            )
        else :
            return MobileDeviceGroup(
        )

    def testMobileDeviceGroup(self):
        """Test MobileDeviceGroup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
