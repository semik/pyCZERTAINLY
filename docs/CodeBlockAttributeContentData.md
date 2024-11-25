# CodeBlockAttributeContentData

CodeBlock attribute content data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | [**ProgrammingLanguageEnum**](ProgrammingLanguageEnum.md) |  | 
**code** | **str** | Block of the code in Base64. Formatting of the code is specified by variable language | 

## Example

```python
from openapi_client.models.code_block_attribute_content_data import CodeBlockAttributeContentData

# TODO update the JSON string below
json = "{}"
# create an instance of CodeBlockAttributeContentData from a JSON string
code_block_attribute_content_data_instance = CodeBlockAttributeContentData.from_json(json)
# print the JSON string representation of the object
print(CodeBlockAttributeContentData.to_json())

# convert the object into a dict
code_block_attribute_content_data_dict = code_block_attribute_content_data_instance.to_dict()
# create an instance of CodeBlockAttributeContentData from a dict
code_block_attribute_content_data_from_dict = CodeBlockAttributeContentData.from_dict(code_block_attribute_content_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


