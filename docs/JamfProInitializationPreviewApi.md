# jamf.JamfProInitializationPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_initialize_database_connection_post**](JamfProInitializationPreviewApi.md#system_initialize_database_connection_post) | **POST** /system/initialize-database-connection | Provide Database Password during startup 
[**system_initialize_post**](JamfProInitializationPreviewApi.md#system_initialize_post) | **POST** /system/initialize | Set up fresh installed Jamf Pro Server 


# **system_initialize_database_connection_post**
> system_initialize_database_connection_post(database_password)

Provide Database Password during startup 

Provide database password during startup

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
    api_instance = jamf.JamfProInitializationPreviewApi(api_client)
    database_password = jamf.DatabasePassword() # DatabasePassword | 

    try:
        # Provide Database Password during startup 
        api_instance.system_initialize_database_connection_post(database_password)
    except ApiException as e:
        print("Exception when calling JamfProInitializationPreviewApi->system_initialize_database_connection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_password** | [**DatabasePassword**](DatabasePassword.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | Incorrect database password. |  -  |
**403** | Access to this endpoint is forbidden after successful initialization of JamfPro or database password is configured. |  -  |
**429** | Limit of requests per second was exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_initialize_post**
> system_initialize_post(initialize)

Set up fresh installed Jamf Pro Server 

Set up fresh installed Jamf Pro Server 

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
    api_instance = jamf.JamfProInitializationPreviewApi(api_client)
    initialize = jamf.Initialize() # Initialize | 

    try:
        # Set up fresh installed Jamf Pro Server 
        api_instance.system_initialize_post(initialize)
    except ApiException as e:
        print("Exception when calling JamfProInitializationPreviewApi->system_initialize_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initialize** | [**Initialize**](Initialize.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | The following are codes returned by this call: INVALID_ACTIVATION_CODE - activation code provided is not valid or is expired INVALID_STATE - The system is in an invalid state to be initialized. FIELD_REQUIRED - A required field was not provided.  The field name will be provided on the response.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

