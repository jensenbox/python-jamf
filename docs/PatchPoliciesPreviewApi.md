# openapi_client.PatchPoliciesPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_patch_policies_get**](PatchPoliciesPreviewApi.md#patch_patch_policies_get) | **GET** /patch/patch-policies | Return a list of patch policies 
[**patch_patch_policies_id_dashboard_delete**](PatchPoliciesPreviewApi.md#patch_patch_policies_id_dashboard_delete) | **DELETE** /patch/patch-policies/{id}/dashboard | Remove a patch policy from the dashboard 
[**patch_patch_policies_id_dashboard_get**](PatchPoliciesPreviewApi.md#patch_patch_policies_id_dashboard_get) | **GET** /patch/patch-policies/{id}/dashboard | Return whether or not the requested patch policy is on the dashboard 
[**patch_patch_policies_id_dashboard_post**](PatchPoliciesPreviewApi.md#patch_patch_policies_id_dashboard_post) | **POST** /patch/patch-policies/{id}/dashboard | Add a patch policy to the dashboard 


# **patch_patch_policies_get**
> list[PatchPolicySummary] patch_patch_policies_get(on_dashboard=on_dashboard, enabled=enabled)

Return a list of patch policies 

Returns a list of patch policies.

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
    api_instance = openapi_client.PatchPoliciesPreviewApi(api_client)
    on_dashboard = False # bool | Filters whether or not the patch policies are on the dashboard. (optional) (default to False)
enabled = False # bool | Filters whether or not the patch policies are enabled. (optional) (default to False)

    try:
        # Return a list of patch policies 
        api_response = api_instance.patch_patch_policies_get(on_dashboard=on_dashboard, enabled=enabled)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchPoliciesPreviewApi->patch_patch_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_dashboard** | **bool**| Filters whether or not the patch policies are on the dashboard. | [optional] [default to False]
 **enabled** | **bool**| Filters whether or not the patch policies are enabled. | [optional] [default to False]

### Return type

[**list[PatchPolicySummary]**](PatchPolicySummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filtered list of patch policy summaries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_patch_policies_id_dashboard_delete**
> patch_patch_policies_id_dashboard_delete(id)

Remove a patch policy from the dashboard 

Removes a patch policy from the dashboard.

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
    api_instance = openapi_client.PatchPoliciesPreviewApi(api_client)
    id = 56 # int | patch id

    try:
        # Remove a patch policy from the dashboard 
        api_instance.patch_patch_policies_id_dashboard_delete(id)
    except ApiException as e:
        print("Exception when calling PatchPoliciesPreviewApi->patch_patch_policies_id_dashboard_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| patch id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_patch_policies_id_dashboard_get**
> PatchPolicyOnDashboard patch_patch_policies_id_dashboard_get(id)

Return whether or not the requested patch policy is on the dashboard 

Returns whether or not the requested patch policy is on the dashboard

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
    api_instance = openapi_client.PatchPoliciesPreviewApi(api_client)
    id = 56 # int | patch policy id

    try:
        # Return whether or not the requested patch policy is on the dashboard 
        api_response = api_instance.patch_patch_policies_id_dashboard_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchPoliciesPreviewApi->patch_patch_policies_id_dashboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| patch policy id | 

### Return type

[**PatchPolicyOnDashboard**](PatchPolicyOnDashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Whether the Patch Policy is on the Dashboard. |  -  |
**404** | The requested Patch Policy does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_patch_policies_id_dashboard_post**
> patch_patch_policies_id_dashboard_post(id)

Add a patch policy to the dashboard 

Adds a patch policy to the dashboard.

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
    api_instance = openapi_client.PatchPoliciesPreviewApi(api_client)
    id = 56 # int | patch policy id

    try:
        # Add a patch policy to the dashboard 
        api_instance.patch_patch_policies_id_dashboard_post(id)
    except ApiException as e:
        print("Exception when calling PatchPoliciesPreviewApi->patch_patch_policies_id_dashboard_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| patch policy id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

