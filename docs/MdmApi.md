# openapi_client.MdmApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preview_mdm_renew_profile_udid_post**](MdmApi.md#preview_mdm_renew_profile_udid_post) | **POST** /preview/mdm/renew-profile/{udid} | Renew MDM Profile 


# **preview_mdm_renew_profile_udid_post**
> preview_mdm_renew_profile_udid_post(udid)

Renew MDM Profile 

Renews the device's MDM Profile, including the device identity certificate within the MDM Profile. 

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
    api_instance = openapi_client.MdmApi(api_client)
    udid = 'udid_example' # str | udid of the device

    try:
        # Renew MDM Profile 
        api_instance.preview_mdm_renew_profile_udid_post(udid)
    except ApiException as e:
        print("Exception when calling MdmApi->preview_mdm_renew_profile_udid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **udid** | **str**| udid of the device | 

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
**202** | Renew Profile action was queued with APNs. |  -  |
**403** | Insufficient privileges to perform this action or Renew MDM Profile is not enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

