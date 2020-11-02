# ComputerExtensionAttribute

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_id** | **str** | An identifier of extension attribute definition. | [optional] 
**name** | **str** | A human-readable name by which attribute can be referred to. | [optional] [readonly] 
**description** | **str** | An additional explanation of exact attribute meaning, possible values, etc. | [optional] [readonly] 
**enabled** | **bool** |  | [optional] [readonly] 
**multi_value** | **bool** |  | [optional] [readonly] 
**values** | **list[str]** | A value of extension attribute, in some rare cases there may be multiple values present, hence the array.  | [optional] 
**data_type** | **str** | A data type of extension attribute. | [optional] [readonly] 
**options** | **list[str]** | A closed list of possible values (applies to &#x60;popup&#x60; input type).  | [optional] [readonly] 
**input_type** | **str** | The input method. &#x60;text&#x60; is most common and means simply free text, &#x60;popup&#x60; i a closed list of values from which one or many can be selected and &#x60;script&#x60; value is calculated and can never be set directly.  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


