# MetadataResponseDto

Metadata response attributes with their source connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **str** | UUID of the Connector | [optional] 
**connector_name** | **str** | Name of the Connector | [optional] 
**source_object_type** | [**Resource**](Resource.md) |  | [optional] 
**items** | [**List[ResponseMetadataDto]**](ResponseMetadataDto.md) | List of Metadata | 

## Example

```python
from openapi_client.models.metadata_response_dto import MetadataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataResponseDto from a JSON string
metadata_response_dto_instance = MetadataResponseDto.from_json(json)
# print the JSON string representation of the object
print(MetadataResponseDto.to_json())

# convert the object into a dict
metadata_response_dto_dict = metadata_response_dto_instance.to_dict()
# create an instance of MetadataResponseDto from a dict
metadata_response_dto_from_dict = MetadataResponseDto.from_dict(metadata_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


