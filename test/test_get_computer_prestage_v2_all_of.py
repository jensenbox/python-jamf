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
from jamf.models.get_computer_prestage_v2_all_of import GetComputerPrestageV2AllOf  # noqa: E501
from jamf.rest import ApiException

class TestGetComputerPrestageV2AllOf(unittest.TestCase):
    """GetComputerPrestageV2AllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetComputerPrestageV2AllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.get_computer_prestage_v2_all_of.GetComputerPrestageV2AllOf()  # noqa: E501
        if include_optional :
            return GetComputerPrestageV2AllOf(
                id = '1', 
                profile_uuid = '29d-a8d8f-b8sdjndf-dsa9', 
                site_id = '5', 
                version_lock = 0
            )
        else :
            return GetComputerPrestageV2AllOf(
        )

    def testGetComputerPrestageV2AllOf(self):
        """Test GetComputerPrestageV2AllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
