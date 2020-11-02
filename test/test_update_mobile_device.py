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
from openapi_client.models.update_mobile_device import UpdateMobileDevice  # noqa: E501
from openapi_client.rest import ApiException

class TestUpdateMobileDevice(unittest.TestCase):
    """UpdateMobileDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateMobileDevice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.update_mobile_device.UpdateMobileDevice()  # noqa: E501
        if include_optional :
            return UpdateMobileDevice(
                name = 'Jan's Mobile Device', 
                asset_tag = '8675309', 
                site_id = 1, 
                location = openapi_client.models.location.Location(
                    username = 'admin', 
                    real_name = 'IT Bob', 
                    email_address = 'ITBob@jamf.com', 
                    position = 'IT Team Lead', 
                    phone_number = '555-555-5555', 
                    department = openapi_client.models.location_department.Location_department(
                        name = 'IT', 
                        id = 1, ), 
                    building = openapi_client.models.location_building.Location_building(
                        name = 'Eau Claire', 
                        id = 1, ), 
                    room = '4th Floor - Quad 3', ), 
                updated_extension_attributes = [
                    openapi_client.models.extension_attribute.ExtensionAttribute(
                        id = 1, 
                        name = 'Example EA', 
                        type = 'STRING', 
                        value = [
                            'EA Value'
                            ], 
                        is_extension_attribute_collection_allowed = False, )
                    ], 
                ios = openapi_client.models.update_ios.UpdateIos(
                    purchasing = openapi_client.models.purchasing.Purchasing(
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
                        purchasing_contact = 'Nick in IT', ), ), 
                apple_tv = openapi_client.models.update_apple_tv.UpdateAppleTv(
                    airplay_password = '12345', 
                    purchasing = openapi_client.models.purchasing.Purchasing(
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
                        purchasing_contact = 'Nick in IT', ), )
            )
        else :
            return UpdateMobileDevice(
        )

    def testUpdateMobileDevice(self):
        """Test UpdateMobileDevice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
