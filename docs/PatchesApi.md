# jamf.PatchesApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_id_get**](PatchesApi.md#patch_id_get) | **GET** /patch/{id} | Return Active Patch Summary 
[**patch_id_put**](PatchesApi.md#patch_id_put) | **PUT** /patch/{id} | Update patch report 
[**patch_id_versions_get**](PatchesApi.md#patch_id_versions_get) | **GET** /patch/{id}/versions | Return patch versions 
[**patch_obj_policy_id_get**](PatchesApi.md#patch_obj_policy_id_get) | **GET** /patch/obj/policy/{id} | Return Patch Policy Summary 
[**patch_svc_disclaimer_agree_post**](PatchesApi.md#patch_svc_disclaimer_agree_post) | **POST** /patch/svc/disclaimerAgree | Accept Patch reporting disclaimer 


# **patch_id_get**
> ActivePatchSummary patch_id_get(id)

Return Active Patch Summary 

Returns active patch summary.

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
    api_instance = jamf.PatchesApi(api_client)
    id = 56 # int | patch id

    try:
        # Return Active Patch Summary 
        api_response = api_instance.patch_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesApi->patch_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| patch id | 

### Return type

[**ActivePatchSummary**](ActivePatchSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active Patch Summary |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_id_put**
> ActivePatchSummary patch_id_put(id, active_patch_summary)

Update patch report 

Updates patch report.

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
    api_instance = jamf.PatchesApi(api_client)
    id = 56 # int | patch id
active_patch_summary = jamf.ActivePatchSummary() # ActivePatchSummary | Active patch summary.

    try:
        # Update patch report 
        api_response = api_instance.patch_id_put(id, active_patch_summary)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesApi->patch_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| patch id | 
 **active_patch_summary** | [**ActivePatchSummary**](ActivePatchSummary.md)| Active patch summary. | 

### Return type

[**ActivePatchSummary**](ActivePatchSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active Patch Summary |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_id_versions_get**
> list[PatchVersion] patch_id_versions_get(id)

Return patch versions 

Returns patch versions.

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
    api_instance = jamf.PatchesApi(api_client)
    id = 56 # int | patch id

    try:
        # Return patch versions 
        api_response = api_instance.patch_id_versions_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesApi->patch_id_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| patch id | 

### Return type

[**list[PatchVersion]**](PatchVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Patch versions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_obj_policy_id_get**
> PatchPolicySummary patch_obj_policy_id_get(id)

Return Patch Policy Summary 

Returns patch policy summary.

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
    api_instance = jamf.PatchesApi(api_client)
    id = 56 # int | patch policy id

    try:
        # Return Patch Policy Summary 
        api_response = api_instance.patch_obj_policy_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesApi->patch_obj_policy_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| patch policy id | 

### Return type

[**PatchPolicySummary**](PatchPolicySummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Patch policy summary found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_svc_disclaimer_agree_post**
> patch_svc_disclaimer_agree_post()

Accept Patch reporting disclaimer 

Accept Patch reporting disclaimer

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
    api_instance = jamf.PatchesApi(api_client)
    
    try:
        # Accept Patch reporting disclaimer 
        api_instance.patch_svc_disclaimer_agree_post()
    except ApiException as e:
        print("Exception when calling PatchesApi->patch_svc_disclaimer_agree_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

