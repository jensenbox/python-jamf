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
from jamf.models.tv_os_details import TvOsDetails  # noqa: E501
from jamf.rest import ApiException

class TestTvOsDetails(unittest.TestCase):
    """TvOsDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TvOsDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.tv_os_details.TvOsDetails()  # noqa: E501
        if include_optional :
            return TvOsDetails(
                model = 'Apple TV 3rd Generation Rev 2', 
                model_identifier = 'AppleTV3,2', 
                model_number = 'MD199LL', 
                supervised = True, 
                airplay_password = '1234', 
                device_id = '1', 
                locales = '0', 
                purchasing = jamf.models.purchasing_v2.PurchasingV2(
                    purchased = True, 
                    leased = False, 
                    po_number = '8675309', 
                    vendor = 'Apple', 
                    apple_care_id = '9546567.0', 
                    purchase_price = '$399', 
                    purchasing_account = 'IT Budget', 
                    po_date = '2019-02-04T21:09:31.661Z', 
                    warranty_expires_date = '2019-02-04T21:09:31.661Z', 
                    lease_expires_date = '2019-02-04T21:09:31.661Z', 
                    life_expectancy = 7, 
                    purchasing_contact = 'Nick in IT', ), 
                configuration_profiles = [
                    jamf.models.configuration_profile.ConfigurationProfile(
                        display_name = 'Test WiFi', 
                        version = '1', 
                        uuid = 'D29DD9FB-0D5B-422F-A3A2-ABBC5848E949', 
                        identifier = 'ac2-server4.D0EFAC2D-326C-4BB6-87E6-2BCB88490AAA', )
                    ]
            )
        else :
            return TvOsDetails(
        )

    def testTvOsDetails(self):
        """Test TvOsDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
