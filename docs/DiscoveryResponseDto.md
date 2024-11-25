# DiscoveryResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discoveries** | [**List[DiscoveryHistoryDto]**](DiscoveryHistoryDto.md) | Discoveries | 
**items_per_page** | **int** | Number of entries per page | 
**page_number** | **int** | Page number for the request | 
**total_pages** | **int** | Number of pages available | 
**total_items** | **int** | Number of items available | 

## Example

```python
from openapi_client.models.discovery_response_dto import DiscoveryResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryResponseDto from a JSON string
discovery_response_dto_instance = DiscoveryResponseDto.from_json(json)
# print the JSON string representation of the object
print(DiscoveryResponseDto.to_json())

# convert the object into a dict
discovery_response_dto_dict = discovery_response_dto_instance.to_dict()
# create an instance of DiscoveryResponseDto from a dict
discovery_response_dto_from_dict = DiscoveryResponseDto.from_dict(discovery_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


