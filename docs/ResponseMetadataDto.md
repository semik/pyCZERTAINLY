# ResponseMetadataDto

Response metadata attribute instance with content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Attribute | [optional] 
**name** | **str** | Name of the Attribute | 
**label** | **str** | Label of the the Attribute | 
**type** | [**AttributeType**](AttributeType.md) |  | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**content** | [**List[BaseAttributeContentDto]**](BaseAttributeContentDto.md) | Content of the Attribute | [optional] 
**source_objects** | [**List[NameAndUuidDto]**](NameAndUuidDto.md) | Source Objects | 

## Example

```python
from pyCZERTAINLY.models.response_metadata_dto import ResponseMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseMetadataDto from a JSON string
response_metadata_dto_instance = ResponseMetadataDto.from_json(json)
# print the JSON string representation of the object
print(ResponseMetadataDto.to_json())

# convert the object into a dict
response_metadata_dto_dict = response_metadata_dto_instance.to_dict()
# create an instance of ResponseMetadataDto from a dict
response_metadata_dto_from_dict = ResponseMetadataDto.from_dict(response_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


