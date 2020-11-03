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
from jamf.models.computer_general import ComputerGeneral  # noqa: E501
from jamf.rest import ApiException

class TestComputerGeneral(unittest.TestCase):
    """ComputerGeneral unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComputerGeneral
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = jamf.models.computer_general.ComputerGeneral()  # noqa: E501
        if include_optional :
            return ComputerGeneral(
                name = 'Boalime', 
                last_ip_address = '247.185.82.186', 
                last_reported_ip = '247.185.82.186', 
                jamf_binary_version = '9.27', 
                platform = 'Mac', 
                barcode1 = '5 12345 678900', 
                barcode2 = '5 12345 678900', 
                asset_tag = '304822', 
                remote_management = jamf.models.computer_remote_management.ComputerRemoteManagement(
                    managed = True, 
                    management_username = 'rootname', 
                    management_password = 'example password', ), 
                supervised = True, 
                mdm_capable = jamf.models.computer_mdm_capability.ComputerMdmCapability(
                    capable = True, 
                    capable_users = ["admin","rootadmin"], ), 
                report_date = '2018-10-31T18:04:13Z', 
                last_contact_time = '2018-10-31T18:04:13Z', 
                last_cloud_backup_date = '2018-10-31T18:04:13Z', 
                last_enrolled_date = '2018-10-31T18:04:13Z', 
                mdm_profile_expiration = '2018-10-31T18:04:13Z', 
                initial_entry_date = 'Wed Oct 31 00:00:00 GMT 2018', 
                distribution_point = 'distribution point name', 
                enrollment_method = jamf.models.enrollment_method.EnrollmentMethod(
                    id = '1', 
                    object_name = 'user@domain.com', 
                    object_type = 'User-initiated - no invitation', ), 
                site = jamf.models.v1_site.V1Site(
                    id = '1', 
                    name = 'Eau Claire', ), 
                itunes_store_account_active = True, 
                enrolled_via_automated_device_enrollment = True, 
                user_approved_mdm = True, 
                extension_attributes = [
                    jamf.models.computer_extension_attribute.ComputerExtensionAttribute(
                        definition_id = '23', 
                        name = 'Some Attribute', 
                        description = 'Some Attribute defines how much Foo impacts Bar.', 
                        enabled = True, 
                        multi_value = True, 
                        values = ["foo","bar"], 
                        data_type = 'STRING', 
                        options = ["foo","bar"], 
                        input_type = 'TEXT', )
                    ]
            )
        else :
            return ComputerGeneral(
        )

    def testComputerGeneral(self):
        """Test ComputerGeneral"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
