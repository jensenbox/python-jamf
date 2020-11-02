# coding: utf-8

# flake8: noqa
"""
    Jamf Pro API

    ## Overview This is a sample Jamf Pro server which allows for usage without any authentication. The Jamf Pro environment which supports the Try it Out functionality does not run the current beta version of Jamf Pro, thus any newly added endpoints will result in an error and should be used soley for documentation purposes.   # noqa: E501

    The version of the OpenAPI document: 10.25.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from jamf.models.access_groups_search_results import AccessGroupsSearchResults
from jamf.models.access_groups_v2_search_results import AccessGroupsV2SearchResults
from jamf.models.account import Account
from jamf.models.account_group import AccountGroup
from jamf.models.account_preferences import AccountPreferences
from jamf.models.account_preferences_v1 import AccountPreferencesV1
from jamf.models.active_patch_history import ActivePatchHistory
from jamf.models.active_patch_history_search_results import ActivePatchHistorySearchResults
from jamf.models.active_patch_summary import ActivePatchSummary
from jamf.models.admin_account import AdminAccount
from jamf.models.advanced_search import AdvancedSearch
from jamf.models.advanced_search_criteria_choices import AdvancedSearchCriteriaChoices
from jamf.models.advanced_search_search_results import AdvancedSearchSearchResults
from jamf.models.advanced_user_content_search import AdvancedUserContentSearch
from jamf.models.advanced_user_content_search_search_results import AdvancedUserContentSearchSearchResults
from jamf.models.android_details import AndroidDetails
from jamf.models.android_details_computer import AndroidDetailsComputer
from jamf.models.api_error import ApiError
from jamf.models.api_error_cause import ApiErrorCause
from jamf.models.app_dynamics_config import AppDynamicsConfig
from jamf.models.app_request_form_input_field import AppRequestFormInputField
from jamf.models.app_request_form_input_field_search_results import AppRequestFormInputFieldSearchResults
from jamf.models.app_request_settings import AppRequestSettings
from jamf.models.apple_tv_details import AppleTvDetails
from jamf.models.assign_remove_profile_response_sync_state import AssignRemoveProfileResponseSyncState
from jamf.models.auth_account import AuthAccount
from jamf.models.auth_account_v1 import AuthAccountV1
from jamf.models.auth_token import AuthToken
from jamf.models.auth_token_v1 import AuthTokenV1
from jamf.models.authorization import Authorization
from jamf.models.authorization_v1 import AuthorizationV1
from jamf.models.branding_configuration import BrandingConfiguration
from jamf.models.branding_image_url import BrandingImageUrl
from jamf.models.branding_search_results import BrandingSearchResults
from jamf.models.building import Building
from jamf.models.building_search_results import BuildingSearchResults
from jamf.models.cache_settings import CacheSettings
from jamf.models.categories_search_results import CategoriesSearchResults
from jamf.models.category import Category
from jamf.models.certificate_details import CertificateDetails
from jamf.models.certificate_identity_v2 import CertificateIdentityV2
from jamf.models.certificate_key import CertificateKey
from jamf.models.client_check_in import ClientCheckIn
from jamf.models.client_check_in_v2 import ClientCheckInV2
from jamf.models.cloud_ldap_configuration_request import CloudLdapConfigurationRequest
from jamf.models.cloud_ldap_configuration_response import CloudLdapConfigurationResponse
from jamf.models.cloud_ldap_configuration_search_results import CloudLdapConfigurationSearchResults
from jamf.models.cloud_ldap_configuration_short_response import CloudLdapConfigurationShortResponse
from jamf.models.cloud_ldap_configuration_update import CloudLdapConfigurationUpdate
from jamf.models.cloud_ldap_connection_pool_statistics import CloudLdapConnectionPoolStatistics
from jamf.models.cloud_ldap_keystore import CloudLdapKeystore
from jamf.models.cloud_ldap_keystore_file import CloudLdapKeystoreFile
from jamf.models.cloud_ldap_mappings_request import CloudLdapMappingsRequest
from jamf.models.cloud_ldap_mappings_response import CloudLdapMappingsResponse
from jamf.models.cloud_ldap_server_request import CloudLdapServerRequest
from jamf.models.cloud_ldap_server_response import CloudLdapServerResponse
from jamf.models.cloud_ldap_server_update import CloudLdapServerUpdate
from jamf.models.computer_application import ComputerApplication
from jamf.models.computer_attachment import ComputerAttachment
from jamf.models.computer_certificate import ComputerCertificate
from jamf.models.computer_configuration_profile import ComputerConfigurationProfile
from jamf.models.computer_content_caching import ComputerContentCaching
from jamf.models.computer_content_caching_alert import ComputerContentCachingAlert
from jamf.models.computer_content_caching_cache_detail import ComputerContentCachingCacheDetail
from jamf.models.computer_content_caching_data_migration_error import ComputerContentCachingDataMigrationError
from jamf.models.computer_content_caching_data_migration_error_user_info import ComputerContentCachingDataMigrationErrorUserInfo
from jamf.models.computer_content_caching_parent import ComputerContentCachingParent
from jamf.models.computer_content_caching_parent_alert import ComputerContentCachingParentAlert
from jamf.models.computer_content_caching_parent_capabilities import ComputerContentCachingParentCapabilities
from jamf.models.computer_content_caching_parent_details import ComputerContentCachingParentDetails
from jamf.models.computer_content_caching_parent_local_network import ComputerContentCachingParentLocalNetwork
from jamf.models.computer_disk import ComputerDisk
from jamf.models.computer_disk_encryption import ComputerDiskEncryption
from jamf.models.computer_extension_attribute import ComputerExtensionAttribute
from jamf.models.computer_font import ComputerFont
from jamf.models.computer_general import ComputerGeneral
from jamf.models.computer_general_update import ComputerGeneralUpdate
from jamf.models.computer_hardware import ComputerHardware
from jamf.models.computer_hardware_update import ComputerHardwareUpdate
from jamf.models.computer_ibeacon import ComputerIbeacon
from jamf.models.computer_inventory_response import ComputerInventoryResponse
from jamf.models.computer_inventory_search_results import ComputerInventorySearchResults
from jamf.models.computer_inventory_update_request import ComputerInventoryUpdateRequest
from jamf.models.computer_licensed_software import ComputerLicensedSoftware
from jamf.models.computer_local_user_account import ComputerLocalUserAccount
from jamf.models.computer_location import ComputerLocation
from jamf.models.computer_mdm_capability import ComputerMdmCapability
from jamf.models.computer_operating_system import ComputerOperatingSystem
from jamf.models.computer_operating_system_update import ComputerOperatingSystemUpdate
from jamf.models.computer_overview import ComputerOverview
from jamf.models.computer_package_receipts import ComputerPackageReceipts
from jamf.models.computer_partition import ComputerPartition
from jamf.models.computer_partition_encryption import ComputerPartitionEncryption
from jamf.models.computer_partition_file_vault2_state import ComputerPartitionFileVault2State
from jamf.models.computer_plugin import ComputerPlugin
from jamf.models.computer_prestage import ComputerPrestage
from jamf.models.computer_prestage_all_of import ComputerPrestageAllOf
from jamf.models.computer_prestage_search_results import ComputerPrestageSearchResults
from jamf.models.computer_prestage_search_results_v2 import ComputerPrestageSearchResultsV2
from jamf.models.computer_prestage_v2 import ComputerPrestageV2
from jamf.models.computer_prestage_v2_all_of import ComputerPrestageV2AllOf
from jamf.models.computer_printer import ComputerPrinter
from jamf.models.computer_purchase import ComputerPurchase
from jamf.models.computer_remote_management import ComputerRemoteManagement
from jamf.models.computer_section import ComputerSection
from jamf.models.computer_security import ComputerSecurity
from jamf.models.computer_service import ComputerService
from jamf.models.computer_software_update import ComputerSoftwareUpdate
from jamf.models.computer_storage import ComputerStorage
from jamf.models.computer_user_and_location import ComputerUserAndLocation
from jamf.models.computers_search_results import ComputersSearchResults
from jamf.models.configuration_profile import ConfigurationProfile
from jamf.models.country import Country
from jamf.models.country_codes import CountryCodes
from jamf.models.current_account import CurrentAccount
from jamf.models.current_authorization import CurrentAuthorization
from jamf.models.database_password import DatabasePassword
from jamf.models.day_of_week import DayOfWeek
from jamf.models.department import Department
from jamf.models.departments_search_results import DepartmentsSearchResults
from jamf.models.device_communication_settings import DeviceCommunicationSettings
from jamf.models.device_enrollment_device import DeviceEnrollmentDevice
from jamf.models.device_enrollment_device_search_results import DeviceEnrollmentDeviceSearchResults
from jamf.models.device_enrollment_disown_body import DeviceEnrollmentDisownBody
from jamf.models.device_enrollment_disown_response import DeviceEnrollmentDisownResponse
from jamf.models.device_enrollment_instance import DeviceEnrollmentInstance
from jamf.models.device_enrollment_instance_search_results import DeviceEnrollmentInstanceSearchResults
from jamf.models.device_enrollment_instance_sync_status import DeviceEnrollmentInstanceSyncStatus
from jamf.models.device_enrollment_prestage import DeviceEnrollmentPrestage
from jamf.models.device_enrollment_prestage_v2 import DeviceEnrollmentPrestageV2
from jamf.models.device_enrollment_token import DeviceEnrollmentToken
from jamf.models.ebook import Ebook
from jamf.models.ebook_exclusions import EbookExclusions
from jamf.models.ebook_limitations import EbookLimitations
from jamf.models.ebook_limitations_users import EbookLimitationsUsers
from jamf.models.ebook_scope import EbookScope
from jamf.models.ebook_search_results import EbookSearchResults
from jamf.models.engage import Engage
from jamf.models.enrollment_access_group import EnrollmentAccessGroup
from jamf.models.enrollment_access_group_v2 import EnrollmentAccessGroupV2
from jamf.models.enrollment_customization import EnrollmentCustomization
from jamf.models.enrollment_customization_branding_settings import EnrollmentCustomizationBrandingSettings
from jamf.models.enrollment_customization_dependencies import EnrollmentCustomizationDependencies
from jamf.models.enrollment_customization_dependency import EnrollmentCustomizationDependency
from jamf.models.enrollment_customization_ldap_group_access import EnrollmentCustomizationLdapGroupAccess
from jamf.models.enrollment_customization_panel import EnrollmentCustomizationPanel
from jamf.models.enrollment_customization_panel_ldap_auth import EnrollmentCustomizationPanelLdapAuth
from jamf.models.enrollment_customization_panel_ldap_auth_all_of import EnrollmentCustomizationPanelLdapAuthAllOf
from jamf.models.enrollment_customization_panel_list import EnrollmentCustomizationPanelList
from jamf.models.enrollment_customization_panel_sso_auth import EnrollmentCustomizationPanelSsoAuth
from jamf.models.enrollment_customization_panel_sso_auth_all_of import EnrollmentCustomizationPanelSsoAuthAllOf
from jamf.models.enrollment_customization_panel_text import EnrollmentCustomizationPanelText
from jamf.models.enrollment_customization_panel_text_all_of import EnrollmentCustomizationPanelTextAllOf
from jamf.models.enrollment_customization_search_results import EnrollmentCustomizationSearchResults
from jamf.models.enrollment_customization_search_results_v2 import EnrollmentCustomizationSearchResultsV2
from jamf.models.enrollment_customization_v2 import EnrollmentCustomizationV2
from jamf.models.enrollment_method import EnrollmentMethod
from jamf.models.enrollment_process_text_object import EnrollmentProcessTextObject
from jamf.models.enrollment_settings import EnrollmentSettings
from jamf.models.enrollment_settings_developer_certificate_identity import EnrollmentSettingsDeveloperCertificateIdentity
from jamf.models.enrollment_settings_v2 import EnrollmentSettingsV2
from jamf.models.extension_attribute import ExtensionAttribute
from jamf.models.extension_attribute_v2 import ExtensionAttributeV2
from jamf.models.file_attachment import FileAttachment
from jamf.models.file_attachment_delete import FileAttachmentDelete
from jamf.models.file_attachment_v2 import FileAttachmentV2
from jamf.models.filter import Filter
from jamf.models.get_computer_prestage import GetComputerPrestage
from jamf.models.get_computer_prestage_all_of import GetComputerPrestageAllOf
from jamf.models.get_computer_prestage_v2 import GetComputerPrestageV2
from jamf.models.get_computer_prestage_v2_all_of import GetComputerPrestageV2AllOf
from jamf.models.get_enrollment_customization import GetEnrollmentCustomization
from jamf.models.get_enrollment_customization_all_of import GetEnrollmentCustomizationAllOf
from jamf.models.get_enrollment_customization_panel import GetEnrollmentCustomizationPanel
from jamf.models.get_enrollment_customization_panel_all_of import GetEnrollmentCustomizationPanelAllOf
from jamf.models.get_enrollment_customization_panel_ldap_auth import GetEnrollmentCustomizationPanelLdapAuth
from jamf.models.get_enrollment_customization_panel_ldap_auth_all_of import GetEnrollmentCustomizationPanelLdapAuthAllOf
from jamf.models.get_enrollment_customization_panel_sso_auth import GetEnrollmentCustomizationPanelSsoAuth
from jamf.models.get_enrollment_customization_panel_sso_auth_all_of import GetEnrollmentCustomizationPanelSsoAuthAllOf
from jamf.models.get_enrollment_customization_panel_text import GetEnrollmentCustomizationPanelText
from jamf.models.get_mobile_device_prestage import GetMobileDevicePrestage
from jamf.models.get_mobile_device_prestage_v2 import GetMobileDevicePrestageV2
from jamf.models.get_mobile_device_prestage_v2_all_of import GetMobileDevicePrestageV2AllOf
from jamf.models.group_mappings import GroupMappings
from jamf.models.group_membership import GroupMembership
from jamf.models.group_test_search import GroupTestSearch
from jamf.models.group_test_search_request import GroupTestSearchRequest
from jamf.models.group_test_search_response import GroupTestSearchResponse
from jamf.models.history_search_results import HistorySearchResults
from jamf.models.history_search_results_v1 import HistorySearchResultsV1
from jamf.models.href_response import HrefResponse
from jamf.models.ids import Ids
from jamf.models.initialize import Initialize
from jamf.models.inline_object import InlineObject
from jamf.models.inline_object1 import InlineObject1
from jamf.models.inline_object2 import InlineObject2
from jamf.models.inline_object3 import InlineObject3
from jamf.models.inventory_information import InventoryInformation
from jamf.models.inventory_preload_csv_error import InventoryPreloadCsvError
from jamf.models.inventory_preload_csv_validation_error import InventoryPreloadCsvValidationError
from jamf.models.inventory_preload_csv_validation_error_cause import InventoryPreloadCsvValidationErrorCause
from jamf.models.inventory_preload_csv_validation_error_cause_all_of import InventoryPreloadCsvValidationErrorCauseAllOf
from jamf.models.inventory_preload_csv_validation_success import InventoryPreloadCsvValidationSuccess
from jamf.models.inventory_preload_extension_attribute import InventoryPreloadExtensionAttribute
from jamf.models.inventory_preload_invalid_csv_response import InventoryPreloadInvalidCsvResponse
from jamf.models.inventory_preload_record import InventoryPreloadRecord
from jamf.models.inventory_preload_record_search_results import InventoryPreloadRecordSearchResults
from jamf.models.inventory_preload_record_search_results_v2 import InventoryPreloadRecordSearchResultsV2
from jamf.models.inventory_preload_record_v2 import InventoryPreloadRecordV2
from jamf.models.ios_details import IosDetails
from jamf.models.ios_details_applications import IosDetailsApplications
from jamf.models.ios_details_attachments import IosDetailsAttachments
from jamf.models.ios_details_certificates import IosDetailsCertificates
from jamf.models.ios_details_computer import IosDetailsComputer
from jamf.models.ios_details_ebooks import IosDetailsEbooks
from jamf.models.ios_details_v2 import IosDetailsV2
from jamf.models.ios_details_v2_attachments import IosDetailsV2Attachments
from jamf.models.ios_details_v2_certificates import IosDetailsV2Certificates
from jamf.models.ios_details_v2_computer import IosDetailsV2Computer
from jamf.models.jamf_pro_information import JamfProInformation
from jamf.models.jamf_pro_server_url import JamfProServerUrl
from jamf.models.jamf_pro_version import JamfProVersion
from jamf.models.language_code import LanguageCode
from jamf.models.ldap_group import LdapGroup
from jamf.models.ldap_group_search_results import LdapGroupSearchResults
from jamf.models.ldap_server import LdapServer
from jamf.models.locale import Locale
from jamf.models.location import Location
from jamf.models.location_building import LocationBuilding
from jamf.models.location_department import LocationDepartment
from jamf.models.location_information import LocationInformation
from jamf.models.location_information_v2 import LocationInformationV2
from jamf.models.location_v2 import LocationV2
from jamf.models.mdm_signing_certificate import MDMSigningCertificate
from jamf.models.markdown import Markdown
from jamf.models.membership_mappings import MembershipMappings
from jamf.models.membership_test_search_request import MembershipTestSearchRequest
from jamf.models.membership_test_search_response import MembershipTestSearchResponse
from jamf.models.memcached_endpoints import MemcachedEndpoints
from jamf.models.mobile_device import MobileDevice
from jamf.models.mobile_device_details import MobileDeviceDetails
from jamf.models.mobile_device_details_v2 import MobileDeviceDetailsV2
from jamf.models.mobile_device_details_v2_site import MobileDeviceDetailsV2Site
from jamf.models.mobile_device_extension_attribute_results import MobileDeviceExtensionAttributeResults
from jamf.models.mobile_device_extension_attribute_results_extension_attributes import MobileDeviceExtensionAttributeResultsExtensionAttributes
from jamf.models.mobile_device_group import MobileDeviceGroup
from jamf.models.mobile_device_prestage import MobileDevicePrestage
from jamf.models.mobile_device_prestage_all_of import MobileDevicePrestageAllOf
from jamf.models.mobile_device_prestage_name import MobileDevicePrestageName
from jamf.models.mobile_device_prestage_name_v2 import MobileDevicePrestageNameV2
from jamf.models.mobile_device_prestage_names import MobileDevicePrestageNames
from jamf.models.mobile_device_prestage_names_v2 import MobileDevicePrestageNamesV2
from jamf.models.mobile_device_prestage_search_results import MobileDevicePrestageSearchResults
from jamf.models.mobile_device_prestage_search_results_v2 import MobileDevicePrestageSearchResultsV2
from jamf.models.mobile_device_prestage_v2 import MobileDevicePrestageV2
from jamf.models.mobile_device_prestage_v2_all_of import MobileDevicePrestageV2AllOf
from jamf.models.mobile_device_search_params import MobileDeviceSearchParams
from jamf.models.mobile_device_search_results import MobileDeviceSearchResults
from jamf.models.mobile_device_search_results_v2 import MobileDeviceSearchResultsV2
from jamf.models.mobile_device_v2 import MobileDeviceV2
from jamf.models.network import Network
from jamf.models.network_v2 import NetworkV2
from jamf.models.notification import Notification
from jamf.models.object_history import ObjectHistory
from jamf.models.object_history_note import ObjectHistoryNote
from jamf.models.object_history_v1 import ObjectHistoryV1
from jamf.models.order_by import OrderBy
from jamf.models.parent_app import ParentApp
from jamf.models.patch_policy_attempt import PatchPolicyAttempt
from jamf.models.patch_policy_attempt_action import PatchPolicyAttemptAction
from jamf.models.patch_policy_log import PatchPolicyLog
from jamf.models.patch_policy_log_search_results import PatchPolicyLogSearchResults
from jamf.models.patch_policy_on_dashboard import PatchPolicyOnDashboard
from jamf.models.patch_policy_summary import PatchPolicySummary
from jamf.models.patch_version import PatchVersion
from jamf.models.policy_properties import PolicyProperties
from jamf.models.prestage_dependencies import PrestageDependencies
from jamf.models.prestage_dependency import PrestageDependency
from jamf.models.prestage_file_attachment import PrestageFileAttachment
from jamf.models.prestage_file_attachment_v2 import PrestageFileAttachmentV2
from jamf.models.prestage_purchasing_information import PrestagePurchasingInformation
from jamf.models.prestage_purchasing_information_v2 import PrestagePurchasingInformationV2
from jamf.models.prestage_scope import PrestageScope
from jamf.models.prestage_scope_assignment import PrestageScopeAssignment
from jamf.models.prestage_scope_assignment_v2 import PrestageScopeAssignmentV2
from jamf.models.prestage_scope_response import PrestageScopeResponse
from jamf.models.prestage_scope_response_v2 import PrestageScopeResponseV2
from jamf.models.prestage_scope_update import PrestageScopeUpdate
from jamf.models.prestage_scope_v2 import PrestageScopeV2
from jamf.models.prestage_sync_status import PrestageSyncStatus
from jamf.models.prestage_sync_status_v2 import PrestageSyncStatusV2
from jamf.models.process_texts_search_results import ProcessTextsSearchResults
from jamf.models.provisioning_profile import ProvisioningProfile
from jamf.models.purchasing import Purchasing
from jamf.models.purchasing_v2 import PurchasingV2
from jamf.models.put_computer_prestage import PutComputerPrestage
from jamf.models.put_computer_prestage_all_of import PutComputerPrestageAllOf
from jamf.models.put_computer_prestage_v2 import PutComputerPrestageV2
from jamf.models.put_mobile_device_prestage import PutMobileDevicePrestage
from jamf.models.put_mobile_device_prestage_v2 import PutMobileDevicePrestageV2
from jamf.models.recalculation_results import RecalculationResults
from jamf.models.recipient import Recipient
from jamf.models.recipients import Recipients
from jamf.models.reenrollment import Reenrollment
from jamf.models.retry_patch_policy_params import RetryPatchPolicyParams
from jamf.models.script import Script
from jamf.models.scripts_search_results import ScriptsSearchResults
from jamf.models.search_active_patch_history_params import SearchActivePatchHistoryParams
from jamf.models.search_params import SearchParams
from jamf.models.search_patch_policy_log_params import SearchPatchPolicyLogParams
from jamf.models.security import Security
from jamf.models.security_v2 import SecurityV2
from jamf.models.self_service_install_settings import SelfServiceInstallSettings
from jamf.models.self_service_interaction_settings import SelfServiceInteractionSettings
from jamf.models.self_service_login_settings import SelfServiceLoginSettings
from jamf.models.self_service_settings import SelfServiceSettings
from jamf.models.session import Session
from jamf.models.site import Site
from jamf.models.smart_search_criterion import SmartSearchCriterion
from jamf.models.software_title_configuration import SoftwareTitleConfiguration
from jamf.models.software_title_patch_policy_summaries import SoftwareTitlePatchPolicySummaries
from jamf.models.sso_keystore import SsoKeystore
from jamf.models.sso_keystore_all_of import SsoKeystoreAllOf
from jamf.models.sso_keystore_cert_parse_response import SsoKeystoreCertParseResponse
from jamf.models.sso_keystore_details import SsoKeystoreDetails
from jamf.models.sso_keystore_parse import SsoKeystoreParse
from jamf.models.sso_keystore_response import SsoKeystoreResponse
from jamf.models.sso_keystore_response_with_details import SsoKeystoreResponseWithDetails
from jamf.models.sso_keystore_with_details import SsoKeystoreWithDetails
from jamf.models.sso_metadata_url import SsoMetadataUrl
from jamf.models.sso_settings import SsoSettings
from jamf.models.startup_status import StartupStatus
from jamf.models.static_user_group import StaticUserGroup
from jamf.models.supervision_identity import SupervisionIdentity
from jamf.models.supervision_identity_certificate_upload import SupervisionIdentityCertificateUpload
from jamf.models.supervision_identity_create import SupervisionIdentityCreate
from jamf.models.supervision_identity_search_results import SupervisionIdentitySearchResults
from jamf.models.supervision_identity_update import SupervisionIdentityUpdate
from jamf.models.teacher_features import TeacherFeatures
from jamf.models.teacher_settings_request import TeacherSettingsRequest
from jamf.models.teacher_settings_response import TeacherSettingsResponse
from jamf.models.time_frame import TimeFrame
from jamf.models.time_zone import TimeZone
from jamf.models.tv_os_details import TvOsDetails
from jamf.models.update_apple_tv import UpdateAppleTv
from jamf.models.update_ios import UpdateIos
from jamf.models.update_ios_v2 import UpdateIosV2
from jamf.models.update_mobile_device import UpdateMobileDevice
from jamf.models.update_mobile_device_v2 import UpdateMobileDeviceV2
from jamf.models.update_tv_os import UpdateTvOs
from jamf.models.user_attributes import UserAttributes
from jamf.models.user_mappings import UserMappings
from jamf.models.user_test_search import UserTestSearch
from jamf.models.user_test_search_request import UserTestSearchRequest
from jamf.models.user_test_search_response import UserTestSearchResponse
from jamf.models.v1_site import V1Site
from jamf.models.vpp_admin_account import VPPAdminAccount
from jamf.models.venafi_ca_record import VenafiCaRecord
from jamf.models.venafi_service_status import VenafiServiceStatus
from jamf.models.vpp_token_subscription import VppTokenSubscription
from jamf.models.web_link import WebLink
