# openapi_client.JamfProServerUrlPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_jamf_pro_server_url_get**](JamfProServerUrlPreviewApi.md#v1_jamf_pro_server_url_get) | **GET** /v1/jamf-pro-server-url | Get Jamf Pro Server URL settings 
[**v1_jamf_pro_server_url_history_get**](JamfProServerUrlPreviewApi.md#v1_jamf_pro_server_url_history_get) | **GET** /v1/jamf-pro-server-url/history | Get Jamf Pro Server URL settings history 
[**v1_jamf_pro_server_url_history_post**](JamfProServerUrlPreviewApi.md#v1_jamf_pro_server_url_history_post) | **POST** /v1/jamf-pro-server-url/history | Add Jamf Pro Server URL settings history notes 
[**v1_jamf_pro_server_url_put**](JamfProServerUrlPreviewApi.md#v1_jamf_pro_server_url_put) | **PUT** /v1/jamf-pro-server-url | Update Jamf Pro Server URL settings 


# **v1_jamf_pro_server_url_get**
> JamfProServerUrl v1_jamf_pro_server_url_get()

Get Jamf Pro Server URL settings 

Get Jamf Pro Server URL settings

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
    api_instance = openapi_client.JamfProServerUrlPreviewApi(api_client)
    
    try:
        # Get Jamf Pro Server URL settings 
        api_response = api_instance.v1_jamf_pro_server_url_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JamfProServerUrlPreviewApi->v1_jamf_pro_server_url_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JamfProServerUrl**](JamfProServerUrl.md)

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

# **v1_jamf_pro_server_url_history_get**
> HistorySearchResults v1_jamf_pro_server_url_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get Jamf Pro Server URL settings history 

Gets Jamf Pro Server URL settings history

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
    api_instance = openapi_client.JamfProServerUrlPreviewApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'date:desc' # str | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'date:desc')

    try:
        # Get Jamf Pro Server URL settings history 
        api_response = api_instance.v1_jamf_pro_server_url_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JamfProServerUrlPreviewApi->v1_jamf_pro_server_url_history_get: %s\n" % e)
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
**200** | Details of Jamf Pro Server URL settings history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_jamf_pro_server_url_history_post**
> ObjectHistory v1_jamf_pro_server_url_history_post(object_history_note)

Add Jamf Pro Server URL settings history notes 

Adds Jamf Pro Server URL settings history notes

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
    api_instance = openapi_client.JamfProServerUrlPreviewApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | History notes to create

    try:
        # Add Jamf Pro Server URL settings history notes 
        api_response = api_instance.v1_jamf_pro_server_url_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JamfProServerUrlPreviewApi->v1_jamf_pro_server_url_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_history_note** | [**ObjectHistoryNote**](ObjectHistoryNote.md)| History notes to create | 

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
**201** | Notes to Jamf Pro Server URL settings history were added |  -  |
**403** | Jamf Pro Server URL is managed by Jamf Cloud |  -  |
**503** | Jamf Pro Server URL history does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_jamf_pro_server_url_put**
> JamfProServerUrl v1_jamf_pro_server_url_put(jamf_pro_server_url)

Update Jamf Pro Server URL settings 

Update Jamf Pro Server URL settings

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
    api_instance = openapi_client.JamfProServerUrlPreviewApi(api_client)
    jamf_pro_server_url = openapi_client.JamfProServerUrl() # JamfProServerUrl | Jamf Pro Server URL settings object

    try:
        # Update Jamf Pro Server URL settings 
        api_response = api_instance.v1_jamf_pro_server_url_put(jamf_pro_server_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JamfProServerUrlPreviewApi->v1_jamf_pro_server_url_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jamf_pro_server_url** | [**JamfProServerUrl**](JamfProServerUrl.md)| Jamf Pro Server URL settings object | 

### Return type

[**JamfProServerUrl**](JamfProServerUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jamf Pro Server URL settings updated |  -  |
**403** | Jamf Pro Server URL is managed by Jamf Cloud |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

