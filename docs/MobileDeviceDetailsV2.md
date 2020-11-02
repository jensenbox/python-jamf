# MobileDeviceDetailsV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**asset_tag** | **str** |  | [optional] 
**last_inventory_update_timestamp** | **datetime** |  | [optional] 
**os_version** | **str** |  | [optional] 
**os_build** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**udid** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**wifi_mac_address** | **str** |  | [optional] 
**bluetooth_mac_address** | **str** |  | [optional] 
**managed** | **bool** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**initial_entry_timestamp** | **datetime** |  | [optional] 
**last_enrollment_timestamp** | **datetime** |  | [optional] 
**mdm_profile_expiration_timestamp** | **datetime** |  | [optional] 
**device_ownership_level** | **str** |  | [optional] 
**enrollment_method** | **str** |  | [optional] 
**site** | [**MobileDeviceDetailsV2Site**](MobileDeviceDetailsV2Site.md) |  | [optional] 
**extension_attributes** | [**list[ExtensionAttributeV2]**](ExtensionAttributeV2.md) |  | [optional] 
**location** | [**LocationV2**](LocationV2.md) |  | [optional] 
**type** | **str** | Based on the value of this either ios, appleTv, android objects will be populated. | [optional] 
**ios** | [**IosDetailsV2**](IosDetailsV2.md) |  | [optional] 
**tvos** | [**TvOsDetails**](TvOsDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


