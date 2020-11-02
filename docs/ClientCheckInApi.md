# openapi_client.ClientCheckInApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_check_in_get**](ClientCheckInApi.md#v1_check_in_get) | **GET** /v1/check-in | Get Client Check-In settings 
[**v1_check_in_history_get**](ClientCheckInApi.md#v1_check_in_history_get) | **GET** /v1/check-in/history | Get Client Check-In history object 
[**v1_check_in_history_post**](ClientCheckInApi.md#v1_check_in_history_post) | **POST** /v1/check-in/history | Add a Note to Client Check-In History 
[**v1_check_in_put**](ClientCheckInApi.md#v1_check_in_put) | **PUT** /v1/check-in | Update Client Check-In object 
[**v2_check_in_get**](ClientCheckInApi.md#v2_check_in_get) | **GET** /v2/check-in | Get Client Check-In settings 
[**v2_check_in_history_get**](ClientCheckInApi.md#v2_check_in_history_get) | **GET** /v2/check-in/history | Get Client Check-In history object 
[**v2_check_in_history_post**](ClientCheckInApi.md#v2_check_in_history_post) | **POST** /v2/check-in/history | Add a Note to Client Check-In History 
[**v2_check_in_put**](ClientCheckInApi.md#v2_check_in_put) | **PUT** /v2/check-in | Update Client Check-In object 


# **v1_check_in_get**
> ClientCheckIn v1_check_in_get()

Get Client Check-In settings 

Gets `Client Check-In` object. 

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
    api_instance = openapi_client.ClientCheckInApi(api_client)
    
    try:
        # Get Client Check-In settings 
        api_response = api_instance.v1_check_in_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientCheckInApi->v1_check_in_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientCheckIn**](ClientCheckIn.md)

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

# **v1_check_in_history_get**
> HistorySearchResults v1_check_in_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort, search=search)

Get Client Check-In history object 

Gets Client Check-In history object 

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
    api_instance = openapi_client.ClientCheckInApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'date:desc' # str | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc (optional) (default to 'date:desc')
search = '' # str | Query in the RSQL format, allowing to filter history notes collection. Default search is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: search=username!=admin and details==*disabled* and date<2019-12-15 (optional) (default to '')

    try:
        # Get Client Check-In history object 
        api_response = api_instance.v1_check_in_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort, search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientCheckInApi->v1_check_in_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc | [optional] [default to &#39;date:desc&#39;]
 **search** | **str**| Query in the RSQL format, allowing to filter history notes collection. Default search is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: search&#x3D;username!&#x3D;admin and details&#x3D;&#x3D;*disabled* and date&lt;2019-12-15 | [optional] [default to &#39;&#39;]

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
**200** | Details of Client Check-In history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_check_in_history_post**
> ObjectHistory v1_check_in_history_post(object_history_note)

Add a Note to Client Check-In History 

Adds Client Check-In history object notes 

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
    api_instance = openapi_client.ClientCheckInApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add a Note to Client Check-In History 
        api_response = api_instance.v1_check_in_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientCheckInApi->v1_check_in_history_post: %s\n" % e)
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
**201** | Notes of Client Check-In history were added |  -  |
**503** | Client Check-In history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_check_in_put**
> ClientCheckIn v1_check_in_put(client_check_in)

Update Client Check-In object 

Update Client Check-In object 

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
    api_instance = openapi_client.ClientCheckInApi(api_client)
    client_check_in = openapi_client.ClientCheckIn() # ClientCheckIn | Client Check-In object to update

    try:
        # Update Client Check-In object 
        api_response = api_instance.v1_check_in_put(client_check_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientCheckInApi->v1_check_in_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_check_in** | [**ClientCheckIn**](ClientCheckIn.md)| Client Check-In object to update | 

### Return type

[**ClientCheckIn**](ClientCheckIn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Client Check-In was updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_check_in_get**
> ClientCheckInV2 v2_check_in_get()

Get Client Check-In settings 

Gets `Client Check-In` object. 

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
    api_instance = openapi_client.ClientCheckInApi(api_client)
    
    try:
        # Get Client Check-In settings 
        api_response = api_instance.v2_check_in_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientCheckInApi->v2_check_in_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientCheckInV2**](ClientCheckInV2.md)

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

# **v2_check_in_history_get**
> HistorySearchResultsV1 v2_check_in_history_get(page=page, page_size=page_size, sort=sort, filter=filter)

Get Client Check-In history object 

Gets Client Check-In history object 

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
    api_instance = openapi_client.ClientCheckInApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is name:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,username:asc  (optional) (default to ["date:desc"])
filter = '' # str | Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter=username!=admin and details==*disabled* and date<2019-12-15 (optional) (default to '')

    try:
        # Get Client Check-In history object 
        api_response = api_instance.v2_check_in_history_get(page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientCheckInApi->v2_check_in_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is name:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,username:asc  | [optional] [default to [&quot;date:desc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter&#x3D;username!&#x3D;admin and details&#x3D;&#x3D;*disabled* and date&lt;2019-12-15 | [optional] [default to &#39;&#39;]

### Return type

[**HistorySearchResultsV1**](HistorySearchResultsV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Client Check-In history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_check_in_history_post**
> HrefResponse v2_check_in_history_post(object_history_note)

Add a Note to Client Check-In History 

Adds Client Check-In history object notes 

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
    api_instance = openapi_client.ClientCheckInApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add a Note to Client Check-In History 
        api_response = api_instance.v2_check_in_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientCheckInApi->v2_check_in_history_post: %s\n" % e)
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
**201** | Notes of Client Check-In history were added |  -  |
**503** | Client Check-In history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_check_in_put**
> ClientCheckInV2 v2_check_in_put(client_check_in_v2)

Update Client Check-In object 

Update Client Check-In object 

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
    api_instance = openapi_client.ClientCheckInApi(api_client)
    client_check_in_v2 = openapi_client.ClientCheckInV2() # ClientCheckInV2 | Client Check-In object to update

    try:
        # Update Client Check-In object 
        api_response = api_instance.v2_check_in_put(client_check_in_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientCheckInApi->v2_check_in_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_check_in_v2** | [**ClientCheckInV2**](ClientCheckInV2.md)| Client Check-In object to update | 

### Return type

[**ClientCheckInV2**](ClientCheckInV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client Check-In was updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

