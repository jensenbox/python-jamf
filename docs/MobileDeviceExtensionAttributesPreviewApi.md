# jamf.MobileDeviceExtensionAttributesPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_extension_attributes_get**](MobileDeviceExtensionAttributesPreviewApi.md#devices_extension_attributes_get) | **GET** /devices/extensionAttributes | Get Mobile Device Extension Attribute values placed in select paramter 


# **devices_extension_attributes_get**
> MobileDeviceExtensionAttributeResults devices_extension_attributes_get(select=select)

Get Mobile Device Extension Attribute values placed in select paramter 

Gets Mobile Device Extension Attribute values placed in select parameter.

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
    api_instance = jamf.MobileDeviceExtensionAttributesPreviewApi(api_client)
    select = 'name' # str | Acceptable values currently include: * name  (optional) (default to 'name')

    try:
        # Get Mobile Device Extension Attribute values placed in select paramter 
        api_response = api_instance.devices_extension_attributes_get(select=select)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDeviceExtensionAttributesPreviewApi->devices_extension_attributes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Acceptable values currently include: * name  | [optional] [default to &#39;name&#39;]

### Return type

[**MobileDeviceExtensionAttributeResults**](MobileDeviceExtensionAttributeResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Extension Attributes retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

