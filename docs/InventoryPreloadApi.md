# openapi_client.InventoryPreloadApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_preload_csv_template_get**](InventoryPreloadApi.md#inventory_preload_csv_template_get) | **GET** /inventory-preload/csv-template | Get the Inventory Preload CSV template 
[**inventory_preload_delete**](InventoryPreloadApi.md#inventory_preload_delete) | **DELETE** /inventory-preload | Delete all Inventory Preload records 
[**inventory_preload_get**](InventoryPreloadApi.md#inventory_preload_get) | **GET** /inventory-preload | Return all Inventory Preload records 
[**inventory_preload_history_get**](InventoryPreloadApi.md#inventory_preload_history_get) | **GET** /inventory-preload/history | Get Inventory Preload history entries 
[**inventory_preload_history_notes_post**](InventoryPreloadApi.md#inventory_preload_history_notes_post) | **POST** /inventory-preload/history/notes | Add Inventory Preload history object notes 
[**inventory_preload_id_delete**](InventoryPreloadApi.md#inventory_preload_id_delete) | **DELETE** /inventory-preload/{id} | Delete an Inventory Preload record 
[**inventory_preload_id_get**](InventoryPreloadApi.md#inventory_preload_id_get) | **GET** /inventory-preload/{id} | Get an Inventory Preload record 
[**inventory_preload_id_put**](InventoryPreloadApi.md#inventory_preload_id_put) | **PUT** /inventory-preload/{id} | Update an Inventory Preload record 
[**inventory_preload_post**](InventoryPreloadApi.md#inventory_preload_post) | **POST** /inventory-preload | Create a new Inventory Preload record using JSON or CSV 
[**inventory_preload_validate_csv_post**](InventoryPreloadApi.md#inventory_preload_validate_csv_post) | **POST** /inventory-preload/validate-csv | Validate a given CSV file 
[**v1_inventory_preload_csv_template_get**](InventoryPreloadApi.md#v1_inventory_preload_csv_template_get) | **GET** /v1/inventory-preload/csv-template | Retrieve the Inventory Preload CSV template 
[**v1_inventory_preload_delete**](InventoryPreloadApi.md#v1_inventory_preload_delete) | **DELETE** /v1/inventory-preload | Delete all Inventory Preload records 
[**v1_inventory_preload_get**](InventoryPreloadApi.md#v1_inventory_preload_get) | **GET** /v1/inventory-preload | Return all Inventory Preload records 
[**v1_inventory_preload_history_get**](InventoryPreloadApi.md#v1_inventory_preload_history_get) | **GET** /v1/inventory-preload/history | Get Inventory Preload history entries 
[**v1_inventory_preload_history_post**](InventoryPreloadApi.md#v1_inventory_preload_history_post) | **POST** /v1/inventory-preload/history | Add Inventory Preload history object notes 
[**v1_inventory_preload_id_delete**](InventoryPreloadApi.md#v1_inventory_preload_id_delete) | **DELETE** /v1/inventory-preload/{id} | Delete an Inventory Preload record 
[**v1_inventory_preload_id_get**](InventoryPreloadApi.md#v1_inventory_preload_id_get) | **GET** /v1/inventory-preload/{id} | Get an Inventory Preload record 
[**v1_inventory_preload_id_put**](InventoryPreloadApi.md#v1_inventory_preload_id_put) | **PUT** /v1/inventory-preload/{id} | Update an Inventory Preload record 
[**v1_inventory_preload_post**](InventoryPreloadApi.md#v1_inventory_preload_post) | **POST** /v1/inventory-preload | Create a new Inventory Preload record using JSON or CSV 
[**v1_inventory_preload_validate_csv_post**](InventoryPreloadApi.md#v1_inventory_preload_validate_csv_post) | **POST** /v1/inventory-preload/validate-csv | Validate a given CSV file 
[**v2_inventory_preload_csv_get**](InventoryPreloadApi.md#v2_inventory_preload_csv_get) | **GET** /v2/inventory-preload/csv | Download all Inventory Preload records
[**v2_inventory_preload_csv_post**](InventoryPreloadApi.md#v2_inventory_preload_csv_post) | **POST** /v2/inventory-preload/csv | Create one or more new Inventory Preload records using CSV 
[**v2_inventory_preload_csv_template_get**](InventoryPreloadApi.md#v2_inventory_preload_csv_template_get) | **GET** /v2/inventory-preload/csv-template | Download the Inventory Preload CSV template
[**v2_inventory_preload_csv_validate_post**](InventoryPreloadApi.md#v2_inventory_preload_csv_validate_post) | **POST** /v2/inventory-preload/csv-validate | Validate a given CSV file 
[**v2_inventory_preload_history_get**](InventoryPreloadApi.md#v2_inventory_preload_history_get) | **GET** /v2/inventory-preload/history | Get Inventory Preload history entries 
[**v2_inventory_preload_history_post**](InventoryPreloadApi.md#v2_inventory_preload_history_post) | **POST** /v2/inventory-preload/history | Add Inventory Preload history object notes
[**v2_inventory_preload_records_delete_all_post**](InventoryPreloadApi.md#v2_inventory_preload_records_delete_all_post) | **POST** /v2/inventory-preload/records/delete-all | Delete all Inventory Preload records 
[**v2_inventory_preload_records_get**](InventoryPreloadApi.md#v2_inventory_preload_records_get) | **GET** /v2/inventory-preload/records | Return all Inventory Preload records
[**v2_inventory_preload_records_id_delete**](InventoryPreloadApi.md#v2_inventory_preload_records_id_delete) | **DELETE** /v2/inventory-preload/records/{id} | Delete an Inventory Preload record 
[**v2_inventory_preload_records_id_get**](InventoryPreloadApi.md#v2_inventory_preload_records_id_get) | **GET** /v2/inventory-preload/records/{id} | Get an Inventory Preload record
[**v2_inventory_preload_records_id_put**](InventoryPreloadApi.md#v2_inventory_preload_records_id_put) | **PUT** /v2/inventory-preload/records/{id} | Update an Inventory Preload record
[**v2_inventory_preload_records_post**](InventoryPreloadApi.md#v2_inventory_preload_records_post) | **POST** /v2/inventory-preload/records | Create a new Inventory Preload record using JSON


# **inventory_preload_csv_template_get**
> object inventory_preload_csv_template_get()

Get the Inventory Preload CSV template 

Retrieves the Inventory Preload CSV template.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    
    try:
        # Get the Inventory Preload CSV template 
        api_response = api_instance.inventory_preload_csv_template_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_csv_template_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_preload_delete**
> inventory_preload_delete()

Delete all Inventory Preload records 

Deletes all Inventory Preload records.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    
    try:
        # Delete all Inventory Preload records 
        api_instance.inventory_preload_delete()
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_delete: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_preload_get**
> list[InventoryPreloadRecordSearchResults] inventory_preload_get(page=page, pagesize=pagesize, sort=sort, sort_by=sort_by)

Return all Inventory Preload records 

Returns all Inventory Preload records.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    page = 0 # int |  (optional) (default to 0)
pagesize = 100 # int |  (optional) (default to 100)
sort = 'ASC' # str |  (optional) (default to 'ASC')
sort_by = 'id' # str |  (optional) (default to 'id')

    try:
        # Return all Inventory Preload records 
        api_response = api_instance.inventory_preload_get(page=page, pagesize=pagesize, sort=sort, sort_by=sort_by)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **pagesize** | **int**|  | [optional] [default to 100]
 **sort** | **str**|  | [optional] [default to &#39;ASC&#39;]
 **sort_by** | **str**|  | [optional] [default to &#39;id&#39;]

### Return type

[**list[InventoryPreloadRecordSearchResults]**](InventoryPreloadRecordSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_preload_history_get**
> HistorySearchResults inventory_preload_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get Inventory Preload history entries 

Gets Inventory Preload history entries.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'date:desc' # str | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'date:desc')

    try:
        # Get Inventory Preload history entries 
        api_response = api_instance.inventory_preload_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to &#39;date:desc&#39;]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_preload_history_notes_post**
> ObjectHistory inventory_preload_history_notes_post(object_history_note)

Add Inventory Preload history object notes 

Adds Inventory Preload history object notes.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | History notes to create

    try:
        # Add Inventory Preload history object notes 
        api_response = api_instance.inventory_preload_history_notes_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_history_notes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_history_note** | [**ObjectHistoryNote**](ObjectHistoryNote.md)| History notes to create | 

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
**201** | Notes of Inventory Preload history were added |  -  |
**503** | Inventory Preload history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_preload_id_delete**
> inventory_preload_id_delete(id)

Delete an Inventory Preload record 

Deletes an Inventory Preload record.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    id = 56 # int | Inventory Preload identifier

    try:
        # Delete an Inventory Preload record 
        api_instance.inventory_preload_id_delete(id)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Inventory Preload identifier | 

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
**204** | OK |  -  |
**404** | Inventory Preload record with specified id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_preload_id_get**
> InventoryPreloadRecord inventory_preload_id_get(id)

Get an Inventory Preload record 

Retrieves an Inventory Preload record.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    id = 56 # int | Inventory Preload identifier

    try:
        # Get an Inventory Preload record 
        api_response = api_instance.inventory_preload_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Inventory Preload identifier | 

### Return type

[**InventoryPreloadRecord**](InventoryPreloadRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Inventory Preload record with specified id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_preload_id_put**
> InventoryPreloadRecord inventory_preload_id_put(id, inventory_preload_record)

Update an Inventory Preload record 

Updates an Inventory Preload record.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    id = 56 # int | Inventory Preload identifier
inventory_preload_record = openapi_client.InventoryPreloadRecord() # InventoryPreloadRecord | Inventory Preload record to update

    try:
        # Update an Inventory Preload record 
        api_response = api_instance.inventory_preload_id_put(id, inventory_preload_record)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Inventory Preload identifier | 
 **inventory_preload_record** | [**InventoryPreloadRecord**](InventoryPreloadRecord.md)| Inventory Preload record to update | 

### Return type

[**InventoryPreloadRecord**](InventoryPreloadRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Inventory Preload record with specified id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_preload_post**
> InventoryPreloadRecord inventory_preload_post(inventory_preload_record)

Create a new Inventory Preload record using JSON or CSV 

Create a new Inventory Preload record using JSON or CSV. A CSV template can be downloaded from /api/inventory-preload/csv-template. Serial number and device type are required. All other fields are optional. When a matching serial number exists in the Inventory Preload data, the record will be overwritten with the CSV data. If the CSV file contains a new username and an email address is provided, the new user is created in Jamf Pro. If the CSV file contains an existing username, the following user-related fields are updated in Jamf Pro. Full Name, Email Address, Phone Number, Position. This endpoint does not do full validation of each record in the CSV data. To do full validation, use the /inventory-preload/validate-csv endpoint first. 

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    inventory_preload_record = openapi_client.InventoryPreloadRecord() # InventoryPreloadRecord | Inventory Preload record or records to be created

    try:
        # Create a new Inventory Preload record using JSON or CSV 
        api_response = api_instance.inventory_preload_post(inventory_preload_record)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_preload_record** | [**InventoryPreloadRecord**](InventoryPreloadRecord.md)| Inventory Preload record or records to be created | 

### Return type

[**InventoryPreloadRecord**](InventoryPreloadRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_preload_validate_csv_post**
> InventoryPreloadCsvValidationSuccess inventory_preload_validate_csv_post(body)

Validate a given CSV file 

Validate a given CSV file. Serial number and device type are required. All other fields are optional. A CSV template can be downloaded from /api/inventory-preload/csv-template. 

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    body = None # object | Inventory Preload records to be validated. A CSV template can be downloaded from /api/inventory-preload/csv-template

    try:
        # Validate a given CSV file 
        api_response = api_instance.inventory_preload_validate_csv_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->inventory_preload_validate_csv_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Inventory Preload records to be validated. A CSV template can be downloaded from /api/inventory-preload/csv-template | 

### Return type

[**InventoryPreloadCsvValidationSuccess**](InventoryPreloadCsvValidationSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_csv_template_get**
> object v1_inventory_preload_csv_template_get()

Retrieve the Inventory Preload CSV template 

Retrieves the Inventory Preload CSV template.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    
    try:
        # Retrieve the Inventory Preload CSV template 
        api_response = api_instance.v1_inventory_preload_csv_template_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_csv_template_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_delete**
> v1_inventory_preload_delete()

Delete all Inventory Preload records 

Deletes all Inventory Preload records.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    
    try:
        # Delete all Inventory Preload records 
        api_instance.v1_inventory_preload_delete()
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_delete: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_get**
> InventoryPreloadRecordSearchResults v1_inventory_preload_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Return all Inventory Preload records 

Returns all Inventory Preload records.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'id:asc' # str | Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'id:asc')

    try:
        # Return all Inventory Preload records 
        api_response = api_instance.v1_inventory_preload_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Default sort is id:asc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to &#39;id:asc&#39;]

### Return type

[**InventoryPreloadRecordSearchResults**](InventoryPreloadRecordSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_history_get**
> HistorySearchResults v1_inventory_preload_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)

Get Inventory Preload history entries 

Gets Inventory Preload history entries.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    page = 0 # int |  (optional) (default to 0)
size = 100 # int |  (optional) (default to 100)
pagesize = 100 # int |  (optional) (default to 100)
page_size = 100 # int |  (optional) (default to 100)
sort = 'date:desc' # str | Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort=date:desc,name:asc  (optional) (default to 'date:desc')

    try:
        # Get Inventory Preload history entries 
        api_response = api_instance.v1_inventory_preload_history_get(page=page, size=size, pagesize=pagesize, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 100]
 **pagesize** | **int**|  | [optional] [default to 100]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | **str**| Sorting criteria in the format: property:asc/desc. Default sort is date:desc. Multiple sort criteria are supported and must be separated with a comma. Example: sort&#x3D;date:desc,name:asc  | [optional] [default to &#39;date:desc&#39;]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_history_post**
> ObjectHistory v1_inventory_preload_history_post(object_history_note)

Add Inventory Preload history object notes 

Adds Inventory Preload history object notes.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | History notes to create

    try:
        # Add Inventory Preload history object notes 
        api_response = api_instance.v1_inventory_preload_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_history_note** | [**ObjectHistoryNote**](ObjectHistoryNote.md)| History notes to create | 

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
**201** | Notes of Inventory Preload history were added |  -  |
**503** | Inventory Preload history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_id_delete**
> v1_inventory_preload_id_delete(id)

Delete an Inventory Preload record 

Deletes an Inventory Preload record.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    id = 56 # int | Inventory Preload identifier

    try:
        # Delete an Inventory Preload record 
        api_instance.v1_inventory_preload_id_delete(id)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Inventory Preload identifier | 

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
**204** | OK |  -  |
**404** | Inventory Preload record with specified id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_id_get**
> InventoryPreloadRecord v1_inventory_preload_id_get(id)

Get an Inventory Preload record 

Retrieves an Inventory Preload record.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    id = 56 # int | Inventory Preload identifier

    try:
        # Get an Inventory Preload record 
        api_response = api_instance.v1_inventory_preload_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Inventory Preload identifier | 

### Return type

[**InventoryPreloadRecord**](InventoryPreloadRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Inventory Preload record with specified id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_id_put**
> InventoryPreloadRecord v1_inventory_preload_id_put(id, inventory_preload_record)

Update an Inventory Preload record 

Updates an Inventory Preload record.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    id = 56 # int | Inventory Preload identifier
inventory_preload_record = openapi_client.InventoryPreloadRecord() # InventoryPreloadRecord | Inventory Preload record to update

    try:
        # Update an Inventory Preload record 
        api_response = api_instance.v1_inventory_preload_id_put(id, inventory_preload_record)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Inventory Preload identifier | 
 **inventory_preload_record** | [**InventoryPreloadRecord**](InventoryPreloadRecord.md)| Inventory Preload record to update | 

### Return type

[**InventoryPreloadRecord**](InventoryPreloadRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Inventory Preload record with specified id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_post**
> InventoryPreloadRecord v1_inventory_preload_post(inventory_preload_record)

Create a new Inventory Preload record using JSON or CSV 

Create a new Inventory Preload record using JSON or CSV. A CSV template can be downloaded from /api/inventory-preload/csv-template. Serial number and device type are required. All other fields are optional. When a matching serial number exists in the Inventory Preload data, the record will be overwritten with the CSV data. If the CSV file contains a new username and an email address is provided, the new user is created in Jamf Pro. If the CSV file contains an existing username, the following user-related fields are updated in Jamf Pro. Full Name, Email Address, Phone Number, Position. This endpoint does not do full validation of each record in the CSV data. To do full validation, use the /inventory-preload/validate-csv endpoint first. 

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    inventory_preload_record = openapi_client.InventoryPreloadRecord() # InventoryPreloadRecord | Inventory Preload record or records to be created

    try:
        # Create a new Inventory Preload record using JSON or CSV 
        api_response = api_instance.v1_inventory_preload_post(inventory_preload_record)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_preload_record** | [**InventoryPreloadRecord**](InventoryPreloadRecord.md)| Inventory Preload record or records to be created | 

### Return type

[**InventoryPreloadRecord**](InventoryPreloadRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_inventory_preload_validate_csv_post**
> InventoryPreloadCsvValidationSuccess v1_inventory_preload_validate_csv_post(body)

Validate a given CSV file 

Validate a given CSV file. Serial number and device type are required. All other fields are optional. A CSV template can be downloaded from /api/inventory-preload/csv-template. 

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    body = None # object | Inventory Preload records to be validated. A CSV template can be downloaded from /api/inventory-preload/csv-template

    try:
        # Validate a given CSV file 
        api_response = api_instance.v1_inventory_preload_validate_csv_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v1_inventory_preload_validate_csv_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Inventory Preload records to be validated. A CSV template can be downloaded from /api/inventory-preload/csv-template | 

### Return type

[**InventoryPreloadCsvValidationSuccess**](InventoryPreloadCsvValidationSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_csv_get**
> str v2_inventory_preload_csv_get()

Download all Inventory Preload records

Returns all Inventory Preload records as a CSV file.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    
    try:
        # Download all Inventory Preload records
        api_response = api_instance.v2_inventory_preload_csv_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_csv_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Disposition - A header field named &#x60;Content-Disposition&#x60; is returned with the file name contained in its value, which is always &#x60;inventory-preload-template.csv&#x60;.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_csv_post**
> list[HrefResponse] v2_inventory_preload_csv_post(file)

Create one or more new Inventory Preload records using CSV 

Create one or more new Inventory Preload records using CSV. A CSV template can be downloaded from /v2/inventory-preload/csv-template. Serial number and device type are required. All other fields are optional. When a matching serial number exists in the Inventory Preload data, the record will be overwritten with the CSV data. If the CSV file contains a new username and an email address is provided, the new user is created in Jamf Pro. If the CSV file contains an existing username, the following user-related fields are updated in Jamf Pro. Full Name, Email Address, Phone Number, Position. This endpoint does not do full validation of each record in the CSV data. To do full validation, use the `/v2/inventory-preload/csv-validate` endpoint first. 

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    file = 'file_example' # str | The CSV file to upload

    try:
        # Create one or more new Inventory Preload records using CSV 
        api_response = api_instance.v2_inventory_preload_csv_post(file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_csv_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| The CSV file to upload | 

### Return type

[**list[HrefResponse]**](HrefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_csv_template_get**
> str v2_inventory_preload_csv_template_get()

Download the Inventory Preload CSV template

Retrieves the Inventory Preload CSV file template.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    
    try:
        # Download the Inventory Preload CSV template
        api_response = api_instance.v2_inventory_preload_csv_template_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_csv_template_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Disposition - A header field named &#x60;Content-Disposition&#x60; is returned with the file name contained in its value, which is always &#x60;inventory-preload-template.csv&#x60;.  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_csv_validate_post**
> InventoryPreloadCsvValidationSuccess v2_inventory_preload_csv_validate_post(file)

Validate a given CSV file 

Validate a given CSV file. Serial number and device type are required. All other fields are optional. A CSV template can be downloaded from `/v2/inventory-preload/csv-template`. 

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    file = 'file_example' # str | The CSV file to upload

    try:
        # Validate a given CSV file 
        api_response = api_instance.v2_inventory_preload_csv_validate_post(file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_csv_validate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| The CSV file to upload | 

### Return type

[**InventoryPreloadCsvValidationSuccess**](InventoryPreloadCsvValidationSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_history_get**
> HistorySearchResults v2_inventory_preload_history_get(page=page, page_size=page_size, sort=sort)

Get Inventory Preload history entries 

Gets Inventory Preload history entries.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["date:desc"] # list[str] | Sorting criteria in the format: `property:asc/desc`. Default sort is `date:desc`. Multiple sort criteria are supported and must be separated with a comma.  Example: `sort=date:desc,name:asc`.  (optional) (default to ["date:desc"])

    try:
        # Get Inventory Preload history entries 
        api_response = api_instance.v2_inventory_preload_history_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: &#x60;property:asc/desc&#x60;. Default sort is &#x60;date:desc&#x60;. Multiple sort criteria are supported and must be separated with a comma.  Example: &#x60;sort&#x3D;date:desc,name:asc&#x60;.  | [optional] [default to [&quot;date:desc&quot;]]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_history_post**
> HrefResponse v2_inventory_preload_history_post(object_history_note)

Add Inventory Preload history object notes

Adds Inventory Preload history object notes.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    object_history_note = openapi_client.ObjectHistoryNote() # ObjectHistoryNote | History notes to create

    try:
        # Add Inventory Preload history object notes
        api_response = api_instance.v2_inventory_preload_history_post(object_history_note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_history_note** | [**ObjectHistoryNote**](ObjectHistoryNote.md)| History notes to create | 

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
**201** | Notes of Inventory Preload history were added |  -  |
**503** | Inventory Preload history can not be saved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_records_delete_all_post**
> v2_inventory_preload_records_delete_all_post()

Delete all Inventory Preload records 

Deletes all Inventory Preload records.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    
    try:
        # Delete all Inventory Preload records 
        api_instance.v2_inventory_preload_records_delete_all_post()
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_records_delete_all_post: %s\n" % e)
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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_records_get**
> InventoryPreloadRecordSearchResultsV2 v2_inventory_preload_records_get(page=page, page_size=page_size, sort=sort)

Return all Inventory Preload records

Returns all Inventory Preload records.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:asc"] # list[str] | Sorting criteria in the format: `property:asc/desc`. Default sort is `id:asc`. Multiple sort criteria are supported and must be separated with a comma.  Example: `sort=date:desc,name:asc`.  (optional) (default to ["id:asc"])

    try:
        # Return all Inventory Preload records
        api_response = api_instance.v2_inventory_preload_records_get(page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: &#x60;property:asc/desc&#x60;. Default sort is &#x60;id:asc&#x60;. Multiple sort criteria are supported and must be separated with a comma.  Example: &#x60;sort&#x3D;date:desc,name:asc&#x60;.  | [optional] [default to [&quot;id:asc&quot;]]

### Return type

[**InventoryPreloadRecordSearchResultsV2**](InventoryPreloadRecordSearchResultsV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_records_id_delete**
> v2_inventory_preload_records_id_delete(id)

Delete an Inventory Preload record 

Deletes an Inventory Preload record.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    id = 'id_example' # str | Inventory Preload identifier

    try:
        # Delete an Inventory Preload record 
        api_instance.v2_inventory_preload_records_id_delete(id)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_records_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Inventory Preload identifier | 

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
**204** | OK |  -  |
**404** | Inventory Preload record with specified id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_records_id_get**
> InventoryPreloadRecordV2 v2_inventory_preload_records_id_get(id)

Get an Inventory Preload record

Retrieves an Inventory Preload record.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    id = 'id_example' # str | Inventory Preload identifier

    try:
        # Get an Inventory Preload record
        api_response = api_instance.v2_inventory_preload_records_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_records_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Inventory Preload identifier | 

### Return type

[**InventoryPreloadRecordV2**](InventoryPreloadRecordV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Inventory Preload record with specified id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_records_id_put**
> InventoryPreloadRecordV2 v2_inventory_preload_records_id_put(id, inventory_preload_record_v2)

Update an Inventory Preload record

Updates an Inventory Preload record.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    id = 'id_example' # str | Inventory Preload identifier
inventory_preload_record_v2 = openapi_client.InventoryPreloadRecordV2() # InventoryPreloadRecordV2 | Inventory Preload record to update

    try:
        # Update an Inventory Preload record
        api_response = api_instance.v2_inventory_preload_records_id_put(id, inventory_preload_record_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_records_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Inventory Preload identifier | 
 **inventory_preload_record_v2** | [**InventoryPreloadRecordV2**](InventoryPreloadRecordV2.md)| Inventory Preload record to update | 

### Return type

[**InventoryPreloadRecordV2**](InventoryPreloadRecordV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Inventory Preload record with specified id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_inventory_preload_records_post**
> HrefResponse v2_inventory_preload_records_post(inventory_preload_record_v2)

Create a new Inventory Preload record using JSON

Create a new Inventory Preload record using JSON.

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
    api_instance = openapi_client.InventoryPreloadApi(api_client)
    inventory_preload_record_v2 = openapi_client.InventoryPreloadRecordV2() # InventoryPreloadRecordV2 | Inventory Preload record to be created.

    try:
        # Create a new Inventory Preload record using JSON
        api_response = api_instance.v2_inventory_preload_records_post(inventory_preload_record_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryPreloadApi->v2_inventory_preload_records_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_preload_record_v2** | [**InventoryPreloadRecordV2**](InventoryPreloadRecordV2.md)| Inventory Preload record to be created. | 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

