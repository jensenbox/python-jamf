# openapi_client.SelfServicePreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_obj_selfservice_get**](SelfServicePreviewApi.md#settings_obj_selfservice_get) | **GET** /settings/obj/selfservice | Get an object representation of Self Service settings 
[**settings_obj_selfservice_put**](SelfServicePreviewApi.md#settings_obj_selfservice_put) | **PUT** /settings/obj/selfservice | Put an object representation of Self Service settings 


# **settings_obj_selfservice_get**
> SelfServiceSettings settings_obj_selfservice_get()

Get an object representation of Self Service settings 

gets an object representation of Self Service settings 

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
    api_instance = openapi_client.SelfServicePreviewApi(api_client)
    
    try:
        # Get an object representation of Self Service settings 
        api_response = api_instance.settings_obj_selfservice_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SelfServicePreviewApi->settings_obj_selfservice_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SelfServiceSettings**](SelfServiceSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful GET  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_obj_selfservice_put**
> SelfServiceSettings settings_obj_selfservice_put(self_service_settings)

Put an object representation of Self Service settings 

puts an object representation of Self Service settings 

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
    api_instance = openapi_client.SelfServicePreviewApi(api_client)
    self_service_settings = openapi_client.SelfServiceSettings() # SelfServiceSettings | object that contains all editable global fields to alter Self Service settings 

    try:
        # Put an object representation of Self Service settings 
        api_response = api_instance.settings_obj_selfservice_put(self_service_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SelfServicePreviewApi->settings_obj_selfservice_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_service_settings** | [**SelfServiceSettings**](SelfServiceSettings.md)| object that contains all editable global fields to alter Self Service settings  | 

### Return type

[**SelfServiceSettings**](SelfServiceSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful PUT  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

