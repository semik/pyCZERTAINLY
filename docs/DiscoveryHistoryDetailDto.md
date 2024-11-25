# DiscoveryHistoryDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**kind** | **str** | Discovery Kind | 
**status** | [**DiscoveryStatus**](DiscoveryStatus.md) |  | 
**connector_status** | [**DiscoveryStatus**](DiscoveryStatus.md) |  | 
**message** | **str** | Failure/Success Messages | [optional] 
**start_time** | **datetime** | Date and time when Discovery started | [optional] 
**end_time** | **datetime** | Date and time when Discovery finished | [optional] 
**total_certificates_discovered** | **int** | Number of certificates that are discovered | [optional] [default to 0]
**connector_total_certificates_discovered** | **int** | Number of certificates that were discovered by connector | [optional] [default to 0]
**connector_uuid** | **str** | UUID of the Discovery Provider | 
**connector_name** | **str** | Name of the Discovery Provider | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Discovery Attributes | 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 
**metadata** | [**List[MetadataResponseDto]**](MetadataResponseDto.md) | Metadata of the Discovery | [optional] 
**triggers** | [**List[TriggerDto]**](TriggerDto.md) | List of associated triggers | 

## Example

```python
from pyCZERTAINLY.models.discovery_history_detail_dto import DiscoveryHistoryDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryHistoryDetailDto from a JSON string
discovery_history_detail_dto_instance = DiscoveryHistoryDetailDto.from_json(json)
# print the JSON string representation of the object
print(DiscoveryHistoryDetailDto.to_json())

# convert the object into a dict
discovery_history_detail_dto_dict = discovery_history_detail_dto_instance.to_dict()
# create an instance of DiscoveryHistoryDetailDto from a dict
discovery_history_detail_dto_from_dict = DiscoveryHistoryDetailDto.from_dict(discovery_history_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


