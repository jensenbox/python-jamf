# jamf.CacheSettingsApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_cache_settings_get**](CacheSettingsApi.md#v1_cache_settings_get) | **GET** /v1/cache-settings | Get Cache Settings 
[**v1_cache_settings_put**](CacheSettingsApi.md#v1_cache_settings_put) | **PUT** /v1/cache-settings | Update Cache Settings 


# **v1_cache_settings_get**
> CacheSettings v1_cache_settings_get()

Get Cache Settings 

gets cache settings

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
    api_instance = jamf.CacheSettingsApi(api_client)
    
    try:
        # Get Cache Settings 
        api_response = api_instance.v1_cache_settings_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CacheSettingsApi->v1_cache_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CacheSettings**](CacheSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | cache settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cache_settings_put**
> CacheSettings v1_cache_settings_put(cache_settings)

Update Cache Settings 

updates cache settings 

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
    api_instance = jamf.CacheSettingsApi(api_client)
    cache_settings = jamf.CacheSettings() # CacheSettings | 

    try:
        # Update Cache Settings 
        api_response = api_instance.v1_cache_settings_put(cache_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CacheSettingsApi->v1_cache_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_settings** | [**CacheSettings**](CacheSettings.md)|  | 

### Return type

[**CacheSettings**](CacheSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | cache has been updated |  -  |
**403** | The following code is returned by this call: HOSTED_ENVIRONMENT - PUT command is not available in hosted environments.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

