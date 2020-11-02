# openapi_client.BuildingsApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_buildings_delete_multiple_post**](BuildingsApi.md#v1_buildings_delete_multiple_post) | **POST** /v1/buildings/delete-multiple | Delete multiple Buildings by their ids 
[**v1_buildings_get**](BuildingsApi.md#v1_buildings_get) | **GET** /v1/buildings | Search for sorted and paged Buildings 
[**v1_buildings_id_delete**](BuildingsApi.md#v1_buildings_id_delete) | **DELETE** /v1/buildings/{id} | Remove specified Building record 
[**v1_buildings_id_get**](BuildingsApi.md#v1_buildings_id_get) | **GET** /v1/buildings/{id} | Get specified Building object 
[**v1_buildings_id_history_get**](BuildingsApi.md#v1_buildings_id_history_get) | **GET** /v1/buildings/{id}/history | Get specified Building History object 
[**v1_buildings_id_history_post**](BuildingsApi.md#v1_buildings_id_history_post) | **POST** /v1/buildings/{id}/history | Add specified Building history object notes 
[**v1_buildings_id_put**](BuildingsApi.md#v1_buildings_id_put) | **PUT** /v1/buildings/{id} | Update specified Building object 
[**v1_buildings_post**](BuildingsApi.md#v1_buildings_post) | **POST** /v1/buildings | Create Building record 


# **v1_buildings_delete_multiple_post**
> v1_buildings_delete_multiple_post(ids)

Delete multiple Buildings by their ids 

multiple many Buildings by their ids

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
    api_instance = openapi_client.BuildingsApi(api_client)
    ids = openapi_client.Ids() # Ids | ids of the building to be deleted

    try:
        # Delete multiple Buildings by their ids 
        api_instance.v1_buildings_delete_multiple_post(ids)
    except ApiException as e:
        print("Exception when calling BuildingsApi->v1_buildings_delete_multiple_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**Ids**](Ids.md)| ids of the building to be deleted | 

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
**204** | All building ids passed in request sucessfully deleted. |  -  |
**400** | Request processed.  Returns ids and error codes of any buildings unable to be deleted.  Expected error codes: INVALID_ID - id does not exist SYSTEM_EXCEPTION - a system exception occurred trying to delete the building. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_buildings_get**
> BuildingSearchResults v1_buildings_get(page=page, page_size=page_size, sort=sort, filter=filter)

Search for sorted and paged Buildings 

Search for sorted and paged buildings

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
    api_instance = openapi_client.BuildingsApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:asc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["id:asc"])
filter = '' # str | Query in the RSQL format, allowing to filter buildings collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: name, streetAddress1, streetAddress2, city, stateProvince, zipPostalCode, country. This param can be combined with paging and sorting. Example: filter=city==\"Chicago\" and name==\"*build*\" (optional) (default to '')

    try:
        # Search for sorted and paged Buildings 
        api_response = api_instance.v1_buildings_get(page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildingsApi->v1_buildings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;id:asc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter buildings collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: name, streetAddress1, streetAddress2, city, stateProvince, zipPostalCode, country. This param can be combined with paging and sorting. Example: filter&#x3D;city&#x3D;&#x3D;\&quot;Chicago\&quot; and name&#x3D;&#x3D;\&quot;*build*\&quot; | [optional] [default to &#39;&#39;]

### Return type

[**BuildingSearchResults**](BuildingSearchResults.md)

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

# **v1_buildings_id_delete**
> v1_buildings_id_delete(id)

Remove specified Building record 

Removes specified building record 

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
    api_instance = openapi_client.BuildingsApi(api_client)
    id = 'id_example' # str | instance id of building record

    try:
        # Remove specified Building record 
        api_instance.v1_buildings_id_delete(id)
    except ApiException as e:
        print("Exception when calling BuildingsApi->v1_buildings_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of building record | 

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
**204** | Building record was deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_buildings_id_get**
> Building v1_buildings_id_get(id)

Get specified Building object 

Gets specified Building object 

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
    api_instance = openapi_client.BuildingsApi(api_client)
    id = 'id_example' # str | instance id of building record

    try:
        # Get specified Building object 
        api_response = api_instance.v1_buildings_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildingsApi->v1_buildings_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of building record | 

### Return type

[**Building**](Building.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of building were found |  -  |
**404** | Specified building object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_buildings_id_history_get**
> HistorySearchResults v1_buildings_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)

Get specified Building History object 

Gets specified Building history object 

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
    api_instance = openapi_client.BuildingsApi(api_client)
    id = 'id_example' # str | instance id of building history record
page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["date:desc"])
filter = '' # str | Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter=username!=admin and details==*disabled* and date<2019-12-15 (optional) (default to '')

    try:
        # Get specified Building History object 
        api_response = api_instance.v1_buildings_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildingsApi->v1_buildings_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of building history record | 
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
**200** | Details of building history were found |  -  |
**404** | Specified building object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_buildings_id_history_post**
> ObjectHistory v1_buildings_id_history_post(id, object_history_note)

Add specified Building history object notes 

Adds specified Building history object notes 

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
    api_instance = openapi_client.BuildingsApi(api_client)
    id = 'id_example' # str | instance id of building history record
object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add specified Building history object notes 
        api_response = api_instance.v1_buildings_id_history_post(id, object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildingsApi->v1_buildings_id_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of building history record | 
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
**201** | Notes of building history were added |  -  |
**404** | Specified building object does not exist. |  -  |
**503** | Building history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_buildings_id_put**
> Building v1_buildings_id_put(id, building)

Update specified Building object 

Update specified building object 

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
    api_instance = openapi_client.BuildingsApi(api_client)
    id = 'id_example' # str | instance id of building record
building = openapi_client.Building() # Building | building object to update. ids defined in this body will be ignored

    try:
        # Update specified Building object 
        api_response = api_instance.v1_buildings_id_put(id, building)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildingsApi->v1_buildings_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of building record | 
 **building** | [**Building**](Building.md)| building object to update. ids defined in this body will be ignored | 

### Return type

[**Building**](Building.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Building update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_buildings_post**
> HrefResponse v1_buildings_post(building)

Create Building record 

Create building record 

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
    api_instance = openapi_client.BuildingsApi(api_client)
    building = openapi_client.Building() # Building | building object to create. ids defined in this body will be ignored

    try:
        # Create Building record 
        api_response = api_instance.v1_buildings_post(building)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BuildingsApi->v1_buildings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **building** | [**Building**](Building.md)| building object to create. ids defined in this body will be ignored | 

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
**201** | Building record was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

