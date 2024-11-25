# CustomAttributeDefinitionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute | 
**name** | **str** | Name of the Attribute | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**description** | **str** | Attribute description | 
**enabled** | **bool** | Boolean determining if the Attribute is enabled. Required only for Custom Attribute | [optional] 
**resources** | [**List[Resource]**](Resource.md) | List of resources for custom attribute | 

## Example

```python
from openapi_client.models.custom_attribute_definition_dto import CustomAttributeDefinitionDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeDefinitionDto from a JSON string
custom_attribute_definition_dto_instance = CustomAttributeDefinitionDto.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeDefinitionDto.to_json())

# convert the object into a dict
custom_attribute_definition_dto_dict = custom_attribute_definition_dto_instance.to_dict()
# create an instance of CustomAttributeDefinitionDto from a dict
custom_attribute_definition_dto_from_dict = CustomAttributeDefinitionDto.from_dict(custom_attribute_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


