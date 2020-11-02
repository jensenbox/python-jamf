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
from openapi_client.models.mobile_device import MobileDevice  # noqa: E501
from openapi_client.rest import ApiException

class TestMobileDevice(unittest.TestCase):
    """MobileDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MobileDevice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.mobile_device.MobileDevice()  # noqa: E501
        if include_optional :
            return MobileDevice(
                id = 1, 
                name = 'iPad', 
                serial_number = 'DMQVGC0DHLA0', 
                wifi_mac_address = 'C4:84:66:92:78:00', 
                udid = '0dad565fb40b010a9e490440188063a378721069', 
                phone_number = '651-555-5555 Ext111', 
                model = 'iPad 5th Generation (Wi-Fi)', 
                model_identifier = 'iPad6,11', 
                username = 'admin', 
                type = 'ios'
            )
        else :
            return MobileDevice(
        )

    def testMobileDevice(self):
        """Test MobileDevice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()