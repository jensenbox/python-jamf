# jamf.SmartMobileDeviceGroupsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_mobile_devices_id_recalculate_smart_groups_post**](SmartMobileDeviceGroupsPreviewApi.md#v1_mobile_devices_id_recalculate_smart_groups_post) | **POST** /v1/mobile-devices/{id}/recalculate-smart-groups | Recalculate all smart groups for the given device id and then return count of smart groups that device fall into 
[**v1_smart_mobile_device_groups_id_recalculate_post**](SmartMobileDeviceGroupsPreviewApi.md#v1_smart_mobile_device_groups_id_recalculate_post) | **POST** /v1/smart-mobile-device-groups/{id}/recalculate | Recalculate a smart group for the given id then return the ids for the devices in the smart group 


# **v1_mobile_devices_id_recalculate_smart_groups_post**
> RecalculationResults v1_mobile_devices_id_recalculate_smart_groups_post(id)

Recalculate all smart groups for the given device id and then return count of smart groups that device fall into 

Recalculates all smart groups for the given device id and then returns the count of smart groups the device falls into 

### Example

```python
from __future__ import print_function
import time
import jamf
from jamf.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://tryitout.jamfcloud.com/uapi
# See configuration.py for a list of all supported configuration parameters.
configuration = jamf.Configuration(
    host = "https://tryitout.jamfcloud.com/uapi"
)


# Enter a context with an instance of the API client
with jamf.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jamf.SmartMobileDeviceGroupsPreviewApi(api_client)
    id = 56 # int | id of mobile device

    try:
        # Recalculate all smart groups for the given device id and then return count of smart groups that device fall into 
        api_response = api_instance.v1_mobile_devices_id_recalculate_smart_groups_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartMobileDeviceGroupsPreviewApi->v1_mobile_devices_id_recalculate_smart_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of mobile device | 

### Return type

[**RecalculationResults**](RecalculationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | smart group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_smart_mobile_device_groups_id_recalculate_post**
> RecalculationResults v1_smart_mobile_device_groups_id_recalculate_post(id)

Recalculate a smart group for the given id then return the ids for the devices in the smart group 

recalculates a smart group for the given id and then returns the ids for the devices in the smart group 

### Example

```python
from __future__ import print_function
import time
import jamf
from jamf.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://tryitout.jamfcloud.com/uapi
# See configuration.py for a list of all supported configuration parameters.
configuration = jamf.Configuration(
    host = "https://tryitout.jamfcloud.com/uapi"
)


# Enter a context with an instance of the API client
with jamf.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = jamf.SmartMobileDeviceGroupsPreviewApi(api_client)
    id = 56 # int | instance id of smart group

    try:
        # Recalculate a smart group for the given id then return the ids for the devices in the smart group 
        api_response = api_instance.v1_smart_mobile_device_groups_id_recalculate_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartMobileDeviceGroupsPreviewApi->v1_smart_mobile_device_groups_id_recalculate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| instance id of smart group | 

### Return type

[**RecalculationResults**](RecalculationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | smart group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

