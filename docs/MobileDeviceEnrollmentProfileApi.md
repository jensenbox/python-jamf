# jamf.MobileDeviceEnrollmentProfileApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_mobile_device_enrollment_profile_id_download_profile_get**](MobileDeviceEnrollmentProfileApi.md#v1_mobile_device_enrollment_profile_id_download_profile_get) | **GET** /v1/mobile-device-enrollment-profile/{id}/download-profile | Retrieve the MDM Enrollment Profile 


# **v1_mobile_device_enrollment_profile_id_download_profile_get**
> file v1_mobile_device_enrollment_profile_id_download_profile_get(id)

Retrieve the MDM Enrollment Profile 

Retrieve the MDM Enrollment Profile

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
    api_instance = jamf.MobileDeviceEnrollmentProfileApi(api_client)
    id = 'id_example' # str | MDM Enrollment Profile identifier

    try:
        # Retrieve the MDM Enrollment Profile 
        api_response = api_instance.v1_mobile_device_enrollment_profile_id_download_profile_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDeviceEnrollmentProfileApi->v1_mobile_device_enrollment_profile_id_download_profile_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| MDM Enrollment Profile identifier | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-apple-aspen-config

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

