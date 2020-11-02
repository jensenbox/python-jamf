# openapi_client.UserSessionPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_get**](UserSessionPreviewApi.md#user_get) | **GET** /user | Return all Jamf Pro user acounts 
[**user_update_session_post**](UserSessionPreviewApi.md#user_update_session_post) | **POST** /user/updateSession | Update values in the User&#39;s current session 


# **user_get**
> list[Account] user_get()

Return all Jamf Pro user acounts 

Return all Jamf Pro user acounts. 

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
    api_instance = openapi_client.UserSessionPreviewApi(api_client)
    
    try:
        # Return all Jamf Pro user acounts 
        api_response = api_instance.user_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserSessionPreviewApi->user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all Jamf Pro user acounts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update_session_post**
> Session user_update_session_post(session=session)

Update values in the User's current session 

Updates values in the user's current session. 

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
    api_instance = openapi_client.UserSessionPreviewApi(api_client)
    session = openapi_client.Session() # Session | Values to update in user's current session. (optional)

    try:
        # Update values in the User's current session 
        api_response = api_instance.user_update_session_post(session=session)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserSessionPreviewApi->user_update_session_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | [**Session**](Session.md)| Values to update in user&#39;s current session. | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user&#39;s current session has been sucessfully updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

