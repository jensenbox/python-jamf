# openapi_client.EnrollmentCustomizationApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_enrollment_customization_get**](EnrollmentCustomizationApi.md#v1_enrollment_customization_get) | **GET** /v1/enrollment-customization | Retrieve sorted and paged Enrollment Customizations 
[**v1_enrollment_customization_id_delete**](EnrollmentCustomizationApi.md#v1_enrollment_customization_id_delete) | **DELETE** /v1/enrollment-customization/{id} | Delete an Enrollment Customization with the supplied id 
[**v1_enrollment_customization_id_get**](EnrollmentCustomizationApi.md#v1_enrollment_customization_id_get) | **GET** /v1/enrollment-customization/{id} | Retrieve an Enrollment Customization with the supplied id 
[**v1_enrollment_customization_id_history_get**](EnrollmentCustomizationApi.md#v1_enrollment_customization_id_history_get) | **GET** /v1/enrollment-customization/{id}/history | Get sorted and paged Enrollment Customization history objects 
[**v1_enrollment_customization_id_history_post**](EnrollmentCustomizationApi.md#v1_enrollment_customization_id_history_post) | **POST** /v1/enrollment-customization/{id}/history | Add Enrollment Customization history object notes 
[**v1_enrollment_customization_id_prestages_get**](EnrollmentCustomizationApi.md#v1_enrollment_customization_id_prestages_get) | **GET** /v1/enrollment-customization/{id}/prestages | Retrieve the list of Prestages using this Enrollment Customization 
[**v1_enrollment_customization_id_put**](EnrollmentCustomizationApi.md#v1_enrollment_customization_id_put) | **PUT** /v1/enrollment-customization/{id} | Update an Enrollment Customization 
[**v1_enrollment_customization_images_post**](EnrollmentCustomizationApi.md#v1_enrollment_customization_images_post) | **POST** /v1/enrollment-customization/images | Upload an image
[**v1_enrollment_customization_post**](EnrollmentCustomizationApi.md#v1_enrollment_customization_post) | **POST** /v1/enrollment-customization | Create an Enrollment Customization 
[**v2_enrollment_customizations_get**](EnrollmentCustomizationApi.md#v2_enrollment_customizations_get) | **GET** /v2/enrollment-customizations | Retrieve sorted and paged Enrollment Customizations 
[**v2_enrollment_customizations_id_delete**](EnrollmentCustomizationApi.md#v2_enrollment_customizations_id_delete) | **DELETE** /v2/enrollment-customizations/{id} | Delete an Enrollment Customization with the supplied id 
[**v2_enrollment_customizations_id_get**](EnrollmentCustomizationApi.md#v2_enrollment_customizations_id_get) | **GET** /v2/enrollment-customizations/{id} | Retrieve an Enrollment Customization with the supplied id 
[**v2_enrollment_customizations_id_history_get**](EnrollmentCustomizationApi.md#v2_enrollment_customizations_id_history_get) | **GET** /v2/enrollment-customizations/{id}/history | Get sorted and paged Enrollment Customization history objects 
[**v2_enrollment_customizations_id_history_post**](EnrollmentCustomizationApi.md#v2_enrollment_customizations_id_history_post) | **POST** /v2/enrollment-customizations/{id}/history | Add Enrollment Customization history object notes 
[**v2_enrollment_customizations_id_prestages_get**](EnrollmentCustomizationApi.md#v2_enrollment_customizations_id_prestages_get) | **GET** /v2/enrollment-customizations/{id}/prestages | Retrieve the list of Prestages using this Enrollment Customization 
[**v2_enrollment_customizations_id_put**](EnrollmentCustomizationApi.md#v2_enrollment_customizations_id_put) | **PUT** /v2/enrollment-customizations/{id} | Update an Enrollment Customization 
[**v2_enrollment_customizations_images_post**](EnrollmentCustomizationApi.md#v2_enrollment_customizations_images_post) | **POST** /v2/enrollment-customizations/images | Upload an image
[**v2_enrollment_customizations_post**](EnrollmentCustomizationApi.md#v2_enrollment_customizations_post) | **POST** /v2/enrollment-customizations | Create an Enrollment Customization 


# **v1_enrollment_customization_get**
> EnrollmentCustomizationSearchResults v1_enrollment_customization_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Retrieve sorted and paged Enrollment Customizations 

Retrieves sorted and paged Enrollment Customizations

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'id:asc' # str | Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'id:asc')

    try:
        # Retrieve sorted and paged Enrollment Customizations 
        api_response = api_instance.v1_enrollment_customization_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v1_enrollment_customization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to &#39;id:asc&#39;]

### Return type

[**EnrollmentCustomizationSearchResults**](EnrollmentCustomizationSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_delete**
> v1_enrollment_customization_id_delete(id)

Delete an Enrollment Customization with the supplied id 

Deletes an Enrollment Customization with the supplied id

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 56 # int | Enrollment Customization identifier

    try:
        # Delete an Enrollment Customization with the supplied id 
        api_instance.v1_enrollment_customization_id_delete(id)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v1_enrollment_customization_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 

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
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_get**
> GetEnrollmentCustomization v1_enrollment_customization_id_get(id)

Retrieve an Enrollment Customization with the supplied id 

Retrieves an Enrollment Customization with the supplied id

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 56 # int | Enrollment Customization identifier

    try:
        # Retrieve an Enrollment Customization with the supplied id 
        api_response = api_instance.v1_enrollment_customization_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v1_enrollment_customization_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 

### Return type

[**GetEnrollmentCustomization**](GetEnrollmentCustomization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_history_get**
> HistorySearchResults v1_enrollment_customization_id_history_get(id, page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get sorted and paged Enrollment Customization history objects 

Gets sorted and paged enrollment customization history objects

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 56 # int | Enrollment Customization identifier
page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the 'sort' query param is duplicated for each sort criterion, e.g., ...&sort=name%2Casc&sort=date%2Cdesc (optional) (default to ["date:desc"])

    try:
        # Get sorted and paged Enrollment Customization history objects 
        api_response = api_instance.v1_enrollment_customization_id_history_get(id, page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v1_enrollment_customization_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the &#39;sort&#39; query param is duplicated for each sort criterion, e.g., ...&amp;sort&#x3D;name%2Casc&amp;sort&#x3D;date%2Cdesc | [optional] [default to [&quot;date:desc&quot;]]

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
**200** | Details of enrollment customization history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_history_post**
> ObjectHistory v1_enrollment_customization_id_history_post(id, object_history_note)

Add Enrollment Customization history object notes 

Adds enrollment customization history object notes

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 56 # int | Enrollment Customization identifier
object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | History notes to create

    try:
        # Add Enrollment Customization history object notes 
        api_response = api_instance.v1_enrollment_customization_id_history_post(id, object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v1_enrollment_customization_id_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
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
**201** | Notes of enrollment customization history were added |  -  |
**503** | Enrollment customization history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_prestages_get**
> PrestageDependencies v1_enrollment_customization_id_prestages_get(id)

Retrieve the list of Prestages using this Enrollment Customization 

Retrieves the list of Prestages using this Enrollment Customization

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 56 # int | Enrollment Customization identifier

    try:
        # Retrieve the list of Prestages using this Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_prestages_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v1_enrollment_customization_id_prestages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 

### Return type

[**PrestageDependencies**](PrestageDependencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_put**
> GetEnrollmentCustomization v1_enrollment_customization_id_put(id, enrollment_customization)

Update an Enrollment Customization 

Updates an Enrollment Customization

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 56 # int | Enrollment Customization identifier
enrollment_customization = openapi_client.EnrollmentCustomization() # EnrollmentCustomization | Enrollment Customization to update

    try:
        # Update an Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_put(id, enrollment_customization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v1_enrollment_customization_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **enrollment_customization** | [**EnrollmentCustomization**](EnrollmentCustomization.md)| Enrollment Customization to update | 

### Return type

[**GetEnrollmentCustomization**](GetEnrollmentCustomization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_images_post**
> BrandingImageUrl v1_enrollment_customization_images_post(file)

Upload an image

Uploads an image

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    file = '/path/to/file' # file | The file to upload

    try:
        # Upload an image
        api_response = api_instance.v1_enrollment_customization_images_post(file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v1_enrollment_customization_images_post: %s\n" % e)
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

# **v1_enrollment_customization_post**
> GetEnrollmentCustomization v1_enrollment_customization_post(enrollment_customization)

Create an Enrollment Customization 

Create an enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    enrollment_customization = openapi_client.EnrollmentCustomization() # EnrollmentCustomization | Enrollment customization to create.

    try:
        # Create an Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_post(enrollment_customization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v1_enrollment_customization_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_customization** | [**EnrollmentCustomization**](EnrollmentCustomization.md)| Enrollment customization to create. | 

### Return type

[**GetEnrollmentCustomization**](GetEnrollmentCustomization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Enrollment customization was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_customizations_get**
> EnrollmentCustomizationSearchResultsV2 v2_enrollment_customizations_get(page=page, page_size=page_size, sort=sort)

Retrieve sorted and paged Enrollment Customizations 

Retrieves sorted and paged Enrollment Customizations

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:asc"] # list[str] | Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["id:asc"])

    try:
        # Retrieve sorted and paged Enrollment Customizations 
        api_response = api_instance.v2_enrollment_customizations_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v2_enrollment_customizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;id:asc&quot;]]

### Return type

[**EnrollmentCustomizationSearchResultsV2**](EnrollmentCustomizationSearchResultsV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_customizations_id_delete**
> v2_enrollment_customizations_id_delete(id)

Delete an Enrollment Customization with the supplied id 

Deletes an Enrollment Customization with the supplied id

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 'id_example' # str | Enrollment Customization identifier

    try:
        # Delete an Enrollment Customization with the supplied id 
        api_instance.v2_enrollment_customizations_id_delete(id)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v2_enrollment_customizations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enrollment Customization identifier | 

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
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_customizations_id_get**
> EnrollmentCustomizationV2 v2_enrollment_customizations_id_get(id)

Retrieve an Enrollment Customization with the supplied id 

Retrieves an Enrollment Customization with the supplied id

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 'id_example' # str | Enrollment Customization identifier

    try:
        # Retrieve an Enrollment Customization with the supplied id 
        api_response = api_instance.v2_enrollment_customizations_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v2_enrollment_customizations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enrollment Customization identifier | 

### Return type

[**EnrollmentCustomizationV2**](EnrollmentCustomizationV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_customizations_id_history_get**
> HistorySearchResults v2_enrollment_customizations_id_history_get(id, page=page, page_size=page_size, sort=sort)

Get sorted and paged Enrollment Customization history objects 

Gets sorted and paged enrollment customization history objects

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 'id_example' # str | Enrollment Customization identifier
page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the 'sort' query param is duplicated for each sort criterion, e.g., ...&sort=name%2Casc&sort=date%2Cdesc (optional) (default to ["date:desc"])

    try:
        # Get sorted and paged Enrollment Customization history objects 
        api_response = api_instance.v2_enrollment_customizations_id_history_get(id, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v2_enrollment_customizations_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enrollment Customization identifier | 
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the &#39;sort&#39; query param is duplicated for each sort criterion, e.g., ...&amp;sort&#x3D;name%2Casc&amp;sort&#x3D;date%2Cdesc | [optional] [default to [&quot;date:desc&quot;]]

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
**200** | Details of enrollment customization history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_customizations_id_history_post**
> ObjectHistory v2_enrollment_customizations_id_history_post(id, object_history_note)

Add Enrollment Customization history object notes 

Adds enrollment customization history object notes

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 'id_example' # str | Enrollment Customization identifier
object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | History notes to create

    try:
        # Add Enrollment Customization history object notes 
        api_response = api_instance.v2_enrollment_customizations_id_history_post(id, object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v2_enrollment_customizations_id_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enrollment Customization identifier | 
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
**201** | Notes of enrollment customization history were added |  -  |
**503** | Enrollment customization history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_customizations_id_prestages_get**
> PrestageDependencies v2_enrollment_customizations_id_prestages_get(id)

Retrieve the list of Prestages using this Enrollment Customization 

Retrieves the list of Prestages using this Enrollment Customization

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 'id_example' # str | Enrollment Customization identifier

    try:
        # Retrieve the list of Prestages using this Enrollment Customization 
        api_response = api_instance.v2_enrollment_customizations_id_prestages_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v2_enrollment_customizations_id_prestages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enrollment Customization identifier | 

### Return type

[**PrestageDependencies**](PrestageDependencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_customizations_id_put**
> EnrollmentCustomizationV2 v2_enrollment_customizations_id_put(id, enrollment_customization_v2)

Update an Enrollment Customization 

Updates an Enrollment Customization

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    id = 'id_example' # str | Enrollment Customization identifier
enrollment_customization_v2 = openapi_client.EnrollmentCustomizationV2() # EnrollmentCustomizationV2 | Enrollment Customization to update

    try:
        # Update an Enrollment Customization 
        api_response = api_instance.v2_enrollment_customizations_id_put(id, enrollment_customization_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v2_enrollment_customizations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enrollment Customization identifier | 
 **enrollment_customization_v2** | [**EnrollmentCustomizationV2**](EnrollmentCustomizationV2.md)| Enrollment Customization to update | 

### Return type

[**EnrollmentCustomizationV2**](EnrollmentCustomizationV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_customizations_images_post**
> BrandingImageUrl v2_enrollment_customizations_images_post(file)

Upload an image

Uploads an image

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    file = '/path/to/file' # file | The file to upload

    try:
        # Upload an image
        api_response = api_instance.v2_enrollment_customizations_images_post(file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v2_enrollment_customizations_images_post: %s\n" % e)
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

# **v2_enrollment_customizations_post**
> HrefResponse v2_enrollment_customizations_post(enrollment_customization_v2)

Create an Enrollment Customization 

Create an enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationApi(api_client)
    enrollment_customization_v2 = openapi_client.EnrollmentCustomizationV2() # EnrollmentCustomizationV2 | Enrollment customization to create.

    try:
        # Create an Enrollment Customization 
        api_response = api_instance.v2_enrollment_customizations_post(enrollment_customization_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationApi->v2_enrollment_customizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_customization_v2** | [**EnrollmentCustomizationV2**](EnrollmentCustomizationV2.md)| Enrollment customization to create. | 

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
**201** | Enrollment customization was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

