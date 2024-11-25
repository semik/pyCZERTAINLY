# ConnectorMetadataPromotionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Metadata UUID | 
**connector_uuid** | **str** | Connector UUID | 

## Example

```python
from pyCZERTAINLY.models.connector_metadata_promotion_request_dto import ConnectorMetadataPromotionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorMetadataPromotionRequestDto from a JSON string
connector_metadata_promotion_request_dto_instance = ConnectorMetadataPromotionRequestDto.from_json(json)
# print the JSON string representation of the object
print(ConnectorMetadataPromotionRequestDto.to_json())

# convert the object into a dict
connector_metadata_promotion_request_dto_dict = connector_metadata_promotion_request_dto_instance.to_dict()
# create an instance of ConnectorMetadataPromotionRequestDto from a dict
connector_metadata_promotion_request_dto_from_dict = ConnectorMetadataPromotionRequestDto.from_dict(connector_metadata_promotion_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


