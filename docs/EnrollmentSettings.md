# EnrollmentSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_install_single_profile** | **bool** |  | [optional] [default to False]
**is_signing_mdm_profile_enabled** | **bool** |  | [optional] [default to False]
**mdm_signing_certificate** | [**MDMSigningCertificate**](MDMSigningCertificate.md) |  | [optional] 
**is_restrict_reenrollment** | **bool** |  | [optional] [default to False]
**is_flush_location_information** | **bool** |  | [optional] [default to False]
**is_flush_location_history_information** | **bool** |  | [optional] [default to False]
**is_flush_policy_history** | **bool** |  | [optional] [default to False]
**is_flush_extension_attributes** | **bool** |  | [optional] [default to False]
**flush_mdm_commands_on_reenroll** | **str** |  | [optional] [default to 'DELETE_EVERYTHING_EXCEPT_ACKNOWLEDGED']
**is_enabled_macos_enterprise_enrollment** | **bool** |  | [optional] [default to False]
**management_username** | **str** |  | [optional] [default to '']
**management_password** | **str** |  | [optional] [default to 'null']
**password_type** | **str** |  | [optional] [default to 'STATIC']
**random_password_length** | **int** |  | [optional] [default to 8]
**is_create_management_account** | **bool** |  | [optional] [default to True]
**is_hide_management_account** | **bool** |  | [optional] [default to False]
**is_allow_ssh_only_management_account** | **bool** |  | [optional] [default to False]
**is_ensure_ssh_running** | **bool** |  | [optional] [default to True]
**is_launch_self_service** | **bool** |  | [optional] [default to False]
**is_sign_quick_add** | **bool** |  | [optional] [default to False]
**developer_certificate_identity** | [**EnrollmentSettingsDeveloperCertificateIdentity**](EnrollmentSettingsDeveloperCertificateIdentity.md) |  | [optional] 
**developer_certificate_identity_details** | [**CertificateDetails**](CertificateDetails.md) |  | [optional] 
**mdm_signing_certificate_details** | [**CertificateDetails**](CertificateDetails.md) |  | [optional] 
**is_enable_ios_enterprise_enrollment** | **bool** |  | [optional] [default to True]
**is_enable_ios_personal_enrollment** | **bool** |  | [optional] [default to False]
**personal_device_enrollment_type** | **str** |  | [optional] [default to 'PERSONALDEVICEPROFILES']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


