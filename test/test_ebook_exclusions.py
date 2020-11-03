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
from jamf.models.ebook_exclusions import EbookExclusions  # noqa: E501
from jamf.rest import ApiException

class TestEbookExclusions(unittest.TestCase):
    """EbookExclusions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EbookExclusions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.ebook_exclusions.EbookExclusions()  # noqa: E501
        if include_optional :
            return EbookExclusions(
                computer_ids = [
                    '-1'
                    ], 
                computer_group_ids = [
                    '-1'
                    ], 
                mobile_device_ids = [
                    '-1'
                    ], 
                mobile_device_group_ids = [
                    '-1'
                    ], 
                building_ids = [
                    '-1'
                    ], 
                department_ids = [
                    '-1'
                    ], 
                user_ids = [
                    '-1'
                    ], 
                user_group_ids = [
                    '-1'
                    ], 
                limitations = jamf.models.ebook_limitations.EbookLimitations(
                    network_segments = [
                        '1'
                        ], 
                    users = [
                        jamf.models.ebook_limitations_users.EbookLimitations_users(
                            name = 'admin', )
                        ], 
                    user_groups = [
                        '1'
                        ], )
            )
        else :
            return EbookExclusions(
        )

    def testEbookExclusions(self):
        """Test EbookExclusions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
