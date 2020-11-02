# openapi_client.EnrollmentApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_enrollment_access_groups_get**](EnrollmentApi.md#v1_enrollment_access_groups_get) | **GET** /v1/enrollment/access-groups | Retrieve the configured LDAP groups configured for User-Initiated Enrollment 
[**v1_enrollment_access_groups_group_key_delete**](EnrollmentApi.md#v1_enrollment_access_groups_group_key_delete) | **DELETE** /v1/enrollment/access-groups/{group-key} | Delete an LDAP group&#39;s access to user initiated Enrollment 
[**v1_enrollment_access_groups_group_key_get**](EnrollmentApi.md#v1_enrollment_access_groups_group_key_get) | **GET** /v1/enrollment/access-groups/{group-key} | Retrieve the configured LDAP groups configured for User-Initiated Enrollment 
[**v1_enrollment_access_groups_group_key_put**](EnrollmentApi.md#v1_enrollment_access_groups_group_key_put) | **PUT** /v1/enrollment/access-groups/{group-key} | Modify the configured LDAP groups configured for User-Initiated Enrollment 
[**v1_enrollment_filtered_language_codes_get**](EnrollmentApi.md#v1_enrollment_filtered_language_codes_get) | **GET** /v1/enrollment/filtered-language-codes | Retrieve the list of languages and corresponding ISO 639-1 Codes but only those not already added to Enrollment 
[**v1_enrollment_get**](EnrollmentApi.md#v1_enrollment_get) | **GET** /v1/enrollment | Get Enrollment object and Re-enrollment settings 
[**v1_enrollment_history_get**](EnrollmentApi.md#v1_enrollment_history_get) | **GET** /v1/enrollment/history | Get sorted and paged Enrollment history object 
[**v1_enrollment_history_post**](EnrollmentApi.md#v1_enrollment_history_post) | **POST** /v1/enrollment/history | Add Enrollment history object notes 
[**v1_enrollment_language_codes_get**](EnrollmentApi.md#v1_enrollment_language_codes_get) | **GET** /v1/enrollment/language-codes | Retrieve the list of languages and corresponding ISO 639-1 Codes 
[**v1_enrollment_languages_get**](EnrollmentApi.md#v1_enrollment_languages_get) | **GET** /v1/enrollment/languages | Get an array of the language codes that have Enrollment messaging 
[**v1_enrollment_languages_language_delete**](EnrollmentApi.md#v1_enrollment_languages_language_delete) | **DELETE** /v1/enrollment/languages/{language} | Delete the Enrollment messaging for a language 
[**v1_enrollment_languages_language_get**](EnrollmentApi.md#v1_enrollment_languages_language_get) | **GET** /v1/enrollment/languages/{language} | Retrieve the Enrollment messaging for a language 
[**v1_enrollment_languages_language_put**](EnrollmentApi.md#v1_enrollment_languages_language_put) | **PUT** /v1/enrollment/languages/{language} | Edit Enrollment messaging for a language 
[**v1_enrollment_put**](EnrollmentApi.md#v1_enrollment_put) | **PUT** /v1/enrollment | Update Enrollment object 
[**v2_enrollment_access_groups_get**](EnrollmentApi.md#v2_enrollment_access_groups_get) | **GET** /v2/enrollment/access-groups | Retrieve the configured LDAP groups configured for User-Initiated Enrollment 
[**v2_enrollment_access_groups_server_id_group_id_delete**](EnrollmentApi.md#v2_enrollment_access_groups_server_id_group_id_delete) | **DELETE** /v2/enrollment/access-groups/{serverId}/{groupId} | Delete an LDAP group&#39;s access to user initiated Enrollment 
[**v2_enrollment_access_groups_server_id_group_id_get**](EnrollmentApi.md#v2_enrollment_access_groups_server_id_group_id_get) | **GET** /v2/enrollment/access-groups/{serverId}/{groupId} | Retrieve the configured LDAP groups configured for User-Initiated Enrollment 
[**v2_enrollment_access_groups_server_id_group_id_put**](EnrollmentApi.md#v2_enrollment_access_groups_server_id_group_id_put) | **PUT** /v2/enrollment/access-groups/{serverId}/{groupId} | Modify the configured LDAP groups configured for User-Initiated Enrollment 
[**v2_enrollment_filtered_language_codes_get**](EnrollmentApi.md#v2_enrollment_filtered_language_codes_get) | **GET** /v2/enrollment/filtered-language-codes | Retrieve the list of languages and corresponding ISO 639-1 Codes but only those not already added to Enrollment 
[**v2_enrollment_get**](EnrollmentApi.md#v2_enrollment_get) | **GET** /v2/enrollment | Get Enrollment object and Re-enrollment settings 
[**v2_enrollment_history_get**](EnrollmentApi.md#v2_enrollment_history_get) | **GET** /v2/enrollment/history | Get sorted and paged Enrollment history object 
[**v2_enrollment_history_post**](EnrollmentApi.md#v2_enrollment_history_post) | **POST** /v2/enrollment/history | Add Enrollment history object notes 
[**v2_enrollment_language_codes_get**](EnrollmentApi.md#v2_enrollment_language_codes_get) | **GET** /v2/enrollment/language-codes | Retrieve the list of languages and corresponding ISO 639-1 Codes 
[**v2_enrollment_languages_get**](EnrollmentApi.md#v2_enrollment_languages_get) | **GET** /v2/enrollment/languages | Get an array of the language codes that have Enrollment messaging 
[**v2_enrollment_languages_language_id_delete**](EnrollmentApi.md#v2_enrollment_languages_language_id_delete) | **DELETE** /v2/enrollment/languages/{languageId} | Delete the Enrollment messaging for a language 
[**v2_enrollment_languages_language_id_get**](EnrollmentApi.md#v2_enrollment_languages_language_id_get) | **GET** /v2/enrollment/languages/{languageId} | Retrieve the Enrollment messaging for a language 
[**v2_enrollment_languages_language_id_put**](EnrollmentApi.md#v2_enrollment_languages_language_id_put) | **PUT** /v2/enrollment/languages/{languageId} | Edit Enrollment messaging for a language 
[**v2_enrollment_put**](EnrollmentApi.md#v2_enrollment_put) | **PUT** /v2/enrollment | Update Enrollment object 


# **v1_enrollment_access_groups_get**
> AccessGroupsSearchResults v1_enrollment_access_groups_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Retrieve the configured LDAP groups configured for User-Initiated Enrollment 

Retrieves the configured LDAP groups configured for User-Initiated Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'name:asc' # str | Sorting criteria in the format: property:asc/desc. Default sort is name:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'name:asc')

    try:
        # Retrieve the configured LDAP groups configured for User-Initiated Enrollment 
        api_response = api_instance.v1_enrollment_access_groups_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_access_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Default sort is name:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to &#39;name:asc&#39;]

### Return type

[**AccessGroupsSearchResults**](AccessGroupsSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found access groups matching search params. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_access_groups_group_key_delete**
> v1_enrollment_access_groups_group_key_delete(group_key)

Delete an LDAP group's access to user initiated Enrollment 

Deletes an LDAP group's access to user initiated enrollment. The group \"All LDAP Users\" cannot be deleted, but it can be modified to disallow User-Initiated Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    group_key = 'group_key_example' # str | The group key is a string composed of the LDAP server ID, underscore and the LDAP group id. Example: ``1_2``

    try:
        # Delete an LDAP group's access to user initiated Enrollment 
        api_instance.v1_enrollment_access_groups_group_key_delete(group_key)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_access_groups_group_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_key** | **str**| The group key is a string composed of the LDAP server ID, underscore and the LDAP group id. Example: &#x60;&#x60;1_2&#x60;&#x60; | 

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
**204** | Successful deletion |  -  |
**400** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_access_groups_group_key_get**
> EnrollmentAccessGroup v1_enrollment_access_groups_group_key_get(group_key)

Retrieve the configured LDAP groups configured for User-Initiated Enrollment 

Retrieves the configured LDAP groups configured for User-Initiated Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    group_key = 'group_key_example' # str | The group key is a string composed of the LDAP server ID, underscore and the LDAP group id. Example: ``1_2``

    try:
        # Retrieve the configured LDAP groups configured for User-Initiated Enrollment 
        api_response = api_instance.v1_enrollment_access_groups_group_key_get(group_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_access_groups_group_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_key** | **str**| The group key is a string composed of the LDAP server ID, underscore and the LDAP group id. Example: &#x60;&#x60;1_2&#x60;&#x60; | 

### Return type

[**EnrollmentAccessGroup**](EnrollmentAccessGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful query |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_access_groups_group_key_put**
> EnrollmentAccessGroup v1_enrollment_access_groups_group_key_put(group_key, enrollment_access_group=enrollment_access_group)

Modify the configured LDAP groups configured for User-Initiated Enrollment 

Modifies the configured LDAP groups configured for User-Initiated Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    group_key = 'group_key_example' # str | The group key is a string composed of the LDAP server ID, underscore and the LDAP group id. Example: ``1_2``
enrollment_access_group = openapi_client.EnrollmentAccessGroup() # EnrollmentAccessGroup |  (optional)

    try:
        # Modify the configured LDAP groups configured for User-Initiated Enrollment 
        api_response = api_instance.v1_enrollment_access_groups_group_key_put(group_key, enrollment_access_group=enrollment_access_group)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_access_groups_group_key_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_key** | **str**| The group key is a string composed of the LDAP server ID, underscore and the LDAP group id. Example: &#x60;&#x60;1_2&#x60;&#x60; | 
 **enrollment_access_group** | [**EnrollmentAccessGroup**](EnrollmentAccessGroup.md)|  | [optional] 

### Return type

[**EnrollmentAccessGroup**](EnrollmentAccessGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful query |  -  |
**400** | Bad request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_filtered_language_codes_get**
> list[LanguageCode] v1_enrollment_filtered_language_codes_get()

Retrieve the list of languages and corresponding ISO 639-1 Codes but only those not already added to Enrollment 

Retrieves the list of languages and corresponding ISO 639-1 Codes, but only those not already added to Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    
    try:
        # Retrieve the list of languages and corresponding ISO 639-1 Codes but only those not already added to Enrollment 
        api_response = api_instance.v1_enrollment_filtered_language_codes_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_filtered_language_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LanguageCode]**](LanguageCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves the list of languages and corresponding ISO 639-1 Codes, but only those not already added to Enrollment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_get**
> EnrollmentSettings v1_enrollment_get()

Get Enrollment object and Re-enrollment settings 

Gets Enrollment object and re-enrollment settings. The settings can be altered without providing the existing management password by providing the following value for managementPassword:  \\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff 

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    
    try:
        # Get Enrollment object and Re-enrollment settings 
        api_response = api_instance.v1_enrollment_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnrollmentSettings**](EnrollmentSettings.md)

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

# **v1_enrollment_history_get**
> HistorySearchResults v1_enrollment_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get sorted and paged Enrollment history object 

Gets sorted and paged Enrollment history object 

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'date:desc' # str | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'date:desc')

    try:
        # Get sorted and paged Enrollment history object 
        api_response = api_instance.v1_enrollment_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Details of enrollment history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_history_post**
> ObjectHistory v1_enrollment_history_post(object_history_note)

Add Enrollment history object notes 

Adds Enrollment history object notes 

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add Enrollment history object notes 
        api_response = api_instance.v1_enrollment_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** | Notes of enrollment history were added |  -  |
**503** | Enrollment history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_language_codes_get**
> list[LanguageCode] v1_enrollment_language_codes_get()

Retrieve the list of languages and corresponding ISO 639-1 Codes 

Retrieves the list of languages and corresponding ISO 639-1 Codes.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    
    try:
        # Retrieve the list of languages and corresponding ISO 639-1 Codes 
        api_response = api_instance.v1_enrollment_language_codes_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_language_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LanguageCode]**](LanguageCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of languages and corresponding ISO 639-1 Codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_languages_get**
> ProcessTextsSearchResults v1_enrollment_languages_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get an array of the language codes that have Enrollment messaging 

Returns an array of the language codes that have enrollment messaging currently configured.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'languageCode:asc' # str | Sorting criteria in the format: property:asc/desc. Default sort is languageCode:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'languageCode:asc')

    try:
        # Get an array of the language codes that have Enrollment messaging 
        api_response = api_instance.v1_enrollment_languages_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_languages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Default sort is languageCode:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to &#39;languageCode:asc&#39;]

### Return type

[**ProcessTextsSearchResults**](ProcessTextsSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found languages matching search params. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_languages_language_delete**
> v1_enrollment_languages_language_delete(language)

Delete the Enrollment messaging for a language 

Delete the enrollment messaging for a language.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    language = 'language_example' # str | Two letter ISO 639-1 Language Code

    try:
        # Delete the Enrollment messaging for a language 
        api_instance.v1_enrollment_languages_language_delete(language)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_languages_language_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Two letter ISO 639-1 Language Code | 

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
**204** | Successful deletetion |  -  |
**404** | Language not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_languages_language_get**
> EnrollmentProcessTextObject v1_enrollment_languages_language_get(language)

Retrieve the Enrollment messaging for a language 

Retrieves the enrollment messaging for a language.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    language = 'language_example' # str | Two letter ISO 639-1 Language Code

    try:
        # Retrieve the Enrollment messaging for a language 
        api_response = api_instance.v1_enrollment_languages_language_get(language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_languages_language_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Two letter ISO 639-1 Language Code | 

### Return type

[**EnrollmentProcessTextObject**](EnrollmentProcessTextObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Language not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_languages_language_put**
> EnrollmentProcessTextObject v1_enrollment_languages_language_put(language, enrollment_process_text_object=enrollment_process_text_object)

Edit Enrollment messaging for a language 

Edit enrollment messaging for a language.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    language = 'language_example' # str | Two letter ISO 639-1 Language Code
enrollment_process_text_object = openapi_client.EnrollmentProcessTextObject() # EnrollmentProcessTextObject |  (optional)

    try:
        # Edit Enrollment messaging for a language 
        api_response = api_instance.v1_enrollment_languages_language_put(language, enrollment_process_text_object=enrollment_process_text_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_languages_language_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Two letter ISO 639-1 Language Code | 
 **enrollment_process_text_object** | [**EnrollmentProcessTextObject**](EnrollmentProcessTextObject.md)|  | [optional] 

### Return type

[**EnrollmentProcessTextObject**](EnrollmentProcessTextObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enrollment_put**
> EnrollmentSettings v1_enrollment_put(enrollment_settings)

Update Enrollment object 

Update enrollment object. Regarding the `developerCertificateIdentity`, if this object is omitted, the certificate will not be deleted from Jamf Pro. The `identityKeystore` is the entire cert file as a base64 encoded string. The `md5Sum` field is not required in the PUT request, but is calculated and returned in the response. 

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    enrollment_settings = openapi_client.EnrollmentSettings() # EnrollmentSettings | Update enrollment

    try:
        # Update Enrollment object 
        api_response = api_instance.v1_enrollment_put(enrollment_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v1_enrollment_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_settings** | [**EnrollmentSettings**](EnrollmentSettings.md)| Update enrollment | 

### Return type

[**EnrollmentSettings**](EnrollmentSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated enrollment object |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_access_groups_get**
> AccessGroupsV2SearchResults v2_enrollment_access_groups_get(page=page, page_size=page_size, sort=sort)

Retrieve the configured LDAP groups configured for User-Initiated Enrollment 

Retrieves the configured LDAP groups configured for User-Initiated Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["name:asc"] # list[str] | Sorting criteria in the format: `property:asc/desc`. Default sort is `name:asc`. Multiple sort criteria are supported and must be separated with a comma. Example: `sort=date:desc,name:asc`.  (optional) (default to ["name:asc"])

    try:
        # Retrieve the configured LDAP groups configured for User-Initiated Enrollment 
        api_response = api_instance.v2_enrollment_access_groups_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_access_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: &#x60;property:asc/desc&#x60;. Default sort is &#x60;name:asc&#x60;. Multiple sort criteria are supported and must be separated with a comma. Example: &#x60;sort&#x3D;date:desc,name:asc&#x60;.  | [optional] [default to [&quot;name:asc&quot;]]

### Return type

[**AccessGroupsV2SearchResults**](AccessGroupsV2SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found access groups matching search params. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_access_groups_server_id_group_id_delete**
> v2_enrollment_access_groups_server_id_group_id_delete(server_id, group_id)

Delete an LDAP group's access to user initiated Enrollment 

Deletes an LDAP group's access to user initiated enrollment. The group \"All LDAP Users\" cannot be deleted, but it can be modified to disallow User-Initiated Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    server_id = 'server_id_example' # str | LDAP server id
group_id = 'group_id_example' # str | LDAP group id.

    try:
        # Delete an LDAP group's access to user initiated Enrollment 
        api_instance.v2_enrollment_access_groups_server_id_group_id_delete(server_id, group_id)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_access_groups_server_id_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| LDAP server id | 
 **group_id** | **str**| LDAP group id. | 

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
**204** | Successful deletion |  -  |
**400** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_access_groups_server_id_group_id_get**
> EnrollmentAccessGroupV2 v2_enrollment_access_groups_server_id_group_id_get(server_id, group_id)

Retrieve the configured LDAP groups configured for User-Initiated Enrollment 

Retrieves the configured LDAP groups configured for User-Initiated Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    server_id = 'server_id_example' # str | LDAP server id.
group_id = 'group_id_example' # str | LDAP group id.

    try:
        # Retrieve the configured LDAP groups configured for User-Initiated Enrollment 
        api_response = api_instance.v2_enrollment_access_groups_server_id_group_id_get(server_id, group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_access_groups_server_id_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| LDAP server id. | 
 **group_id** | **str**| LDAP group id. | 

### Return type

[**EnrollmentAccessGroupV2**](EnrollmentAccessGroupV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful query |  -  |
**404** | Group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_access_groups_server_id_group_id_put**
> EnrollmentAccessGroupV2 v2_enrollment_access_groups_server_id_group_id_put(server_id, group_id, enrollment_access_group_v2=enrollment_access_group_v2)

Modify the configured LDAP groups configured for User-Initiated Enrollment 

Modifies the configured LDAP groups configured for User-Initiated Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    server_id = 'server_id_example' # str | LDAP server id.
group_id = 'group_id_example' # str | LDAP group id.
enrollment_access_group_v2 = openapi_client.EnrollmentAccessGroupV2() # EnrollmentAccessGroupV2 |  (optional)

    try:
        # Modify the configured LDAP groups configured for User-Initiated Enrollment 
        api_response = api_instance.v2_enrollment_access_groups_server_id_group_id_put(server_id, group_id, enrollment_access_group_v2=enrollment_access_group_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_access_groups_server_id_group_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| LDAP server id. | 
 **group_id** | **str**| LDAP group id. | 
 **enrollment_access_group_v2** | [**EnrollmentAccessGroupV2**](EnrollmentAccessGroupV2.md)|  | [optional] 

### Return type

[**EnrollmentAccessGroupV2**](EnrollmentAccessGroupV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful query |  -  |
**400** | Bad request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_filtered_language_codes_get**
> list[LanguageCode] v2_enrollment_filtered_language_codes_get()

Retrieve the list of languages and corresponding ISO 639-1 Codes but only those not already added to Enrollment 

Retrieves the list of languages and corresponding ISO 639-1 Codes, but only those not already added to Enrollment.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    
    try:
        # Retrieve the list of languages and corresponding ISO 639-1 Codes but only those not already added to Enrollment 
        api_response = api_instance.v2_enrollment_filtered_language_codes_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_filtered_language_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LanguageCode]**](LanguageCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves the list of languages and corresponding ISO 639-1 Codes, but only those not already added to Enrollment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_get**
> EnrollmentSettingsV2 v2_enrollment_get()

Get Enrollment object and Re-enrollment settings 

Gets Enrollment object and re-enrollment settings. The settings can be altered without providing the existing management password by providing the following value for `managementPassword`: `\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff\\uffff`. 

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    
    try:
        # Get Enrollment object and Re-enrollment settings 
        api_response = api_instance.v2_enrollment_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EnrollmentSettingsV2**](EnrollmentSettingsV2.md)

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

# **v2_enrollment_history_get**
> HistorySearchResults v2_enrollment_history_get(page=page, page_size=page_size, sort=sort)

Get sorted and paged Enrollment history object 

Gets sorted and paged Enrollment history object 

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: `property:asc/desc`. Default sort is `date:desc`. Multiple sort criteria are supported and must be separated with a comma. Example: `sort=date:desc,name:asc`.  (optional) (default to ["date:desc"])

    try:
        # Get sorted and paged Enrollment history object 
        api_response = api_instance.v2_enrollment_history_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: &#x60;property:asc/desc&#x60;. Default sort is &#x60;date:desc&#x60;. Multiple sort criteria are supported and must be separated with a comma. Example: &#x60;sort&#x3D;date:desc,name:asc&#x60;.  | [optional] [default to [&quot;date:desc&quot;]]

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
**200** | Details of enrollment history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_history_post**
> HrefResponse v2_enrollment_history_post(object_history_note)

Add Enrollment history object notes 

Adds Enrollment history object notes 

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add Enrollment history object notes 
        api_response = api_instance.v2_enrollment_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_history_post: %s\n" % e)
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
**201** | Notes of enrollment history were added |  -  |
**503** | Enrollment history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_language_codes_get**
> list[LanguageCode] v2_enrollment_language_codes_get()

Retrieve the list of languages and corresponding ISO 639-1 Codes 

Retrieves the list of languages and corresponding ISO 639-1 Codes.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    
    try:
        # Retrieve the list of languages and corresponding ISO 639-1 Codes 
        api_response = api_instance.v2_enrollment_language_codes_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_language_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LanguageCode]**](LanguageCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of languages and corresponding ISO 639-1 Codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_languages_get**
> ProcessTextsSearchResults v2_enrollment_languages_get(page=page, page_size=page_size, sort=sort)

Get an array of the language codes that have Enrollment messaging 

Returns an array of the language codes that have enrollment messaging currently configured.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["languageCode:asc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is `languageCode:asc`. Multiple sort criteria are supported and must be separated with a comma. Example: `sort=date:desc,name:asc`.  (optional) (default to ["languageCode:asc"])

    try:
        # Get an array of the language codes that have Enrollment messaging 
        api_response = api_instance.v2_enrollment_languages_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_languages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is &#x60;languageCode:asc&#x60;. Multiple sort criteria are supported and must be separated with a comma. Example: &#x60;sort&#x3D;date:desc,name:asc&#x60;.  | [optional] [default to [&quot;languageCode:asc&quot;]]

### Return type

[**ProcessTextsSearchResults**](ProcessTextsSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found languages matching search params. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_languages_language_id_delete**
> v2_enrollment_languages_language_id_delete(language_id)

Delete the Enrollment messaging for a language 

Delete the enrollment messaging for a language.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    language_id = 'language_id_example' # str | Two letter ISO 639-1 Language Code

    try:
        # Delete the Enrollment messaging for a language 
        api_instance.v2_enrollment_languages_language_id_delete(language_id)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_languages_language_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_id** | **str**| Two letter ISO 639-1 Language Code | 

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
**204** | Successful deletetion |  -  |
**404** | Language not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_languages_language_id_get**
> EnrollmentProcessTextObject v2_enrollment_languages_language_id_get(language_id)

Retrieve the Enrollment messaging for a language 

Retrieves the enrollment messaging for a language.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    language_id = 'language_id_example' # str | Two letter ISO 639-1 Language Code

    try:
        # Retrieve the Enrollment messaging for a language 
        api_response = api_instance.v2_enrollment_languages_language_id_get(language_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_languages_language_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_id** | **str**| Two letter ISO 639-1 Language Code | 

### Return type

[**EnrollmentProcessTextObject**](EnrollmentProcessTextObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Language not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_languages_language_id_put**
> EnrollmentProcessTextObject v2_enrollment_languages_language_id_put(language_id, enrollment_process_text_object=enrollment_process_text_object)

Edit Enrollment messaging for a language 

Edit enrollment messaging for a language.

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    language_id = 'language_id_example' # str | Two letter ISO 639-1 Language Code
enrollment_process_text_object = openapi_client.EnrollmentProcessTextObject() # EnrollmentProcessTextObject |  (optional)

    try:
        # Edit Enrollment messaging for a language 
        api_response = api_instance.v2_enrollment_languages_language_id_put(language_id, enrollment_process_text_object=enrollment_process_text_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_languages_language_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_id** | **str**| Two letter ISO 639-1 Language Code | 
 **enrollment_process_text_object** | [**EnrollmentProcessTextObject**](EnrollmentProcessTextObject.md)|  | [optional] 

### Return type

[**EnrollmentProcessTextObject**](EnrollmentProcessTextObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_enrollment_put**
> EnrollmentSettingsV2 v2_enrollment_put(enrollment_settings_v2)

Update Enrollment object 

Update enrollment object. Regarding the `developerCertificateIdentity`, if this object is omitted, the certificate will not be deleted from Jamf Pro. The `identityKeystore` is the entire cert file as a base64 encoded string. The `md5Sum` field is not required in the PUT request, but is calculated and returned in the response. 

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
    api_instance = openapi_client.EnrollmentApi(api_client)
    enrollment_settings_v2 = openapi_client.EnrollmentSettingsV2() # EnrollmentSettingsV2 | Update enrollment

    try:
        # Update Enrollment object 
        api_response = api_instance.v2_enrollment_put(enrollment_settings_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EnrollmentApi->v2_enrollment_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_settings_v2** | [**EnrollmentSettingsV2**](EnrollmentSettingsV2.md)| Update enrollment | 

### Return type

[**EnrollmentSettingsV2**](EnrollmentSettingsV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated enrollment object |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

