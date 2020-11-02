# jamf.MobileDevicesApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_mobile_devices_get**](MobileDevicesApi.md#v1_mobile_devices_get) | **GET** /v1/mobile-devices | Get Mobile Device objects 
[**v1_mobile_devices_id_detail_get**](MobileDevicesApi.md#v1_mobile_devices_id_detail_get) | **GET** /v1/mobile-devices/{id}/detail | Get Mobile Device 
[**v1_mobile_devices_id_get**](MobileDevicesApi.md#v1_mobile_devices_id_get) | **GET** /v1/mobile-devices/{id} | Get Mobile Device 
[**v1_mobile_devices_id_patch**](MobileDevicesApi.md#v1_mobile_devices_id_patch) | **PATCH** /v1/mobile-devices/{id} | Update fields on a mobile device that are allowed to be modified by users 
[**v1_search_mobile_devices_post**](MobileDevicesApi.md#v1_search_mobile_devices_post) | **POST** /v1/search-mobile-devices | Search Mobile Devices 
[**v2_mobile_devices_get**](MobileDevicesApi.md#v2_mobile_devices_get) | **GET** /v2/mobile-devices | Get Mobile Device objects 
[**v2_mobile_devices_id_detail_get**](MobileDevicesApi.md#v2_mobile_devices_id_detail_get) | **GET** /v2/mobile-devices/{id}/detail | Get Mobile Device 
[**v2_mobile_devices_id_get**](MobileDevicesApi.md#v2_mobile_devices_id_get) | **GET** /v2/mobile-devices/{id} | Get Mobile Device 
[**v2_mobile_devices_id_patch**](MobileDevicesApi.md#v2_mobile_devices_id_patch) | **PATCH** /v2/mobile-devices/{id} | Update fields on a mobile device that are allowed to be modified by users 


# **v1_mobile_devices_get**
> list[MobileDevice] v1_mobile_devices_get()

Get Mobile Device objects 

Gets Mobile Device objects. 

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
    api_instance = jamf.MobileDevicesApi(api_client)
    
    try:
        # Get Mobile Device objects 
        api_response = api_instance.v1_mobile_devices_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDevicesApi->v1_mobile_devices_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MobileDevice]**](MobileDevice.md)

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

# **v1_mobile_devices_id_detail_get**
> MobileDeviceDetails v1_mobile_devices_id_detail_get(id)

Get Mobile Device 

Get MobileDevice

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
    api_instance = jamf.MobileDevicesApi(api_client)
    id = 56 # int | instance id of mobile device record

    try:
        # Get Mobile Device 
        api_response = api_instance.v1_mobile_devices_id_detail_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDevicesApi->v1_mobile_devices_id_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| instance id of mobile device record | 

### Return type

[**MobileDeviceDetails**](MobileDeviceDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_mobile_devices_id_get**
> MobileDevice v1_mobile_devices_id_get(id)

Get Mobile Device 

Get MobileDevice

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
    api_instance = jamf.MobileDevicesApi(api_client)
    id = 56 # int | instance id of mobile device record

    try:
        # Get Mobile Device 
        api_response = api_instance.v1_mobile_devices_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDevicesApi->v1_mobile_devices_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| instance id of mobile device record | 

### Return type

[**MobileDevice**](MobileDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_mobile_devices_id_patch**
> MobileDeviceDetails v1_mobile_devices_id_patch(id, update_mobile_device)

Update fields on a mobile device that are allowed to be modified by users 

Updates fields on a mobile device that are allowed to be modified by users.

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
    api_instance = jamf.MobileDevicesApi(api_client)
    id = 56 # int | instance id of mobile device record
update_mobile_device = jamf.UpdateMobileDevice() # UpdateMobileDevice | 

    try:
        # Update fields on a mobile device that are allowed to be modified by users 
        api_response = api_instance.v1_mobile_devices_id_patch(id, update_mobile_device)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDevicesApi->v1_mobile_devices_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| instance id of mobile device record | 
 **update_mobile_device** | [**UpdateMobileDevice**](UpdateMobileDevice.md)|  | 

### Return type

[**MobileDeviceDetails**](MobileDeviceDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_search_mobile_devices_post**
> MobileDeviceSearchResults v1_search_mobile_devices_post(mobile_device_search_params=mobile_device_search_params)

Search Mobile Devices 

Search Mobile Devices

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
    api_instance = jamf.MobileDevicesApi(api_client)
    mobile_device_search_params = jamf.MobileDeviceSearchParams() # MobileDeviceSearchParams |  (optional)

    try:
        # Search Mobile Devices 
        api_response = api_instance.v1_search_mobile_devices_post(mobile_device_search_params=mobile_device_search_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDevicesApi->v1_search_mobile_devices_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_device_search_params** | [**MobileDeviceSearchParams**](MobileDeviceSearchParams.md)|  | [optional] 

### Return type

[**MobileDeviceSearchResults**](MobileDeviceSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found buildings matching search params. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_mobile_devices_get**
> MobileDeviceSearchResultsV2 v2_mobile_devices_get(page=page, page_size=page_size, sort=sort)

Get Mobile Device objects 

Gets Mobile Device objects. 

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
    api_instance = jamf.MobileDevicesApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:asc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["id:asc"])

    try:
        # Get Mobile Device objects 
        api_response = api_instance.v2_mobile_devices_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDevicesApi->v2_mobile_devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;id:asc&quot;]]

### Return type

[**MobileDeviceSearchResultsV2**](MobileDeviceSearchResultsV2.md)

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

# **v2_mobile_devices_id_detail_get**
> MobileDeviceDetailsV2 v2_mobile_devices_id_detail_get(id)

Get Mobile Device 

Get MobileDevice

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
    api_instance = jamf.MobileDevicesApi(api_client)
    id = 'id_example' # str | instance id of mobile device record

    try:
        # Get Mobile Device 
        api_response = api_instance.v2_mobile_devices_id_detail_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDevicesApi->v2_mobile_devices_id_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of mobile device record | 

### Return type

[**MobileDeviceDetailsV2**](MobileDeviceDetailsV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful response |  -  |
**404** | Specified mobile device object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_mobile_devices_id_get**
> MobileDeviceV2 v2_mobile_devices_id_get(id)

Get Mobile Device 

Get MobileDevice

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
    api_instance = jamf.MobileDevicesApi(api_client)
    id = 'id_example' # str | instance id of mobile device record

    try:
        # Get Mobile Device 
        api_response = api_instance.v2_mobile_devices_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDevicesApi->v2_mobile_devices_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of mobile device record | 

### Return type

[**MobileDeviceV2**](MobileDeviceV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful response |  -  |
**404** | Specified mobile device object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_mobile_devices_id_patch**
> MobileDeviceDetailsV2 v2_mobile_devices_id_patch(id, update_mobile_device_v2)

Update fields on a mobile device that are allowed to be modified by users 

Updates fields on a mobile device that are allowed to be modified by users.

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
    api_instance = jamf.MobileDevicesApi(api_client)
    id = 'id_example' # str | instance id of mobile device record
update_mobile_device_v2 = jamf.UpdateMobileDeviceV2() # UpdateMobileDeviceV2 | 

    try:
        # Update fields on a mobile device that are allowed to be modified by users 
        api_response = api_instance.v2_mobile_devices_id_patch(id, update_mobile_device_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MobileDevicesApi->v2_mobile_devices_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of mobile device record | 
 **update_mobile_device_v2** | [**UpdateMobileDeviceV2**](UpdateMobileDeviceV2.md)|  | 

### Return type

[**MobileDeviceDetailsV2**](MobileDeviceDetailsV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful response |  -  |
**403** | Account not allowed to modify device |  -  |
**404** | Specified mobile device object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

