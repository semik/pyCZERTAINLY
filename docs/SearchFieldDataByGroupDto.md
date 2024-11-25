# SearchFieldDataByGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_field_source** | [**FilterFieldSource**](FilterFieldSource.md) |  | 
**search_field_data** | [**List[SearchFieldDataDto]**](SearchFieldDataDto.md) | List of search fields for specified search group | [optional] 

## Example

```python
from pyCZERTAINLY.models.search_field_data_by_group_dto import SearchFieldDataByGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFieldDataByGroupDto from a JSON string
search_field_data_by_group_dto_instance = SearchFieldDataByGroupDto.from_json(json)
# print the JSON string representation of the object
print(SearchFieldDataByGroupDto.to_json())

# convert the object into a dict
search_field_data_by_group_dto_dict = search_field_data_by_group_dto_instance.to_dict()
# create an instance of SearchFieldDataByGroupDto from a dict
search_field_data_by_group_dto_from_dict = SearchFieldDataByGroupDto.from_dict(search_field_data_by_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


