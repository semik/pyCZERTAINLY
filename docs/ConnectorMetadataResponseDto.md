# ConnectorMetadataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Metadata Name | 
**uuid** | **str** | Metadata UUID | 
**content_type** | [**AttributeContentType**](AttributeContentType.md) |  | 
**label** | **str** | Metadata Label | 
**connector_uuid** | **str** | Connector UUID | 

## Example

```python
from pyCZERTAINLY.models.connector_metadata_response_dto import ConnectorMetadataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorMetadataResponseDto from a JSON string
connector_metadata_response_dto_instance = ConnectorMetadataResponseDto.from_json(json)
# print the JSON string representation of the object
print(ConnectorMetadataResponseDto.to_json())

# convert the object into a dict
connector_metadata_response_dto_dict = connector_metadata_response_dto_instance.to_dict()
# create an instance of ConnectorMetadataResponseDto from a dict
connector_metadata_response_dto_from_dict = ConnectorMetadataResponseDto.from_dict(connector_metadata_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


