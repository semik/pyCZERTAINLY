# ResponseAttributeDto

Response attribute with content for object it belongs to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute | [optional] 
**name** | **str** | Name of the Attribute | 
**label** | **str** | Label of the the Attribute | 
**type** | [**AttributeType**](AttributeType.md) |  | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**content** | [**List[BaseAttributeContentDto]**](BaseAttributeContentDto.md) | Content of the Attribute | [optional] 

## Example

```python
from pyCZERTAINLY.models.response_attribute_dto import ResponseAttributeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseAttributeDto from a JSON string
response_attribute_dto_instance = ResponseAttributeDto.from_json(json)
# print the JSON string representation of the object
print(ResponseAttributeDto.to_json())

# convert the object into a dict
response_attribute_dto_dict = response_attribute_dto_instance.to_dict()
# create an instance of ResponseAttributeDto from a dict
response_attribute_dto_from_dict = ResponseAttributeDto.from_dict(response_attribute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


