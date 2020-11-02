# openapi_client.InventoryInformationPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_inventory_information_get**](InventoryInformationPreviewApi.md#v1_inventory_information_get) | **GET** /v1/inventory-information | Get statistics about managed/unmanaged devices and computers in the inventory 


# **v1_inventory_information_get**
> InventoryInformation v1_inventory_information_get()

Get statistics about managed/unmanaged devices and computers in the inventory 

Gets statistics about managed/unmanaged devices and computers in the inventory. 

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
    api_instance = openapi_client.InventoryInformationPreviewApi(api_client)
    
    try:
        # Get statistics about managed/unmanaged devices and computers in the inventory 
        api_response = api_instance.v1_inventory_information_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryInformationPreviewApi->v1_inventory_information_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InventoryInformation**](InventoryInformation.md)

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

