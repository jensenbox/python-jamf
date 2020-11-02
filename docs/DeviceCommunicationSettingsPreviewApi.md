# jamf.DeviceCommunicationSettingsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preview_device_communication_settings_get**](DeviceCommunicationSettingsPreviewApi.md#preview_device_communication_settings_get) | **GET** /preview/device-communication-settings | Retrieves all settings for device communication 
[**preview_device_communication_settings_put**](DeviceCommunicationSettingsPreviewApi.md#preview_device_communication_settings_put) | **PUT** /preview/device-communication-settings | Update device communication settings 


# **preview_device_communication_settings_get**
> DeviceCommunicationSettings preview_device_communication_settings_get()

Retrieves all settings for device communication 

Retrieves all device communication settings, including automatic renewal of the MDM profile. 

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
    api_instance = jamf.DeviceCommunicationSettingsPreviewApi(api_client)
    
    try:
        # Retrieves all settings for device communication 
        api_response = api_instance.preview_device_communication_settings_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceCommunicationSettingsPreviewApi->preview_device_communication_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceCommunicationSettings**](DeviceCommunicationSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Device Communication Settings retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_device_communication_settings_put**
> DeviceCommunicationSettings preview_device_communication_settings_put(device_communication_settings)

Update device communication settings 

Update device communication settings 

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
    api_instance = jamf.DeviceCommunicationSettingsPreviewApi(api_client)
    device_communication_settings = jamf.DeviceCommunicationSettings() # DeviceCommunicationSettings | 

    try:
        # Update device communication settings 
        api_response = api_instance.preview_device_communication_settings_put(device_communication_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceCommunicationSettingsPreviewApi->preview_device_communication_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_communication_settings** | [**DeviceCommunicationSettings**](DeviceCommunicationSettings.md)|  | 

### Return type

[**DeviceCommunicationSettings**](DeviceCommunicationSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Device communication settings updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

