# jamf.ParentAppPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_parent_app_get**](ParentAppPreviewApi.md#v1_parent_app_get) | **GET** /v1/parent-app | Get the current Jamf Parent app settings 
[**v1_parent_app_history_get**](ParentAppPreviewApi.md#v1_parent_app_history_get) | **GET** /v1/parent-app/history | Get Jamf Parent app settings history 
[**v1_parent_app_history_post**](ParentAppPreviewApi.md#v1_parent_app_history_post) | **POST** /v1/parent-app/history | Add Jamf Parent app settings history notes 
[**v1_parent_app_put**](ParentAppPreviewApi.md#v1_parent_app_put) | **PUT** /v1/parent-app | Update Jamf Parent app settings 


# **v1_parent_app_get**
> ParentApp v1_parent_app_get()

Get the current Jamf Parent app settings 

Get the current Jamf Parent app settings 

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
    api_instance = jamf.ParentAppPreviewApi(api_client)
    
    try:
        # Get the current Jamf Parent app settings 
        api_response = api_instance.v1_parent_app_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParentAppPreviewApi->v1_parent_app_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ParentApp**](ParentApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the current Jamf Parent app settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_parent_app_history_get**
> HistorySearchResults v1_parent_app_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get Jamf Parent app settings history 

Gets Jamf Parent app settings history 

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
    api_instance = jamf.ParentAppPreviewApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'date:desc' # str | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'date:desc')

    try:
        # Get Jamf Parent app settings history 
        api_response = api_instance.v1_parent_app_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParentAppPreviewApi->v1_parent_app_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to &#39;date:desc&#39;]

### Return type

[**HistorySearchResults**](HistorySearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Jamf Parent app settings history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_parent_app_history_post**
> ObjectHistory v1_parent_app_history_post(object_history_note)

Add Jamf Parent app settings history notes 

Adds Jamf Parent app settings history notes 

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
    api_instance = jamf.ParentAppPreviewApi(api_client)
    object_history_note = jamf.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add Jamf Parent app settings history notes 
        api_response = api_instance.v1_parent_app_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParentAppPreviewApi->v1_parent_app_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_history_note** | [**ObjectHistoryNote**](ObjectHistoryNote.md)| history notes to create | 

### Return type

[**ObjectHistory**](ObjectHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Notes to Jamf Parent app settings history were added |  -  |
**503** | Jamf Parent app history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_parent_app_put**
> ParentApp v1_parent_app_put(parent_app)

Update Jamf Parent app settings 

Update Jamf Parent app settings 

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
    api_instance = jamf.ParentAppPreviewApi(api_client)
    parent_app = jamf.ParentApp() # ParentApp | Jamf Parent app settings to save.

    try:
        # Update Jamf Parent app settings 
        api_response = api_instance.v1_parent_app_put(parent_app)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParentAppPreviewApi->v1_parent_app_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_app** | [**ParentApp**](ParentApp.md)| Jamf Parent app settings to save. | 

### Return type

[**ParentApp**](ParentApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jamf Parent app settings updated |  -  |
**400** | Bad Request, could not parse input. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

