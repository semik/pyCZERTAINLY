# IntegerAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | **int** | Integer attribute value | 

## Example

```python
from pyCZERTAINLY.models.integer_attribute_content import IntegerAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of IntegerAttributeContent from a JSON string
integer_attribute_content_instance = IntegerAttributeContent.from_json(json)
# print the JSON string representation of the object
print(IntegerAttributeContent.to_json())

# convert the object into a dict
integer_attribute_content_dict = integer_attribute_content_instance.to_dict()
# create an instance of IntegerAttributeContent from a dict
integer_attribute_content_from_dict = IntegerAttributeContent.from_dict(integer_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


