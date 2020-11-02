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
from openapi_client.models.computer_hardware import ComputerHardware  # noqa: E501
from openapi_client.rest import ApiException

class TestComputerHardware(unittest.TestCase):
    """ComputerHardware unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComputerHardware
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.computer_hardware.ComputerHardware()  # noqa: E501
        if include_optional :
            return ComputerHardware(
                make = 'Apple', 
                model = '13-inch MacBook Pro (Mid 2012)', 
                model_identifier = 'MacBookPro9,2', 
                serial_number = 'C02ZC2QYLVDL', 
                processor_speed_mhz = 2100, 
                processor_count = 2, 
                core_count = 2, 
                processor_type = 'Intel Core i5', 
                processor_architecture = 'i386', 
                bus_speed_mhz = 2133, 
                cache_size_kilobytes = 3072, 
                network_adapter_type = 'Foo', 
                mac_address = '6A:2C:4B:B7:65:B5', 
                alt_network_adapter_type = 'Bar', 
                alt_mac_address = '82:45:58:44:dc:01', 
                total_ram_megabytes = 4096, 
                open_ram_slots = 0, 
                battery_capacity_percent = 85, 
                smc_version = '2.2f38', 
                nic_speed = 'N/A', 
                optical_drive = 'MATSHITA DVD-R UJ-8A8', 
                boot_rom = 'MBP91.00D3.B08', 
                ble_capable = False, 
                extension_attributes = [
                    openapi_client.models.computer_extension_attribute.ComputerExtensionAttribute(
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
            return ComputerHardware(
        )

    def testComputerHardware(self):
        """Test ComputerHardware"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()