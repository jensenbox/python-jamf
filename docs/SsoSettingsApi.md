# openapi_client.SsoSettingsApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_sso_dependencies_get**](SsoSettingsApi.md#v1_sso_dependencies_get) | **GET** /v1/sso/dependencies | Retrieve the list of Enrollment Customizations using SSO 
[**v1_sso_disable_post**](SsoSettingsApi.md#v1_sso_disable_post) | **POST** /v1/sso/disable | Disable SSO 
[**v1_sso_get**](SsoSettingsApi.md#v1_sso_get) | **GET** /v1/sso | Retrieve the current Single Sign On configuration settings 
[**v1_sso_history_get**](SsoSettingsApi.md#v1_sso_history_get) | **GET** /v1/sso/history | Get SSO history object 
[**v1_sso_history_post**](SsoSettingsApi.md#v1_sso_history_post) | **POST** /v1/sso/history | Add SSO history object notes 
[**v1_sso_metadata_download_get**](SsoSettingsApi.md#v1_sso_metadata_download_get) | **GET** /v1/sso/metadata/download | Download the Jamf Pro SAML metadata file 
[**v1_sso_put**](SsoSettingsApi.md#v1_sso_put) | **PUT** /v1/sso | Updates the current Single Sign On configuration settings 
[**v1_sso_validate_post**](SsoSettingsApi.md#v1_sso_validate_post) | **POST** /v1/sso/validate | Endpoint for validation of a saml metadata url 


# **v1_sso_dependencies_get**
> EnrollmentCustomizationDependencies v1_sso_dependencies_get()

Retrieve the list of Enrollment Customizations using SSO 

Retrieves the list of Enrollment Customizations using SSO

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
    api_instance = openapi_client.SsoSettingsApi(api_client)
    
    try:
        # Retrieve the list of Enrollment Customizations using SSO 
        api_response = api_instance.v1_sso_dependencies_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoSettingsApi->v1_sso_dependencies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnrollmentCustomizationDependencies**](EnrollmentCustomizationDependencies.md)

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

# **v1_sso_disable_post**
> v1_sso_disable_post()

Disable SSO 

Disable SSO

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
    api_instance = openapi_client.SsoSettingsApi(api_client)
    
    try:
        # Disable SSO 
        api_instance.v1_sso_disable_post()
    except ApiException as e:
        print("Exception when calling SsoSettingsApi->v1_sso_disable_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**202** | SSO has been disabled |  -  |
**400** | SSO object don&#39;t exist or is already disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_sso_get**
> SsoSettings v1_sso_get()

Retrieve the current Single Sign On configuration settings 

Retrieves the current Single Sign On configuration settings

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
    api_instance = openapi_client.SsoSettingsApi(api_client)
    
    try:
        # Retrieve the current Single Sign On configuration settings 
        api_response = api_instance.v1_sso_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoSettingsApi->v1_sso_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SsoSettings**](SsoSettings.md)

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

# **v1_sso_history_get**
> HistorySearchResults v1_sso_history_get(page=page, page_size=page_size, sort=sort, filter=filter)

Get SSO history object 

Gets SSO history object 

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
    api_instance = openapi_client.SsoSettingsApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:desc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["id:desc"])
filter = '' # str | Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter=username!=admin and details==*disabled* and date<2019-12-15 (optional) (default to '')

    try:
        # Get SSO history object 
        api_response = api_instance.v1_sso_history_get(page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoSettingsApi->v1_sso_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;id:desc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter&#x3D;username!&#x3D;admin and details&#x3D;&#x3D;*disabled* and date&lt;2019-12-15 | [optional] [default to &#39;&#39;]

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
**200** | Details of SSO history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_sso_history_post**
> HrefResponse v1_sso_history_post(object_history_note)

Add SSO history object notes 

Adds SSO history object notes

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
    api_instance = openapi_client.SsoSettingsApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add SSO history object notes 
        api_response = api_instance.v1_sso_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoSettingsApi->v1_sso_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_history_note** | [**ObjectHistoryNote**](ObjectHistoryNote.md)| history notes to create | 

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
**201** | Notes of SSO history were added |  -  |
**503** | SSO object history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_sso_metadata_download_get**
> file v1_sso_metadata_download_get()

Download the Jamf Pro SAML metadata file 

Download the Jamf Pro SAML metadata file

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
    api_instance = openapi_client.SsoSettingsApi(api_client)
    
    try:
        # Download the Jamf Pro SAML metadata file 
        api_response = api_instance.v1_sso_metadata_download_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoSettingsApi->v1_sso_metadata_download_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful resposne |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_sso_put**
> SsoSettings v1_sso_put(sso_settings)

Updates the current Single Sign On configuration settings 

Updates the current Single Sign On configuration settings

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
    api_instance = openapi_client.SsoSettingsApi(api_client)
    sso_settings = openapi_client.SsoSettings() # SsoSettings | 

    try:
        # Updates the current Single Sign On configuration settings 
        api_response = api_instance.v1_sso_put(sso_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoSettingsApi->v1_sso_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_settings** | [**SsoSettings**](SsoSettings.md)|  | 

### Return type

[**SsoSettings**](SsoSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The update was successful and the newly updated object is returned. |  -  |
**400** | Bad Request. Either required fields are missing or there was a validation exception. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_sso_validate_post**
> v1_sso_validate_post(sso_metadata_url)

Endpoint for validation of a saml metadata url 

Validation of a content available under provided metadata URL.

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
    api_instance = openapi_client.SsoSettingsApi(api_client)
    sso_metadata_url = openapi_client.SsoMetadataUrl() # SsoMetadataUrl | url to validate

    try:
        # Endpoint for validation of a saml metadata url 
        api_instance.v1_sso_validate_post(sso_metadata_url)
    except ApiException as e:
        print("Exception when calling SsoSettingsApi->v1_sso_validate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_metadata_url** | [**SsoMetadataUrl**](SsoMetadataUrl.md)| url to validate | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | valid metadata url |  -  |
**400** | provided metadata URL is not valid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

