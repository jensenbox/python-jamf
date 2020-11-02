# openapi_client.ComputerPrestagesApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_computer_prestages_get**](ComputerPrestagesApi.md#v1_computer_prestages_get) | **GET** /v1/computer-prestages | Search for sorted and paged Computer Prestages 
[**v1_computer_prestages_id_delete**](ComputerPrestagesApi.md#v1_computer_prestages_id_delete) | **DELETE** /v1/computer-prestages/{id} | Delete a Computer Prestage with the supplied id 
[**v1_computer_prestages_id_get**](ComputerPrestagesApi.md#v1_computer_prestages_id_get) | **GET** /v1/computer-prestages/{id} | Retrieve a Computer Prestage with the supplied id 
[**v1_computer_prestages_id_put**](ComputerPrestagesApi.md#v1_computer_prestages_id_put) | **PUT** /v1/computer-prestages/{id} | Update a Computer Prestage 
[**v1_computer_prestages_id_scope_delete**](ComputerPrestagesApi.md#v1_computer_prestages_id_scope_delete) | **DELETE** /v1/computer-prestages/{id}/scope | Remove device Scope for a specific Computer Prestage 
[**v1_computer_prestages_id_scope_get**](ComputerPrestagesApi.md#v1_computer_prestages_id_scope_get) | **GET** /v1/computer-prestages/{id}/scope | Get device Scope for a specific Computer Prestage 
[**v1_computer_prestages_id_scope_post**](ComputerPrestagesApi.md#v1_computer_prestages_id_scope_post) | **POST** /v1/computer-prestages/{id}/scope | Add device Scope for a specific Computer Prestage 
[**v1_computer_prestages_id_scope_put**](ComputerPrestagesApi.md#v1_computer_prestages_id_scope_put) | **PUT** /v1/computer-prestages/{id}/scope | Replace device Scope for a specific Computer Prestage 
[**v1_computer_prestages_post**](ComputerPrestagesApi.md#v1_computer_prestages_post) | **POST** /v1/computer-prestages | Create a Computer Prestage 
[**v1_computer_prestages_scope_get**](ComputerPrestagesApi.md#v1_computer_prestages_scope_get) | **GET** /v1/computer-prestages/scope | Get all device Scope for all Computer Prestages 
[**v2_computer_prestages_get**](ComputerPrestagesApi.md#v2_computer_prestages_get) | **GET** /v2/computer-prestages | Get sorted and paged Computer Prestages 
[**v2_computer_prestages_id_delete**](ComputerPrestagesApi.md#v2_computer_prestages_id_delete) | **DELETE** /v2/computer-prestages/{id} | Delete a Computer Prestage with the supplied id 
[**v2_computer_prestages_id_get**](ComputerPrestagesApi.md#v2_computer_prestages_id_get) | **GET** /v2/computer-prestages/{id} | Retrieve a Computer Prestage with the supplied id 
[**v2_computer_prestages_id_put**](ComputerPrestagesApi.md#v2_computer_prestages_id_put) | **PUT** /v2/computer-prestages/{id} | Update a Computer Prestage 
[**v2_computer_prestages_id_scope_delete_multiple_post**](ComputerPrestagesApi.md#v2_computer_prestages_id_scope_delete_multiple_post) | **POST** /v2/computer-prestages/{id}/scope/delete-multiple | Remove device Scope for a specific Computer Prestage 
[**v2_computer_prestages_id_scope_get**](ComputerPrestagesApi.md#v2_computer_prestages_id_scope_get) | **GET** /v2/computer-prestages/{id}/scope | Get device Scope for a specific Computer Prestage 
[**v2_computer_prestages_id_scope_post**](ComputerPrestagesApi.md#v2_computer_prestages_id_scope_post) | **POST** /v2/computer-prestages/{id}/scope | Add device Scope for a specific Computer Prestage 
[**v2_computer_prestages_id_scope_put**](ComputerPrestagesApi.md#v2_computer_prestages_id_scope_put) | **PUT** /v2/computer-prestages/{id}/scope | Replace device Scope for a specific Computer Prestage 
[**v2_computer_prestages_post**](ComputerPrestagesApi.md#v2_computer_prestages_post) | **POST** /v2/computer-prestages | Create a Computer Prestage 
[**v2_computer_prestages_scope_get**](ComputerPrestagesApi.md#v2_computer_prestages_scope_get) | **GET** /v2/computer-prestages/scope | Get all device Scope for all Computer Prestages 


# **v1_computer_prestages_get**
> ComputerPrestageSearchResults v1_computer_prestages_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Search for sorted and paged Computer Prestages 

Search for sorted and paged computer prestages

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'id:asc' # str | Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'id:asc')

    try:
        # Search for sorted and paged Computer Prestages 
        api_response = api_instance.v1_computer_prestages_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_get: %s\n" % e)
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

[**ComputerPrestageSearchResults**](ComputerPrestageSearchResults.md)

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

# **v1_computer_prestages_id_delete**
> v1_computer_prestages_id_delete(id)

Delete a Computer Prestage with the supplied id 

Deletes a Computer Prestage with the supplied id

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 56 # int | Computer Prestage identifier

    try:
        # Delete a Computer Prestage with the supplied id 
        api_instance.v1_computer_prestages_id_delete(id)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Computer Prestage identifier | 

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

# **v1_computer_prestages_id_get**
> GetComputerPrestage v1_computer_prestages_id_get(id)

Retrieve a Computer Prestage with the supplied id 

Retrieves a Computer Prestage with the supplied id

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 56 # int | Computer Prestage identifier

    try:
        # Retrieve a Computer Prestage with the supplied id 
        api_response = api_instance.v1_computer_prestages_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Computer Prestage identifier | 

### Return type

[**GetComputerPrestage**](GetComputerPrestage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Computer Prestage with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computer_prestages_id_put**
> GetComputerPrestage v1_computer_prestages_id_put(id, put_computer_prestage)

Update a Computer Prestage 

Updates a Computer Prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 56 # int | Computer Prestage identifier
put_computer_prestage = openapi_client.PutComputerPrestage() # PutComputerPrestage | Computer Prestage to update

    try:
        # Update a Computer Prestage 
        api_response = api_instance.v1_computer_prestages_id_put(id, put_computer_prestage)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Computer Prestage identifier | 
 **put_computer_prestage** | [**PutComputerPrestage**](PutComputerPrestage.md)| Computer Prestage to update | 

### Return type

[**GetComputerPrestage**](GetComputerPrestage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Computer Prestage with that id does not exist |  -  |
**409** | The Computer Prestage was modified by another process. Read the Computer Prestage again for updated changes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computer_prestages_id_scope_delete**
> PrestageScopeResponse v1_computer_prestages_id_scope_delete(id, prestage_scope_update)

Remove device Scope for a specific Computer Prestage 

Remove device scope for a specific computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 56 # int | Computer Prestage identifier
prestage_scope_update = openapi_client.PrestageScopeUpdate() # PrestageScopeUpdate | Serial Numbers to remove from scope

    try:
        # Remove device Scope for a specific Computer Prestage 
        api_response = api_instance.v1_computer_prestages_id_scope_delete(id, prestage_scope_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_id_scope_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Computer Prestage identifier | 
 **prestage_scope_update** | [**PrestageScopeUpdate**](PrestageScopeUpdate.md)| Serial Numbers to remove from scope | 

### Return type

[**PrestageScopeResponse**](PrestageScopeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | One or more serial numbers are not valid |  -  |
**404** | Computer Prestage with that id does not exist |  -  |
**409** | Optimistic Lock Error - The prestage you are trying to update has been updated by another process |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computer_prestages_id_scope_get**
> PrestageScopeResponse v1_computer_prestages_id_scope_get(id)

Get device Scope for a specific Computer Prestage 

Get device scope for a specific computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 56 # int | Computer Prestage identifier

    try:
        # Get device Scope for a specific Computer Prestage 
        api_response = api_instance.v1_computer_prestages_id_scope_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_id_scope_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Computer Prestage identifier | 

### Return type

[**PrestageScopeResponse**](PrestageScopeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Computer Prestage with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computer_prestages_id_scope_post**
> PrestageScopeResponse v1_computer_prestages_id_scope_post(id, prestage_scope_update)

Add device Scope for a specific Computer Prestage 

Add device scope for a specific computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 56 # int | Computer Prestage identifier
prestage_scope_update = openapi_client.PrestageScopeUpdate() # PrestageScopeUpdate | Serial Numbers to scope

    try:
        # Add device Scope for a specific Computer Prestage 
        api_response = api_instance.v1_computer_prestages_id_scope_post(id, prestage_scope_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_id_scope_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Computer Prestage identifier | 
 **prestage_scope_update** | [**PrestageScopeUpdate**](PrestageScopeUpdate.md)| Serial Numbers to scope | 

### Return type

[**PrestageScopeResponse**](PrestageScopeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | One or more serial numbers are not valid |  -  |
**404** | Computer Prestage with that id does not exist |  -  |
**409** | Optimistic Lock Error - The prestage you are trying to update has been updated by another process |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computer_prestages_id_scope_put**
> PrestageScopeResponse v1_computer_prestages_id_scope_put(id, prestage_scope_update)

Replace device Scope for a specific Computer Prestage 

Replace device scope for a specific computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 56 # int | Computer Prestage identifier
prestage_scope_update = openapi_client.PrestageScopeUpdate() # PrestageScopeUpdate | Serial Numbers to scope

    try:
        # Replace device Scope for a specific Computer Prestage 
        api_response = api_instance.v1_computer_prestages_id_scope_put(id, prestage_scope_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_id_scope_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Computer Prestage identifier | 
 **prestage_scope_update** | [**PrestageScopeUpdate**](PrestageScopeUpdate.md)| Serial Numbers to scope | 

### Return type

[**PrestageScopeResponse**](PrestageScopeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | One or more serial numbers are not valid |  -  |
**404** | Computer Prestage with that id does not exist |  -  |
**409** | Optimistic Lock Error - The prestage you are trying to update has been updated by another process |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computer_prestages_post**
> GetComputerPrestage v1_computer_prestages_post(computer_prestage)

Create a Computer Prestage 

Create a computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    computer_prestage = openapi_client.ComputerPrestage() # ComputerPrestage | Computer Prestage to create. ids defined in this body will be ignored

    try:
        # Create a Computer Prestage 
        api_response = api_instance.v1_computer_prestages_post(computer_prestage)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **computer_prestage** | [**ComputerPrestage**](ComputerPrestage.md)| Computer Prestage to create. ids defined in this body will be ignored | 

### Return type

[**GetComputerPrestage**](GetComputerPrestage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Computer Prestage was created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computer_prestages_scope_get**
> PrestageScope v1_computer_prestages_scope_get()

Get all device Scope for all Computer Prestages 

Get all device scope for all computer prestages

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    
    try:
        # Get all device Scope for all Computer Prestages 
        api_response = api_instance.v1_computer_prestages_scope_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v1_computer_prestages_scope_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrestageScope**](PrestageScope.md)

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

# **v2_computer_prestages_get**
> ComputerPrestageSearchResultsV2 v2_computer_prestages_get(page=page, page_size=page_size, sort=sort)

Get sorted and paged Computer Prestages 

Gets sorted and paged computer prestages

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:desc"] # list[str] | Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["id:desc"])

    try:
        # Get sorted and paged Computer Prestages 
        api_response = api_instance.v2_computer_prestages_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;id:desc&quot;]]

### Return type

[**ComputerPrestageSearchResultsV2**](ComputerPrestageSearchResultsV2.md)

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

# **v2_computer_prestages_id_delete**
> v2_computer_prestages_id_delete(id)

Delete a Computer Prestage with the supplied id 

Deletes a Computer Prestage with the supplied id

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 'id_example' # str | Computer Prestage identifier

    try:
        # Delete a Computer Prestage with the supplied id 
        api_instance.v2_computer_prestages_id_delete(id)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Computer Prestage identifier | 

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

# **v2_computer_prestages_id_get**
> GetComputerPrestageV2 v2_computer_prestages_id_get(id)

Retrieve a Computer Prestage with the supplied id 

Retrieves a Computer Prestage with the supplied id

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 'id_example' # str | Computer Prestage identifier

    try:
        # Retrieve a Computer Prestage with the supplied id 
        api_response = api_instance.v2_computer_prestages_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Computer Prestage identifier | 

### Return type

[**GetComputerPrestageV2**](GetComputerPrestageV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Computer Prestage with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_computer_prestages_id_put**
> GetComputerPrestageV2 v2_computer_prestages_id_put(id, put_computer_prestage_v2)

Update a Computer Prestage 

Updates a Computer Prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 'id_example' # str | Computer Prestage identifier
put_computer_prestage_v2 = openapi_client.PutComputerPrestageV2() # PutComputerPrestageV2 | Computer Prestage to update

    try:
        # Update a Computer Prestage 
        api_response = api_instance.v2_computer_prestages_id_put(id, put_computer_prestage_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Computer Prestage identifier | 
 **put_computer_prestage_v2** | [**PutComputerPrestageV2**](PutComputerPrestageV2.md)| Computer Prestage to update | 

### Return type

[**GetComputerPrestageV2**](GetComputerPrestageV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Computer Prestage with that id does not exist |  -  |
**409** | The Computer Prestage was modified by another process. Read the Computer Prestage again for updated changes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_computer_prestages_id_scope_delete_multiple_post**
> PrestageScopeResponseV2 v2_computer_prestages_id_scope_delete_multiple_post(id, prestage_scope_update)

Remove device Scope for a specific Computer Prestage 

Remove device scope for a specific computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 'id_example' # str | Computer Prestage identifier
prestage_scope_update = openapi_client.PrestageScopeUpdate() # PrestageScopeUpdate | Serial Numbers to remove from scope

    try:
        # Remove device Scope for a specific Computer Prestage 
        api_response = api_instance.v2_computer_prestages_id_scope_delete_multiple_post(id, prestage_scope_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_id_scope_delete_multiple_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Computer Prestage identifier | 
 **prestage_scope_update** | [**PrestageScopeUpdate**](PrestageScopeUpdate.md)| Serial Numbers to remove from scope | 

### Return type

[**PrestageScopeResponseV2**](PrestageScopeResponseV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | One or more serial numbers are not valid |  -  |
**404** | Computer Prestage with that id does not exist |  -  |
**409** | Optimistic Lock Error - The prestage you are trying to update has been updated by another process |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_computer_prestages_id_scope_get**
> PrestageScopeResponseV2 v2_computer_prestages_id_scope_get(id)

Get device Scope for a specific Computer Prestage 

Get device scope for a specific computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 'id_example' # str | Computer Prestage identifier

    try:
        # Get device Scope for a specific Computer Prestage 
        api_response = api_instance.v2_computer_prestages_id_scope_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_id_scope_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Computer Prestage identifier | 

### Return type

[**PrestageScopeResponseV2**](PrestageScopeResponseV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Computer Prestage with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_computer_prestages_id_scope_post**
> PrestageScopeResponseV2 v2_computer_prestages_id_scope_post(id, prestage_scope_update)

Add device Scope for a specific Computer Prestage 

Add device scope for a specific computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 'id_example' # str | Computer Prestage identifier
prestage_scope_update = openapi_client.PrestageScopeUpdate() # PrestageScopeUpdate | Serial Numbers to scope

    try:
        # Add device Scope for a specific Computer Prestage 
        api_response = api_instance.v2_computer_prestages_id_scope_post(id, prestage_scope_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_id_scope_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Computer Prestage identifier | 
 **prestage_scope_update** | [**PrestageScopeUpdate**](PrestageScopeUpdate.md)| Serial Numbers to scope | 

### Return type

[**PrestageScopeResponseV2**](PrestageScopeResponseV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | One or more serial numbers are not valid |  -  |
**404** | Computer Prestage with that id does not exist |  -  |
**409** | Optimistic Lock Error - The prestage you are trying to update has been updated by another process |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_computer_prestages_id_scope_put**
> PrestageScopeResponseV2 v2_computer_prestages_id_scope_put(id, prestage_scope_update)

Replace device Scope for a specific Computer Prestage 

Replace device scope for a specific computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    id = 'id_example' # str | Computer Prestage identifier
prestage_scope_update = openapi_client.PrestageScopeUpdate() # PrestageScopeUpdate | Serial Numbers to scope

    try:
        # Replace device Scope for a specific Computer Prestage 
        api_response = api_instance.v2_computer_prestages_id_scope_put(id, prestage_scope_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_id_scope_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Computer Prestage identifier | 
 **prestage_scope_update** | [**PrestageScopeUpdate**](PrestageScopeUpdate.md)| Serial Numbers to scope | 

### Return type

[**PrestageScopeResponseV2**](PrestageScopeResponseV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | One or more serial numbers are not valid |  -  |
**404** | Computer Prestage with that id does not exist |  -  |
**409** | Optimistic Lock Error - The prestage you are trying to update has been updated by another process |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_computer_prestages_post**
> HrefResponse v2_computer_prestages_post(computer_prestage_v2)

Create a Computer Prestage 

Create a computer prestage

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    computer_prestage_v2 = openapi_client.ComputerPrestageV2() # ComputerPrestageV2 | Computer Prestage to create. ids defined in this body will be ignored

    try:
        # Create a Computer Prestage 
        api_response = api_instance.v2_computer_prestages_post(computer_prestage_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **computer_prestage_v2** | [**ComputerPrestageV2**](ComputerPrestageV2.md)| Computer Prestage to create. ids defined in this body will be ignored | 

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
**201** | Computer Prestage was created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_computer_prestages_scope_get**
> PrestageScopeV2 v2_computer_prestages_scope_get()

Get all device Scope for all Computer Prestages 

Get all device scope for all computer prestages

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
    api_instance = openapi_client.ComputerPrestagesApi(api_client)
    
    try:
        # Get all device Scope for all Computer Prestages 
        api_response = api_instance.v2_computer_prestages_scope_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerPrestagesApi->v2_computer_prestages_scope_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrestageScopeV2**](PrestageScopeV2.md)

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

