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
from jamf.models.get_computer_prestage_v2 import GetComputerPrestageV2  # noqa: E501
from jamf.rest import ApiException

class TestGetComputerPrestageV2(unittest.TestCase):
    """GetComputerPrestageV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetComputerPrestageV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.get_computer_prestage_v2.GetComputerPrestageV2()  # noqa: E501
        if include_optional :
            return GetComputerPrestageV2(
                display_name = 'Example Mobile Prestage Name', 
                mandatory = False, 
                mdm_removable = True, 
                support_phone_number = '5555555555', 
                support_email_address = 'example@example.com', 
                department = 'Oxbow', 
                default_prestage = False, 
                enrollment_site_id = '-1', 
                keep_existing_site_membership = True, 
                keep_existing_location_information = True, 
                require_authentication = True, 
                authentication_prompt = 'LDAP authentication prompt', 
                prevent_activation_lock = True, 
                enable_device_based_activation_lock = True, 
                device_enrollment_program_instance_id = '5', 
                skip_setup_items = {"Location":true,"Privacy":false}, 
                location_information = jamf.models.location_information_v2.LocationInformationV2(
                    username = 'name', 
                    realname = 'realName', 
                    phone = '123-456-7890', 
                    email = 'test@jamf.com', 
                    room = 'room', 
                    position = 'postion', 
                    department_id = '1', 
                    building_id = '1', 
                    id = '-1', 
                    version_lock = 1, ), 
                purchasing_information = jamf.models.prestage_purchasing_information_v2.PrestagePurchasingInformationV2(
                    id = '-1', 
                    leased = True, 
                    purchased = True, 
                    apple_care_id = 'abcd', 
                    po_number = '53-1', 
                    vendor = 'Example Vendor', 
                    purchase_price = '$500', 
                    life_expectancy = 5, 
                    purchasing_account = 'admin', 
                    purchasing_contact = 'true', 
                    lease_date = '2019-01-01', 
                    po_date = '2019-01-01', 
                    warranty_date = '2019-01-01', 
                    version_lock = 1, ), 
                anchor_certificates = [
                    'xNE5HRgotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg=='
                    ], 
                enrollment_customization_id = '2', 
                language = 'en', 
                region = 'US', 
                auto_advance_setup = True, 
                install_profiles_during_setup = True, 
                prestage_installed_profile_ids = [
                    '1'
                    ], 
                custom_package_ids = [
                    '1'
                    ], 
                custom_package_distribution_point_id = '1', 
                id = '1', 
                profile_uuid = '29d-a8d8f-b8sdjndf-dsa9', 
                site_id = '5', 
                version_lock = 0
            )
        else :
            return GetComputerPrestageV2(
                display_name = 'Example Mobile Prestage Name',
                mandatory = False,
                mdm_removable = True,
                support_phone_number = '5555555555',
                support_email_address = 'example@example.com',
                department = 'Oxbow',
                default_prestage = False,
                enrollment_site_id = '-1',
                keep_existing_site_membership = True,
                keep_existing_location_information = True,
                require_authentication = True,
                authentication_prompt = 'LDAP authentication prompt',
                prevent_activation_lock = True,
                enable_device_based_activation_lock = True,
                device_enrollment_program_instance_id = '5',
                location_information = jamf.models.location_information_v2.LocationInformationV2(
                    username = 'name', 
                    realname = 'realName', 
                    phone = '123-456-7890', 
                    email = 'test@jamf.com', 
                    room = 'room', 
                    position = 'postion', 
                    department_id = '1', 
                    building_id = '1', 
                    id = '-1', 
                    version_lock = 1, ),
                purchasing_information = jamf.models.prestage_purchasing_information_v2.PrestagePurchasingInformationV2(
                    id = '-1', 
                    leased = True, 
                    purchased = True, 
                    apple_care_id = 'abcd', 
                    po_number = '53-1', 
                    vendor = 'Example Vendor', 
                    purchase_price = '$500', 
                    life_expectancy = 5, 
                    purchasing_account = 'admin', 
                    purchasing_contact = 'true', 
                    lease_date = '2019-01-01', 
                    po_date = '2019-01-01', 
                    warranty_date = '2019-01-01', 
                    version_lock = 1, ),
                auto_advance_setup = True,
                install_profiles_during_setup = True,
                prestage_installed_profile_ids = [
                    '1'
                    ],
                custom_package_ids = [
                    '1'
                    ],
                custom_package_distribution_point_id = '1',
        )

    def testGetComputerPrestageV2(self):
        """Test GetComputerPrestageV2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
