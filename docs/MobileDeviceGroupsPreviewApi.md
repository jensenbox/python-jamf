# jamf.MobileDeviceGroupsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_mobile_device_groups_get**](MobileDeviceGroupsPreviewApi.md#v1_mobile_device_groups_get) | **GET** /v1/mobile-device-groups | Return the list of all Mobile Device Groups 


# **v1_mobile_device_groups_get**
> list[MobileDeviceGroup] v1_mobile_device_groups_get()

Return the list of all Mobile Device Groups 

Returns the list of all mobile device groups. 

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
    api_instance = jamf.MobileDeviceGroupsPreviewApi(api_client)
    
    try:
        # Return the list of all Mobile Device Groups 
        api_response = api_instance.v1_mobile_device_groups_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDeviceGroupsPreviewApi->v1_mobile_device_groups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MobileDeviceGroup]**](MobileDeviceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

