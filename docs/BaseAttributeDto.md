# BaseAttributeDto

Base Attribute definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute for unique identification | 
**name** | **str** | Name of the Attribute that is used for identification | 
**description** | **str** | Optional description of the Attribute, should contain helper text on what is expected | [optional] 
**type** | [**AttributeType**](AttributeType.md) |  | 
**content** | **object** | Content of the Attribute | [optional] 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**properties** | [**CustomAttributeProperties**](CustomAttributeProperties.md) |  | 
**constraints** | [**List[BaseAttributeConstraint]**](BaseAttributeConstraint.md) | Optional regular expressions and constraints used for validating the Attribute content | [optional] 
**attribute_callback** | [**AttributeCallback**](AttributeCallback.md) |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.base_attribute_dto import BaseAttributeDto

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAttributeDto from a JSON string
base_attribute_dto_instance = BaseAttributeDto.from_json(json)
# print the JSON string representation of the object
print(BaseAttributeDto.to_json())

# convert the object into a dict
base_attribute_dto_dict = base_attribute_dto_instance.to_dict()
# create an instance of BaseAttributeDto from a dict
base_attribute_dto_from_dict = BaseAttributeDto.from_dict(base_attribute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


