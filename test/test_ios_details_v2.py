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
from jamf.models.ios_details_v2 import IosDetailsV2  # noqa: E501
from jamf.rest import ApiException

class TestIosDetailsV2(unittest.TestCase):
    """IosDetailsV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IosDetailsV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.ios_details_v2.IosDetailsV2()  # noqa: E501
        if include_optional :
            return IosDetailsV2(
                model = 'iPad 5th Generation (Wi-Fi)', 
                model_identifier = 'ipad6,11', 
                model_number = 'MP2F2LL', 
                supervised = True, 
                battery_level = 100, 
                last_backup_timestamp = '2018-10-15T16:39:56Z', 
                capacity_mb = 27503, 
                available_mb = 26646, 
                percentage_used = 3, 
                shared = False, 
                device_locator_service_enabled = False, 
                do_not_disturb_enabled = False, 
                cloud_backup_enabled = False, 
                last_cloud_backup_timestamp = '2018-10-15T16:39:56.307Z', 
                location_services_enabled = False, 
                i_tunes_store_account_active = False, 
                ble_capable = False, 
                computer = jamf.models.ios_details_v2_computer.IosDetailsV2_computer(
                    name = 'Bob's MacBook', 
                    id = '1', ), 
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
                security = jamf.models.security_v2.SecurityV2(
                    data_protected = False, 
                    block_level_encryption_capable = True, 
                    file_level_encryption_capable = True, 
                    passcode_present = False, 
                    passcode_compliant = True, 
                    passcode_compliant_with_profile = True, 
                    hardware_encryption = 3, 
                    activation_lock_enabled = False, 
                    jail_break_detected = False, ), 
                network = jamf.models.network_v2.NetworkV2(
                    cellular_technology = 'Unknown', 
                    voice_roaming_enabled = False, 
                    imei = '59 105109 176278 3', 
                    iccid = '8991101200003204514', 
                    meid = '15302309236898', 
                    carrier_settings_version = '33.1', 
                    current_carrier_network = 'Verizon Wireless', 
                    current_mobile_country_code = '311', 
                    current_mobile_network_code = '480', 
                    home_carrier_network = 'Verizon', 
                    home_mobile_country_code = 'US', 
                    home_mobile_network_code = '480', 
                    data_roaming_enabled = True, 
                    roaming = False, 
                    personal_hotspot_enabled = False, 
                    phone_number = '555-555-5555 ext 5', ), 
                applications = [
                    jamf.models.ios_details_applications.IosDetails_applications(
                        identifier = 'com.apple.airport.mobileairportutility', 
                        name = 'AirPort Utility', 
                        version = '135.24', 
                        short_version = '7.0', )
                    ], 
                certificates = [
                    jamf.models.ios_details_v2_certificates.IosDetailsV2_certificates(
                        common_name = '3B259E4B-FAD5-4860-B1DD-336ADA786EBA', 
                        identity = False, )
                    ], 
                ebooks = [
                    jamf.models.ios_details_ebooks.IosDetails_ebooks(
                        author = 'Homer J Simpson', 
                        title = 'The Odyssey', 
                        version = '0.1', )
                    ], 
                configuration_profiles = [
                    jamf.models.configuration_profile.ConfigurationProfile(
                        display_name = 'Test WiFi', 
                        version = '1', 
                        uuid = 'D29DD9FB-0D5B-422F-A3A2-ABBC5848E949', 
                        identifier = 'ac2-server4.D0EFAC2D-326C-4BB6-87E6-2BCB88490AAA', )
                    ], 
                provisioning_profiles = [
                    jamf.models.provisioning_profile.ProvisioningProfile(
                        display_name = 'jamfnation', 
                        uuid = '89AF33FC-123C-1231-AEFD-9C3ED123AFCC', 
                        expiration_date = '2018-10-24T21:57:37Z', )
                    ], 
                attachments = [
                    jamf.models.ios_details_v2_attachments.IosDetailsV2_attachments(
                        name = 'Bob's Attachment', 
                        id = '1', )
                    ]
            )
        else :
            return IosDetailsV2(
        )

    def testIosDetailsV2(self):
        """Test IosDetailsV2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
