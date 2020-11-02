# openapi_client.AdvancedMobileDeviceSearchesApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_advanced_mobile_device_searches_choices_get**](AdvancedMobileDeviceSearchesApi.md#v1_advanced_mobile_device_searches_choices_get) | **GET** /v1/advanced-mobile-device-searches/choices | Get Mobile Device Advanced Search criteria choices 
[**v1_advanced_mobile_device_searches_delete_multiple_post**](AdvancedMobileDeviceSearchesApi.md#v1_advanced_mobile_device_searches_delete_multiple_post) | **POST** /v1/advanced-mobile-device-searches/delete-multiple | Remove specified Advanced Search objects 
[**v1_advanced_mobile_device_searches_get**](AdvancedMobileDeviceSearchesApi.md#v1_advanced_mobile_device_searches_get) | **GET** /v1/advanced-mobile-device-searches | Get Advanced Search objects 
[**v1_advanced_mobile_device_searches_id_delete**](AdvancedMobileDeviceSearchesApi.md#v1_advanced_mobile_device_searches_id_delete) | **DELETE** /v1/advanced-mobile-device-searches/{id} | Remove specified Advanced Search object 
[**v1_advanced_mobile_device_searches_id_get**](AdvancedMobileDeviceSearchesApi.md#v1_advanced_mobile_device_searches_id_get) | **GET** /v1/advanced-mobile-device-searches/{id} | Get specified Advanced Search object 
[**v1_advanced_mobile_device_searches_id_put**](AdvancedMobileDeviceSearchesApi.md#v1_advanced_mobile_device_searches_id_put) | **PUT** /v1/advanced-mobile-device-searches/{id} | Get specified Advanced Search object 
[**v1_advanced_mobile_device_searches_post**](AdvancedMobileDeviceSearchesApi.md#v1_advanced_mobile_device_searches_post) | **POST** /v1/advanced-mobile-device-searches | Create Advanced Search object 


# **v1_advanced_mobile_device_searches_choices_get**
> AdvancedSearchCriteriaChoices v1_advanced_mobile_device_searches_choices_get(criteria, site=site, contains=contains)

Get Mobile Device Advanced Search criteria choices 

Gets Mobile Device Advanced Search criteria choices. A list of potentially valid choices can be found by navigating to the Criteria page of the Advanced Mobile Device Search creation process. A few are \"App Name\", \"Building\", and \"Display Name\". 

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
    api_instance = openapi_client.AdvancedMobileDeviceSearchesApi(api_client)
    criteria = 'criteria_example' # str | 
site = '-1' # str |  (optional) (default to '-1')
contains = 'null' # str |  (optional) (default to 'null')

    try:
        # Get Mobile Device Advanced Search criteria choices 
        api_response = api_instance.v1_advanced_mobile_device_searches_choices_get(criteria, site=site, contains=contains)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedMobileDeviceSearchesApi->v1_advanced_mobile_device_searches_choices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criteria** | **str**|  | 
 **site** | **str**|  | [optional] [default to &#39;-1&#39;]
 **contains** | **str**|  | [optional] [default to &#39;null&#39;]

### Return type

[**AdvancedSearchCriteriaChoices**](AdvancedSearchCriteriaChoices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Criteria choices retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_mobile_device_searches_delete_multiple_post**
> v1_advanced_mobile_device_searches_delete_multiple_post(ids)

Remove specified Advanced Search objects 

Removes specified Advanced Search Objects 

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
    api_instance = openapi_client.AdvancedMobileDeviceSearchesApi(api_client)
    ids = openapi_client.Ids() # Ids | ids of the building to be deleted

    try:
        # Remove specified Advanced Search objects 
        api_instance.v1_advanced_mobile_device_searches_delete_multiple_post(ids)
    except ApiException as e:
        print("Exception when calling AdvancedMobileDeviceSearchesApi->v1_advanced_mobile_device_searches_delete_multiple_post: %s\n" % e)
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
**204** | Successful response - Advanced searches deleted |  -  |
**400** | At least one target Advanced Search does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_mobile_device_searches_get**
> AdvancedSearchSearchResults v1_advanced_mobile_device_searches_get()

Get Advanced Search objects 

Gets Advanced Search Objects 

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
    api_instance = openapi_client.AdvancedMobileDeviceSearchesApi(api_client)
    
    try:
        # Get Advanced Search objects 
        api_response = api_instance.v1_advanced_mobile_device_searches_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedMobileDeviceSearchesApi->v1_advanced_mobile_device_searches_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdvancedSearchSearchResults**](AdvancedSearchSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Advanced searches retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_mobile_device_searches_id_delete**
> v1_advanced_mobile_device_searches_id_delete(id)

Remove specified Advanced Search object 

Removes specified Advanced Search Object 

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
    api_instance = openapi_client.AdvancedMobileDeviceSearchesApi(api_client)
    id = 'id_example' # str | instance id of advanced search record

    try:
        # Remove specified Advanced Search object 
        api_instance.v1_advanced_mobile_device_searches_id_delete(id)
    except ApiException as e:
        print("Exception when calling AdvancedMobileDeviceSearchesApi->v1_advanced_mobile_device_searches_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of advanced search record | 

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
**204** | Successful response - Advanced search deleted |  -  |
**404** | Target Advanced Search does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_mobile_device_searches_id_get**
> AdvancedSearch v1_advanced_mobile_device_searches_id_get(id)

Get specified Advanced Search object 

Gets Specified Advanced Search Object 

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
    api_instance = openapi_client.AdvancedMobileDeviceSearchesApi(api_client)
    id = 'id_example' # str | id of target Advanced Search

    try:
        # Get specified Advanced Search object 
        api_response = api_instance.v1_advanced_mobile_device_searches_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedMobileDeviceSearchesApi->v1_advanced_mobile_device_searches_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of target Advanced Search | 

### Return type

[**AdvancedSearch**](AdvancedSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Advanced Search retrieved |  -  |
**404** | Target Advanced Search does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_mobile_device_searches_id_put**
> AdvancedSearch v1_advanced_mobile_device_searches_id_put(id, advanced_search)

Get specified Advanced Search object 

Gets Specified Advanced Search Object 

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
    api_instance = openapi_client.AdvancedMobileDeviceSearchesApi(api_client)
    id = 'id_example' # str | id of target Advanced Search
advanced_search = openapi_client.AdvancedSearch() # AdvancedSearch | 

    try:
        # Get specified Advanced Search object 
        api_response = api_instance.v1_advanced_mobile_device_searches_id_put(id, advanced_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedMobileDeviceSearchesApi->v1_advanced_mobile_device_searches_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of target Advanced Search | 
 **advanced_search** | [**AdvancedSearch**](AdvancedSearch.md)|  | 

### Return type

[**AdvancedSearch**](AdvancedSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - Advanced Search updated |  -  |
**404** | Target Advanced Search does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_advanced_mobile_device_searches_post**
> HrefResponse v1_advanced_mobile_device_searches_post(advanced_search)

Create Advanced Search object 

Creates Advanced Search Object 

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
    api_instance = openapi_client.AdvancedMobileDeviceSearchesApi(api_client)
    advanced_search = openapi_client.AdvancedSearch() # AdvancedSearch | 

    try:
        # Create Advanced Search object 
        api_response = api_instance.v1_advanced_mobile_device_searches_post(advanced_search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvancedMobileDeviceSearchesApi->v1_advanced_mobile_device_searches_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advanced_search** | [**AdvancedSearch**](AdvancedSearch.md)|  | 

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
**201** | Successful response - Advanced search created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

