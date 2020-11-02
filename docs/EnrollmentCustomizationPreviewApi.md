# openapi_client.EnrollmentCustomizationPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_enrollment_customization_id_all_get**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_all_get) | **GET** /v1/enrollment-customization/{id}/all | Get all Panels for single Enrollment Customization 
[**v1_enrollment_customization_id_all_panel_id_delete**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_all_panel_id_delete) | **DELETE** /v1/enrollment-customization/{id}/all/{panel-id} | Delete a single Panel from an Enrollment Customization 
[**v1_enrollment_customization_id_all_panel_id_get**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_all_panel_id_get) | **GET** /v1/enrollment-customization/{id}/all/{panel-id} | Get a single Panel for a single Enrollment Customization 
[**v1_enrollment_customization_id_ldap_panel_id_delete**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_ldap_panel_id_delete) | **DELETE** /v1/enrollment-customization/{id}/ldap/{panel-id} | Delete an LDAP single panel from an Enrollment Customization 
[**v1_enrollment_customization_id_ldap_panel_id_get**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_ldap_panel_id_get) | **GET** /v1/enrollment-customization/{id}/ldap/{panel-id} | Get a single LDAP panel for a single Enrollment Customization 
[**v1_enrollment_customization_id_ldap_panel_id_put**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_ldap_panel_id_put) | **PUT** /v1/enrollment-customization/{id}/ldap/{panel-id} | Update a single LDAP Panel for a single Enrollment Customization 
[**v1_enrollment_customization_id_ldap_post**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_ldap_post) | **POST** /v1/enrollment-customization/{id}/ldap | Create an LDAP Panel for a single Enrollment Customization 
[**v1_enrollment_customization_id_sso_panel_id_delete**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_sso_panel_id_delete) | **DELETE** /v1/enrollment-customization/{id}/sso/{panel-id} | Delete a single SSO Panel from an Enrollment Customization 
[**v1_enrollment_customization_id_sso_panel_id_get**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_sso_panel_id_get) | **GET** /v1/enrollment-customization/{id}/sso/{panel-id} | Get a single SSO Panel for a single Enrollment Customization 
[**v1_enrollment_customization_id_sso_panel_id_put**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_sso_panel_id_put) | **PUT** /v1/enrollment-customization/{id}/sso/{panel-id} | Update a single SSO Panel for a single Enrollment Customization 
[**v1_enrollment_customization_id_sso_post**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_sso_post) | **POST** /v1/enrollment-customization/{id}/sso | Create an SSO Panel for a single Enrollment Customization 
[**v1_enrollment_customization_id_text_panel_id_delete**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_text_panel_id_delete) | **DELETE** /v1/enrollment-customization/{id}/text/{panel-id} | Delete a Text single Panel from an Enrollment Customization 
[**v1_enrollment_customization_id_text_panel_id_get**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_text_panel_id_get) | **GET** /v1/enrollment-customization/{id}/text/{panel-id} | Get a single Text Panel for a single Enrollment Customization 
[**v1_enrollment_customization_id_text_panel_id_markdown_get**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_text_panel_id_markdown_get) | **GET** /v1/enrollment-customization/{id}/text/{panel-id}/markdown | Get the markdown output of a single Text Panel for a single Enrollment 
[**v1_enrollment_customization_id_text_panel_id_put**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_text_panel_id_put) | **PUT** /v1/enrollment-customization/{id}/text/{panel-id} | Update a single Text Panel for a single Enrollment Customization 
[**v1_enrollment_customization_id_text_post**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_id_text_post) | **POST** /v1/enrollment-customization/{id}/text | Create a Text Panel for a single Enrollment Customization 
[**v1_enrollment_customization_parse_markdown_post**](EnrollmentCustomizationPreviewApi.md#v1_enrollment_customization_parse_markdown_post) | **POST** /v1/enrollment-customization/parse-markdown | Parse the given string as markdown text and return Html output 


# **v1_enrollment_customization_id_all_get**
> EnrollmentCustomizationPanelList v1_enrollment_customization_id_all_get(id)

Get all Panels for single Enrollment Customization 

Get all panels for single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier

    try:
        # Get all Panels for single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_all_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 

### Return type

[**EnrollmentCustomizationPanelList**](EnrollmentCustomizationPanelList.md)

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

# **v1_enrollment_customization_id_all_panel_id_delete**
> v1_enrollment_customization_id_all_panel_id_delete(id, panel_id)

Delete a single Panel from an Enrollment Customization 

Delete a single panel from an Enrollment Customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier

    try:
        # Delete a single Panel from an Enrollment Customization 
        api_instance.v1_enrollment_customization_id_all_panel_id_delete(id, panel_id)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_all_panel_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 

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

# **v1_enrollment_customization_id_all_panel_id_get**
> GetEnrollmentCustomizationPanel v1_enrollment_customization_id_all_panel_id_get(id, panel_id)

Get a single Panel for a single Enrollment Customization 

Get a single panel for a single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier

    try:
        # Get a single Panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_all_panel_id_get(id, panel_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_all_panel_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 

### Return type

[**GetEnrollmentCustomizationPanel**](GetEnrollmentCustomizationPanel.md)

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

# **v1_enrollment_customization_id_ldap_panel_id_delete**
> v1_enrollment_customization_id_ldap_panel_id_delete(id, panel_id)

Delete an LDAP single panel from an Enrollment Customization 

Delete an LDAP single Panel from an Enrollment Customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier

    try:
        # Delete an LDAP single panel from an Enrollment Customization 
        api_instance.v1_enrollment_customization_id_ldap_panel_id_delete(id, panel_id)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_ldap_panel_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 

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

# **v1_enrollment_customization_id_ldap_panel_id_get**
> GetEnrollmentCustomizationPanelLdapAuth v1_enrollment_customization_id_ldap_panel_id_get(id, panel_id)

Get a single LDAP panel for a single Enrollment Customization 

Get a single LDAP panel for a single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier

    try:
        # Get a single LDAP panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_ldap_panel_id_get(id, panel_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_ldap_panel_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 

### Return type

[**GetEnrollmentCustomizationPanelLdapAuth**](GetEnrollmentCustomizationPanelLdapAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization or Panel does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_ldap_panel_id_put**
> GetEnrollmentCustomizationPanelLdapAuth v1_enrollment_customization_id_ldap_panel_id_put(id, panel_id, enrollment_customization_panel_ldap_auth)

Update a single LDAP Panel for a single Enrollment Customization 

Update a single LDAP panel for a single enrollment customization. If multiple LDAP access groups are defined with the same name and id, only one will be saved.

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier
enrollment_customization_panel_ldap_auth = openapi_client.EnrollmentCustomizationPanelLdapAuth() # EnrollmentCustomizationPanelLdapAuth | Enrollment Customization Panel to update

    try:
        # Update a single LDAP Panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_ldap_panel_id_put(id, panel_id, enrollment_customization_panel_ldap_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_ldap_panel_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 
 **enrollment_customization_panel_ldap_auth** | [**EnrollmentCustomizationPanelLdapAuth**](EnrollmentCustomizationPanelLdapAuth.md)| Enrollment Customization Panel to update | 

### Return type

[**GetEnrollmentCustomizationPanelLdapAuth**](GetEnrollmentCustomizationPanelLdapAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization or Panel does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_ldap_post**
> GetEnrollmentCustomizationPanelLdapAuth v1_enrollment_customization_id_ldap_post(id, enrollment_customization_panel_ldap_auth)

Create an LDAP Panel for a single Enrollment Customization 

Create an LDAP panel for a single enrollment customization. If multiple LDAP access groups are defined with the same name and id, only one will be saved.

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
enrollment_customization_panel_ldap_auth = openapi_client.EnrollmentCustomizationPanelLdapAuth() # EnrollmentCustomizationPanelLdapAuth | Enrollment Customization Panel to create

    try:
        # Create an LDAP Panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_ldap_post(id, enrollment_customization_panel_ldap_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_ldap_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **enrollment_customization_panel_ldap_auth** | [**EnrollmentCustomizationPanelLdapAuth**](EnrollmentCustomizationPanelLdapAuth.md)| Enrollment Customization Panel to create | 

### Return type

[**GetEnrollmentCustomizationPanelLdapAuth**](GetEnrollmentCustomizationPanelLdapAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | LDAP panel was created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_sso_panel_id_delete**
> v1_enrollment_customization_id_sso_panel_id_delete(id, panel_id)

Delete a single SSO Panel from an Enrollment Customization 

Delete a single SSO panel from an Enrollment Customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier

    try:
        # Delete a single SSO Panel from an Enrollment Customization 
        api_instance.v1_enrollment_customization_id_sso_panel_id_delete(id, panel_id)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_sso_panel_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 

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

# **v1_enrollment_customization_id_sso_panel_id_get**
> GetEnrollmentCustomizationPanelSsoAuth v1_enrollment_customization_id_sso_panel_id_get(id, panel_id)

Get a single SSO Panel for a single Enrollment Customization 

Get a single SSO panel for a single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier

    try:
        # Get a single SSO Panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_sso_panel_id_get(id, panel_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_sso_panel_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 

### Return type

[**GetEnrollmentCustomizationPanelSsoAuth**](GetEnrollmentCustomizationPanelSsoAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization or Panel does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_sso_panel_id_put**
> GetEnrollmentCustomizationPanelSsoAuth v1_enrollment_customization_id_sso_panel_id_put(id, panel_id, enrollment_customization_panel_sso_auth)

Update a single SSO Panel for a single Enrollment Customization 

Update a single SSO panel for a single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier
enrollment_customization_panel_sso_auth = openapi_client.EnrollmentCustomizationPanelSsoAuth() # EnrollmentCustomizationPanelSsoAuth | Enrollment Customization Panel to update

    try:
        # Update a single SSO Panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_sso_panel_id_put(id, panel_id, enrollment_customization_panel_sso_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_sso_panel_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 
 **enrollment_customization_panel_sso_auth** | [**EnrollmentCustomizationPanelSsoAuth**](EnrollmentCustomizationPanelSsoAuth.md)| Enrollment Customization Panel to update | 

### Return type

[**GetEnrollmentCustomizationPanelSsoAuth**](GetEnrollmentCustomizationPanelSsoAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization or Panel does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_sso_post**
> GetEnrollmentCustomizationPanelSsoAuth v1_enrollment_customization_id_sso_post(id, enrollment_customization_panel_sso_auth)

Create an SSO Panel for a single Enrollment Customization 

Create an SSO panel for a single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
enrollment_customization_panel_sso_auth = openapi_client.EnrollmentCustomizationPanelSsoAuth() # EnrollmentCustomizationPanelSsoAuth | Enrollment Customization Panel to create

    try:
        # Create an SSO Panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_sso_post(id, enrollment_customization_panel_sso_auth)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_sso_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **enrollment_customization_panel_sso_auth** | [**EnrollmentCustomizationPanelSsoAuth**](EnrollmentCustomizationPanelSsoAuth.md)| Enrollment Customization Panel to create | 

### Return type

[**GetEnrollmentCustomizationPanelSsoAuth**](GetEnrollmentCustomizationPanelSsoAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Auth panel was created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_text_panel_id_delete**
> v1_enrollment_customization_id_text_panel_id_delete(id, panel_id)

Delete a Text single Panel from an Enrollment Customization 

Delete a Text single panel from an Enrollment Customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier

    try:
        # Delete a Text single Panel from an Enrollment Customization 
        api_instance.v1_enrollment_customization_id_text_panel_id_delete(id, panel_id)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_text_panel_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 

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

# **v1_enrollment_customization_id_text_panel_id_get**
> GetEnrollmentCustomizationPanelText v1_enrollment_customization_id_text_panel_id_get(id, panel_id)

Get a single Text Panel for a single Enrollment Customization 

Get a single Text panel for a single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier

    try:
        # Get a single Text Panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_text_panel_id_get(id, panel_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_text_panel_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 

### Return type

[**GetEnrollmentCustomizationPanelText**](GetEnrollmentCustomizationPanelText.md)

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

# **v1_enrollment_customization_id_text_panel_id_markdown_get**
> Markdown v1_enrollment_customization_id_text_panel_id_markdown_get(id, panel_id)

Get the markdown output of a single Text Panel for a single Enrollment 

Get the markdown output of a single Text panel for a single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier

    try:
        # Get the markdown output of a single Text Panel for a single Enrollment 
        api_response = api_instance.v1_enrollment_customization_id_text_panel_id_markdown_get(id, panel_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_text_panel_id_markdown_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 

### Return type

[**Markdown**](Markdown.md)

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

# **v1_enrollment_customization_id_text_panel_id_put**
> GetEnrollmentCustomizationPanelText v1_enrollment_customization_id_text_panel_id_put(id, panel_id, enrollment_customization_panel_text)

Update a single Text Panel for a single Enrollment Customization 

Update a single Text panel for a single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
panel_id = 56 # int | Panel object identifier
enrollment_customization_panel_text = openapi_client.EnrollmentCustomizationPanelText() # EnrollmentCustomizationPanelText | Enrollment Customization Panel to update

    try:
        # Update a single Text Panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_text_panel_id_put(id, panel_id, enrollment_customization_panel_text)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_text_panel_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **panel_id** | **int**| Panel object identifier | 
 **enrollment_customization_panel_text** | [**EnrollmentCustomizationPanelText**](EnrollmentCustomizationPanelText.md)| Enrollment Customization Panel to update | 

### Return type

[**GetEnrollmentCustomizationPanelText**](GetEnrollmentCustomizationPanelText.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Enrollment Customization or Panel does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_id_text_post**
> GetEnrollmentCustomizationPanelText v1_enrollment_customization_id_text_post(id, enrollment_customization_panel_text)

Create a Text Panel for a single Enrollment Customization 

Create a Text panel for a single enrollment customization

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    id = 56 # int | Enrollment Customization identifier
enrollment_customization_panel_text = openapi_client.EnrollmentCustomizationPanelText() # EnrollmentCustomizationPanelText | Enrollment Customization Panel to create

    try:
        # Create a Text Panel for a single Enrollment Customization 
        api_response = api_instance.v1_enrollment_customization_id_text_post(id, enrollment_customization_panel_text)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_id_text_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Enrollment Customization identifier | 
 **enrollment_customization_panel_text** | [**EnrollmentCustomizationPanelText**](EnrollmentCustomizationPanelText.md)| Enrollment Customization Panel to create | 

### Return type

[**GetEnrollmentCustomizationPanelText**](GetEnrollmentCustomizationPanelText.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Text panel was created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_customization_parse_markdown_post**
> Markdown v1_enrollment_customization_parse_markdown_post(markdown)

Parse the given string as markdown text and return Html output 

Parse the given string as markdown text and return Html output

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
    api_instance = openapi_client.EnrollmentCustomizationPreviewApi(api_client)
    markdown = openapi_client.Markdown() # Markdown | Enrollment Customization Panel to create

    try:
        # Parse the given string as markdown text and return Html output 
        api_response = api_instance.v1_enrollment_customization_parse_markdown_post(markdown)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentCustomizationPreviewApi->v1_enrollment_customization_parse_markdown_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **markdown** | [**Markdown**](Markdown.md)| Enrollment Customization Panel to create | 

### Return type

[**Markdown**](Markdown.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

