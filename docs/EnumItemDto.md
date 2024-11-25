# EnumItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Enum item code | 
**label** | **str** | Enum item display label | 
**description** | **str** | Enum item description | [optional] 

## Example

```python
from openapi_client.models.enum_item_dto import EnumItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of EnumItemDto from a JSON string
enum_item_dto_instance = EnumItemDto.from_json(json)
# print the JSON string representation of the object
print(EnumItemDto.to_json())

# convert the object into a dict
enum_item_dto_dict = enum_item_dto_instance.to_dict()
# create an instance of EnumItemDto from a dict
enum_item_dto_from_dict = EnumItemDto.from_dict(enum_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


