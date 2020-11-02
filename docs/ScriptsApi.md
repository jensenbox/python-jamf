# openapi_client.ScriptsApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_scripts_get**](ScriptsApi.md#v1_scripts_get) | **GET** /v1/scripts | Search for sorted and paged Scripts 
[**v1_scripts_id_delete**](ScriptsApi.md#v1_scripts_id_delete) | **DELETE** /v1/scripts/{id} | Delete a Script at the specified id 
[**v1_scripts_id_download_get**](ScriptsApi.md#v1_scripts_id_download_get) | **GET** /v1/scripts/{id}/download | Download a text file of the Script contents 
[**v1_scripts_id_get**](ScriptsApi.md#v1_scripts_id_get) | **GET** /v1/scripts/{id} | Retrieve a full script object 
[**v1_scripts_id_history_get**](ScriptsApi.md#v1_scripts_id_history_get) | **GET** /v1/scripts/{id}/history | Get specified Script history object 
[**v1_scripts_id_history_post**](ScriptsApi.md#v1_scripts_id_history_post) | **POST** /v1/scripts/{id}/history | Add specified Script history object notes 
[**v1_scripts_id_put**](ScriptsApi.md#v1_scripts_id_put) | **PUT** /v1/scripts/{id} | Replace the script at the id with the supplied information 
[**v1_scripts_post**](ScriptsApi.md#v1_scripts_post) | **POST** /v1/scripts | Create a Script 


# **v1_scripts_get**
> ScriptsSearchResults v1_scripts_get(page=page, page_size=page_size, sort=sort, filter=filter)

Search for sorted and paged Scripts 

Search for sorted and paged scripts

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
    api_instance = openapi_client.ScriptsApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["name:asc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is name:asc. Multiple sort criteria are supported and must be separated with a comma. Fields allowed in the query: `id`, `name`, `info`, `notes`, `priority`, `categoryId`, `categoryName`, `parameter4` up to `parameter11`, `osRequirements`, `scriptContents`. Example: sort=date:desc,name:asc  (optional) (default to ["name:asc"])
filter = '' # str | Query in the RSQL format, allowing to filter scripts collection. Default search is empty query - returning all results for the requested page. Fields allowed in the query: `id`, `name`, `info`, `notes`, `priority`, `categoryId`, `categoryName`, `parameter4` up to `parameter11`, `osRequirements`, `scriptContents`. This param can be combined with paging and sorting. Example: filter=categoryName==\"Category\" and name==\"*script name*\" (optional) (default to '')

    try:
        # Search for sorted and paged Scripts 
        api_response = api_instance.v1_scripts_get(page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptsApi->v1_scripts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is name:asc. Multiple sort criteria are supported and must be separated with a comma. Fields allowed in the query: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;info&#x60;, &#x60;notes&#x60;, &#x60;priority&#x60;, &#x60;categoryId&#x60;, &#x60;categoryName&#x60;, &#x60;parameter4&#x60; up to &#x60;parameter11&#x60;, &#x60;osRequirements&#x60;, &#x60;scriptContents&#x60;. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;name:asc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter scripts collection. Default search is empty query - returning all results for the requested page. Fields allowed in the query: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;info&#x60;, &#x60;notes&#x60;, &#x60;priority&#x60;, &#x60;categoryId&#x60;, &#x60;categoryName&#x60;, &#x60;parameter4&#x60; up to &#x60;parameter11&#x60;, &#x60;osRequirements&#x60;, &#x60;scriptContents&#x60;. This param can be combined with paging and sorting. Example: filter&#x3D;categoryName&#x3D;&#x3D;\&quot;Category\&quot; and name&#x3D;&#x3D;\&quot;*script name*\&quot; | [optional] [default to &#39;&#39;]

### Return type

[**ScriptsSearchResults**](ScriptsSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found scripts matching search params. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_scripts_id_delete**
> v1_scripts_id_delete(id)

Delete a Script at the specified id 

Deletes a script at the specified id

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
    api_instance = openapi_client.ScriptsApi(api_client)
    id = 'id_example' # str | Script object identifier

    try:
        # Delete a Script at the specified id 
        api_instance.v1_scripts_id_delete(id)
    except ApiException as e:
        print("Exception when calling ScriptsApi->v1_scripts_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Script object identifier | 

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
**204** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_scripts_id_download_get**
> file v1_scripts_id_download_get(id)

Download a text file of the Script contents 

Download a text file of the script contents

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
    api_instance = openapi_client.ScriptsApi(api_client)
    id = 'id_example' # str | id of the script to be downloaded

    try:
        # Download a text file of the Script contents 
        api_response = api_instance.v1_scripts_id_download_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptsApi->v1_scripts_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the script to be downloaded | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The script of the specified id |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_scripts_id_get**
> Script v1_scripts_id_get(id)

Retrieve a full script object 

Retrieves a full script object

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
    api_instance = openapi_client.ScriptsApi(api_client)
    id = 'id_example' # str | Script object identifier

    try:
        # Retrieve a full script object 
        api_response = api_instance.v1_scripts_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptsApi->v1_scripts_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Script object identifier | 

### Return type

[**Script**](Script.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Script with that ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_scripts_id_history_get**
> HistorySearchResults v1_scripts_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)

Get specified Script history object 

Gets specified Script history object 

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
    api_instance = openapi_client.ScriptsApi(api_client)
    id = 'id_example' # str | id of script history record
page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to ["date:desc"])
filter = '' # str | Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter=username!=admin and details==*disabled* and date<2019-12-15 (optional) (default to '')

    try:
        # Get specified Script history object 
        api_response = api_instance.v1_scripts_id_history_get(id, page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptsApi->v1_scripts_id_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of script history record | 
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to [&quot;date:desc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter history notes collection. Default filter is empty query - returning all results for the requested page. Fields allowed in the query: username, date, note, details. This param can be combined with paging and sorting. Example: filter&#x3D;username!&#x3D;admin and details&#x3D;&#x3D;*disabled* and date&lt;2019-12-15 | [optional] [default to &#39;&#39;]

### Return type

[**HistorySearchResults**](HistorySearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Specified script does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_scripts_id_history_post**
> ObjectHistory v1_scripts_id_history_post(id, object_history_note)

Add specified Script history object notes 

Adds specified Script history object notes 

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
    api_instance = openapi_client.ScriptsApi(api_client)
    id = 'id_example' # str | instance id of script history record
object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | history notes to create

    try:
        # Add specified Script history object notes 
        api_response = api_instance.v1_scripts_id_history_post(id, object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptsApi->v1_scripts_id_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of script history record | 
 **object_history_note** | [**ObjectHistoryNote**](ObjectHistoryNote.md)| history notes to create | 

### Return type

[**ObjectHistory**](ObjectHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Notes of script history were added |  -  |
**404** | Specified script does not exist. |  -  |
**503** | Script history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_scripts_id_put**
> Script v1_scripts_id_put(id, script)

Replace the script at the id with the supplied information 

Replaces the script at the id with the supplied information

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
    api_instance = openapi_client.ScriptsApi(api_client)
    id = 'id_example' # str | Script object identifier
script = openapi_client.Script() # Script | new script to upload to existing id. ids defined in this body will be ignored

    try:
        # Replace the script at the id with the supplied information 
        api_response = api_instance.v1_scripts_id_put(id, script)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptsApi->v1_scripts_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Script object identifier | 
 **script** | [**Script**](Script.md)| new script to upload to existing id. ids defined in this body will be ignored | 

### Return type

[**Script**](Script.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Script at id was updated |  -  |
**404** | Script with that id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_scripts_post**
> HrefResponse v1_scripts_post(script)

Create a Script 

Creates a script

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
    api_instance = openapi_client.ScriptsApi(api_client)
    script = openapi_client.Script() # Script | new script to create. ids defined in this body will be ignored

    try:
        # Create a Script 
        api_response = api_instance.v1_scripts_post(script)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptsApi->v1_scripts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script** | [**Script**](Script.md)| new script to create. ids defined in this body will be ignored | 

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
**201** | Script created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

