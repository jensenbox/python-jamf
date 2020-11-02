# openapi_client.AdvancedUserContentSearchesApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_advanced_user_content_searches_get**](AdvancedUserContentSearchesApi.md#v1_advanced_user_content_searches_get) | **GET** /v1/advanced-user-content-searches | Get All Advanced User Content Search objects 
[**v1_advanced_user_content_searches_id_delete**](AdvancedUserContentSearchesApi.md#v1_advanced_user_content_searches_id_delete) | **DELETE** /v1/advanced-user-content-searches/{id} | Remove specified Advanced User Content Search object 
[**v1_advanced_user_content_searches_id_get**](AdvancedUserContentSearchesApi.md#v1_advanced_user_content_searches_id_get) | **GET** /v1/advanced-user-content-searches/{id} | Get Specified Advanced User Content Search object 
[**v1_advanced_user_content_searches_id_put**](AdvancedUserContentSearchesApi.md#v1_advanced_user_content_searches_id_put) | **PUT** /v1/advanced-user-content-searches/{id} | Get Specified Advanced User Content Search object 
[**v1_advanced_user_content_searches_post**](AdvancedUserContentSearchesApi.md#v1_advanced_user_content_searches_post) | **POST** /v1/advanced-user-content-searches | Create Advanced User Content Search object 


# **v1_advanced_user_content_searches_get**
> AdvancedUserContentSearchSearchResults v1_advanced_user_content_searches_get()

Get All Advanced User Content Search objects 

Get All Advanced User Content Search Objects 

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
    api_instance = openapi_client.AdvancedUserContentSearchesApi(api_client)
    
    try:
        # Get All Advanced User Content Search objects 
        api_response = api_instance.v1_advanced_user_content_searches_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedUserContentSearchesApi->v1_advanced_user_content_searches_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdvancedUserContentSearchSearchResults**](AdvancedUserContentSearchSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Advanced User Content Searches retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_user_content_searches_id_delete**
> v1_advanced_user_content_searches_id_delete(id)

Remove specified Advanced User Content Search object 

Removes specified Advanced User Content Search Object 

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
    api_instance = openapi_client.AdvancedUserContentSearchesApi(api_client)
    id = 'id_example' # str | instance id of Advanced User Content Search record

    try:
        # Remove specified Advanced User Content Search object 
        api_instance.v1_advanced_user_content_searches_id_delete(id)
    except ApiException as e:
        print("Exception when calling AdvancedUserContentSearchesApi->v1_advanced_user_content_searches_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of Advanced User Content Search record | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response - Advanced User Content Search deleted |  -  |
**404** | Target Advanced User Content Search does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_user_content_searches_id_get**
> AdvancedUserContentSearch v1_advanced_user_content_searches_id_get(id)

Get Specified Advanced User Content Search object 

Gets Specified Advanced User Content Search Object 

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
    api_instance = openapi_client.AdvancedUserContentSearchesApi(api_client)
    id = 'id_example' # str | id of target Advanced User Content Search

    try:
        # Get Specified Advanced User Content Search object 
        api_response = api_instance.v1_advanced_user_content_searches_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedUserContentSearchesApi->v1_advanced_user_content_searches_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of target Advanced User Content Search | 

### Return type

[**AdvancedUserContentSearch**](AdvancedUserContentSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Advanced User Content Search retrieved |  -  |
**404** | Target Advanced User Content Search does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_user_content_searches_id_put**
> AdvancedUserContentSearch v1_advanced_user_content_searches_id_put(id, advanced_user_content_search)

Get Specified Advanced User Content Search object 

Gets Specified Advanced User Content Search Object 

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
    api_instance = openapi_client.AdvancedUserContentSearchesApi(api_client)
    id = 'id_example' # str | id of target Advanced User Content Search
advanced_user_content_search = openapi_client.AdvancedUserContentSearch() # AdvancedUserContentSearch | 

    try:
        # Get Specified Advanced User Content Search object 
        api_response = api_instance.v1_advanced_user_content_searches_id_put(id, advanced_user_content_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedUserContentSearchesApi->v1_advanced_user_content_searches_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of target Advanced User Content Search | 
 **advanced_user_content_search** | [**AdvancedUserContentSearch**](AdvancedUserContentSearch.md)|  | 

### Return type

[**AdvancedUserContentSearch**](AdvancedUserContentSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Advanced User Content Search updated |  -  |
**404** | Target Advanced User Content Search does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_user_content_searches_post**
> HrefResponse v1_advanced_user_content_searches_post(advanced_user_content_search)

Create Advanced User Content Search object 

Creates Advanced User Content Search Object 

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
    api_instance = openapi_client.AdvancedUserContentSearchesApi(api_client)
    advanced_user_content_search = openapi_client.AdvancedUserContentSearch() # AdvancedUserContentSearch | 

    try:
        # Create Advanced User Content Search object 
        api_response = api_instance.v1_advanced_user_content_searches_post(advanced_user_content_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedUserContentSearchesApi->v1_advanced_user_content_searches_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advanced_user_content_search** | [**AdvancedUserContentSearch**](AdvancedUserContentSearch.md)|  | 

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
**201** | Successful response - Advanced User Content Search created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

