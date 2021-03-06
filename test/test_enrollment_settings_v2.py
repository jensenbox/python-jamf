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
from jamf.models.enrollment_settings_v2 import EnrollmentSettingsV2  # noqa: E501
from jamf.rest import ApiException

class TestEnrollmentSettingsV2(unittest.TestCase):
    """EnrollmentSettingsV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EnrollmentSettingsV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.enrollment_settings_v2.EnrollmentSettingsV2()  # noqa: E501
        if include_optional :
            return EnrollmentSettingsV2(
                install_single_profile = True, 
                signing_mdm_profile_enabled = True, 
                mdm_signing_certificate = jamf.models.certificate_identity_v2.CertificateIdentityV2(
                    filename = '0', 
                    keystore_password = '0', 
                    identity_keystore = ZXhhbXBsZSBvZiBhIGJhc2U2NCBlbmNvZGVkIHZhbGlkIHAxMi4ga2V5c3RvcmUgZmlsZQ==, 
                    md5_sum = '0', ), 
                restrict_reenrollment = True, 
                flush_location_information = True, 
                flush_location_history_information = True, 
                flush_policy_history = True, 
                flush_extension_attributes = True, 
                flush_mdm_commands_on_reenroll = 'DELETE_EVERYTHING_EXCEPT_ACKNOWLEDGED', 
                mac_os_enterprise_enrollment_enabled = True, 
                management_username = '0', 
                management_password = '0', 
                management_password_set = True, 
                password_type = 'STATIC', 
                random_password_length = 56, 
                create_management_account = True, 
                hide_management_account = True, 
                allow_ssh_only_management_account = True, 
                ensure_ssh_running = True, 
                launch_self_service = True, 
                sign_quick_add = True, 
                developer_certificate_identity = jamf.models.certificate_identity_v2.CertificateIdentityV2(
                    filename = '0', 
                    keystore_password = '0', 
                    identity_keystore = ZXhhbXBsZSBvZiBhIGJhc2U2NCBlbmNvZGVkIHZhbGlkIHAxMi4ga2V5c3RvcmUgZmlsZQ==, 
                    md5_sum = '0', ), 
                developer_certificate_identity_details = jamf.models.certificate_details.CertificateDetails(
                    subject = '0', 
                    serial_number = '0', ), 
                mdm_signing_certificate_details = jamf.models.certificate_details.CertificateDetails(
                    subject = '0', 
                    serial_number = '0', ), 
                ios_enterprise_enrollment_enabled = True, 
                ios_personal_enrollment_enabled = True, 
                personal_device_enrollment_type = 'PERSONALDEVICEPROFILES'
            )
        else :
            return EnrollmentSettingsV2(
        )

    def testEnrollmentSettingsV2(self):
        """Test EnrollmentSettingsV2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
