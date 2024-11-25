# CodeBlockAttributeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Content Reference | [optional] 
**data** | [**CodeBlockAttributeContentData**](CodeBlockAttributeContentData.md) |  | 

## Example

```python
from pyCZERTAINLY.models.code_block_attribute_content import CodeBlockAttributeContent

# TODO update the JSON string below
json = "{}"
# create an instance of CodeBlockAttributeContent from a JSON string
code_block_attribute_content_instance = CodeBlockAttributeContent.from_json(json)
# print the JSON string representation of the object
print(CodeBlockAttributeContent.to_json())

# convert the object into a dict
code_block_attribute_content_dict = code_block_attribute_content_instance.to_dict()
# create an instance of CodeBlockAttributeContent from a dict
code_block_attribute_content_from_dict = CodeBlockAttributeContent.from_dict(code_block_attribute_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


