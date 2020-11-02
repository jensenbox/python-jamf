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
from openapi_client.models.purchasing import Purchasing  # noqa: E501
from openapi_client.rest import ApiException

class TestPurchasing(unittest.TestCase):
    """Purchasing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Purchasing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.purchasing.Purchasing()  # noqa: E501
        if include_optional :
            return Purchasing(
                is_purchased = True, 
                is_leased = False, 
                po_number = '8675309', 
                vendor = 'Apple', 
                apple_care_id = '9546567.0', 
                purchase_price = '$399', 
                purchasing_account = 'IT Budget', 
                po_date = '2019-02-04T21:09:31.661Z', 
                warranty_expires_date = '2019-02-04T21:09:31.661Z', 
                lease_expires_date = '2019-02-04T21:09:31.661Z', 
                life_expectancy = 7, 
                purchasing_contact = 'Nick in IT'
            )
        else :
            return Purchasing(
        )

    def testPurchasing(self):
        """Test Purchasing"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()