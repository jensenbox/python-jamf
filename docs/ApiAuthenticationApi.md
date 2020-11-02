# jamf.ApiAuthenticationApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_current_post**](ApiAuthenticationApi.md#auth_current_post) | **POST** /auth/current | Get the authorization details associated with the current API token 
[**auth_get**](ApiAuthenticationApi.md#auth_get) | **GET** /auth | Get all the Authorization details associated with the current api 
[**auth_invalidate_token_post**](ApiAuthenticationApi.md#auth_invalidate_token_post) | **POST** /auth/invalidateToken | Invalidate current token 
[**auth_keep_alive_post**](ApiAuthenticationApi.md#auth_keep_alive_post) | **POST** /auth/keepAlive | Invalidate existing token and generates new token 
[**auth_tokens_post**](ApiAuthenticationApi.md#auth_tokens_post) | **POST** /auth/tokens | Create a token based on other authentication details (basic, etc.) 
[**v1_auth_get**](ApiAuthenticationApi.md#v1_auth_get) | **GET** /v1/auth | Get all the Authorization details associated with the current api 
[**v1_auth_invalidate_token_post**](ApiAuthenticationApi.md#v1_auth_invalidate_token_post) | **POST** /v1/auth/invalidate-token | Invalidate current token 
[**v1_auth_keep_alive_post**](ApiAuthenticationApi.md#v1_auth_keep_alive_post) | **POST** /v1/auth/keep-alive | Invalidate existing token and generates new token 
[**v1_auth_token_post**](ApiAuthenticationApi.md#v1_auth_token_post) | **POST** /v1/auth/token | Create a token based on other authentication details (basic, etc.) 


# **auth_current_post**
> CurrentAuthorization auth_current_post()

Get the authorization details associated with the current API token 

Get the authorization details associated with the current API token for the users current site

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
    api_instance = jamf.ApiAuthenticationApi(api_client)
    
    try:
        # Get the authorization details associated with the current API token 
        api_response = api_instance.auth_current_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiAuthenticationApi->auth_current_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentAuthorization**](CurrentAuthorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorization details for users current site. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_get**
> Authorization auth_get()

Get all the Authorization details associated with the current api 

Get all the authorization details associated with the current api token

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
    api_instance = jamf.ApiAuthenticationApi(api_client)
    
    try:
        # Get all the Authorization details associated with the current api 
        api_response = api_instance.auth_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiAuthenticationApi->auth_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current authorization details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_invalidate_token_post**
> auth_invalidate_token_post()

Invalidate current token 

Invalidates current token

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
    api_instance = jamf.ApiAuthenticationApi(api_client)
    
    try:
        # Invalidate current token 
        api_instance.auth_invalidate_token_post()
    except ApiException as e:
        print("Exception when calling ApiAuthenticationApi->auth_invalidate_token_post: %s\n" % e)
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
**204** | token invalidated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_keep_alive_post**
> AuthToken auth_keep_alive_post()

Invalidate existing token and generates new token 

Invalidates existing token and generates new token with extended expiration based on existing token credentials.

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
    api_instance = jamf.ApiAuthenticationApi(api_client)
    
    try:
        # Invalidate existing token and generates new token 
        api_response = api_instance.auth_keep_alive_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiAuthenticationApi->auth_keep_alive_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_tokens_post**
> AuthToken auth_tokens_post()

Create a token based on other authentication details (basic, etc.) 

Create a token based on other authentication details (basic, etc.) 

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
    api_instance = jamf.ApiAuthenticationApi(api_client)
    
    try:
        # Create a token based on other authentication details (basic, etc.) 
        api_response = api_instance.auth_tokens_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiAuthenticationApi->auth_tokens_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New auth token generated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_get**
> AuthorizationV1 v1_auth_get()

Get all the Authorization details associated with the current api 

Get all the authorization details associated with the current api token

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
    api_instance = jamf.ApiAuthenticationApi(api_client)
    
    try:
        # Get all the Authorization details associated with the current api 
        api_response = api_instance.v1_auth_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiAuthenticationApi->v1_auth_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthorizationV1**](AuthorizationV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current authorization details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_invalidate_token_post**
> v1_auth_invalidate_token_post()

Invalidate current token 

Invalidates current token

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
    api_instance = jamf.ApiAuthenticationApi(api_client)
    
    try:
        # Invalidate current token 
        api_instance.v1_auth_invalidate_token_post()
    except ApiException as e:
        print("Exception when calling ApiAuthenticationApi->v1_auth_invalidate_token_post: %s\n" % e)
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
**204** | token invalidated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_keep_alive_post**
> AuthTokenV1 v1_auth_keep_alive_post()

Invalidate existing token and generates new token 

Invalidates existing token and generates new token with extended expiration based on existing token credentials.

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
    api_instance = jamf.ApiAuthenticationApi(api_client)
    
    try:
        # Invalidate existing token and generates new token 
        api_response = api_instance.v1_auth_keep_alive_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiAuthenticationApi->v1_auth_keep_alive_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthTokenV1**](AuthTokenV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_token_post**
> AuthTokenV1 v1_auth_token_post()

Create a token based on other authentication details (basic, etc.) 

Create a token based on other authentication details (basic, etc.) 

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
    api_instance = jamf.ApiAuthenticationApi(api_client)
    
    try:
        # Create a token based on other authentication details (basic, etc.) 
        api_response = api_instance.v1_auth_token_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiAuthenticationApi->v1_auth_token_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthTokenV1**](AuthTokenV1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New auth token generated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

