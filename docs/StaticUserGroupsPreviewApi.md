# jamf.StaticUserGroupsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_static_user_groups_get**](StaticUserGroupsPreviewApi.md#v1_static_user_groups_get) | **GET** /v1/static-user-groups | Return a list of all Static User Groups 
[**v1_static_user_groups_id_get**](StaticUserGroupsPreviewApi.md#v1_static_user_groups_id_get) | **GET** /v1/static-user-groups/{id} | Return a specific Static User Group by id 


# **v1_static_user_groups_get**
> list[StaticUserGroup] v1_static_user_groups_get()

Return a list of all Static User Groups 

Returns a list of all static user groups. 

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
    api_instance = jamf.StaticUserGroupsPreviewApi(api_client)
    
    try:
        # Return a list of all Static User Groups 
        api_response = api_instance.v1_static_user_groups_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StaticUserGroupsPreviewApi->v1_static_user_groups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StaticUserGroup]**](StaticUserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_static_user_groups_id_get**
> StaticUserGroup v1_static_user_groups_id_get(id)

Return a specific Static User Group by id 

Returns a specific static user group by id. 

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
    api_instance = jamf.StaticUserGroupsPreviewApi(api_client)
    id = 56 # int | Instance id of static user group record

    try:
        # Return a specific Static User Group by id 
        api_response = api_instance.v1_static_user_groups_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StaticUserGroupsPreviewApi->v1_static_user_groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id of static user group record | 

### Return type

[**StaticUserGroup**](StaticUserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Specified static user group object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

