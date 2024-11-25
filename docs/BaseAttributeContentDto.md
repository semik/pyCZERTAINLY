# BaseAttributeContentDto

Base Attribute content definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **object** | Content Data | 

## Example

```python
from pyCZERTAINLY.models.base_attribute_content_dto import BaseAttributeContentDto

# TODO update the JSON string below
json = "{}"
# create an instance of BaseAttributeContentDto from a JSON string
base_attribute_content_dto_instance = BaseAttributeContentDto.from_json(json)
# print the JSON string representation of the object
print(BaseAttributeContentDto.to_json())

# convert the object into a dict
base_attribute_content_dto_dict = base_attribute_content_dto_instance.to_dict()
# create an instance of BaseAttributeContentDto from a dict
base_attribute_content_dto_from_dict = BaseAttributeContentDto.from_dict(base_attribute_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


