# openapi_client.EbooksApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_ebooks_get**](EbooksApi.md#v1_ebooks_get) | **GET** /v1/ebooks | Get Ebook object 
[**v1_ebooks_id_get**](EbooksApi.md#v1_ebooks_id_get) | **GET** /v1/ebooks/{id} | Get specified Ebook object 
[**v1_ebooks_id_scope_get**](EbooksApi.md#v1_ebooks_id_scope_get) | **GET** /v1/ebooks/{id}/scope | Get specified scope of Ebook object 


# **v1_ebooks_get**
> EbookSearchResults v1_ebooks_get(page=page, page_size=page_size, sort=sort)

Get Ebook object 

Gets ebook object

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
    api_instance = openapi_client.EbooksApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["name:asc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is name:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["name:asc"])

    try:
        # Get Ebook object 
        api_response = api_instance.v1_ebooks_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EbooksApi->v1_ebooks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is name:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;name:asc&quot;]]

### Return type

[**EbookSearchResults**](EbookSearchResults.md)

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

# **v1_ebooks_id_get**
> Ebook v1_ebooks_id_get(id)

Get specified Ebook object 

Gets specified Ebook object 

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
    api_instance = openapi_client.EbooksApi(api_client)
    id = 'id_example' # str | instance id of ebook record

    try:
        # Get specified Ebook object 
        api_response = api_instance.v1_ebooks_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EbooksApi->v1_ebooks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of ebook record | 

### Return type

[**Ebook**](Ebook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details about ebook were found for given id |  -  |
**404** | Specified ebook object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ebooks_id_scope_get**
> EbookScope v1_ebooks_id_scope_get(id)

Get specified scope of Ebook object 

Gets specified scope of Ebook object 

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
    api_instance = openapi_client.EbooksApi(api_client)
    id = 'id_example' # str | instance id of ebook record

    try:
        # Get specified scope of Ebook object 
        api_response = api_instance.v1_ebooks_id_scope_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EbooksApi->v1_ebooks_id_scope_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of ebook record | 

### Return type

[**EbookScope**](EbookScope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of scope for ebook were found |  -  |
**404** | Specified scope for ebook object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

