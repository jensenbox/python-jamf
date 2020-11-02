# jamf.TomcatSettingsPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_issue_tomcat_ssl_certificate_post**](TomcatSettingsPreviewApi.md#settings_issue_tomcat_ssl_certificate_post) | **POST** /settings/issueTomcatSslCertificate | Generate a SSL Certificate using Jamf Certificate Authority 


# **settings_issue_tomcat_ssl_certificate_post**
> settings_issue_tomcat_ssl_certificate_post()

Generate a SSL Certificate using Jamf Certificate Authority 

generate a SSL Certificate using Jamf Certificate Authority

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
    api_instance = jamf.TomcatSettingsPreviewApi(api_client)
    
    try:
        # Generate a SSL Certificate using Jamf Certificate Authority 
        api_instance.settings_issue_tomcat_ssl_certificate_post()
    except ApiException as e:
        print("Exception when calling TomcatSettingsPreviewApi->settings_issue_tomcat_ssl_certificate_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**204** | SSL certificate created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

