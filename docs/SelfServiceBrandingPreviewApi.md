# jamf.SelfServiceBrandingPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**self_service_branding_configurations_get**](SelfServiceBrandingPreviewApi.md#self_service_branding_configurations_get) | **GET** /self-service/branding/configurations | Search for sorted and paged branding configurations 
[**self_service_branding_configurations_id_delete**](SelfServiceBrandingPreviewApi.md#self_service_branding_configurations_id_delete) | **DELETE** /self-service/branding/configurations/{id} | Delete the Self Service branding configuration indicated by the provided id 
[**self_service_branding_configurations_id_get**](SelfServiceBrandingPreviewApi.md#self_service_branding_configurations_id_get) | **GET** /self-service/branding/configurations/{id} | Read a single Self Service branding configuration indicated by the provided id 
[**self_service_branding_configurations_id_put**](SelfServiceBrandingPreviewApi.md#self_service_branding_configurations_id_put) | **PUT** /self-service/branding/configurations/{id} | Update a Self Service branding configuration with the supplied details 
[**self_service_branding_configurations_post**](SelfServiceBrandingPreviewApi.md#self_service_branding_configurations_post) | **POST** /self-service/branding/configurations | Create a Self Service branding configuration with the supplied 
[**self_service_branding_images_post**](SelfServiceBrandingPreviewApi.md#self_service_branding_images_post) | **POST** /self-service/branding/images | Upload an image 


# **self_service_branding_configurations_get**
> BrandingSearchResults self_service_branding_configurations_get(page=page, pagesize=pagesize, size=size, page_size=page_size, sort=sort)

Search for sorted and paged branding configurations 

Search for sorted and paged branding configurations

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
    api_instance = jamf.SelfServiceBrandingPreviewApi(api_client)
    page = 0 # int |  (optional) (default to 0)
pagesize = 100 # int |  (optional) (default to 100)
size = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'id' # str | Specifies the attribute to sort by. Defaults to ascending order. Prefix the attribute name with a minus (-) symbol for descending order. (optional) (default to 'id')

    try:
        # Search for sorted and paged branding configurations 
        api_response = api_instance.self_service_branding_configurations_get(page=page, pagesize=pagesize, size=size, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SelfServiceBrandingPreviewApi->self_service_branding_configurations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **pagesize** | **int**|  | [optional] [default to 100]
 **size** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Specifies the attribute to sort by. Defaults to ascending order. Prefix the attribute name with a minus (-) symbol for descending order. | [optional] [default to &#39;id&#39;]

### Return type

[**BrandingSearchResults**](BrandingSearchResults.md)

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

# **self_service_branding_configurations_id_delete**
> self_service_branding_configurations_id_delete(id)

Delete the Self Service branding configuration indicated by the provided id 

Delete the Self Service branding configuration indicated by the provided id.

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
    api_instance = jamf.SelfServiceBrandingPreviewApi(api_client)
    id = 56 # int | id of branding configuration

    try:
        # Delete the Self Service branding configuration indicated by the provided id 
        api_instance.self_service_branding_configurations_id_delete(id)
    except ApiException as e:
        print("Exception when calling SelfServiceBrandingPreviewApi->self_service_branding_configurations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of branding configuration | 

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
**204** | Successful response |  -  |
**404** | Invalid id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_service_branding_configurations_id_get**
> BrandingConfiguration self_service_branding_configurations_id_get(id)

Read a single Self Service branding configuration indicated by the provided id 

Read a single Self Service branding configuration indicated by the provided id.

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
    api_instance = jamf.SelfServiceBrandingPreviewApi(api_client)
    id = 56 # int | id of branding configuration

    try:
        # Read a single Self Service branding configuration indicated by the provided id 
        api_response = api_instance.self_service_branding_configurations_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SelfServiceBrandingPreviewApi->self_service_branding_configurations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of branding configuration | 

### Return type

[**BrandingConfiguration**](BrandingConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, iOS Branding, macOS Branding

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_service_branding_configurations_id_put**
> BrandingConfiguration self_service_branding_configurations_id_put(id, branding_configuration=branding_configuration)

Update a Self Service branding configuration with the supplied details 

Update a Self Service branding configuration with the supplied details

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
    api_instance = jamf.SelfServiceBrandingPreviewApi(api_client)
    id = 56 # int | id of branding configuration
branding_configuration = jamf.BrandingConfiguration() # BrandingConfiguration | The branding configuration values to update (optional)

    try:
        # Update a Self Service branding configuration with the supplied details 
        api_response = api_instance.self_service_branding_configurations_id_put(id, branding_configuration=branding_configuration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SelfServiceBrandingPreviewApi->self_service_branding_configurations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of branding configuration | 
 **branding_configuration** | [**BrandingConfiguration**](BrandingConfiguration.md)| The branding configuration values to update | [optional] 

### Return type

[**BrandingConfiguration**](BrandingConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Invalid id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_service_branding_configurations_post**
> BrandingConfiguration self_service_branding_configurations_post(branding_configuration=branding_configuration)

Create a Self Service branding configuration with the supplied 

Create a Self Service branding configuration with the supplied details

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
    api_instance = jamf.SelfServiceBrandingPreviewApi(api_client)
    branding_configuration = jamf.BrandingConfiguration() # BrandingConfiguration | The branding configuration to create (optional)

    try:
        # Create a Self Service branding configuration with the supplied 
        api_response = api_instance.self_service_branding_configurations_post(branding_configuration=branding_configuration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SelfServiceBrandingPreviewApi->self_service_branding_configurations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branding_configuration** | [**BrandingConfiguration**](BrandingConfiguration.md)| The branding configuration to create | [optional] 

### Return type

[**BrandingConfiguration**](BrandingConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_service_branding_images_post**
> BrandingImageUrl self_service_branding_images_post(file)

Upload an image 

Uploads an image

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
    api_instance = jamf.SelfServiceBrandingPreviewApi(api_client)
    file = '/path/to/file' # file | The file to upload

    try:
        # Upload an image 
        api_response = api_instance.self_service_branding_images_post(file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SelfServiceBrandingPreviewApi->self_service_branding_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The file to upload | 

### Return type

[**BrandingImageUrl**](BrandingImageUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Image successfully uploaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

