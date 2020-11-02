# DeviceEnrollmentPrestageV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**mandatory** | **bool** |  | 
**mdm_removable** | **bool** |  | 
**support_phone_number** | **str** |  | 
**support_email_address** | **str** |  | 
**department** | **str** |  | 
**default_prestage** | **bool** |  | 
**enrollment_site_id** | **str** |  | 
**keep_existing_site_membership** | **bool** |  | 
**keep_existing_location_information** | **bool** |  | 
**require_authentication** | **bool** |  | 
**authentication_prompt** | **str** |  | 
**prevent_activation_lock** | **bool** |  | 
**enable_device_based_activation_lock** | **bool** |  | 
**device_enrollment_program_instance_id** | **str** |  | 
**skip_setup_items** | **dict(str, bool)** |  | [optional] 
**location_information** | [**LocationInformationV2**](LocationInformationV2.md) |  | 
**purchasing_information** | [**PrestagePurchasingInformationV2**](PrestagePurchasingInformationV2.md) |  | 
**anchor_certificates** | **list[str]** | The Base64 encoded PEM Certificate | [optional] 
**enrollment_customization_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**auto_advance_setup** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


