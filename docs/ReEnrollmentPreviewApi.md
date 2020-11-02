# jamf.ReEnrollmentPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_reenrollment_get**](ReEnrollmentPreviewApi.md#v1_reenrollment_get) | **GET** /v1/reenrollment | Get Re-enrollment object 
[**v1_reenrollment_history_get**](ReEnrollmentPreviewApi.md#v1_reenrollment_history_get) | **GET** /v1/reenrollment/history | Get Re-enrollment history object 
[**v1_reenrollment_history_post**](ReEnrollmentPreviewApi.md#v1_reenrollment_history_post) | **POST** /v1/reenrollment/history | Add specified Re-enrollment history object notes 
[**v1_reenrollment_put**](ReEnrollmentPreviewApi.md#v1_reenrollment_put) | **PUT** /v1/reenrollment | Update the Re-enrollment object 


# **v1_reenrollment_get**
> Reenrollment v1_reenrollment_get()

Get Re-enrollment object 

Gets Re-enrollment object 

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
    api_instance = jamf.ReEnrollmentPreviewApi(api_client)
    
    try:
        # Get Re-enrollment object 
        api_response = api_instance.v1_reenrollment_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReEnrollmentPreviewApi->v1_reenrollment_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Reenrollment**](Reenrollment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Re-enrollment object were found |  -  |
**404** | Re-enrollment object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_reenrollment_history_get**
> HistorySearchResults v1_reenrollment_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get Re-enrollment history object 

Gets Re-enrollment history object 

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
    api_instance = jamf.ReEnrollmentPreviewApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'date:desc' # str | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'date:desc')

    try:
        # Get Re-enrollment history object 
        api_response = api_instance.v1_reenrollment_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReEnrollmentPreviewApi->v1_reenrollment_history_get: %s\n" % e)
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
**200** | Details of re-enrollment history were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_reenrollment_history_post**
> ObjectHistory v1_reenrollment_history_post(object_history_note)

Add specified Re-enrollment history object notes 

Adds specified Re-enrollment history object notes 

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
    api_instance = jamf.ReEnrollmentPreviewApi(api_client)
    object_history_note = jamf.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add specified Re-enrollment history object notes 
        api_response = api_instance.v1_reenrollment_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReEnrollmentPreviewApi->v1_reenrollment_history_post: %s\n" % e)
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
**201** | Notes of re-enrollment history were added |  -  |
**503** | Re-enrollment history can not be saved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_reenrollment_put**
> Reenrollment v1_reenrollment_put(reenrollment)

Update the Re-enrollment object 

Update the Re-enrollment object 

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
    api_instance = jamf.ReEnrollmentPreviewApi(api_client)
    reenrollment = jamf.Reenrollment() # Reenrollment | Re-enrollment object to update

    try:
        # Update the Re-enrollment object 
        api_response = api_instance.v1_reenrollment_put(reenrollment)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReEnrollmentPreviewApi->v1_reenrollment_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reenrollment** | [**Reenrollment**](Reenrollment.md)| Re-enrollment object to update | 

### Return type

[**Reenrollment**](Reenrollment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Re-enrollment record was updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

