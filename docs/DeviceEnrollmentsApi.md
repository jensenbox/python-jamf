# openapi_client.DeviceEnrollmentsApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_device_enrollments_get**](DeviceEnrollmentsApi.md#v1_device_enrollments_get) | **GET** /v1/device-enrollments | Read all sorted and paged Device Enrollment instances 
[**v1_device_enrollments_id_delete**](DeviceEnrollmentsApi.md#v1_device_enrollments_id_delete) | **DELETE** /v1/device-enrollments/{id} | Delete a Device Enrollment Instance with the supplied id 
[**v1_device_enrollments_id_disown_post**](DeviceEnrollmentsApi.md#v1_device_enrollments_id_disown_post) | **POST** /v1/device-enrollments/{id}/disown | Disown devices from the given Device Enrollment Instance 
[**v1_device_enrollments_id_get**](DeviceEnrollmentsApi.md#v1_device_enrollments_id_get) | **GET** /v1/device-enrollments/{id} | Retrieve a Device Enrollment Instance with the supplied id 
[**v1_device_enrollments_id_history_get**](DeviceEnrollmentsApi.md#v1_device_enrollments_id_history_get) | **GET** /v1/device-enrollments/{id}/history | Get sorted and paged Device Enrollment history objects 
[**v1_device_enrollments_id_history_post**](DeviceEnrollmentsApi.md#v1_device_enrollments_id_history_post) | **POST** /v1/device-enrollments/{id}/history | Add Device Enrollment history object notes 
[**v1_device_enrollments_id_put**](DeviceEnrollmentsApi.md#v1_device_enrollments_id_put) | **PUT** /v1/device-enrollments/{id} | Update a Device Enrollment Instance with the supplied id 
[**v1_device_enrollments_id_syncs_get**](DeviceEnrollmentsApi.md#v1_device_enrollments_id_syncs_get) | **GET** /v1/device-enrollments/{id}/syncs | Get all instance sync states for a single Device Enrollment Instance 
[**v1_device_enrollments_id_syncs_latest_get**](DeviceEnrollmentsApi.md#v1_device_enrollments_id_syncs_latest_get) | **GET** /v1/device-enrollments/{id}/syncs/latest | Get the latest sync state for a single Device Enrollment Instance 
[**v1_device_enrollments_id_upload_token_put**](DeviceEnrollmentsApi.md#v1_device_enrollments_id_upload_token_put) | **PUT** /v1/device-enrollments/{id}/upload-token | Update a Device Enrollment Instance with the supplied Token 
[**v1_device_enrollments_public_key_get**](DeviceEnrollmentsApi.md#v1_device_enrollments_public_key_get) | **GET** /v1/device-enrollments/public-key | Retrieve the Jamf Pro Device Enrollment public key 
[**v1_device_enrollments_syncs_get**](DeviceEnrollmentsApi.md#v1_device_enrollments_syncs_get) | **GET** /v1/device-enrollments/syncs | Get all instance sync states for all Device Enrollment Instances 
[**v1_device_enrollments_upload_token_post**](DeviceEnrollmentsApi.md#v1_device_enrollments_upload_token_post) | **POST** /v1/device-enrollments/upload-token | Create a Device Enrollment Instance with the supplied Token 


# **v1_device_enrollments_get**
> DeviceEnrollmentInstanceSearchResults v1_device_enrollments_get(page=page, page_size=page_size, sort=sort)

Read all sorted and paged Device Enrollment instances 

Search for sorted and paged device enrollment instances

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:asc"] # list[str] | Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["id:asc"])

    try:
        # Read all sorted and paged Device Enrollment instances 
        api_response = api_instance.v1_device_enrollments_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;id:asc&quot;]]

### Return type

[**DeviceEnrollmentInstanceSearchResults**](DeviceEnrollmentInstanceSearchResults.md)

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

# **v1_device_enrollments_id_delete**
> v1_device_enrollments_id_delete(id)

Delete a Device Enrollment Instance with the supplied id 

Deletes a Device Enrollment Instance with the supplied id

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier

    try:
        # Delete a Device Enrollment Instance with the supplied id 
        api_instance.v1_device_enrollments_id_delete(id)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 

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
**204** | Success |  -  |
**404** | Device Enrollment Instance with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_device_enrollments_id_disown_post**
> DeviceEnrollmentDisownResponse v1_device_enrollments_id_disown_post(id, device_enrollment_disown_body=device_enrollment_disown_body)

Disown devices from the given Device Enrollment Instance 

Disowns devices from the given device enrollment instance

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier
device_enrollment_disown_body = openapi_client.DeviceEnrollmentDisownBody() # DeviceEnrollmentDisownBody | List of device serial numbers to disown (optional)

    try:
        # Disown devices from the given Device Enrollment Instance 
        api_response = api_instance.v1_device_enrollments_id_disown_post(id, device_enrollment_disown_body=device_enrollment_disown_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_id_disown_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 
 **device_enrollment_disown_body** | [**DeviceEnrollmentDisownBody**](DeviceEnrollmentDisownBody.md)| List of device serial numbers to disown | [optional] 

### Return type

[**DeviceEnrollmentDisownResponse**](DeviceEnrollmentDisownResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Could not find device enrollment program instance for given id |  -  |
**500** | Something went wrong. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_device_enrollments_id_get**
> DeviceEnrollmentInstance v1_device_enrollments_id_get(id)

Retrieve a Device Enrollment Instance with the supplied id 

Retrieves a Device Enrollment Instance with the supplied id

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier

    try:
        # Retrieve a Device Enrollment Instance with the supplied id 
        api_response = api_instance.v1_device_enrollments_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 

### Return type

[**DeviceEnrollmentInstance**](DeviceEnrollmentInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Device Enrollment Instance with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_device_enrollments_id_history_get**
> HistorySearchResults v1_device_enrollments_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)

Get sorted and paged Device Enrollment history objects 

Gets sorted and paged device enrollment history objects

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier
page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the 'sort' query param is duplicated for each sort criterion, e.g., ...&sort=name%2Casc&sort=date%2Cdesc (optional) (default to ["date:desc"])
filter = '' # str | Query in the RSQL format, allowing to filter history notes collection. Default search is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: search=username!=admin and details==*disabled* and date<2019-12-15 (optional) (default to '')

    try:
        # Get sorted and paged Device Enrollment history objects 
        api_response = api_instance.v1_device_enrollments_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property,asc/desc. Default sort order is descending. Multiple sort criteria are supported and must be entered on separate lines in Swagger UI. In the URI the &#39;sort&#39; query param is duplicated for each sort criterion, e.g., ...&amp;sort&#x3D;name%2Casc&amp;sort&#x3D;date%2Cdesc | [optional] [default to [&quot;date:desc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter history notes collection. Default search is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: search&#x3D;username!&#x3D;admin and details&#x3D;&#x3D;*disabled* and date&lt;2019-12-15 | [optional] [default to &#39;&#39;]

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
**200** | Details of device enrollment history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_device_enrollments_id_history_post**
> HrefResponse v1_device_enrollments_id_history_post(id, object_history_note)

Add Device Enrollment history object notes 

Adds device enrollment history object notes

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier
object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | History notes to create

    try:
        # Add Device Enrollment history object notes 
        api_response = api_instance.v1_device_enrollments_id_history_post(id, object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_id_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 
 **object_history_note** | [**ObjectHistoryNote**](ObjectHistoryNote.md)| History notes to create | 

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
**201** | Notes of device enrollment history were added |  -  |
**503** | Device enrollment history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_device_enrollments_id_put**
> DeviceEnrollmentInstance v1_device_enrollments_id_put(id, device_enrollment_instance)

Update a Device Enrollment Instance with the supplied id 

Updates a Device Enrollment Instance with the supplied id

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier
device_enrollment_instance = openapi_client.DeviceEnrollmentInstance() # DeviceEnrollmentInstance | 

    try:
        # Update a Device Enrollment Instance with the supplied id 
        api_response = api_instance.v1_device_enrollments_id_put(id, device_enrollment_instance)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 
 **device_enrollment_instance** | [**DeviceEnrollmentInstance**](DeviceEnrollmentInstance.md)|  | 

### Return type

[**DeviceEnrollmentInstance**](DeviceEnrollmentInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Device Enrollment Instance with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_device_enrollments_id_syncs_get**
> list[DeviceEnrollmentInstanceSyncStatus] v1_device_enrollments_id_syncs_get(id)

Get all instance sync states for a single Device Enrollment Instance 

Get all instance sync states for a single instance

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier

    try:
        # Get all instance sync states for a single Device Enrollment Instance 
        api_response = api_instance.v1_device_enrollments_id_syncs_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_id_syncs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 

### Return type

[**list[DeviceEnrollmentInstanceSyncStatus]**](DeviceEnrollmentInstanceSyncStatus.md)

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

# **v1_device_enrollments_id_syncs_latest_get**
> DeviceEnrollmentInstanceSyncStatus v1_device_enrollments_id_syncs_latest_get(id)

Get the latest sync state for a single Device Enrollment Instance 

Get the latest sync state for a single instance

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier

    try:
        # Get the latest sync state for a single Device Enrollment Instance 
        api_response = api_instance.v1_device_enrollments_id_syncs_latest_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_id_syncs_latest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 

### Return type

[**DeviceEnrollmentInstanceSyncStatus**](DeviceEnrollmentInstanceSyncStatus.md)

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

# **v1_device_enrollments_id_upload_token_put**
> DeviceEnrollmentInstance v1_device_enrollments_id_upload_token_put(id, device_enrollment_token)

Update a Device Enrollment Instance with the supplied Token 

Updates a device enrollment instance with the supplied token.

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    id = 'id_example' # str | Device Enrollment Instance identifier
device_enrollment_token = openapi_client.DeviceEnrollmentToken() # DeviceEnrollmentToken | The downloaded token base 64 encoded from the MDM server to be used to create a new Device Enrollment Instance.

    try:
        # Update a Device Enrollment Instance with the supplied Token 
        api_response = api_instance.v1_device_enrollments_id_upload_token_put(id, device_enrollment_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_id_upload_token_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device Enrollment Instance identifier | 
 **device_enrollment_token** | [**DeviceEnrollmentToken**](DeviceEnrollmentToken.md)| The downloaded token base 64 encoded from the MDM server to be used to create a new Device Enrollment Instance. | 

### Return type

[**DeviceEnrollmentInstance**](DeviceEnrollmentInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Device Enrollment Instance with that id does not exist |  -  |
**500** | Something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_device_enrollments_public_key_get**
> file v1_device_enrollments_public_key_get()

Retrieve the Jamf Pro Device Enrollment public key 

Retrieve the Jamf Pro device enrollment public key

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    
    try:
        # Retrieve the Jamf Pro Device Enrollment public key 
        api_response = api_instance.v1_device_enrollments_public_key_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_public_key_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-pem-file

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_device_enrollments_syncs_get**
> list[DeviceEnrollmentInstanceSyncStatus] v1_device_enrollments_syncs_get()

Get all instance sync states for all Device Enrollment Instances 

Get all instance sync states for all instances

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    
    try:
        # Get all instance sync states for all Device Enrollment Instances 
        api_response = api_instance.v1_device_enrollments_syncs_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_syncs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DeviceEnrollmentInstanceSyncStatus]**](DeviceEnrollmentInstanceSyncStatus.md)

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

# **v1_device_enrollments_upload_token_post**
> HrefResponse v1_device_enrollments_upload_token_post(device_enrollment_token)

Create a Device Enrollment Instance with the supplied Token 

Creates a device enrollment instance with the supplied token.

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
    api_instance = openapi_client.DeviceEnrollmentsApi(api_client)
    device_enrollment_token = openapi_client.DeviceEnrollmentToken() # DeviceEnrollmentToken | The downloaded token base 64 encoded from the MDM server to be used to create a new Device Enrollment Instance.

    try:
        # Create a Device Enrollment Instance with the supplied Token 
        api_response = api_instance.v1_device_enrollments_upload_token_post(device_enrollment_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceEnrollmentsApi->v1_device_enrollments_upload_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_enrollment_token** | [**DeviceEnrollmentToken**](DeviceEnrollmentToken.md)| The downloaded token base 64 encoded from the MDM server to be used to create a new Device Enrollment Instance. | 

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
**201** | Device Enrollment Instance was created |  -  |
**500** | Something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

