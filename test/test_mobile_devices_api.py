# coding: utf-8

"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.mobile_devices_api import MobileDevicesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestMobileDevicesApi(unittest.TestCase):
    """MobileDevicesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.mobile_devices_api.MobileDevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_mobile_devices_get(self):
        """Test case for v1_mobile_devices_get

        Get Mobile Device objects   # noqa: E501
        """
        pass

    def test_v1_mobile_devices_id_detail_get(self):
        """Test case for v1_mobile_devices_id_detail_get

        Get Mobile Device   # noqa: E501
        """
        pass

    def test_v1_mobile_devices_id_get(self):
        """Test case for v1_mobile_devices_id_get

        Get Mobile Device   # noqa: E501
        """
        pass

    def test_v1_mobile_devices_id_patch(self):
        """Test case for v1_mobile_devices_id_patch

        Update fields on a mobile device that are allowed to be modified by users   # noqa: E501
        """
        pass

    def test_v1_search_mobile_devices_post(self):
        """Test case for v1_search_mobile_devices_post

        Search Mobile Devices   # noqa: E501
        """
        pass

    def test_v2_mobile_devices_get(self):
        """Test case for v2_mobile_devices_get

        Get Mobile Device objects   # noqa: E501
        """
        pass

    def test_v2_mobile_devices_id_detail_get(self):
        """Test case for v2_mobile_devices_id_detail_get

        Get Mobile Device   # noqa: E501
        """
        pass

    def test_v2_mobile_devices_id_get(self):
        """Test case for v2_mobile_devices_id_get

        Get Mobile Device   # noqa: E501
        """
        pass

    def test_v2_mobile_devices_id_patch(self):
        """Test case for v2_mobile_devices_id_patch

        Update fields on a mobile device that are allowed to be modified by users   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()