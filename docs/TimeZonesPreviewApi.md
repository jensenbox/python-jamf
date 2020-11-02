# openapi_client.TimeZonesPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_time_zones_get**](TimeZonesPreviewApi.md#v1_time_zones_get) | **GET** /v1/time-zones | Return information about the currently supported Time Zones 


# **v1_time_zones_get**
> list[TimeZone] v1_time_zones_get()

Return information about the currently supported Time Zones 

Returns information about the currently supported time zones 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://tryitout.jamfcloud.com/uapi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://tryitout.jamfcloud.com/uapi"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TimeZonesPreviewApi(api_client)
    
    try:
        # Return information about the currently supported Time Zones 
        api_response = api_instance.v1_time_zones_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TimeZonesPreviewApi->v1_time_zones_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TimeZone]**](TimeZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

