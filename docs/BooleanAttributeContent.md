# BooleanAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **bool** | Boolean attribute value | 

## Example

```python
from pyCZERTAINLY.models.boolean_attribute_content import BooleanAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanAttributeContent from a JSON string
boolean_attribute_content_instance = BooleanAttributeContent.from_json(json)
# print the JSON string representation of the object
print(BooleanAttributeContent.to_json())

# convert the object into a dict
boolean_attribute_content_dict = boolean_attribute_content_instance.to_dict()
# create an instance of BooleanAttributeContent from a dict
boolean_attribute_content_from_dict = BooleanAttributeContent.from_dict(boolean_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


