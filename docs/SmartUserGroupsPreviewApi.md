# openapi_client.SmartUserGroupsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_smart_user_groups_id_recalculate_post**](SmartUserGroupsPreviewApi.md#v1_smart_user_groups_id_recalculate_post) | **POST** /v1/smart-user-groups/{id}/recalculate | Recalculate the smart group for the given id and then return the ids for the users in the smart group 
[**v1_users_id_recalculate_smart_groups_post**](SmartUserGroupsPreviewApi.md#v1_users_id_recalculate_smart_groups_post) | **POST** /v1/users/{id}/recalculate-smart-groups | Recalculate a smart group for the given user id and then return the count of smart groups the user falls into 


# **v1_smart_user_groups_id_recalculate_post**
> RecalculationResults v1_smart_user_groups_id_recalculate_post(id)

Recalculate the smart group for the given id and then return the ids for the users in the smart group 

Recalculates the smart group for the given id and then returns the ids for the users in the smart group 

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
    api_instance = openapi_client.SmartUserGroupsPreviewApi(api_client)
    id = 56 # int | instance id of smart group

    try:
        # Recalculate the smart group for the given id and then return the ids for the users in the smart group 
        api_response = api_instance.v1_smart_user_groups_id_recalculate_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartUserGroupsPreviewApi->v1_smart_user_groups_id_recalculate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| instance id of smart group | 

### Return type

[**RecalculationResults**](RecalculationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | smart group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_id_recalculate_smart_groups_post**
> RecalculationResults v1_users_id_recalculate_smart_groups_post(id)

Recalculate a smart group for the given user id and then return the count of smart groups the user falls into 

Recalculates a smart group for the given user id and then returns the count of smart groups the user falls into 

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
    api_instance = openapi_client.SmartUserGroupsPreviewApi(api_client)
    id = 56 # int | id of user

    try:
        # Recalculate a smart group for the given user id and then return the count of smart groups the user falls into 
        api_response = api_instance.v1_users_id_recalculate_smart_groups_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartUserGroupsPreviewApi->v1_users_id_recalculate_smart_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of user | 

### Return type

[**RecalculationResults**](RecalculationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | smart group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

