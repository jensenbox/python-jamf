# openapi_client.SupervisionIdentitiesPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_supervision_identities_get**](SupervisionIdentitiesPreviewApi.md#v1_supervision_identities_get) | **GET** /v1/supervision-identities | Search for sorted and paged Supervision Identities 
[**v1_supervision_identities_id_delete**](SupervisionIdentitiesPreviewApi.md#v1_supervision_identities_id_delete) | **DELETE** /v1/supervision-identities/{id} | Delete a Supervision Identity with the supplied id 
[**v1_supervision_identities_id_download_get**](SupervisionIdentitiesPreviewApi.md#v1_supervision_identities_id_download_get) | **GET** /v1/supervision-identities/{id}/download | Download the Supervision Identity .p12 file 
[**v1_supervision_identities_id_get**](SupervisionIdentitiesPreviewApi.md#v1_supervision_identities_id_get) | **GET** /v1/supervision-identities/{id} | Retrieve a Supervision Identity with the supplied id 
[**v1_supervision_identities_id_put**](SupervisionIdentitiesPreviewApi.md#v1_supervision_identities_id_put) | **PUT** /v1/supervision-identities/{id} | Update a Supervision Identity with the supplied information 
[**v1_supervision_identities_post**](SupervisionIdentitiesPreviewApi.md#v1_supervision_identities_post) | **POST** /v1/supervision-identities | Create a Supervision Identity for the supplied information 
[**v1_supervision_identities_upload_post**](SupervisionIdentitiesPreviewApi.md#v1_supervision_identities_upload_post) | **POST** /v1/supervision-identities/upload | Upload the Supervision Identity .p12 file 


# **v1_supervision_identities_get**
> SupervisionIdentitySearchResults v1_supervision_identities_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Search for sorted and paged Supervision Identities 

Search for sorted and paged supervision identities

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
    api_instance = openapi_client.SupervisionIdentitiesPreviewApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'id:asc' # str | Sorting criteria in the format: property:asc/desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'id:asc')

    try:
        # Search for sorted and paged Supervision Identities 
        api_response = api_instance.v1_supervision_identities_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupervisionIdentitiesPreviewApi->v1_supervision_identities_get: %s\n" % e)
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

[**SupervisionIdentitySearchResults**](SupervisionIdentitySearchResults.md)

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

# **v1_supervision_identities_id_delete**
> v1_supervision_identities_id_delete(id)

Delete a Supervision Identity with the supplied id 

Deletes a Supervision Identity with the supplied id

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
    api_instance = openapi_client.SupervisionIdentitiesPreviewApi(api_client)
    id = 56 # int | Supervision Identity identifier

    try:
        # Delete a Supervision Identity with the supplied id 
        api_instance.v1_supervision_identities_id_delete(id)
    except ApiException as e:
        print("Exception when calling SupervisionIdentitiesPreviewApi->v1_supervision_identities_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Supervision Identity identifier | 

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
**404** | Supervision Identity with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_supervision_identities_id_download_get**
> file v1_supervision_identities_id_download_get(id)

Download the Supervision Identity .p12 file 

Download the Supervision Identity .p12 file

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
    api_instance = openapi_client.SupervisionIdentitiesPreviewApi(api_client)
    id = 56 # int | Supervision Identity identifier

    try:
        # Download the Supervision Identity .p12 file 
        api_response = api_instance.v1_supervision_identities_id_download_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupervisionIdentitiesPreviewApi->v1_supervision_identities_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Supervision Identity identifier | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_supervision_identities_id_get**
> SupervisionIdentity v1_supervision_identities_id_get(id)

Retrieve a Supervision Identity with the supplied id 

Retrieves a Supervision Identity with the supplied id

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
    api_instance = openapi_client.SupervisionIdentitiesPreviewApi(api_client)
    id = 56 # int | Supervision Identity identifier

    try:
        # Retrieve a Supervision Identity with the supplied id 
        api_response = api_instance.v1_supervision_identities_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupervisionIdentitiesPreviewApi->v1_supervision_identities_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Supervision Identity identifier | 

### Return type

[**SupervisionIdentity**](SupervisionIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Supervision Identity with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_supervision_identities_id_put**
> SupervisionIdentity v1_supervision_identities_id_put(id, supervision_identity_update)

Update a Supervision Identity with the supplied information 

Updates a Supervision Identity with the supplied information

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
    api_instance = openapi_client.SupervisionIdentitiesPreviewApi(api_client)
    id = 56 # int | Supervision Identity identifier
supervision_identity_update = openapi_client.SupervisionIdentityUpdate() # SupervisionIdentityUpdate | 

    try:
        # Update a Supervision Identity with the supplied information 
        api_response = api_instance.v1_supervision_identities_id_put(id, supervision_identity_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupervisionIdentitiesPreviewApi->v1_supervision_identities_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Supervision Identity identifier | 
 **supervision_identity_update** | [**SupervisionIdentityUpdate**](SupervisionIdentityUpdate.md)|  | 

### Return type

[**SupervisionIdentity**](SupervisionIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Supervision Identity with that id does not exist |  -  |
**500** | Something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_supervision_identities_post**
> SupervisionIdentity v1_supervision_identities_post(supervision_identity_create)

Create a Supervision Identity for the supplied information 

Creates a Supervision Identity for the supplied information

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
    api_instance = openapi_client.SupervisionIdentitiesPreviewApi(api_client)
    supervision_identity_create = openapi_client.SupervisionIdentityCreate() # SupervisionIdentityCreate | 

    try:
        # Create a Supervision Identity for the supplied information 
        api_response = api_instance.v1_supervision_identities_post(supervision_identity_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupervisionIdentitiesPreviewApi->v1_supervision_identities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supervision_identity_create** | [**SupervisionIdentityCreate**](SupervisionIdentityCreate.md)|  | 

### Return type

[**SupervisionIdentity**](SupervisionIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**500** | Something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_supervision_identities_upload_post**
> SupervisionIdentity v1_supervision_identities_upload_post(supervision_identity_certificate_upload)

Upload the Supervision Identity .p12 file 

Uploads the Supervision Identity .p12 file

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
    api_instance = openapi_client.SupervisionIdentitiesPreviewApi(api_client)
    supervision_identity_certificate_upload = openapi_client.SupervisionIdentityCertificateUpload() # SupervisionIdentityCertificateUpload | The base 64 encoded .p12 file alone with other needed information

    try:
        # Upload the Supervision Identity .p12 file 
        api_response = api_instance.v1_supervision_identities_upload_post(supervision_identity_certificate_upload)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupervisionIdentitiesPreviewApi->v1_supervision_identities_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supervision_identity_certificate_upload** | [**SupervisionIdentityCertificateUpload**](SupervisionIdentityCertificateUpload.md)| The base 64 encoded .p12 file alone with other needed information | 

### Return type

[**SupervisionIdentity**](SupervisionIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**500** | Something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

