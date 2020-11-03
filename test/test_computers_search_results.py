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
from jamf.models.computers_search_results import ComputersSearchResults  # noqa: E501
from jamf.rest import ApiException

class TestComputersSearchResults(unittest.TestCase):
    """ComputersSearchResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComputersSearchResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.computers_search_results.ComputersSearchResults()  # noqa: E501
        if include_optional :
            return ComputersSearchResults(
                total_count = 3, 
                results = [
                    jamf.models.computer_overview.ComputerOverview(
                        id = '7', 
                        location = jamf.models.computer_location.ComputerLocation(
                            username = 'admin', 
                            position = 'IT Team Lead', 
                            room = '4th Floor - Quad 3', ), 
                        name = 'Zach's hand me down MacBook Pro', 
                        udid = '6E47EF55-5318-494F-A09E-70F613E0AFD1', 
                        serial_number = 'C02L29ECF8J1', 
                        last_contact_date = '2000-04-25T21:09:31.661Z', 
                        last_report_date = '2000-04-25T21:09:31.661Z', 
                        last_enrolled_date = '2000-04-25T21:09:31.661Z', 
                        operating_system_version = '10.9.5', 
                        operating_system_build = 'TK421', 
                        ip_address = '93.184.216.34', 
                        mac_address = 'F3:7C:6F:2C:B6:76', 
                        asset_tag = 'A123BC', 
                        model_identifier = 'MNYF2XX/A', 
                        mdm_access_rights = 1, 
                        is_managed = True, )
                    ]
            )
        else :
            return ComputersSearchResults(
        )

    def testComputersSearchResults(self):
        """Test ComputersSearchResults"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
