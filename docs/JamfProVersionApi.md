# openapi_client.JamfProVersionApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_jamf_pro_version_get**](JamfProVersionApi.md#v1_jamf_pro_version_get) | **GET** /v1/jamf-pro-version | Return information about the Jamf Pro including the current version 


# **v1_jamf_pro_version_get**
> JamfProVersion v1_jamf_pro_version_get()

Return information about the Jamf Pro including the current version 

Returns information about the Jamf Pro including the current version. 

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
    api_instance = openapi_client.JamfProVersionApi(api_client)
    
    try:
        # Return information about the Jamf Pro including the current version 
        api_response = api_instance.v1_jamf_pro_version_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JamfProVersionApi->v1_jamf_pro_version_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JamfProVersion**](JamfProVersion.md)

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

