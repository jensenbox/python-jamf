# openapi_client.CategoriesApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_categories_delete_multiple_post**](CategoriesApi.md#v1_categories_delete_multiple_post) | **POST** /v1/categories/delete-multiple | Delete multiple Categories by their IDs 
[**v1_categories_get**](CategoriesApi.md#v1_categories_get) | **GET** /v1/categories | Get Category objects 
[**v1_categories_id_delete**](CategoriesApi.md#v1_categories_id_delete) | **DELETE** /v1/categories/{id} | Remove specified Category record 
[**v1_categories_id_get**](CategoriesApi.md#v1_categories_id_get) | **GET** /v1/categories/{id} | Get specified Category object 
[**v1_categories_id_history_get**](CategoriesApi.md#v1_categories_id_history_get) | **GET** /v1/categories/{id}/history | Get specified Category history object 
[**v1_categories_id_history_post**](CategoriesApi.md#v1_categories_id_history_post) | **POST** /v1/categories/{id}/history | Add specified Category history object notes 
[**v1_categories_id_put**](CategoriesApi.md#v1_categories_id_put) | **PUT** /v1/categories/{id} | Update specified Category object 
[**v1_categories_post**](CategoriesApi.md#v1_categories_post) | **POST** /v1/categories | Create Category record 


# **v1_categories_delete_multiple_post**
> v1_categories_delete_multiple_post(ids)

Delete multiple Categories by their IDs 

Delete multiple Categories by their IDs

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
    api_instance = openapi_client.CategoriesApi(api_client)
    ids = openapi_client.Ids() # Ids | IDs of the categories to be deleted

    try:
        # Delete multiple Categories by their IDs 
        api_instance.v1_categories_delete_multiple_post(ids)
    except ApiException as e:
        print("Exception when calling CategoriesApi->v1_categories_delete_multiple_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**Ids**](Ids.md)| IDs of the categories to be deleted | 

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
**204** | All Category IDs passed in request sucessfully deleted. |  -  |
**400** | Request processed.  Returns IDs and error codes of any categories unable to be deleted.  Expected error codes: INVALID_ID - id does not exist SYSTEM_EXCEPTION - a system exception occurred trying to delete the category. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_categories_get**
> CategoriesSearchResults v1_categories_get(page=page, page_size=page_size, sort=sort, filter=filter)

Get Category objects 

Gets `Category` objects. 

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
    api_instance = openapi_client.CategoriesApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:asc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["id:asc"])
filter = '' # str | Query in the RSQL format, allowing to filter categories collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: name, priority. This param can be combined with paging and sorting. Example: filter=name==\"Apps*\" and priority>=5 (optional) (default to '')

    try:
        # Get Category objects 
        api_response = api_instance.v1_categories_get(page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->v1_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;id:asc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter categories collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: name, priority. This param can be combined with paging and sorting. Example: filter&#x3D;name&#x3D;&#x3D;\&quot;Apps*\&quot; and priority&gt;&#x3D;5 | [optional] [default to &#39;&#39;]

### Return type

[**CategoriesSearchResults**](CategoriesSearchResults.md)

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

# **v1_categories_id_delete**
> v1_categories_id_delete(id)

Remove specified Category record 

Removes specified category record 

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
    api_instance = openapi_client.CategoriesApi(api_client)
    id = 'id_example' # str | instance id of category record

    try:
        # Remove specified Category record 
        api_instance.v1_categories_id_delete(id)
    except ApiException as e:
        print("Exception when calling CategoriesApi->v1_categories_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of category record | 

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
**204** | Category record was deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_categories_id_get**
> Category v1_categories_id_get(id)

Get specified Category object 

Gets specified Category object 

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
    api_instance = openapi_client.CategoriesApi(api_client)
    id = 'id_example' # str | instance id of category record

    try:
        # Get specified Category object 
        api_response = api_instance.v1_categories_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->v1_categories_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of category record | 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of category were found |  -  |
**404** | Specified category object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_categories_id_history_get**
> HistorySearchResults v1_categories_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)

Get specified Category history object 

Gets specified Category history object 

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
    api_instance = openapi_client.CategoriesApi(api_client)
    id = 'id_example' # str | instance id of category history record
page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["date:desc"])
filter = '' # str | Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter=username!=admin and details==*disabled* and date<2019-12-15 (optional) (default to '')

    try:
        # Get specified Category history object 
        api_response = api_instance.v1_categories_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->v1_categories_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of category history record | 
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;date:desc&quot;]]
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
**200** | Details of category history were found |  -  |
**404** | Specified category object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_categories_id_history_post**
> ObjectHistory v1_categories_id_history_post(id, object_history_note)

Add specified Category history object notes 

Adds specified Category history object notes 

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
    api_instance = openapi_client.CategoriesApi(api_client)
    id = 'id_example' # str | instance id of category history record
object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add specified Category history object notes 
        api_response = api_instance.v1_categories_id_history_post(id, object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->v1_categories_id_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of category history record | 
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
**201** | Notes of category history were added |  -  |
**404** | Specified category object does not exist. |  -  |
**503** | Category history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_categories_id_put**
> Category v1_categories_id_put(id, category)

Update specified Category object 

Update specified category object 

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
    api_instance = openapi_client.CategoriesApi(api_client)
    id = 'id_example' # str | instance id of category record
category = openapi_client.Category() # Category | category object to create. id defined in this body will be ignored

    try:
        # Update specified Category object 
        api_response = api_instance.v1_categories_id_put(id, category)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->v1_categories_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of category record | 
 **category** | [**Category**](Category.md)| category object to create. id defined in this body will be ignored | 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category record was updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_categories_post**
> HrefResponse v1_categories_post(category)

Create Category record 

Create category record 

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
    api_instance = openapi_client.CategoriesApi(api_client)
    category = openapi_client.Category() # Category | category object to create. IDs defined in this body will be ignored

    try:
        # Create Category record 
        api_response = api_instance.v1_categories_post(category)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->v1_categories_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | [**Category**](Category.md)| category object to create. IDs defined in this body will be ignored | 

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
**201** | Category record was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

