# jamf.DeviceEnrollmentsDevicesApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_device_enrollments_id_devices_get**](DeviceEnrollmentsDevicesApi.md#v1_device_enrollments_id_devices_get) | **GET** /v1/device-enrollments/{id}/devices | Retrieve a list of Devices assigned to the supplied id 


# **v1_device_enrollments_id_devices_get**
> DeviceEnrollmentDeviceSearchResults v1_device_enrollments_id_devices_get(id)

Retrieve a list of Devices assigned to the supplied id 

Retrieves a list of devices assigned to the supplied id

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
    api_instance = jamf.DeviceEnrollmentsDevicesApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier

    try:
        # Retrieve a list of Devices assigned to the supplied id 
        api_response = api_instance.v1_device_enrollments_id_devices_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsDevicesApi->v1_device_enrollments_id_devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 

### Return type

[**DeviceEnrollmentDeviceSearchResults**](DeviceEnrollmentDeviceSearchResults.md)

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

