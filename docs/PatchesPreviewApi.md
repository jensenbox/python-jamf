# openapi_client.PatchesPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_disclaimer_agree_post**](PatchesPreviewApi.md#patch_disclaimer_agree_post) | **POST** /patch/disclaimerAgree | Accept Patch reporting disclaimer 
[**patch_obj_id_get**](PatchesPreviewApi.md#patch_obj_id_get) | **GET** /patch/obj/{id} | Return Active Patch Summary 
[**patch_obj_id_put**](PatchesPreviewApi.md#patch_obj_id_put) | **PUT** /patch/obj/{id} | Update patch report 
[**patch_obj_id_versions_get**](PatchesPreviewApi.md#patch_obj_id_versions_get) | **GET** /patch/obj/{id}/versions | Return patch versions 
[**patch_obj_policy_id_logs_eligible_retry_count_get**](PatchesPreviewApi.md#patch_obj_policy_id_logs_eligible_retry_count_get) | **GET** /patch/obj/policy/{id}/logs/eligibleRetryCount | Return the count of the Patch Policy Logs for the policy is that are eligible for a retry attempt 
[**patch_obj_policy_id_software_title_configuration_id_get**](PatchesPreviewApi.md#patch_obj_policy_id_software_title_configuration_id_get) | **GET** /patch/obj/policy/{id}/softwareTitleConfigurationId | Return the Software Title Configuration Id for the given patch 
[**patch_obj_software_title_configuration_id_get**](PatchesPreviewApi.md#patch_obj_software_title_configuration_id_get) | **GET** /patch/obj/softwareTitleConfiguration/{id} | Return the Software Title Configuration 
[**patch_obj_software_title_id_policies_get**](PatchesPreviewApi.md#patch_obj_software_title_id_policies_get) | **GET** /patch/obj/softwareTitle/{id}/policies | Return the Summaries of the Patch Policies for the software title 
[**patch_objs_policy_id_get**](PatchesPreviewApi.md#patch_objs_policy_id_get) | **GET** /patch/objs/policy/{id} | Return Patch Policy Summary 
[**patch_on_dashboard_get**](PatchesPreviewApi.md#patch_on_dashboard_get) | **GET** /patch/onDashboard | Return list of Patch ids on dashboard 
[**patch_retry_policy_post**](PatchesPreviewApi.md#patch_retry_policy_post) | **POST** /patch/retryPolicy | Retry policy 
[**patch_search_active_patch_history_post**](PatchesPreviewApi.md#patch_search_active_patch_history_post) | **POST** /patch/searchActivePatchHistory | Search the history for a Specific Active Patch 
[**patch_search_patch_policy_logs_post**](PatchesPreviewApi.md#patch_search_patch_policy_logs_post) | **POST** /patch/searchPatchPolicyLogs | Return Patch Policy Logs 
[**patch_svc_retry_policy_post**](PatchesPreviewApi.md#patch_svc_retry_policy_post) | **POST** /patch/svc/retryPolicy | Retry policy 


# **patch_disclaimer_agree_post**
> patch_disclaimer_agree_post()

Accept Patch reporting disclaimer 

Accept Patch reporting disclaimer

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    
    try:
        # Accept Patch reporting disclaimer 
        api_instance.patch_disclaimer_agree_post()
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_disclaimer_agree_post: %s\n" % e)
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

# **patch_obj_id_get**
> ActivePatchSummary patch_obj_id_get(id)

Return Active Patch Summary 

Returns active patch summary.

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    id = 56 # int | patch id

    try:
        # Return Active Patch Summary 
        api_response = api_instance.patch_obj_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_obj_id_get: %s\n" % e)
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

# **patch_obj_id_put**
> ActivePatchSummary patch_obj_id_put(id, active_patch_summary)

Update patch report 

Updates patch report.

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    id = 56 # int | patch id
active_patch_summary = openapi_client.ActivePatchSummary() # ActivePatchSummary | Active patch summary.

    try:
        # Update patch report 
        api_response = api_instance.patch_obj_id_put(id, active_patch_summary)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_obj_id_put: %s\n" % e)
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

# **patch_obj_id_versions_get**
> list[PatchVersion] patch_obj_id_versions_get(id)

Return patch versions 

Returns patch versions.

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    id = 56 # int | patch id

    try:
        # Return patch versions 
        api_response = api_instance.patch_obj_id_versions_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_obj_id_versions_get: %s\n" % e)
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

# **patch_obj_policy_id_logs_eligible_retry_count_get**
> int patch_obj_policy_id_logs_eligible_retry_count_get(id)

Return the count of the Patch Policy Logs for the policy is that are eligible for a retry attempt 

return the count of the patch policy logs for the policy ID that are eligible for a retry attempt

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    id = 56 # int | policy id

    try:
        # Return the count of the Patch Policy Logs for the policy is that are eligible for a retry attempt 
        api_response = api_instance.patch_obj_policy_id_logs_eligible_retry_count_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_obj_policy_id_logs_eligible_retry_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| policy id | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Number of patch policy logs found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_obj_policy_id_software_title_configuration_id_get**
> int patch_obj_policy_id_software_title_configuration_id_get(id)

Return the Software Title Configuration Id for the given patch 

Return the Software Title Configuration Id for the given patch policy.

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    id = 56 # int | policy id

    try:
        # Return the Software Title Configuration Id for the given patch 
        api_response = api_instance.patch_obj_policy_id_software_title_configuration_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_obj_policy_id_software_title_configuration_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| policy id | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found software title configuration id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_obj_software_title_configuration_id_get**
> SoftwareTitleConfiguration patch_obj_software_title_configuration_id_get(id)

Return the Software Title Configuration 

Returns the software title configuration.

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    id = 56 # int | software title configuration id

    try:
        # Return the Software Title Configuration 
        api_response = api_instance.patch_obj_software_title_configuration_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_obj_software_title_configuration_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| software title configuration id | 

### Return type

[**SoftwareTitleConfiguration**](SoftwareTitleConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Software Title Configuration found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_obj_software_title_id_policies_get**
> SoftwareTitlePatchPolicySummaries patch_obj_software_title_id_policies_get(id)

Return the Summaries of the Patch Policies for the software title 

Returns the summaries of the patch policies for the software title.

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    id = 56 # int | software title id

    try:
        # Return the Summaries of the Patch Policies for the software title 
        api_response = api_instance.patch_obj_software_title_id_policies_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_obj_software_title_id_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| software title id | 

### Return type

[**SoftwareTitlePatchPolicySummaries**](SoftwareTitlePatchPolicySummaries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Software Title patch policy summaries found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_objs_policy_id_get**
> PatchPolicySummary patch_objs_policy_id_get(id)

Return Patch Policy Summary 

Returns patch policy summary.

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    id = 56 # int | patch policy id

    try:
        # Return Patch Policy Summary 
        api_response = api_instance.patch_objs_policy_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_objs_policy_id_get: %s\n" % e)
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

# **patch_on_dashboard_get**
> list[int] patch_on_dashboard_get()

Return list of Patch ids on dashboard 

Returns list of patch ids on dashboard.

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    
    try:
        # Return list of Patch ids on dashboard 
        api_response = api_instance.patch_on_dashboard_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_on_dashboard_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instance IDs returned in associated array, or if no instances present, an empty array shall be returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_retry_policy_post**
> patch_retry_policy_post(retry_patch_policy_params=retry_patch_policy_params)

Retry policy 

Retry policy

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    retry_patch_policy_params = openapi_client.RetryPatchPolicyParams() # RetryPatchPolicyParams |  (optional)

    try:
        # Retry policy 
        api_instance.patch_retry_policy_post(retry_patch_policy_params=retry_patch_policy_params)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_retry_policy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retry_patch_policy_params** | [**RetryPatchPolicyParams**](RetryPatchPolicyParams.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_search_active_patch_history_post**
> ActivePatchHistorySearchResults patch_search_active_patch_history_post(search_active_patch_history_params=search_active_patch_history_params)

Search the history for a Specific Active Patch 

Searches the history for a specific active patch.  This is used to get detailed information about the computers/devices that a specific patch has been applied to.

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    search_active_patch_history_params = openapi_client.SearchActivePatchHistoryParams() # SearchActivePatchHistoryParams | Parameters for search (optional)

    try:
        # Search the history for a Specific Active Patch 
        api_response = api_instance.patch_search_active_patch_history_post(search_active_patch_history_params=search_active_patch_history_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_search_active_patch_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_active_patch_history_params** | [**SearchActivePatchHistoryParams**](SearchActivePatchHistoryParams.md)| Parameters for search | [optional] 

### Return type

[**ActivePatchHistorySearchResults**](ActivePatchHistorySearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search results.  No matches will be indicated by the return of an empty list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_search_patch_policy_logs_post**
> PatchPolicyLogSearchResults patch_search_patch_policy_logs_post(search_patch_policy_log_params=search_patch_policy_log_params)

Return Patch Policy Logs 

Return patch policy logs

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    search_patch_policy_log_params = openapi_client.SearchPatchPolicyLogParams() # SearchPatchPolicyLogParams |  (optional)

    try:
        # Return Patch Policy Logs 
        api_response = api_instance.patch_search_patch_policy_logs_post(search_patch_policy_log_params=search_patch_policy_log_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_search_patch_policy_logs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_patch_policy_log_params** | [**SearchPatchPolicyLogParams**](SearchPatchPolicyLogParams.md)|  | [optional] 

### Return type

[**PatchPolicyLogSearchResults**](PatchPolicyLogSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Patch policy logs found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_svc_retry_policy_post**
> patch_svc_retry_policy_post(retry_patch_policy_params=retry_patch_policy_params)

Retry policy 

Retry policy

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
    api_instance = openapi_client.PatchesPreviewApi(api_client)
    retry_patch_policy_params = openapi_client.RetryPatchPolicyParams() # RetryPatchPolicyParams |  (optional)

    try:
        # Retry policy 
        api_instance.patch_svc_retry_policy_post(retry_patch_policy_params=retry_patch_policy_params)
    except ApiException as e:
        print("Exception when calling PatchesPreviewApi->patch_svc_retry_policy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retry_patch_policy_params** | [**RetryPatchPolicyParams**](RetryPatchPolicyParams.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

