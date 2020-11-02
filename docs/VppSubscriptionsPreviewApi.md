# jamf.VppSubscriptionsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vpp_subscriptions_get**](VppSubscriptionsPreviewApi.md#vpp_subscriptions_get) | **GET** /vpp/subscriptions | Found all VPP - subscriptions 
[**vpp_subscriptions_id_get**](VppSubscriptionsPreviewApi.md#vpp_subscriptions_id_get) | **GET** /vpp/subscriptions/{id} | Found VPP subscription by id 


# **vpp_subscriptions_get**
> list[VppTokenSubscription] vpp_subscriptions_get()

Found all VPP - subscriptions 

Found all vpp - subscriptions. 

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
    api_instance = jamf.VppSubscriptionsPreviewApi(api_client)
    
    try:
        # Found all VPP - subscriptions 
        api_response = api_instance.vpp_subscriptions_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VppSubscriptionsPreviewApi->vpp_subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VppTokenSubscription]**](VppTokenSubscription.md)

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

# **vpp_subscriptions_id_get**
> VppTokenSubscription vpp_subscriptions_id_get(id)

Found VPP subscription by id 

Found vpp subscription by id. 

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
    api_instance = jamf.VppSubscriptionsPreviewApi(api_client)
    id = 56 # int | id of vpp subscription to be retrieved

    try:
        # Found VPP subscription by id 
        api_response = api_instance.vpp_subscriptions_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VppSubscriptionsPreviewApi->vpp_subscriptions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of vpp subscription to be retrieved | 

### Return type

[**VppTokenSubscription**](VppTokenSubscription.md)

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

