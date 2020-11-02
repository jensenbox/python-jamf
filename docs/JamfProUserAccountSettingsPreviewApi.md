# jamf.JamfProUserAccountSettingsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_obj_preference_key_delete**](JamfProUserAccountSettingsPreviewApi.md#user_obj_preference_key_delete) | **DELETE** /user/obj/preference/{key} | Remove specified setting for authenticated user 
[**user_obj_preference_key_get**](JamfProUserAccountSettingsPreviewApi.md#user_obj_preference_key_get) | **GET** /user/obj/preference/{key} | Get the user setting for the authenticated user and key 
[**user_obj_preference_key_put**](JamfProUserAccountSettingsPreviewApi.md#user_obj_preference_key_put) | **PUT** /user/obj/preference/{key} | Persist the user setting 


# **user_obj_preference_key_delete**
> user_obj_preference_key_delete(key)

Remove specified setting for authenticated user 

Remove specified setting for authenticated user 

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
    api_instance = jamf.JamfProUserAccountSettingsPreviewApi(api_client)
    key = 'key_example' # str | key of user setting to be persisted

    try:
        # Remove specified setting for authenticated user 
        api_instance.user_obj_preference_key_delete(key)
    except ApiException as e:
        print("Exception when calling JamfProUserAccountSettingsPreviewApi->user_obj_preference_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key of user setting to be persisted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | setting was deleted |  -  |
**404** | setting not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_obj_preference_key_get**
> str user_obj_preference_key_get(key)

Get the user setting for the authenticated user and key 

Gets the user setting for the authenticated user and key. 

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
    api_instance = jamf.JamfProUserAccountSettingsPreviewApi(api_client)
    key = 'key_example' # str | user setting to be retrieved

    try:
        # Get the user setting for the authenticated user and key 
        api_response = api_instance.user_obj_preference_key_get(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JamfProUserAccountSettingsPreviewApi->user_obj_preference_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| user setting to be retrieved | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | setting not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_obj_preference_key_put**
> str user_obj_preference_key_put(key, body=body)

Persist the user setting 

Persists the user setting 

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
    api_instance = jamf.JamfProUserAccountSettingsPreviewApi(api_client)
    key = 'key_example' # str | key of user setting to be persisted
body = 'body_example' # str | user setting value to be persisted (optional)

    try:
        # Persist the user setting 
        api_response = api_instance.user_obj_preference_key_put(key, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JamfProUserAccountSettingsPreviewApi->user_obj_preference_key_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| key of user setting to be persisted | 
 **body** | **str**| user setting value to be persisted | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | setting sucessfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

