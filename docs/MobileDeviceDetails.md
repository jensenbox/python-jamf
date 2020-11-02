# MobileDeviceDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
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
**is_managed** | **bool** |  | [optional] 
**initial_entry_timestamp** | **datetime** |  | [optional] 
**last_enrollment_timestamp** | **datetime** |  | [optional] 
**device_ownership_level** | **str** |  | [optional] 
**site** | [**LocationBuilding**](LocationBuilding.md) |  | [optional] 
**extension_attributes** | [**list[ExtensionAttribute]**](ExtensionAttribute.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**type** | **str** | Based on the value of this either ios, appleTv, android objects will be populated. | [optional] 
**ios** | [**IosDetails**](IosDetails.md) |  | [optional] 
**apple_tv** | [**AppleTvDetails**](AppleTvDetails.md) |  | [optional] 
**android** | [**AndroidDetails**](AndroidDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


