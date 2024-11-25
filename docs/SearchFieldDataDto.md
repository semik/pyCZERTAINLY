# SearchFieldDataDto

List of search fields for specified search group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_identifier** | **str** | Identifier of field to search | 
**field_label** | **str** | Label for the field | 
**type** | [**FilterFieldType**](FilterFieldType.md) |  | 
**conditions** | [**List[FilterConditionOperator]**](FilterConditionOperator.md) | List of available conditions for the field | 
**platform_enum** | [**PlatformEnum**](PlatformEnum.md) |  | [optional] 
**attribute_content_type** | [**AttributeContentType**](AttributeContentType.md) |  | [optional] 
**value** | **object** | Available values for the field | [optional] 
**multi_value** | **bool** | Multivalue flag. true &#x3D; yes, false &#x3D; no | [optional] 

## Example

```python
from pyCZERTAINLY.models.search_field_data_dto import SearchFieldDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFieldDataDto from a JSON string
search_field_data_dto_instance = SearchFieldDataDto.from_json(json)
# print the JSON string representation of the object
print(SearchFieldDataDto.to_json())

# convert the object into a dict
search_field_data_dto_dict = search_field_data_dto_instance.to_dict()
# create an instance of SearchFieldDataDto from a dict
search_field_data_dto_from_dict = SearchFieldDataDto.from_dict(search_field_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


