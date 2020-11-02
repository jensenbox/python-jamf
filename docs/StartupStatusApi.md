# openapi_client.StartupStatusApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**startup_status_get**](StartupStatusApi.md#startup_status_get) | **GET** /startup-status | Retrieve information about application startup 


# **startup_status_get**
> StartupStatus startup_status_get()

Retrieve information about application startup 

Retrieves information about application startup. Current startup operation taking place (if any) and overall startup completion percentage.

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
    api_instance = openapi_client.StartupStatusApi(api_client)
    
    try:
        # Retrieve information about application startup 
        api_response = api_instance.startup_status_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StartupStatusApi->startup_status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StartupStatus**](StartupStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

