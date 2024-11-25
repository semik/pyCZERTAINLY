# AttributeDefinitionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute | 
**name** | **str** | Name of the Attribute | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**description** | **str** | Attribute description | 
**enabled** | **bool** | Boolean determining if the Attribute is enabled. Required only for Custom Attribute | [optional] 

## Example

```python
from pyCZERTAINLY.models.attribute_definition_dto import AttributeDefinitionDto

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeDefinitionDto from a JSON string
attribute_definition_dto_instance = AttributeDefinitionDto.from_json(json)
# print the JSON string representation of the object
print(AttributeDefinitionDto.to_json())

# convert the object into a dict
attribute_definition_dto_dict = attribute_definition_dto_instance.to_dict()
# create an instance of AttributeDefinitionDto from a dict
attribute_definition_dto_from_dict = AttributeDefinitionDto.from_dict(attribute_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


