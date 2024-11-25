# KeyAssociationDto

List of associated items

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**resource** | [**Resource**](Resource.md) |  | 

## Example

```python
from pyCZERTAINLY.models.key_association_dto import KeyAssociationDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeyAssociationDto from a JSON string
key_association_dto_instance = KeyAssociationDto.from_json(json)
# print the JSON string representation of the object
print(KeyAssociationDto.to_json())

# convert the object into a dict
key_association_dto_dict = key_association_dto_instance.to_dict()
# create an instance of KeyAssociationDto from a dict
key_association_dto_from_dict = KeyAssociationDto.from_dict(key_association_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


