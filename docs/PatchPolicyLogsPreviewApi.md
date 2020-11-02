# openapi_client.PatchPolicyLogsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_patch_policies_id_logs_get**](PatchPolicyLogsPreviewApi.md#patch_patch_policies_id_logs_get) | **GET** /patch/patch-policies/{id}/logs | Return the Patch Policy Attempt details 


# **patch_patch_policies_id_logs_get**
> list[PatchPolicyAttempt] patch_patch_policies_id_logs_get(id, device_id=device_id)

Return the Patch Policy Attempt details 

Returns the patch policy attempt details

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
    api_instance = openapi_client.PatchPolicyLogsPreviewApi(api_client)
    id = 56 # int | patch policy id
device_id = 56 # int | device id (optional)

    try:
        # Return the Patch Policy Attempt details 
        api_response = api_instance.patch_patch_policies_id_logs_get(id, device_id=device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchPolicyLogsPreviewApi->patch_patch_policies_id_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| patch policy id | 
 **device_id** | **int**| device id | [optional] 

### Return type

[**list[PatchPolicyAttempt]**](PatchPolicyAttempt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Patch Policy Attempt Details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

