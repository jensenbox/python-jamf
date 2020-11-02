# CacheSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] [default to '0']
**name** | **str** |  | [optional] [default to 'cache configuration']
**cache_type** | **str** |  | 
**time_to_live_seconds** | **int** |  | 
**time_to_idle_seconds** | **int** |  | [optional] 
**ehcache_max_bytes_local_heap** | **str** |  | [optional] [default to 'null']
**cache_unique_id** | **str** | The default is for Jamf Pro to generate a UUID, so we can only give an example instead. | 
**elasticache** | **bool** |  | [optional] [default to False]
**memcached_endpoints** | [**list[MemcachedEndpoints]**](MemcachedEndpoints.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


