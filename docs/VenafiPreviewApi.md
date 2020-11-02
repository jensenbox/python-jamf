# openapi_client.VenafiPreviewApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_pki_venafi_id_connection_status_get**](VenafiPreviewApi.md#v1_pki_venafi_id_connection_status_get) | **GET** /v1/pki/venafi/{id}/connection-status | Tests the communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
[**v1_pki_venafi_id_get**](VenafiPreviewApi.md#v1_pki_venafi_id_get) | **GET** /v1/pki/venafi/{id} | Retrieve a Venafi PKI configuration from Jamf Pro 
[**v1_pki_venafi_id_jamf_public_key_get**](VenafiPreviewApi.md#v1_pki_venafi_id_jamf_public_key_get) | **GET** /v1/pki/venafi/{id}/jamf-public-key | Downloads a certificate used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
[**v1_pki_venafi_id_jamf_public_key_regenerate_post**](VenafiPreviewApi.md#v1_pki_venafi_id_jamf_public_key_regenerate_post) | **POST** /v1/pki/venafi/{id}/jamf-public-key/regenerate | Regenerates a certificate used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
[**v1_pki_venafi_id_patch**](VenafiPreviewApi.md#v1_pki_venafi_id_patch) | **PATCH** /v1/pki/venafi/{id} | Update a Venafi PKI configuration in Jamf Pro 
[**v1_pki_venafi_id_proxy_trust_store_delete**](VenafiPreviewApi.md#v1_pki_venafi_id_proxy_trust_store_delete) | **DELETE** /v1/pki/venafi/{id}/proxy-trust-store | Removes the PKI Proxy Server public key used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
[**v1_pki_venafi_id_proxy_trust_store_get**](VenafiPreviewApi.md#v1_pki_venafi_id_proxy_trust_store_get) | **GET** /v1/pki/venafi/{id}/proxy-trust-store | Downloads the PKI Proxy Server public key to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
[**v1_pki_venafi_id_proxy_trust_store_post**](VenafiPreviewApi.md#v1_pki_venafi_id_proxy_trust_store_post) | **POST** /v1/pki/venafi/{id}/proxy-trust-store | Uploads the PKI Proxy Server public key to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
[**v1_pki_venafi_post**](VenafiPreviewApi.md#v1_pki_venafi_post) | **POST** /v1/pki/venafi | Create a PKI configuration in Jamf Pro for Venafi 


# **v1_pki_venafi_id_connection_status_get**
> VenafiServiceStatus v1_pki_venafi_id_connection_status_get(id)

Tests the communication between Jamf Pro and a Jamf Pro PKI Proxy Server 

Tests the communication between Jamf Pro and a Jamf Pro PKI Proxy Server 

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
    api_instance = openapi_client.VenafiPreviewApi(api_client)
    id = 'id_example' # str | ID of the Venafi configuration

    try:
        # Tests the communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
        api_response = api_instance.v1_pki_venafi_id_connection_status_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VenafiPreviewApi->v1_pki_venafi_id_connection_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Venafi configuration | 

### Return type

[**VenafiServiceStatus**](VenafiServiceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully connected to Venafi |  -  |
**503** | Why we failed to connect |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pki_venafi_id_get**
> VenafiCaRecord v1_pki_venafi_id_get(id)

Retrieve a Venafi PKI configuration from Jamf Pro 

Retrieve a Venafi PKI configuration from Jamf Pro 

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
    api_instance = openapi_client.VenafiPreviewApi(api_client)
    id = 'id_example' # str | ID of the Venafi configuration

    try:
        # Retrieve a Venafi PKI configuration from Jamf Pro 
        api_response = api_instance.v1_pki_venafi_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VenafiPreviewApi->v1_pki_venafi_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Venafi configuration | 

### Return type

[**VenafiCaRecord**](VenafiCaRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response returns a Venafi PKI configuration |  -  |
**404** | Certificate Authority not found for Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pki_venafi_id_jamf_public_key_get**
> file v1_pki_venafi_id_jamf_public_key_get(id)

Downloads a certificate used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 

Downloads a certificate for an existing Venafi configuration that can be used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 

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
    api_instance = openapi_client.VenafiPreviewApi(api_client)
    id = 'id_example' # str | ID of the Venafi configuration

    try:
        # Downloads a certificate used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
        api_response = api_instance.v1_pki_venafi_id_jamf_public_key_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VenafiPreviewApi->v1_pki_venafi_id_jamf_public_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Venafi configuration | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pem-certificate-chain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response downloads the certificate |  -  |
**400** | Keystore not found for Certificate Authority |  -  |
**404** | Certificate not found for Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pki_venafi_id_jamf_public_key_regenerate_post**
> v1_pki_venafi_id_jamf_public_key_regenerate_post(id)

Regenerates a certificate used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 

Regenerates a certificate for an existing Venafi configuration that can be used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 

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
    api_instance = openapi_client.VenafiPreviewApi(api_client)
    id = 'id_example' # str | ID of the Venafi configuration

    try:
        # Regenerates a certificate used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
        api_instance.v1_pki_venafi_id_jamf_public_key_regenerate_post(id)
    except ApiException as e:
        print("Exception when calling VenafiPreviewApi->v1_pki_venafi_id_jamf_public_key_regenerate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Venafi configuration | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response regenerates the certificate |  -  |
**404** | Certificate Authority not found for Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pki_venafi_id_patch**
> VenafiCaRecord v1_pki_venafi_id_patch(id, venafi_ca_record)

Update a Venafi PKI configuration in Jamf Pro 

Update a Venafi PKI configuration in Jamf Pro 

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
    api_instance = openapi_client.VenafiPreviewApi(api_client)
    id = 'id_example' # str | ID of the Venafi configuration
venafi_ca_record = openapi_client.VenafiCaRecord() # VenafiCaRecord | 

    try:
        # Update a Venafi PKI configuration in Jamf Pro 
        api_response = api_instance.v1_pki_venafi_id_patch(id, venafi_ca_record)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VenafiPreviewApi->v1_pki_venafi_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Venafi configuration | 
 **venafi_ca_record** | [**VenafiCaRecord**](VenafiCaRecord.md)|  | 

### Return type

[**VenafiCaRecord**](VenafiCaRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response returns a Venafi PKI configuration |  -  |
**400** | Invalid attributes for Certificate Authority configuration |  -  |
**404** | Certificate Authority not found for Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pki_venafi_id_proxy_trust_store_delete**
> v1_pki_venafi_id_proxy_trust_store_delete(id)

Removes the PKI Proxy Server public key used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 

Removes the uploaded PKI Proxy Server public key to do basic TLS certificate validation between Jamf Pro and a Jamf Pro PKI Proxy Server 

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
    api_instance = openapi_client.VenafiPreviewApi(api_client)
    id = 'id_example' # str | ID of the Venafi configuration

    try:
        # Removes the PKI Proxy Server public key used to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
        api_instance.v1_pki_venafi_id_proxy_trust_store_delete(id)
    except ApiException as e:
        print("Exception when calling VenafiPreviewApi->v1_pki_venafi_id_proxy_trust_store_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Venafi configuration | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful removes public key |  -  |
**404** | Certificate Authority not found for Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pki_venafi_id_proxy_trust_store_get**
> file v1_pki_venafi_id_proxy_trust_store_get(id)

Downloads the PKI Proxy Server public key to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 

Downloads the uploaded PKI Proxy Server public key to do basic TLS certificate validation between Jamf Pro and a Jamf Pro PKI Proxy Server 

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
    api_instance = openapi_client.VenafiPreviewApi(api_client)
    id = 'id_example' # str | ID of the Venafi configuration

    try:
        # Downloads the PKI Proxy Server public key to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
        api_response = api_instance.v1_pki_venafi_id_proxy_trust_store_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VenafiPreviewApi->v1_pki_venafi_id_proxy_trust_store_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Venafi configuration | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pem-certificate-chain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response downloads the certificate |  -  |
**400** | Keystore not found for Certificate Authority |  -  |
**404** | Certificate not found for Certificate Authority |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pki_venafi_id_proxy_trust_store_post**
> v1_pki_venafi_id_proxy_trust_store_post(id, body)

Uploads the PKI Proxy Server public key to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 

Uploads the PKI Proxy Server public key to do basic TLS certificate validation between Jamf Pro and a Jamf Pro PKI Proxy Server 

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
    api_instance = openapi_client.VenafiPreviewApi(api_client)
    id = 'id_example' # str | ID of the Venafi configuration
body = '/path/to/file' # file | 

    try:
        # Uploads the PKI Proxy Server public key to secure communication between Jamf Pro and a Jamf Pro PKI Proxy Server 
        api_instance.v1_pki_venafi_id_proxy_trust_store_post(id, body)
    except ApiException as e:
        print("Exception when calling VenafiPreviewApi->v1_pki_venafi_id_proxy_trust_store_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Venafi configuration | 
 **body** | **file**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/pem-certificate-chain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response replaces or removes public key |  -  |
**400** | Keystore not found for Certificate Authority |  -  |
**404** | Certificate not found for Certificate Authority |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pki_venafi_post**
> HrefResponse v1_pki_venafi_post(venafi_ca_record)

Create a PKI configuration in Jamf Pro for Venafi 

Creates a Venafi PKI configuration in Jamf Pro, which can be used to issue certificates 

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
    api_instance = openapi_client.VenafiPreviewApi(api_client)
    venafi_ca_record = openapi_client.VenafiCaRecord() # VenafiCaRecord | 

    try:
        # Create a PKI configuration in Jamf Pro for Venafi 
        api_response = api_instance.v1_pki_venafi_post(venafi_ca_record)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VenafiPreviewApi->v1_pki_venafi_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **venafi_ca_record** | [**VenafiCaRecord**](VenafiCaRecord.md)|  | 

### Return type

[**HrefResponse**](HrefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response creates a Venafi PKI configuration |  -  |
**400** | Invalid attributes for Certificate Authority configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

