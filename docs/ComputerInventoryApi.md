# jamf.ComputerInventoryApi

All URIs are relative to *https://tryitout.jamfcloud.com/uapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_computers_inventory_detail_id_get**](ComputerInventoryApi.md#v1_computers_inventory_detail_id_get) | **GET** /v1/computers-inventory-detail/{id} | Return a Computer details with all sections 
[**v1_computers_inventory_detail_id_patch**](ComputerInventoryApi.md#v1_computers_inventory_detail_id_patch) | **PATCH** /v1/computers-inventory-detail/{id} | Return a updated computer instance 
[**v1_computers_inventory_get**](ComputerInventoryApi.md#v1_computers_inventory_get) | **GET** /v1/computers-inventory | Return a Computer Inventory for paginated list of computers 
[**v1_computers_inventory_id_attachments_attachment_id_delete**](ComputerInventoryApi.md#v1_computers_inventory_id_attachments_attachment_id_delete) | **DELETE** /v1/computers-inventory/{id}/attachments/{attachmentId} | Remove attachment 
[**v1_computers_inventory_id_attachments_attachment_id_get**](ComputerInventoryApi.md#v1_computers_inventory_id_attachments_attachment_id_get) | **GET** /v1/computers-inventory/{id}/attachments/{attachmentId} | Download attachment file 
[**v1_computers_inventory_id_attachments_post**](ComputerInventoryApi.md#v1_computers_inventory_id_attachments_post) | **POST** /v1/computers-inventory/{id}/attachments | Upload attachment and assign to computer 
[**v1_computers_inventory_id_delete**](ComputerInventoryApi.md#v1_computers_inventory_id_delete) | **DELETE** /v1/computers-inventory/{id} | Remove specified Computer record 
[**v1_computers_inventory_id_get**](ComputerInventoryApi.md#v1_computers_inventory_id_get) | **GET** /v1/computers-inventory/{id} | Return a Computer General details 


# **v1_computers_inventory_detail_id_get**
> ComputerInventoryResponse v1_computers_inventory_detail_id_get(id)

Return a Computer details with all sections 

Return a Computer details with all sections

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
    api_instance = jamf.ComputerInventoryApi(api_client)
    id = 'id_example' # str | instance id of computer record

    try:
        # Return a Computer details with all sections 
        api_response = api_instance.v1_computers_inventory_detail_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerInventoryApi->v1_computers_inventory_detail_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of computer record | 

### Return type

[**ComputerInventoryResponse**](ComputerInventoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of computer were found |  -  |
**404** | Specified computer object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computers_inventory_detail_id_patch**
> ComputerInventoryResponse v1_computers_inventory_detail_id_patch(id, computer_inventory_update_request)

Return a updated computer instance 

Return a updated computer instance

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
    api_instance = jamf.ComputerInventoryApi(api_client)
    id = 'id_example' # str | instance id of computer record
computer_inventory_update_request = jamf.ComputerInventoryUpdateRequest() # ComputerInventoryUpdateRequest | 

    try:
        # Return a updated computer instance 
        api_response = api_instance.v1_computers_inventory_detail_id_patch(id, computer_inventory_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerInventoryApi->v1_computers_inventory_detail_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of computer record | 
 **computer_inventory_update_request** | [**ComputerInventoryUpdateRequest**](ComputerInventoryUpdateRequest.md)|  | 

### Return type

[**ComputerInventoryResponse**](ComputerInventoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of computer were found |  -  |
**404** | Specified computer object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computers_inventory_get**
> ComputerInventorySearchResults v1_computers_inventory_get(section=section, page=page, page_size=page_size, sort=sort, filter=filter)

Return a Computer Inventory for paginated list of computers 

Return a Computer Inventory for paginated list of computers

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
    api_instance = jamf.ComputerInventoryApi(api_client)
    section = ["GENERAL"] # list[ComputerSection] | section of computer details, if not specified, General section data is returned. Multiple section parameters are supported, e.g. section=GENERAL&section=HARDWARE (optional) (default to ["GENERAL"])
page = 0 # int |  (optional) (default to 0)
page_size = 100 # int |  (optional) (default to 100)
sort = ["id:asc"] # list[str] | Sorting criteria in the format: `property:asc/desc`. Default sort is `general.name:asc`. Multiple sort criteria are supported and must be separated with a comma.  Fields allowed in the sort: `general.name`, `udid`, `id`, `general.assetTag`, `general.jamfBinaryVersion`, `general.lastContactTime`, `general.lastEnrolledDate`, `general.lastCloudBackupDate`, `general.reportDate`, `general.remoteManagement.managementUsername`, `general.mdmCertificateExpiration`, `general.platform`, `hardware.make`, `hardware.model`, `operatingSystem.build`, `operatingSystem.name`, `operatingSystem.version`, `userAndLocation.realname`, `purchasing.lifeExpectancy`, `purchasing.warrantyDate`  Example: `sort=udid:desc,general.name:asc`.  (optional) (default to ["id:asc"])
filter = '' # str | Query in the RSQL format, allowing to filter computer inventory collection. Default filter is empty query - returning all results for the requested page.  Fields allowed in the query: `general.name`, `udid`, `id`, `general.assetTag`, `general.barcode1`, `general.barcode2`, `general.enrolledViaAutomatedDeviceEnrollment`, `general.lastIpAddress`, `general.itunesStoreAccountActive`, `general.jamfBinaryVersion`, `general.lastContactTime`, `general.lastEnrolledDate`, `general.lastCloudBackupDate`, `general.reportDate`, `general.lastReportedIp`, `general.remoteManagement.managed`, `general.remoteManagement.managementUsername`, `general.mdmCapable.capable`, `general.mdmCertificateExpiration`, `general.platform`, `general.supervised`, `general.userApprovedMdm`, `hardware.bleCapable`, `hardware.macAddress`, `hardware.make`, `hardware.model`, `hardware.modelIdentifier`, `hardware.serialNumber`, `operatingSystem.activeDirectoryStatus`, `operatingSystem.fileVault2Status`, `operatingSystem.build`, `operatingSystem.name`, `operatingSystem.version`, `security.activationLockEnabled`, `userAndLocation.buildingId`, `userAndLocation.departmentId`, `userAndLocation.email`, `userAndLocation.realname`, `userAndLocation.phone`, `userAndLocation.position`,`userAndLocation.room`, `userAndLocation.username`, `purchasing.appleCareId`, `purchasing.lifeExpectancy`, `purchasing.purchased`, `purchasing.leased`, `purchasing.vendor`, `purchasing.warrantyDate`,  This param can be combined with paging and sorting. Example: `filter=general.name==\"Orchard\"`  (optional) (default to '')

    try:
        # Return a Computer Inventory for paginated list of computers 
        api_response = api_instance.v1_computers_inventory_get(section=section, page=page, page_size=page_size, sort=sort, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerInventoryApi->v1_computers_inventory_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section** | [**list[ComputerSection]**](ComputerSection.md)| section of computer details, if not specified, General section data is returned. Multiple section parameters are supported, e.g. section&#x3D;GENERAL&amp;section&#x3D;HARDWARE | [optional] [default to [&quot;GENERAL&quot;]]
 **page** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 100]
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: &#x60;property:asc/desc&#x60;. Default sort is &#x60;general.name:asc&#x60;. Multiple sort criteria are supported and must be separated with a comma.  Fields allowed in the sort: &#x60;general.name&#x60;, &#x60;udid&#x60;, &#x60;id&#x60;, &#x60;general.assetTag&#x60;, &#x60;general.jamfBinaryVersion&#x60;, &#x60;general.lastContactTime&#x60;, &#x60;general.lastEnrolledDate&#x60;, &#x60;general.lastCloudBackupDate&#x60;, &#x60;general.reportDate&#x60;, &#x60;general.remoteManagement.managementUsername&#x60;, &#x60;general.mdmCertificateExpiration&#x60;, &#x60;general.platform&#x60;, &#x60;hardware.make&#x60;, &#x60;hardware.model&#x60;, &#x60;operatingSystem.build&#x60;, &#x60;operatingSystem.name&#x60;, &#x60;operatingSystem.version&#x60;, &#x60;userAndLocation.realname&#x60;, &#x60;purchasing.lifeExpectancy&#x60;, &#x60;purchasing.warrantyDate&#x60;  Example: &#x60;sort&#x3D;udid:desc,general.name:asc&#x60;.  | [optional] [default to [&quot;id:asc&quot;]]
 **filter** | **str**| Query in the RSQL format, allowing to filter computer inventory collection. Default filter is empty query - returning all results for the requested page.  Fields allowed in the query: &#x60;general.name&#x60;, &#x60;udid&#x60;, &#x60;id&#x60;, &#x60;general.assetTag&#x60;, &#x60;general.barcode1&#x60;, &#x60;general.barcode2&#x60;, &#x60;general.enrolledViaAutomatedDeviceEnrollment&#x60;, &#x60;general.lastIpAddress&#x60;, &#x60;general.itunesStoreAccountActive&#x60;, &#x60;general.jamfBinaryVersion&#x60;, &#x60;general.lastContactTime&#x60;, &#x60;general.lastEnrolledDate&#x60;, &#x60;general.lastCloudBackupDate&#x60;, &#x60;general.reportDate&#x60;, &#x60;general.lastReportedIp&#x60;, &#x60;general.remoteManagement.managed&#x60;, &#x60;general.remoteManagement.managementUsername&#x60;, &#x60;general.mdmCapable.capable&#x60;, &#x60;general.mdmCertificateExpiration&#x60;, &#x60;general.platform&#x60;, &#x60;general.supervised&#x60;, &#x60;general.userApprovedMdm&#x60;, &#x60;hardware.bleCapable&#x60;, &#x60;hardware.macAddress&#x60;, &#x60;hardware.make&#x60;, &#x60;hardware.model&#x60;, &#x60;hardware.modelIdentifier&#x60;, &#x60;hardware.serialNumber&#x60;, &#x60;operatingSystem.activeDirectoryStatus&#x60;, &#x60;operatingSystem.fileVault2Status&#x60;, &#x60;operatingSystem.build&#x60;, &#x60;operatingSystem.name&#x60;, &#x60;operatingSystem.version&#x60;, &#x60;security.activationLockEnabled&#x60;, &#x60;userAndLocation.buildingId&#x60;, &#x60;userAndLocation.departmentId&#x60;, &#x60;userAndLocation.email&#x60;, &#x60;userAndLocation.realname&#x60;, &#x60;userAndLocation.phone&#x60;, &#x60;userAndLocation.position&#x60;,&#x60;userAndLocation.room&#x60;, &#x60;userAndLocation.username&#x60;, &#x60;purchasing.appleCareId&#x60;, &#x60;purchasing.lifeExpectancy&#x60;, &#x60;purchasing.purchased&#x60;, &#x60;purchasing.leased&#x60;, &#x60;purchasing.vendor&#x60;, &#x60;purchasing.warrantyDate&#x60;,  This param can be combined with paging and sorting. Example: &#x60;filter&#x3D;general.name&#x3D;&#x3D;\&quot;Orchard\&quot;&#x60;  | [optional] [default to &#39;&#39;]

### Return type

[**ComputerInventorySearchResults**](ComputerInventorySearchResults.md)

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

# **v1_computers_inventory_id_attachments_attachment_id_delete**
> v1_computers_inventory_id_attachments_attachment_id_delete(id, attachment_id)

Remove attachment 

Remove attachment

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
    api_instance = jamf.ComputerInventoryApi(api_client)
    id = 'id_example' # str | instance id of computer record
attachment_id = 'attachment_id_example' # str | instance id of attachment object

    try:
        # Remove attachment 
        api_instance.v1_computers_inventory_id_attachments_attachment_id_delete(id, attachment_id)
    except ApiException as e:
        print("Exception when calling ComputerInventoryApi->v1_computers_inventory_id_attachments_attachment_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of computer record | 
 **attachment_id** | **str**| instance id of attachment object | 

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
**204** | Attachment successfully removed |  -  |
**404** | Specified computer object or attachment does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computers_inventory_id_attachments_attachment_id_get**
> file v1_computers_inventory_id_attachments_attachment_id_get(id, attachment_id)

Download attachment file 

Download attachment file

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
    api_instance = jamf.ComputerInventoryApi(api_client)
    id = 'id_example' # str | instance id of computer record
attachment_id = 'attachment_id_example' # str | instance id of attachment object

    try:
        # Download attachment file 
        api_response = api_instance.v1_computers_inventory_id_attachments_attachment_id_get(id, attachment_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerInventoryApi->v1_computers_inventory_id_attachments_attachment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of computer record | 
 **attachment_id** | **str**| instance id of attachment object | 

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
**200** | Attachment successfully downloaded |  -  |
**404** | Specified computer object or attachment does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computers_inventory_id_attachments_post**
> HrefResponse v1_computers_inventory_id_attachments_post(id, file)

Upload attachment and assign to computer 

Upload attachment and assign to computer

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
    api_instance = jamf.ComputerInventoryApi(api_client)
    id = 'id_example' # str | instance id of computer record
file = '/path/to/file' # file | The file to upload

    try:
        # Upload attachment and assign to computer 
        api_response = api_instance.v1_computers_inventory_id_attachments_post(id, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerInventoryApi->v1_computers_inventory_id_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of computer record | 
 **file** | **file**| The file to upload | 

### Return type

[**HrefResponse**](HrefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully uploaded attachment |  -  |
**404** | Specified computer object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computers_inventory_id_delete**
> v1_computers_inventory_id_delete(id)

Remove specified Computer record 

Remove specified Computer record

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
    api_instance = jamf.ComputerInventoryApi(api_client)
    id = 'id_example' # str | instance id of computer record

    try:
        # Remove specified Computer record 
        api_instance.v1_computers_inventory_id_delete(id)
    except ApiException as e:
        print("Exception when calling ComputerInventoryApi->v1_computers_inventory_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of computer record | 

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
**204** | Computer record sucessfully removed |  -  |
**404** | Specified computer object id does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_computers_inventory_id_get**
> ComputerInventoryResponse v1_computers_inventory_id_get(id, section=section)

Return a Computer General details 

Return a Computer General details

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
    api_instance = jamf.ComputerInventoryApi(api_client)
    id = 'id_example' # str | instance id of computer record
section = ["GENERAL"] # list[ComputerSection] | section of computer details, if not specified, General section data is returned. Multiple section parameters are supported, e.g. section=general&section=hardware (optional) (default to ["GENERAL"])

    try:
        # Return a Computer General details 
        api_response = api_instance.v1_computers_inventory_id_get(id, section=section)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComputerInventoryApi->v1_computers_inventory_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| instance id of computer record | 
 **section** | [**list[ComputerSection]**](ComputerSection.md)| section of computer details, if not specified, General section data is returned. Multiple section parameters are supported, e.g. section&#x3D;general&amp;section&#x3D;hardware | [optional] [default to [&quot;GENERAL&quot;]]

### Return type

[**ComputerInventoryResponse**](ComputerInventoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of computer were found |  -  |
**404** | Specified computer object does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

