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
from openapi_client.models.computer_inventory_search_results import ComputerInventorySearchResults  # noqa: E501
from openapi_client.rest import ApiException

class TestComputerInventorySearchResults(unittest.TestCase):
    """ComputerInventorySearchResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComputerInventorySearchResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.computer_inventory_search_results.ComputerInventorySearchResults()  # noqa: E501
        if include_optional :
            return ComputerInventorySearchResults(
                total_count = 3, 
                results = [
                    openapi_client.models.computer_inventory_response.ComputerInventoryResponse(
                        id = '1', 
                        udid = '123', 
                        general = openapi_client.models.computer_general.ComputerGeneral(
                            name = 'Boalime', 
                            last_ip_address = '247.185.82.186', 
                            last_reported_ip = '247.185.82.186', 
                            jamf_binary_version = '9.27', 
                            platform = 'Mac', 
                            barcode1 = '5 12345 678900', 
                            barcode2 = '5 12345 678900', 
                            asset_tag = '304822', 
                            remote_management = openapi_client.models.computer_remote_management.ComputerRemoteManagement(
                                managed = True, 
                                management_username = 'rootname', 
                                management_password = 'example password', ), 
                            supervised = True, 
                            mdm_capable = openapi_client.models.computer_mdm_capability.ComputerMdmCapability(
                                capable = True, 
                                capable_users = ["admin","rootadmin"], ), 
                            report_date = '2018-10-31T18:04:13Z', 
                            last_contact_time = '2018-10-31T18:04:13Z', 
                            last_cloud_backup_date = '2018-10-31T18:04:13Z', 
                            last_enrolled_date = '2018-10-31T18:04:13Z', 
                            mdm_profile_expiration = '2018-10-31T18:04:13Z', 
                            initial_entry_date = 'Tue Oct 30 17:00:00 PDT 2018', 
                            distribution_point = 'distribution point name', 
                            enrollment_method = openapi_client.models.enrollment_method.EnrollmentMethod(
                                id = '1', 
                                object_name = 'user@domain.com', 
                                object_type = 'User-initiated - no invitation', ), 
                            site = openapi_client.models.v1_site.V1Site(
                                id = '1', 
                                name = 'Eau Claire', ), 
                            itunes_store_account_active = True, 
                            enrolled_via_automated_device_enrollment = True, 
                            user_approved_mdm = True, 
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
                                ], ), 
                        disk_encryption = openapi_client.models.computer_disk_encryption.ComputerDiskEncryption(
                            boot_partition_encryption_details = openapi_client.models.computer_partition_encryption.ComputerPartitionEncryption(
                                partition_name = 'main', 
                                partition_file_vault2_state = 'VALID', 
                                partition_file_vault2_percent = 100, ), 
                            individual_recovery_key_validity_status = 'Valid', 
                            institutional_recovery_key_present = True, 
                            disk_encryption_configuration_name = 'Test configuration', 
                            file_vault2_enabled_user_names = ["admin"], 
                            file_vault2_eligibility_message = 'Not a boot partition', ), 
                        purchasing = openapi_client.models.computer_purchase.ComputerPurchase(
                            leased = True, 
                            purchased = True, 
                            po_number = '53-1', 
                            po_date = 'Mon Dec 31 16:00:00 PST 2018', 
                            vendor = 'Example Vendor', 
                            warranty_date = 'Mon Dec 31 16:00:00 PST 2018', 
                            apple_care_id = 'abcd', 
                            lease_date = 'Mon Dec 31 16:00:00 PST 2018', 
                            purchase_price = '$500', 
                            life_expectancy = 5, 
                            purchasing_account = 'admin', 
                            purchasing_contact = 'true', ), 
                        applications = [
                            openapi_client.models.computer_application.ComputerApplication(
                                name = 'Microsoft Word', 
                                path = '/usr/local/app', 
                                version = '1.0.0', 
                                mac_app_store = True, 
                                size_megabytes = 25, 
                                bundle_id = '1', 
                                update_available = False, 
                                external_version_id = '1', )
                            ], 
                        storage = openapi_client.models.computer_storage.ComputerStorage(
                            boot_drive_available_space_megabytes = 3072, 
                            disks = [
                                openapi_client.models.computer_disk.ComputerDisk(
                                    id = '170', 
                                    device = 'disk0', 
                                    model = 'APPLE HDD TOSHIBA MK5065GSXF', 
                                    revision = '5', 
                                    serial_number = 'a8598f013366', 
                                    size_megabytes = 262144, 
                                    smart_status = 'OK', 
                                    type = 'false', 
                                    partitions = [
                                        openapi_client.models.computer_partition.ComputerPartition(
                                            name = 'Foo', 
                                            size_megabytes = 262144, 
                                            available_megabytes = 131072, 
                                            partition_type = 'BOOT', 
                                            percent_used = 25, 
                                            file_vault2_state = 'VALID', 
                                            file_vault2_progress_percent = 45, 
                                            lvm_managed = True, )
                                        ], )
                                ], ), 
                        user_and_location = openapi_client.models.computer_user_and_location.ComputerUserAndLocation(
                            username = 'Madison Anderson', 
                            realname = '13-inch MacBook', 
                            email = 'email@com.pl', 
                            position = 'IT Team Lead', 
                            phone = '123-456-789', 
                            department_id = '1', 
                            building_id = '1', 
                            room = '5', ), 
                        configuration_profiles = [
                            openapi_client.models.computer_configuration_profile.ComputerConfigurationProfile(
                                id = '1', 
                                username = 'username', 
                                last_installed = '2018-10-31T18:04:13Z', 
                                removable = True, 
                                display_name = 'Displayed profile', 
                                profile_identifier = '0ae590fe-9b30-11ea-bb37-0242ac130002', )
                            ], 
                        printers = [
                            openapi_client.models.computer_printer.ComputerPrinter(
                                name = 'My Printer', 
                                type = 'XYZ 1122', 
                                uri = 'ipp://10.0.0.5', 
                                location = '7th floor', )
                            ], 
                        services = [
                            openapi_client.models.computer_service.ComputerService(
                                name = 'SomeService', )
                            ], 
                        hardware = openapi_client.models.computer_hardware.ComputerHardware(
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
                            ble_capable = False, ), 
                        local_user_accounts = [
                            openapi_client.models.computer_local_user_account.ComputerLocalUserAccount(
                                uid = '501', 
                                username = 'jamf', 
                                full_name = 'John Jamf', 
                                admin = True, 
                                home_directory = '/Users/jamf', 
                                home_directory_size_mb = 131072, 
                                file_vault2_enabled = True, 
                                user_account_type = 'LOCAL', 
                                password_min_length = 4, 
                                password_max_age = 5, 
                                password_min_complex_characters = 5, 
                                password_history_depth = 5, 
                                password_require_alphanumeric = True, 
                                computer_azure_active_directory_id = '1', 
                                user_azure_active_directory_id = '1', 
                                azure_active_directory_id = 'ACTIVATED', )
                            ], 
                        certificates = [
                            openapi_client.models.computer_certificate.ComputerCertificate(
                                common_name = 'jamf.com', 
                                identity = True, 
                                expiration_date = '2030-10-31T18:04:13Z', 
                                username = 'test', 
                                lifecycle_status = 'ACTIVE', 
                                certificate_status = 'ISSUED', )
                            ], 
                        attachments = [
                            openapi_client.models.computer_attachment.ComputerAttachment(
                                id = '1', 
                                name = 'Attachment.pdf', 
                                file_type = 'application/pdf', 
                                size_bytes = 1024, )
                            ], 
                        plugins = [
                            openapi_client.models.computer_plugin.ComputerPlugin(
                                name = 'plugin name', 
                                version = '1.02', 
                                path = '/Applications/', )
                            ], 
                        package_receipts = openapi_client.models.computer_package_receipts.ComputerPackageReceipts(
                            installed_by_jamf_pro = [
                                'com.jamf.protect.JamfProtect'
                                ], 
                            installed_by_installer_swu = [
                                'com.apple.pkg.Core'
                                ], 
                            cached = [
                                'com.jamf.protect.JamfProtect'
                                ], ), 
                        fonts = [
                            openapi_client.models.computer_font.ComputerFont(
                                name = 'font name', 
                                version = '1.02', 
                                path = '/Applications/', )
                            ], 
                        security = openapi_client.models.computer_security.ComputerSecurity(
                            sip_status = 'ENABLED', 
                            gatekeeper_status = 'APP_STORE_AND_IDENTIFIED_DEVELOPERS', 
                            xprotect_version = '1.2.3', 
                            auto_login_disabled = False, 
                            remote_desktop_enabled = True, 
                            activation_lock_enabled = True, 
                            secure_boot_level = 'FULL_SECURITY', 
                            external_boot_level = 'ALLOW_BOOTING_FROM_EXTERNAL_MEDIA', 
                            bootstrap_token_allowed = True, ), 
                        operating_system = openapi_client.models.computer_operating_system.ComputerOperatingSystem(
                            name = 'Mac OS X', 
                            version = '10.9.5', 
                            build = '13A603', 
                            active_directory_status = 'Not Bound', 
                            master_password_set = True, 
                            file_vault2_status = 'ALL_ENCRYPTED', ), 
                        licensed_software = [
                            openapi_client.models.computer_licensed_software.ComputerLicensedSoftware(
                                id = '1', 
                                name = 'Microsoft Word', )
                            ], 
                        ibeacons = [
                            openapi_client.models.computer_ibeacon.ComputerIbeacon(
                                name = 'room A', )
                            ], 
                        software_updates = [
                            openapi_client.models.computer_software_update.ComputerSoftwareUpdate(
                                name = 'BEdit', 
                                version = '1.15.2', 
                                package_name = 'com.apple.pkg.AdditionalEssentials', )
                            ], 
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
                            ], 
                        content_caching = openapi_client.models.computer_content_caching.ComputerContentCaching(
                            computer_content_caching_information_id = '1', 
                            parents = [
                                openapi_client.models.computer_content_caching_parent.ComputerContentCachingParent(
                                    content_caching_parent_id = '1', 
                                    address = 'SomeAddress', 
                                    alerts = openapi_client.models.computer_content_caching_parent_alert.ComputerContentCachingParentAlert(
                                        content_caching_parent_alert_id = '1', 
                                        addresses = [], 
                                        class_name = 'SomeClass', 
                                        post_date = '2018-10-31T18:04:13Z', ), 
                                    details = openapi_client.models.computer_content_caching_parent_details.ComputerContentCachingParentDetails(
                                        content_caching_parent_details_id = '1', 
                                        ac_power = True, 
                                        cache_size_bytes = 0, 
                                        capabilities = openapi_client.models.computer_content_caching_parent_capabilities.ComputerContentCachingParentCapabilities(
                                            content_caching_parent_capabilities_id = '1', 
                                            imports = True, 
                                            namespaces = True, 
                                            personal_content = True, 
                                            query_parameters = True, 
                                            shared_content = True, 
                                            prioritization = True, ), 
                                        portable = True, 
                                        local_network = [
                                            openapi_client.models.computer_content_caching_parent_local_network.ComputerContentCachingParentLocalNetwork(
                                                content_caching_parent_local_network_id = '1', 
                                                speed = 5000, 
                                                wired = True, )
                                            ], ), 
                                    guid = 'CD1E1291-4AF9-4468-B5D5-0F780C13DB2F', 
                                    healthy = True, 
                                    port = 0, 
                                    version = '1', )
                                ], 
                            alerts = [
                                openapi_client.models.computer_content_caching_alert.ComputerContentCachingAlert(
                                    cache_bytes_limit = 0, 
                                    class_name = 'SomeClass', 
                                    path_preventing_access = '/some/path', 
                                    post_date = '2018-10-31T18:04:13Z', 
                                    reserved_volume_bytes = 0, 
                                    resource = 'SomeResource', )
                                ], 
                            activated = False, 
                            active = False, 
                            actual_cache_bytes_used = 0, 
                            cache_details = [
                                openapi_client.models.computer_content_caching_cache_detail.ComputerContentCachingCacheDetail(
                                    computer_content_caching_cache_details_id = '1', 
                                    category_name = 'SomeCategory', 
                                    disk_space_bytes_used = 0, )
                                ], 
                            cache_bytes_free = 23353884672, 
                            cache_bytes_limit = 0, 
                            cache_status = 'OK', 
                            cache_bytes_used = 0, 
                            data_migration_completed = False, 
                            data_migration_progress_percentage = 0, 
                            data_migration_error = openapi_client.models.computer_content_caching_data_migration_error.ComputerContentCachingDataMigrationError(
                                code = 0, 
                                domain = 'SomeDomain', 
                                user_info = [
                                    openapi_client.models.computer_content_caching_data_migration_error_user_info.ComputerContentCachingDataMigrationErrorUserInfo(
                                        key = 'foo', 
                                        value = 'bar', )
                                    ], ), 
                            max_cache_pressure_last1_hour_percentage = 0, 
                            personal_cache_bytes_free = 23353884672, 
                            personal_cache_bytes_limit = 0, 
                            personal_cache_bytes_used = 0, 
                            port = 0, 
                            public_address = 'SomeAddress', 
                            registration_error = 'NOT_ACTIVATED', 
                            registration_response_code = 403, 
                            registration_started = '2018-10-31T18:04:13Z', 
                            registration_status = 'CONTENT_CACHING_FAILED', 
                            restricted_media = False, 
                            server_guid = 'CD1E1291-4AF9-4468-B5D5-0F780C13DB2F', 
                            startup_status = 'FAILED', 
                            tetherator_status = 'CONTENT_CACHING_DISABLED', 
                            total_bytes_are_since = '2018-10-31T18:04:13Z', 
                            total_bytes_dropped = 0, 
                            total_bytes_imported = 0, 
                            total_bytes_returned_to_children = 0, 
                            total_bytes_returned_to_clients = 0, 
                            total_bytes_returned_to_peers = 0, 
                            total_bytes_stored_from_origin = 0, 
                            total_bytes_stored_from_parents = 0, 
                            total_bytes_stored_from_peers = 0, ), 
                        group_memberships = [
                            openapi_client.models.group_membership.GroupMembership(
                                group_id = '1', 
                                group_name = 'groupOne', 
                                smart_group = True, )
                            ], )
                    ]
            )
        else :
            return ComputerInventorySearchResults(
        )

    def testComputerInventorySearchResults(self):
        """Test ComputerInventorySearchResults"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
