# openapi_client.SsoCertificateApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_sso_cert_delete**](SsoCertificateApi.md#v2_sso_cert_delete) | **DELETE** /v2/sso/cert | Delete the currently configured certificate used by SSO 
[**v2_sso_cert_download_get**](SsoCertificateApi.md#v2_sso_cert_download_get) | **GET** /v2/sso/cert/download | Download the certificate currently configured for use with Jamf Pro&#39;s SSO configuration 
[**v2_sso_cert_get**](SsoCertificateApi.md#v2_sso_cert_get) | **GET** /v2/sso/cert | Retrieve the certificate currently configured for use with SSO 
[**v2_sso_cert_parse_post**](SsoCertificateApi.md#v2_sso_cert_parse_post) | **POST** /v2/sso/cert/parse | Parse the certificate to get details about certificate type and keys needed to upload certificate file 
[**v2_sso_cert_post**](SsoCertificateApi.md#v2_sso_cert_post) | **POST** /v2/sso/cert | Jamf Pro will generate a new certificate and use it to sign SSO 
[**v2_sso_cert_put**](SsoCertificateApi.md#v2_sso_cert_put) | **PUT** /v2/sso/cert | Update the certificate used by Jamf Pro to sign SSO requests to the identify provider 


# **v2_sso_cert_delete**
> v2_sso_cert_delete()

Delete the currently configured certificate used by SSO 

Deletes the currently configured certificate used by SSO.

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
    api_instance = openapi_client.SsoCertificateApi(api_client)
    
    try:
        # Delete the currently configured certificate used by SSO 
        api_instance.v2_sso_cert_delete()
    except ApiException as e:
        print("Exception when calling SsoCertificateApi->v2_sso_cert_delete: %s\n" % e)
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
**204** | Operation successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_sso_cert_download_get**
> file v2_sso_cert_download_get()

Download the certificate currently configured for use with Jamf Pro's SSO configuration 

Downloads the certificate currently configured for use with Jamf Pro's SSO configuration

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
    api_instance = openapi_client.SsoCertificateApi(api_client)
    
    try:
        # Download the certificate currently configured for use with Jamf Pro's SSO configuration 
        api_response = api_instance.v2_sso_cert_download_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoCertificateApi->v2_sso_cert_download_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_sso_cert_get**
> SsoKeystoreResponseWithDetails v2_sso_cert_get()

Retrieve the certificate currently configured for use with SSO 

Retrieves the certificate currently configured for use with SSO.

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
    api_instance = openapi_client.SsoCertificateApi(api_client)
    
    try:
        # Retrieve the certificate currently configured for use with SSO 
        api_response = api_instance.v2_sso_cert_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoCertificateApi->v2_sso_cert_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SsoKeystoreResponseWithDetails**](SsoKeystoreResponseWithDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_sso_cert_parse_post**
> SsoKeystoreCertParseResponse v2_sso_cert_parse_post(sso_keystore_parse)

Parse the certificate to get details about certificate type and keys needed to upload certificate file 

Parse the certificate to get details about certificate type and keys needed to upload certificate file.

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
    api_instance = openapi_client.SsoCertificateApi(api_client)
    sso_keystore_parse = openapi_client.SsoKeystoreParse() # SsoKeystoreParse | 

    try:
        # Parse the certificate to get details about certificate type and keys needed to upload certificate file 
        api_response = api_instance.v2_sso_cert_parse_post(sso_keystore_parse)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoCertificateApi->v2_sso_cert_parse_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_keystore_parse** | [**SsoKeystoreParse**](SsoKeystoreParse.md)|  | 

### Return type

[**SsoKeystoreCertParseResponse**](SsoKeystoreCertParseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully parsed the certificate. |  -  |
**400** | One or more parameters were invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_sso_cert_post**
> SsoKeystoreResponseWithDetails v2_sso_cert_post()

Jamf Pro will generate a new certificate and use it to sign SSO 

Jamf Pro will generate a new certificate and use it to sign SSO requests to the identity provider.

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
    api_instance = openapi_client.SsoCertificateApi(api_client)
    
    try:
        # Jamf Pro will generate a new certificate and use it to sign SSO 
        api_response = api_instance.v2_sso_cert_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoCertificateApi->v2_sso_cert_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SsoKeystoreResponseWithDetails**](SsoKeystoreResponseWithDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly generated will be set and returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_sso_cert_put**
> SsoKeystoreResponseWithDetails v2_sso_cert_put(sso_keystore)

Update the certificate used by Jamf Pro to sign SSO requests to the identify provider 

Update the certificate used by Jamf Pro to sign SSO requests to the identify provider.

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
    api_instance = openapi_client.SsoCertificateApi(api_client)
    sso_keystore = openapi_client.SsoKeystore() # SsoKeystore | 

    try:
        # Update the certificate used by Jamf Pro to sign SSO requests to the identify provider 
        api_response = api_instance.v2_sso_cert_put(sso_keystore)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SsoCertificateApi->v2_sso_cert_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sso_keystore** | [**SsoKeystore**](SsoKeystore.md)|  | 

### Return type

[**SsoKeystoreResponseWithDetails**](SsoKeystoreResponseWithDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully changed the keystore. |  -  |
**400** | One or more parameters were invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

