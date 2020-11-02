# jamf.DepartmentsApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_departments_delete_multiple_post**](DepartmentsApi.md#v1_departments_delete_multiple_post) | **POST** /v1/departments/delete-multiple | Deletes all departments by ids passed in body 
[**v1_departments_get**](DepartmentsApi.md#v1_departments_get) | **GET** /v1/departments | Search for Departments 
[**v1_departments_id_delete**](DepartmentsApi.md#v1_departments_id_delete) | **DELETE** /v1/departments/{id} | Remove specified department record 
[**v1_departments_id_get**](DepartmentsApi.md#v1_departments_id_get) | **GET** /v1/departments/{id} | Get specified Department object 
[**v1_departments_id_history_get**](DepartmentsApi.md#v1_departments_id_history_get) | **GET** /v1/departments/{id}/history | Get specified Department history object 
[**v1_departments_id_history_post**](DepartmentsApi.md#v1_departments_id_history_post) | **POST** /v1/departments/{id}/history | Add specified Department history object notes 
[**v1_departments_id_put**](DepartmentsApi.md#v1_departments_id_put) | **PUT** /v1/departments/{id} | Update specified department object 
[**v1_departments_post**](DepartmentsApi.md#v1_departments_post) | **POST** /v1/departments | Create department record 


# **v1_departments_delete_multiple_post**
> v1_departments_delete_multiple_post(ids)

Deletes all departments by ids passed in body 

Deletes all departments by ids passed in body 

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
    api_instance = jamf.DepartmentsApi(api_client)
    ids = jamf.Ids() # Ids | ids of departments to be deleted. pass in an array of ids

    try:
        # Deletes all departments by ids passed in body 
        api_instance.v1_departments_delete_multiple_post(ids)
    except ApiException as e:
        print("Exception when calling DepartmentsApi->v1_departments_delete_multiple_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**Ids**](Ids.md)| ids of departments to be deleted. pass in an array of ids | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | All department ids passed in request sucessfully deleted. |  -  |
**400** | Request processed.  Returns ids and error codes of any departments unable to be deleted.  Expected error codes: INVALID_ID - id does not exist SYSTEM_EXCEPTION - a system exception occured trying to delete the department. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_departments_get**
> DepartmentsSearchResults v1_departments_get(page=page, page_size=page_size, sort=sort, filter=filter)

Search for Departments 

Search for Departments 

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
    api_instance = jamf.DepartmentsApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:asc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["id:asc"])
filter = '' # str | Query in the RSQL format, allowing to filter department collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: id, name. Example: name==\"*department*\" (optional) (default to '')

    try:
        # Search for Departments 
        api_response = api_instance.v1_departments_get(page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DepartmentsApi->v1_departments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;id:asc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter department collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: id, name. Example: name&#x3D;&#x3D;\&quot;*department*\&quot; | [optional] [default to &#39;&#39;]

### Return type

[**DepartmentsSearchResults**](DepartmentsSearchResults.md)

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

# **v1_departments_id_delete**
> v1_departments_id_delete(id)

Remove specified department record 

Removes specified department record 

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
    api_instance = jamf.DepartmentsApi(api_client)
    id = 'id_example' # str | instance id of department record

    try:
        # Remove specified department record 
        api_instance.v1_departments_id_delete(id)
    except ApiException as e:
        print("Exception when calling DepartmentsApi->v1_departments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of department record | 

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
**204** | Department record was deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_departments_id_get**
> Department v1_departments_id_get(id)

Get specified Department object 

Gets specified Department object 

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
    api_instance = jamf.DepartmentsApi(api_client)
    id = 'id_example' # str | instance id of department record

    try:
        # Get specified Department object 
        api_response = api_instance.v1_departments_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DepartmentsApi->v1_departments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of department record | 

### Return type

[**Department**](Department.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of department were found |  -  |
**404** | Specified department object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_departments_id_history_get**
> HistorySearchResults v1_departments_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)

Get specified Department history object 

Gets specified Department history object 

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
    api_instance = jamf.DepartmentsApi(api_client)
    id = 'id_example' # str | instance id of department history record
page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["date:desc"])
filter = '' # str | Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter=username!=admin and details==*disabled* and date<2019-12-15 (optional) (default to '')

    try:
        # Get specified Department history object 
        api_response = api_instance.v1_departments_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DepartmentsApi->v1_departments_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of department history record | 
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;date:desc&quot;]]
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
**200** | Details of department history were found |  -  |
**404** | Specified department object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_departments_id_history_post**
> HrefResponse v1_departments_id_history_post(id, object_history_note)

Add specified Department history object notes 

Adds specified Department history object notes 

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
    api_instance = jamf.DepartmentsApi(api_client)
    id = 'id_example' # str | instance id of department history record
object_history_note = jamf.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add specified Department history object notes 
        api_response = api_instance.v1_departments_id_history_post(id, object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DepartmentsApi->v1_departments_id_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of department history record | 
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
**201** | Notes of department history were added |  -  |
**404** | Specified department object does not exist. |  -  |
**503** | Department history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_departments_id_put**
> Department v1_departments_id_put(id, department)

Update specified department object 

Update specified department object 

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
    api_instance = jamf.DepartmentsApi(api_client)
    id = 'id_example' # str | instance id of department record
department = jamf.Department() # Department | department object to create. ids defined in this body will be ignored

    try:
        # Update specified department object 
        api_response = api_instance.v1_departments_id_put(id, department)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DepartmentsApi->v1_departments_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of department record | 
 **department** | [**Department**](Department.md)| department object to create. ids defined in this body will be ignored | 

### Return type

[**Department**](Department.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Department update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_departments_post**
> HrefResponse v1_departments_post(department)

Create department record 

Create department record 

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
    api_instance = jamf.DepartmentsApi(api_client)
    department = jamf.Department() # Department | department object to create. ids defined in this body will be ignored

    try:
        # Create department record 
        api_response = api_instance.v1_departments_post(department)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DepartmentsApi->v1_departments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department** | [**Department**](Department.md)| department object to create. ids defined in this body will be ignored | 

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
**201** | Department record was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

