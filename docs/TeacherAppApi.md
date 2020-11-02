# openapi_client.TeacherAppApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_teacher_app_get**](TeacherAppApi.md#v1_teacher_app_get) | **GET** /v1/teacher-app | Get the Jamf Teacher settings that you have access to see 
[**v1_teacher_app_history_get**](TeacherAppApi.md#v1_teacher_app_history_get) | **GET** /v1/teacher-app/history | Get Jamf Teacher app settings history 
[**v1_teacher_app_history_post**](TeacherAppApi.md#v1_teacher_app_history_post) | **POST** /v1/teacher-app/history | Add Jamf Teacher app settings history notes 
[**v1_teacher_app_put**](TeacherAppApi.md#v1_teacher_app_put) | **PUT** /v1/teacher-app | Update a Jamf Teacher settings object 


# **v1_teacher_app_get**
> TeacherSettingsResponse v1_teacher_app_get()

Get the Jamf Teacher settings that you have access to see 

Get the Jamf Teacher settings that you have access to see.

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
    api_instance = openapi_client.TeacherAppApi(api_client)
    
    try:
        # Get the Jamf Teacher settings that you have access to see 
        api_response = api_instance.v1_teacher_app_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeacherAppApi->v1_teacher_app_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TeacherSettingsResponse**](TeacherSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Jamf Teacher settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_teacher_app_history_get**
> HistorySearchResults v1_teacher_app_history_get(page=page, page_size=page_size, sort=sort, filter=filter)

Get Jamf Teacher app settings history 

Gets Jamf Teacher app settings history 

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
    api_instance = openapi_client.TeacherAppApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc","username:asc"] # list[str] | Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the 'sort' query param is not duplicated for each sort criterion, e.g., ...&sort=name%2Casc,date%2Cdesc (optional) (default to ["date:desc","username:asc"])
filter = '' # str | Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter=username!=admin and details==*disabled* and date<2019-12-15 (optional) (default to '')

    try:
        # Get Jamf Teacher app settings history 
        api_response = api_instance.v1_teacher_app_history_get(page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeacherAppApi->v1_teacher_app_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the &#39;sort&#39; query param is not duplicated for each sort criterion, e.g., ...&amp;sort&#x3D;name%2Casc,date%2Cdesc | [optional] [default to [&quot;date:desc&quot;,&quot;username:asc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter&#x3D;username!&#x3D;admin and details&#x3D;&#x3D;*disabled* and date&lt;2019-12-15 | [optional] [default to &#39;&#39;]

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
**200** | Details of Jamf Teacher app settings history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_teacher_app_history_post**
> HrefResponse v1_teacher_app_history_post(object_history_note)

Add Jamf Teacher app settings history notes 

Adds Jamf Teacher app settings history notes 

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
    api_instance = openapi_client.TeacherAppApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add Jamf Teacher app settings history notes 
        api_response = api_instance.v1_teacher_app_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeacherAppApi->v1_teacher_app_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_history_note** | [**ObjectHistoryNote**](ObjectHistoryNote.md)| history notes to create | 

### Return type

[**HrefResponse**](HrefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Notes to Jamf Teacher app settings history were added |  -  |
**503** | Jamf Teacher app history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_teacher_app_put**
> TeacherSettingsResponse v1_teacher_app_put(teacher_settings_request)

Update a Jamf Teacher settings object 

Update a Jamf Teacher settings object.

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
    api_instance = openapi_client.TeacherAppApi(api_client)
    teacher_settings_request = openapi_client.TeacherSettingsRequest() # TeacherSettingsRequest | Teacher settings to create.

    try:
        # Update a Jamf Teacher settings object 
        api_response = api_instance.v1_teacher_app_put(teacher_settings_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeacherAppApi->v1_teacher_app_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teacher_settings_request** | [**TeacherSettingsRequest**](TeacherSettingsRequest.md)| Teacher settings to create. | 

### Return type

[**TeacherSettingsResponse**](TeacherSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Jamf Teacher settings. |  -  |
**500** | Update Failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

