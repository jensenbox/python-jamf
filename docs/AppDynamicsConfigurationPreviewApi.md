# jamf.AppDynamicsConfigurationPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_app_dynamics_script_configuration_get**](AppDynamicsConfigurationPreviewApi.md#v1_app_dynamics_script_configuration_get) | **GET** /v1/app-dynamics/script-configuration | Get Application Dynamics Config object 


# **v1_app_dynamics_script_configuration_get**
> AppDynamicsConfig v1_app_dynamics_script_configuration_get()

Get Application Dynamics Config object 

Gets `AppDynamicsConfig` object. Details for using the response as script configuration are available in the official documentation - https://docs.appdynamics.com/display/PRO45/Configure+the+JavaScript+Agent 

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
    api_instance = jamf.AppDynamicsConfigurationPreviewApi(api_client)
    
    try:
        # Get Application Dynamics Config object 
        api_response = api_instance.v1_app_dynamics_script_configuration_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppDynamicsConfigurationPreviewApi->v1_app_dynamics_script_configuration_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AppDynamicsConfig**](AppDynamicsConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | AppDynamics script configuration may be obtained only when AppDynamics monitoring tool is enabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

