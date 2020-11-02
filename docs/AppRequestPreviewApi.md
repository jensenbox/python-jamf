# openapi_client.AppRequestPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_app_request_form_input_fields_get**](AppRequestPreviewApi.md#v1_app_request_form_input_fields_get) | **GET** /v1/app-request/form-input-fields | Search for Form Input Fields 
[**v1_app_request_form_input_fields_id_delete**](AppRequestPreviewApi.md#v1_app_request_form_input_fields_id_delete) | **DELETE** /v1/app-request/form-input-fields/{id} | Remove specified Form Input Field record 
[**v1_app_request_form_input_fields_id_get**](AppRequestPreviewApi.md#v1_app_request_form_input_fields_id_get) | **GET** /v1/app-request/form-input-fields/{id} | Get specified Form Input Field object 
[**v1_app_request_form_input_fields_id_put**](AppRequestPreviewApi.md#v1_app_request_form_input_fields_id_put) | **PUT** /v1/app-request/form-input-fields/{id} | Update specified Form Input Field object 
[**v1_app_request_form_input_fields_post**](AppRequestPreviewApi.md#v1_app_request_form_input_fields_post) | **POST** /v1/app-request/form-input-fields | Create Form Input Field record 
[**v1_app_request_form_input_fields_put**](AppRequestPreviewApi.md#v1_app_request_form_input_fields_put) | **PUT** /v1/app-request/form-input-fields | Replace all Form Input Fields 
[**v1_app_request_settings_get**](AppRequestPreviewApi.md#v1_app_request_settings_get) | **GET** /v1/app-request/settings | Get Applicastion Request Settings 
[**v1_app_request_settings_put**](AppRequestPreviewApi.md#v1_app_request_settings_put) | **PUT** /v1/app-request/settings | Update Application Request Settings 


# **v1_app_request_form_input_fields_get**
> AppRequestFormInputFieldSearchResults v1_app_request_form_input_fields_get()

Search for Form Input Fields 

Search for form input fields

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
    api_instance = openapi_client.AppRequestPreviewApi(api_client)
    
    try:
        # Search for Form Input Fields 
        api_response = api_instance.v1_app_request_form_input_fields_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppRequestPreviewApi->v1_app_request_form_input_fields_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AppRequestFormInputFieldSearchResults**](AppRequestFormInputFieldSearchResults.md)

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

# **v1_app_request_form_input_fields_id_delete**
> v1_app_request_form_input_fields_id_delete(id)

Remove specified Form Input Field record 

Removes specified form input field record 

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
    api_instance = openapi_client.AppRequestPreviewApi(api_client)
    id = 56 # int | Instance id of form input field record

    try:
        # Remove specified Form Input Field record 
        api_instance.v1_app_request_form_input_fields_id_delete(id)
    except ApiException as e:
        print("Exception when calling AppRequestPreviewApi->v1_app_request_form_input_fields_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id of form input field record | 

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
**204** | form input field record was deleted |  -  |
**404** | Specified form input field object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_app_request_form_input_fields_id_get**
> AppRequestFormInputField v1_app_request_form_input_fields_id_get(id)

Get specified Form Input Field object 

Gets specified form input field object 

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
    api_instance = openapi_client.AppRequestPreviewApi(api_client)
    id = 56 # int | Instance id of form input field record

    try:
        # Get specified Form Input Field object 
        api_response = api_instance.v1_app_request_form_input_fields_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppRequestPreviewApi->v1_app_request_form_input_fields_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id of form input field record | 

### Return type

[**AppRequestFormInputField**](AppRequestFormInputField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of form input field were found |  -  |
**404** | Specified form input field object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_app_request_form_input_fields_id_put**
> AppRequestFormInputField v1_app_request_form_input_fields_id_put(id, app_request_form_input_field)

Update specified Form Input Field object 

Update specified form input field object 

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
    api_instance = openapi_client.AppRequestPreviewApi(api_client)
    id = 56 # int | Instance id of form input field record
app_request_form_input_field = openapi_client.AppRequestFormInputField() # AppRequestFormInputField | form input field object to create. ids defined in this body will be ignored

    try:
        # Update specified Form Input Field object 
        api_response = api_instance.v1_app_request_form_input_fields_id_put(id, app_request_form_input_field)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppRequestPreviewApi->v1_app_request_form_input_fields_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id of form input field record | 
 **app_request_form_input_field** | [**AppRequestFormInputField**](AppRequestFormInputField.md)| form input field object to create. ids defined in this body will be ignored | 

### Return type

[**AppRequestFormInputField**](AppRequestFormInputField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | form input field update |  -  |
**400** | Invalid data response |  -  |
**404** | Specified form input field object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_app_request_form_input_fields_post**
> AppRequestFormInputField v1_app_request_form_input_fields_post(app_request_form_input_field)

Create Form Input Field record 

Create form input field record 

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
    api_instance = openapi_client.AppRequestPreviewApi(api_client)
    app_request_form_input_field = openapi_client.AppRequestFormInputField() # AppRequestFormInputField | form input field object to create. ids defined in this body will be ignored

    try:
        # Create Form Input Field record 
        api_response = api_instance.v1_app_request_form_input_fields_post(app_request_form_input_field)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppRequestPreviewApi->v1_app_request_form_input_fields_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_request_form_input_field** | [**AppRequestFormInputField**](AppRequestFormInputField.md)| form input field object to create. ids defined in this body will be ignored | 

### Return type

[**AppRequestFormInputField**](AppRequestFormInputField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | form input field record was created |  -  |
**400** | Invalid data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_app_request_form_input_fields_put**
> list[AppRequestFormInputField] v1_app_request_form_input_fields_put(app_request_form_input_field)

Replace all Form Input Fields 

Replace all form input fields. Will delete, update, and create all input fields accordingly. 

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
    api_instance = openapi_client.AppRequestPreviewApi(api_client)
    app_request_form_input_field = [openapi_client.AppRequestFormInputField()] # list[AppRequestFormInputField] | list of form input fields to replace all existing fields. Will delete, update, and create all input fields accordingly.

    try:
        # Replace all Form Input Fields 
        api_response = api_instance.v1_app_request_form_input_fields_put(app_request_form_input_field)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppRequestPreviewApi->v1_app_request_form_input_fields_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_request_form_input_field** | [**list[AppRequestFormInputField]**](AppRequestFormInputField.md)| list of form input fields to replace all existing fields. Will delete, update, and create all input fields accordingly. | 

### Return type

[**list[AppRequestFormInputField]**](AppRequestFormInputField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | form input fields were replaced |  -  |
**400** | Invalid data response |  -  |
**404** | Specified form input field object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_app_request_settings_get**
> AppRequestSettings v1_app_request_settings_get()

Get Applicastion Request Settings 

Get app request settings 

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
    api_instance = openapi_client.AppRequestPreviewApi(api_client)
    
    try:
        # Get Applicastion Request Settings 
        api_response = api_instance.v1_app_request_settings_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppRequestPreviewApi->v1_app_request_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AppRequestSettings**](AppRequestSettings.md)

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

# **v1_app_request_settings_put**
> AppRequestSettings v1_app_request_settings_put(app_request_settings)

Update Application Request Settings 

Update app request settings 

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
    api_instance = openapi_client.AppRequestPreviewApi(api_client)
    app_request_settings = openapi_client.AppRequestSettings() # AppRequestSettings | App request settings object

    try:
        # Update Application Request Settings 
        api_response = api_instance.v1_app_request_settings_put(app_request_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppRequestPreviewApi->v1_app_request_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_request_settings** | [**AppRequestSettings**](AppRequestSettings.md)| App request settings object | 

### Return type

[**AppRequestSettings**](AppRequestSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App request settings updated |  -  |
**400** | Invalid data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

