# jamf.AppStoreCountryCodesPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_app_store_country_codes_get**](AppStoreCountryCodesPreviewApi.md#v1_app_store_country_codes_get) | **GET** /v1/app-store-country-codes | Return a list of Countries and the associated Codes 


# **v1_app_store_country_codes_get**
> CountryCodes v1_app_store_country_codes_get()

Return a list of Countries and the associated Codes 

Returns a list of countries and the associated codes that can be use for the App Store locale 

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
    api_instance = jamf.AppStoreCountryCodesPreviewApi(api_client)
    
    try:
        # Return a list of Countries and the associated Codes 
        api_response = api_instance.v1_app_store_country_codes_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppStoreCountryCodesPreviewApi->v1_app_store_country_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountryCodes**](CountryCodes.md)

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

