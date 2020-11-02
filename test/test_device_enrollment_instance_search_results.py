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
from openapi_client.models.device_enrollment_instance_search_results import DeviceEnrollmentInstanceSearchResults  # noqa: E501
from openapi_client.rest import ApiException

class TestDeviceEnrollmentInstanceSearchResults(unittest.TestCase):
    """DeviceEnrollmentInstanceSearchResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeviceEnrollmentInstanceSearchResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.device_enrollment_instance_search_results.DeviceEnrollmentInstanceSearchResults()  # noqa: E501
        if include_optional :
            return DeviceEnrollmentInstanceSearchResults(
                total_count = 1, 
                results = [
                    openapi_client.models.device_enrollment_instance.DeviceEnrollmentInstance(
                        id = '1', 
                        name = 'Example Device Enrollment Instance', 
                        supervision_identity_id = '1', 
                        site_id = '-1', 
                        server_name = 'Acme ASM', 
                        server_uuid = 'BASD08C11F3C455', 
                        admin_id = 'admin1234', 
                        org_name = 'Acme Enterprises', 
                        org_email = 'admin@test.com', 
                        org_phone = '555-0123', 
                        org_address = '124 Conch Street, Bikini Bottom, Pacific Ocean', 
                        token_expiration_date = '2000-10-30', )
                    ]
            )
        else :
            return DeviceEnrollmentInstanceSearchResults(
        )

    def testDeviceEnrollmentInstanceSearchResults(self):
        """Test DeviceEnrollmentInstanceSearchResults"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
