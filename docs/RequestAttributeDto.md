# RequestAttributeDto

Request attribute to send attribute content for object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute | 
**name** | **str** | Name of the Attribute | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**content** | [**List[BaseAttributeContentDto]**](BaseAttributeContentDto.md) | Content of the Attribute | 

## Example

```python
from openapi_client.models.request_attribute_dto import RequestAttributeDto

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAttributeDto from a JSON string
request_attribute_dto_instance = RequestAttributeDto.from_json(json)
# print the JSON string representation of the object
print(RequestAttributeDto.to_json())

# convert the object into a dict
request_attribute_dto_dict = request_attribute_dto_instance.to_dict()
# create an instance of RequestAttributeDto from a dict
request_attribute_dto_from_dict = RequestAttributeDto.from_dict(request_attribute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


