# DeviceEnrollmentPrestage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**is_mandatory** | **bool** |  | 
**is_mdm_removable** | **bool** |  | 
**support_phone_number** | **str** |  | 
**support_email_address** | **str** |  | 
**department** | **str** |  | 
**is_default_prestage** | **bool** |  | 
**enrollment_site_id** | **int** |  | 
**is_keep_existing_site_membership** | **bool** |  | 
**is_keep_existing_location_information** | **bool** |  | 
**is_require_authentication** | **bool** |  | 
**authentication_prompt** | **str** |  | 
**is_prevent_activation_lock** | **bool** |  | 
**is_enable_device_based_activation_lock** | **bool** |  | 
**device_enrollment_program_instance_id** | **int** |  | 
**skip_setup_items** | **dict(str, bool)** |  | [optional] 
**location_information** | [**LocationInformation**](LocationInformation.md) |  | 
**purchasing_information** | [**PrestagePurchasingInformation**](PrestagePurchasingInformation.md) |  | 
**anchor_certificates** | **list[str]** | The Base64 encoded PEM Certificate | [optional] 
**enrollment_customization_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


