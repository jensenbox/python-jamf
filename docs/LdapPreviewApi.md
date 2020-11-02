# openapi_client.LdapPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ldap_groups_get**](LdapPreviewApi.md#ldap_groups_get) | **GET** /ldap/groups | Retrieve the configured access groups that contain the text in the search param 
[**ldap_servers_get**](LdapPreviewApi.md#ldap_servers_get) | **GET** /ldap/servers | Retrieve all LDAP Servers including Cloud Identity Providers 


# **ldap_groups_get**
> LdapGroupSearchResults ldap_groups_get(q=q)

Retrieve the configured access groups that contain the text in the search param 

Retrieves the configured access groups that contain the text in the searchParam.

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
    api_instance = openapi_client.LdapPreviewApi(api_client)
    q = 'null' # str | Will perform a \"contains\" search on the names of access groups (optional) (default to 'null')

    try:
        # Retrieve the configured access groups that contain the text in the search param 
        api_response = api_instance.ldap_groups_get(q=q)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LdapPreviewApi->ldap_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Will perform a \&quot;contains\&quot; search on the names of access groups | [optional] [default to &#39;null&#39;]

### Return type

[**LdapGroupSearchResults**](LdapGroupSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful search. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_servers_get**
> list[LdapServer] ldap_servers_get()

Retrieve all LDAP Servers including Cloud Identity Providers 

Retrieves all LDAP Servers including Cloud Identity Providers.

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
    api_instance = openapi_client.LdapPreviewApi(api_client)
    
    try:
        # Retrieve all LDAP Servers including Cloud Identity Providers 
        api_response = api_instance.ldap_servers_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LdapPreviewApi->ldap_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LdapServer]**](LdapServer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully completed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

