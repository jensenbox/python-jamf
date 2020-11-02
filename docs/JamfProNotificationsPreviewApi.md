# jamf.JamfProNotificationsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_alerts_get**](JamfProNotificationsPreviewApi.md#notifications_alerts_get) | **GET** /notifications/alerts | Get Notifications for user and site 
[**notifications_alerts_id_delete**](JamfProNotificationsPreviewApi.md#notifications_alerts_id_delete) | **DELETE** /notifications/alerts/{id} | DEPRECATED - USE \&quot;alerts/{type}/{id}\&quot; INSTEAD. Deletes only Patch Management notifications. 
[**notifications_alerts_type_id_delete**](JamfProNotificationsPreviewApi.md#notifications_alerts_type_id_delete) | **DELETE** /notifications/alerts/{type}/{id} | Delete Notifications 


# **notifications_alerts_get**
> list[Notification] notifications_alerts_get()

Get Notifications for user and site 

Gets notifications for user and site 

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
    api_instance = jamf.JamfProNotificationsPreviewApi(api_client)
    
    try:
        # Get Notifications for user and site 
        api_response = api_instance.notifications_alerts_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JamfProNotificationsPreviewApi->notifications_alerts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Notification]**](Notification.md)

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

# **notifications_alerts_id_delete**
> notifications_alerts_id_delete(id)

DEPRECATED - USE \"alerts/{type}/{id}\" INSTEAD. Deletes only Patch Management notifications. 

DEPRECATED - USE \"alerts/{type}/{id}\" INSTEAD. Deletes only Patch Management notifications. 

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
    api_instance = jamf.JamfProNotificationsPreviewApi(api_client)
    id = 56 # int | instance ID of the notification

    try:
        # DEPRECATED - USE \"alerts/{type}/{id}\" INSTEAD. Deletes only Patch Management notifications. 
        api_instance.notifications_alerts_id_delete(id)
    except ApiException as e:
        print("Exception when calling JamfProNotificationsPreviewApi->notifications_alerts_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| instance ID of the notification | 

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
**204** | Sucessful deletion |  -  |
**403** | User is missing &#39;Dismiss Notifications&#39; privilege |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_alerts_type_id_delete**
> notifications_alerts_type_id_delete(id, type)

Delete Notifications 

Deletes notifications. Options for 'type' are 'PRESTAGE_IMAGING_SECURITY' and 'PATCH_UPDATE'. 

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
    api_instance = jamf.JamfProNotificationsPreviewApi(api_client)
    id = 56 # int | instance ID of the notification
type = 'type_example' # str | type of the notification

    try:
        # Delete Notifications 
        api_instance.notifications_alerts_type_id_delete(id, type)
    except ApiException as e:
        print("Exception when calling JamfProNotificationsPreviewApi->notifications_alerts_type_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| instance ID of the notification | 
 **type** | **str**| type of the notification | 

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
**204** | Sucessful deletion |  -  |
**403** | User is missing &#39;Dismiss Notifications&#39; privilege |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

