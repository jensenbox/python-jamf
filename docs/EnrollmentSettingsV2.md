# EnrollmentSettingsV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_single_profile** | **bool** |  | [optional] [default to False]
**signing_mdm_profile_enabled** | **bool** |  | [optional] [default to False]
**mdm_signing_certificate** | [**CertificateIdentityV2**](CertificateIdentityV2.md) |  | [optional] 
**restrict_reenrollment** | **bool** |  | [optional] [default to False]
**flush_location_information** | **bool** |  | [optional] [default to False]
**flush_location_history_information** | **bool** |  | [optional] [default to False]
**flush_policy_history** | **bool** |  | [optional] [default to False]
**flush_extension_attributes** | **bool** |  | [optional] [default to False]
**flush_mdm_commands_on_reenroll** | **str** |  | [optional] [default to 'DELETE_EVERYTHING_EXCEPT_ACKNOWLEDGED']
**mac_os_enterprise_enrollment_enabled** | **bool** |  | [optional] [default to False]
**management_username** | **str** |  | [optional] [default to '']
**management_password** | **str** |  | [optional] [default to 'null']
**management_password_set** | **bool** |  | [optional] [readonly] 
**password_type** | **str** |  | [optional] [default to 'STATIC']
**random_password_length** | **int** |  | [optional] [default to 8]
**create_management_account** | **bool** |  | [optional] [default to True]
**hide_management_account** | **bool** |  | [optional] [default to False]
**allow_ssh_only_management_account** | **bool** |  | [optional] [default to False]
**ensure_ssh_running** | **bool** |  | [optional] [default to True]
**launch_self_service** | **bool** |  | [optional] [default to False]
**sign_quick_add** | **bool** |  | [optional] [default to False]
**developer_certificate_identity** | [**CertificateIdentityV2**](CertificateIdentityV2.md) |  | [optional] 
**developer_certificate_identity_details** | [**CertificateDetails**](CertificateDetails.md) |  | [optional] 
**mdm_signing_certificate_details** | [**CertificateDetails**](CertificateDetails.md) |  | [optional] 
**ios_enterprise_enrollment_enabled** | **bool** |  | [optional] [default to True]
**ios_personal_enrollment_enabled** | **bool** |  | [optional] [default to False]
**personal_device_enrollment_type** | **str** |  | [optional] [default to 'PERSONALDEVICEPROFILES']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


