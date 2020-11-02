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
from openapi_client.models.location_information import LocationInformation  # noqa: E501
from openapi_client.rest import ApiException

class TestLocationInformation(unittest.TestCase):
    """LocationInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LocationInformation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.location_information.LocationInformation()  # noqa: E501
        if include_optional :
            return LocationInformation(
                username = 'name', 
                realname = 'realName', 
                phone = '123-456-7890', 
                email = 'test@jamf.com', 
                room = 'room', 
                position = 'postion', 
                department_id = 1, 
                building_id = 1, 
                id = 0, 
                version_lock = 1
            )
        else :
            return LocationInformation(
                username = 'name',
                realname = 'realName',
                phone = '123-456-7890',
                email = 'test@jamf.com',
                room = 'room',
                position = 'postion',
                department_id = 1,
                building_id = 1,
                id = 0,
                version_lock = 1,
        )

    def testLocationInformation(self):
        """Test LocationInformation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
