# jamf.SitesPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_sites_get**](SitesPreviewApi.md#settings_sites_get) | **GET** /settings/sites | Find all sites 


# **settings_sites_get**
> list[Site] settings_sites_get()

Find all sites 

Found all sites. 

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
    api_instance = jamf.SitesPreviewApi(api_client)
    
    try:
        # Find all sites 
        api_response = api_instance.settings_sites_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SitesPreviewApi->settings_sites_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Site]**](Site.md)

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

