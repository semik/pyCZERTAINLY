# LocationsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | [**List[LocationDto]**](LocationDto.md) | Locations | 
**items_per_page** | **int** | Number of locations per page | 
**page_number** | **int** | Page number for the request | 
**total_pages** | **int** | Number of pages available | 
**total_items** | **int** | Number of items available | 

## Example

```python
from openapi_client.models.locations_response_dto import LocationsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LocationsResponseDto from a JSON string
locations_response_dto_instance = LocationsResponseDto.from_json(json)
# print the JSON string representation of the object
print(LocationsResponseDto.to_json())

# convert the object into a dict
locations_response_dto_dict = locations_response_dto_instance.to_dict()
# create an instance of LocationsResponseDto from a dict
locations_response_dto_from_dict = LocationsResponseDto.from_dict(locations_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


