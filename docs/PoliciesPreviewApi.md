# jamf.PoliciesPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_obj_policy_properties_get**](PoliciesPreviewApi.md#settings_obj_policy_properties_get) | **GET** /settings/obj/policyProperties | Get Policy Properties object 
[**settings_obj_policy_properties_put**](PoliciesPreviewApi.md#settings_obj_policy_properties_put) | **PUT** /settings/obj/policyProperties | Update Policy Properties object 


# **settings_obj_policy_properties_get**
> PolicyProperties settings_obj_policy_properties_get()

Get Policy Properties object 

Gets `Policy Properties` object. 

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
    api_instance = jamf.PoliciesPreviewApi(api_client)
    
    try:
        # Get Policy Properties object 
        api_response = api_instance.settings_obj_policy_properties_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesPreviewApi->settings_obj_policy_properties_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PolicyProperties**](PolicyProperties.md)

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

# **settings_obj_policy_properties_put**
> PolicyProperties settings_obj_policy_properties_put(policy_properties)

Update Policy Properties object 

Update Policy Properties object (NOTE: isPoliciesRequireNetworkStateChange is a calculated value and will be ignored.) 

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
    api_instance = jamf.PoliciesPreviewApi(api_client)
    policy_properties = jamf.PolicyProperties() # PolicyProperties | Policy Properties object to update

    try:
        # Update Policy Properties object 
        api_response = api_instance.settings_obj_policy_properties_put(policy_properties)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoliciesPreviewApi->settings_obj_policy_properties_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_properties** | [**PolicyProperties**](PolicyProperties.md)| Policy Properties object to update | 

### Return type

[**PolicyProperties**](PolicyProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Policy Properties was updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

