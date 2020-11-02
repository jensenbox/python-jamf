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
from openapi_client.models.mobile_device_details_v2_site import MobileDeviceDetailsV2Site  # noqa: E501
from openapi_client.rest import ApiException

class TestMobileDeviceDetailsV2Site(unittest.TestCase):
    """MobileDeviceDetailsV2Site unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MobileDeviceDetailsV2Site
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.mobile_device_details_v2_site.MobileDeviceDetailsV2Site()  # noqa: E501
        if include_optional :
            return MobileDeviceDetailsV2Site(
                name = 'Eau Claire', 
                id = '1'
            )
        else :
            return MobileDeviceDetailsV2Site(
        )

    def testMobileDeviceDetailsV2Site(self):
        """Test MobileDeviceDetailsV2Site"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()