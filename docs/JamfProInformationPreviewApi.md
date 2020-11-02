# jamf.JamfProInformationPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_jamf_pro_information_get**](JamfProInformationPreviewApi.md#v1_jamf_pro_information_get) | **GET** /v1/jamf-pro-information | Get basic information about the Jamf Pro Server 


# **v1_jamf_pro_information_get**
> JamfProInformation v1_jamf_pro_information_get()

Get basic information about the Jamf Pro Server 

Preview version of the endpoint. There may still be some breaking changes in the future. 

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
    api_instance = jamf.JamfProInformationPreviewApi(api_client)
    
    try:
        # Get basic information about the Jamf Pro Server 
        api_response = api_instance.v1_jamf_pro_information_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JamfProInformationPreviewApi->v1_jamf_pro_information_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JamfProInformation**](JamfProInformation.md)

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

