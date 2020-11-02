# jamf.CloudLdapApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_cloud_ldaps_defaults_mappings_get**](CloudLdapApi.md#v1_cloud_ldaps_defaults_mappings_get) | **GET** /v1/cloud-ldaps/defaults/mappings | Get default mappings
[**v1_cloud_ldaps_defaults_server_configuration_get**](CloudLdapApi.md#v1_cloud_ldaps_defaults_server_configuration_get) | **GET** /v1/cloud-ldaps/defaults/server-configuration | Get default server configuration
[**v1_cloud_ldaps_get**](CloudLdapApi.md#v1_cloud_ldaps_get) | **GET** /v1/cloud-ldaps | Get all Cloud Identity Providers configurations.
[**v1_cloud_ldaps_id_connection_bind_get**](CloudLdapApi.md#v1_cloud_ldaps_id_connection_bind_get) | **GET** /v1/cloud-ldaps/{id}/connection/bind | Get bind connection pool statistics
[**v1_cloud_ldaps_id_connection_search_get**](CloudLdapApi.md#v1_cloud_ldaps_id_connection_search_get) | **GET** /v1/cloud-ldaps/{id}/connection/search | Get search connection pool statistics
[**v1_cloud_ldaps_id_delete**](CloudLdapApi.md#v1_cloud_ldaps_id_delete) | **DELETE** /v1/cloud-ldaps/{id} | Delete Cloud Identity Provider configuration.
[**v1_cloud_ldaps_id_get**](CloudLdapApi.md#v1_cloud_ldaps_id_get) | **GET** /v1/cloud-ldaps/{id} | Get Cloud Identity Provider configuration with given id.
[**v1_cloud_ldaps_id_history_get**](CloudLdapApi.md#v1_cloud_ldaps_id_history_get) | **GET** /v1/cloud-ldaps/{id}/history | Get Cloud Identity Provider history
[**v1_cloud_ldaps_id_history_post**](CloudLdapApi.md#v1_cloud_ldaps_id_history_post) | **POST** /v1/cloud-ldaps/{id}/history | Add Cloud Identity Provider history note
[**v1_cloud_ldaps_id_mappings_get**](CloudLdapApi.md#v1_cloud_ldaps_id_mappings_get) | **GET** /v1/cloud-ldaps/{id}/mappings | Get mappings configurations for Cloud Identity Providers server configuration.
[**v1_cloud_ldaps_id_mappings_put**](CloudLdapApi.md#v1_cloud_ldaps_id_mappings_put) | **PUT** /v1/cloud-ldaps/{id}/mappings | Update Cloud Identity Provider mappings configuration.
[**v1_cloud_ldaps_id_put**](CloudLdapApi.md#v1_cloud_ldaps_id_put) | **PUT** /v1/cloud-ldaps/{id} | Update Cloud Identity Provider configuration
[**v1_cloud_ldaps_id_test_group_post**](CloudLdapApi.md#v1_cloud_ldaps_id_test_group_post) | **POST** /v1/cloud-ldaps/{id}/test-group | Get group test search
[**v1_cloud_ldaps_id_test_user_membership_post**](CloudLdapApi.md#v1_cloud_ldaps_id_test_user_membership_post) | **POST** /v1/cloud-ldaps/{id}/test-user-membership | Get membership test search
[**v1_cloud_ldaps_id_test_user_post**](CloudLdapApi.md#v1_cloud_ldaps_id_test_user_post) | **POST** /v1/cloud-ldaps/{id}/test-user | Get user test search
[**v1_cloud_ldaps_post**](CloudLdapApi.md#v1_cloud_ldaps_post) | **POST** /v1/cloud-ldaps | Create Cloud Identity Provider configuration
[**v1_ldap_keystore_verify_post**](CloudLdapApi.md#v1_ldap_keystore_verify_post) | **POST** /v1/ldap-keystore/verify | Validate keystore for Cloud Identity Provider secure connection


# **v1_cloud_ldaps_defaults_mappings_get**
> CloudLdapMappingsResponse v1_cloud_ldaps_defaults_mappings_get()

Get default mappings

Get default mappings which will work with Google Cloud Identity Provider.

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
    api_instance = jamf.CloudLdapApi(api_client)
    
    try:
        # Get default mappings
        api_response = api_instance.v1_cloud_ldaps_defaults_mappings_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_defaults_mappings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudLdapMappingsResponse**](CloudLdapMappingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default mappings returned. |  -  |
**400** | Files cannot be loaded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_defaults_server_configuration_get**
> CloudLdapConfigurationShortResponse v1_cloud_ldaps_defaults_server_configuration_get()

Get default server configuration

Get default server configuration which will work with Google Cloud Identity Provider.

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
    api_instance = jamf.CloudLdapApi(api_client)
    
    try:
        # Get default server configuration
        api_response = api_instance.v1_cloud_ldaps_defaults_server_configuration_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_defaults_server_configuration_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudLdapConfigurationShortResponse**](CloudLdapConfigurationShortResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default server configuration returned. |  -  |
**400** | Default server configuration cannot be loaded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_get**
> CloudLdapConfigurationSearchResults v1_cloud_ldaps_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get all Cloud Identity Providers configurations.

Returns all configured Cloud Identity Provider instances without keystore data.

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
    api_instance = jamf.CloudLdapApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'id' # str | Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'id')

    try:
        # Get all Cloud Identity Providers configurations.
        api_response = api_instance.v1_cloud_ldaps_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to &#39;id&#39;]

### Return type

[**CloudLdapConfigurationSearchResults**](CloudLdapConfigurationSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider configurations returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_connection_bind_get**
> CloudLdapConnectionPoolStatistics v1_cloud_ldaps_id_connection_bind_get(id)

Get bind connection pool statistics

Get all search connection pool for chosen Cloud Identity Provider. numConnectionsClosedDefunct - The number of connections that have been closed as defunct. numConnectionsClosedExpired - The number of connections that have been closed because they were expired. numConnectionsClosedUnneeded - The number of connections that have been closed because they were no longer needed. numFailedCheckouts - The number of failed attempts to check out a connection from the pool. numFailedConnectionAttempts - The number of failed attempts to create a connection for use in the pool. numReleasedValid - The number of valid connections released back to the pool. numSuccessfulCheckouts - The number of successful attempts to check out a connection from the pool. numSuccessfulCheckoutsNewConnection - The number of successful checkout attempts that had to create a new connection because none were available. numSuccessfulConnectionAttempts - The number successful attempts to create a connection for use in the pool. maximumAvailableConnections - The maximum number of connections that may be available in the pool at any time. numSuccessfulCheckoutsWithoutWait - The number of successful checkout attempts that were able to take an existing connection without waiting. numSuccessfulCheckoutsAfterWait - The number of successful checkout attempts that retrieved a connection from the pool after waiting for it to become available. numAvailableConnections - The number of connections currently available for use in the pool. 

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier

    try:
        # Get bind connection pool statistics
        api_response = api_instance.v1_cloud_ldaps_id_connection_bind_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_connection_bind_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 

### Return type

[**CloudLdapConnectionPoolStatistics**](CloudLdapConnectionPoolStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider bind connection pool statistics returned. |  -  |
**400** | Bind connection pool statistics data is not available. |  -  |
**404** | Cloud Identity Provider bind connection pool statistics does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_connection_search_get**
> CloudLdapConnectionPoolStatistics v1_cloud_ldaps_id_connection_search_get(id)

Get search connection pool statistics

Get all search connection pool for chosen Cloud Identity Provider. numConnectionsClosedDefunct - The number of connections that have been closed as defunct. numConnectionsClosedExpired - The number of connections that have been closed because they were expired. numConnectionsClosedUnneeded - The number of connections that have been closed because they were no longer needed. numFailedCheckouts - The number of failed attempts to check out a connection from the pool. numFailedConnectionAttempts - The number of failed attempts to create a connection for use in the pool. numReleasedValid - The number of valid connections released back to the pool. numSuccessfulCheckouts - The number of successful attempts to check out a connection from the pool. numSuccessfulCheckoutsNewConnection - The number of successful checkout attempts that had to create a new connection because none were available. numSuccessfulConnectionAttempts - The number successful attempts to create a connection for use in the pool. maximumAvailableConnections - The maximum number of connections that may be available in the pool at any time. numSuccessfulCheckoutsWithoutWait - The number of successful checkout attempts that were able to take an existing connection without waiting. numSuccessfulCheckoutsAfterWait - The number of successful checkout attempts that retrieved a connection from the pool after waiting for it to become available. numAvailableConnections - The number of connections currently available for use in the pool. 

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier

    try:
        # Get search connection pool statistics
        api_response = api_instance.v1_cloud_ldaps_id_connection_search_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_connection_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 

### Return type

[**CloudLdapConnectionPoolStatistics**](CloudLdapConnectionPoolStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider search connection pool statistics returned. |  -  |
**400** | Search connection pool statistics data is not available. |  -  |
**404** | Cloud Identity Provider search connection pool statistics does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_delete**
> v1_cloud_ldaps_id_delete(id)

Delete Cloud Identity Provider configuration.

Delete Cloud Identity Provider configuration.

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier

    try:
        # Delete Cloud Identity Provider configuration.
        api_instance.v1_cloud_ldaps_id_delete(id)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 

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
**204** | Cloud Identity Provider configuration deleted. |  -  |
**400** | Id can only be a number. |  -  |
**404** | Cloud Identity Provider configuration does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_get**
> CloudLdapConfigurationResponse v1_cloud_ldaps_id_get(id)

Get Cloud Identity Provider configuration with given id.

Get Cloud Identity Provider configuration with given id.

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier

    try:
        # Get Cloud Identity Provider configuration with given id.
        api_response = api_instance.v1_cloud_ldaps_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 

### Return type

[**CloudLdapConfigurationResponse**](CloudLdapConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider configuration returned. |  -  |
**400** | Id can only be a number. |  -  |
**404** | Specified Cloud Identity Provider configuration does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_history_get**
> HistorySearchResults v1_cloud_ldaps_id_history_get(id, page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get Cloud Identity Provider history

Gets specified Cloud Identity Provider object history

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier
page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'date:desc' # str | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'date:desc')

    try:
        # Get Cloud Identity Provider history
        api_response = api_instance.v1_cloud_ldaps_id_history_get(id, page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to &#39;date:desc&#39;]

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
**200** | Details of Cloud Identity Provider history were found |  -  |
**400** | Id can only be a number. |  -  |
**404** | Specified Cloud Identity Provider object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_history_post**
> ObjectHistory v1_cloud_ldaps_id_history_post(id, object_history_note)

Add Cloud Identity Provider history note

Adds specified Cloud Identity Provider object history notes 

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier
object_history_note = jamf.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add Cloud Identity Provider history note
        api_response = api_instance.v1_cloud_ldaps_id_history_post(id, object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 
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
**201** | Notes of Cloud Identity Provider history were added |  -  |
**404** | Specified Cloud Identity Provider object does not exist. |  -  |
**503** | Notes of Cloud Identity Provider can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_mappings_get**
> CloudLdapMappingsResponse v1_cloud_ldaps_id_mappings_get(id)

Get mappings configurations for Cloud Identity Providers server configuration.

Get all mappings configurations for Cloud Identity Providers server configuration.

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier

    try:
        # Get mappings configurations for Cloud Identity Providers server configuration.
        api_response = api_instance.v1_cloud_ldaps_id_mappings_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_mappings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 

### Return type

[**CloudLdapMappingsResponse**](CloudLdapMappingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider mappings configuration returned. |  -  |
**400** | Id can only be a number. |  -  |
**404** | Specified mappings settings for Cloud Identity Provider configuration do not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_mappings_put**
> CloudLdapMappingsResponse v1_cloud_ldaps_id_mappings_put(id, cloud_ldap_mappings_request)

Update Cloud Identity Provider mappings configuration.

Update Cloud Identity Provider mappings configuration. Cannot be used for partial updates, all content body must be sent.

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier
cloud_ldap_mappings_request = jamf.CloudLdapMappingsRequest() # CloudLdapMappingsRequest | Cloud Identity Provider mappings to update.

    try:
        # Update Cloud Identity Provider mappings configuration.
        api_response = api_instance.v1_cloud_ldaps_id_mappings_put(id, cloud_ldap_mappings_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_mappings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 
 **cloud_ldap_mappings_request** | [**CloudLdapMappingsRequest**](CloudLdapMappingsRequest.md)| Cloud Identity Provider mappings to update. | 

### Return type

[**CloudLdapMappingsResponse**](CloudLdapMappingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider mappings configuration updated. |  -  |
**400** | One or more parameters were invalid. |  -  |
**404** | Specified Cloud Identity Provider configuration does not exist. |  -  |
**409** | Cloud Identity Provider id from request path do not match id in request body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_put**
> CloudLdapConfigurationResponse v1_cloud_ldaps_id_put(id, cloud_ldap_configuration_update)

Update Cloud Identity Provider configuration

Update Cloud Identity Provider configuration. Cannot be used for partial updates, all content body must be sent.

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier
cloud_ldap_configuration_update = jamf.CloudLdapConfigurationUpdate() # CloudLdapConfigurationUpdate | Cloud Identity Provider configuration to update

    try:
        # Update Cloud Identity Provider configuration
        api_response = api_instance.v1_cloud_ldaps_id_put(id, cloud_ldap_configuration_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 
 **cloud_ldap_configuration_update** | [**CloudLdapConfigurationUpdate**](CloudLdapConfigurationUpdate.md)| Cloud Identity Provider configuration to update | 

### Return type

[**CloudLdapConfigurationResponse**](CloudLdapConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider configuration updated |  -  |
**400** | One or more parameters were invalid. |  -  |
**404** | Cloud Identity Provider configuration does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_test_group_post**
> GroupTestSearchResponse v1_cloud_ldaps_id_test_group_post(id, group_test_search_request)

Get group test search

Do test search to ensure about configuration and mappings

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier
group_test_search_request = jamf.GroupTestSearchRequest() # GroupTestSearchRequest | Search request

    try:
        # Get group test search
        api_response = api_instance.v1_cloud_ldaps_id_test_group_post(id, group_test_search_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_test_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 
 **group_test_search_request** | [**GroupTestSearchRequest**](GroupTestSearchRequest.md)| Search request | 

### Return type

[**GroupTestSearchResponse**](GroupTestSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider test search result returned. |  -  |
**404** | Cloud Identity Provider does not exist or is not active. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_test_user_membership_post**
> MembershipTestSearchResponse v1_cloud_ldaps_id_test_user_membership_post(id, membership_test_search_request)

Get membership test search

Do test search to ensure about configuration and mappings

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier
membership_test_search_request = jamf.MembershipTestSearchRequest() # MembershipTestSearchRequest | Search request

    try:
        # Get membership test search
        api_response = api_instance.v1_cloud_ldaps_id_test_user_membership_post(id, membership_test_search_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_test_user_membership_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 
 **membership_test_search_request** | [**MembershipTestSearchRequest**](MembershipTestSearchRequest.md)| Search request | 

### Return type

[**MembershipTestSearchResponse**](MembershipTestSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider test search result returned. |  -  |
**404** | Cloud Identity Provider does not exist or is not active. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_id_test_user_post**
> UserTestSearchResponse v1_cloud_ldaps_id_test_user_post(id, user_test_search_request)

Get user test search

Do test search to ensure about configuration and mappings

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
    api_instance = jamf.CloudLdapApi(api_client)
    id = 'id_example' # str | Cloud Identity Provider identifier
user_test_search_request = jamf.UserTestSearchRequest() # UserTestSearchRequest | Search request

    try:
        # Get user test search
        api_response = api_instance.v1_cloud_ldaps_id_test_user_post(id, user_test_search_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_id_test_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Cloud Identity Provider identifier | 
 **user_test_search_request** | [**UserTestSearchRequest**](UserTestSearchRequest.md)| Search request | 

### Return type

[**UserTestSearchResponse**](UserTestSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cloud Identity Provider test search result returned. |  -  |
**404** | Cloud Identity Provider does not exist or is not active. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cloud_ldaps_post**
> CloudLdapConfigurationResponse v1_cloud_ldaps_post(cloud_ldap_configuration_request)

Create Cloud Identity Provider configuration

Create new Cloud Identity Provider configuration with unique display name. If mappings not provided, then defaults will be generated instead.

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
    api_instance = jamf.CloudLdapApi(api_client)
    cloud_ldap_configuration_request = jamf.CloudLdapConfigurationRequest() # CloudLdapConfigurationRequest | Cloud Identity Provider configuration to create

    try:
        # Create Cloud Identity Provider configuration
        api_response = api_instance.v1_cloud_ldaps_post(cloud_ldap_configuration_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_cloud_ldaps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_ldap_configuration_request** | [**CloudLdapConfigurationRequest**](CloudLdapConfigurationRequest.md)| Cloud Identity Provider configuration to create | 

### Return type

[**CloudLdapConfigurationResponse**](CloudLdapConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Cloud Identity Provider configuration created |  -  |
**400** | Cloud Identity Provider configuration cannot be saved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ldap_keystore_verify_post**
> CloudLdapKeystore v1_ldap_keystore_verify_post(cloud_ldap_keystore_file)

Validate keystore for Cloud Identity Provider secure connection

Validate keystore for Cloud Identity Provider secure connection

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
    api_instance = jamf.CloudLdapApi(api_client)
    cloud_ldap_keystore_file = jamf.CloudLdapKeystoreFile() # CloudLdapKeystoreFile | 

    try:
        # Validate keystore for Cloud Identity Provider secure connection
        api_response = api_instance.v1_ldap_keystore_verify_post(cloud_ldap_keystore_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudLdapApi->v1_ldap_keystore_verify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_ldap_keystore_file** | [**CloudLdapKeystoreFile**](CloudLdapKeystoreFile.md)|  | 

### Return type

[**CloudLdapKeystore**](CloudLdapKeystore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keystore verified. |  -  |
**400** | One or more invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

