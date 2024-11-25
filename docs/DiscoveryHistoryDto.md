# DiscoveryHistoryDto

Discoveries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**kind** | **str** | Discovery Kind | 
**status** | [**DiscoveryStatus**](DiscoveryStatus.md) |  | 
**start_time** | **datetime** | Date and time when Discovery started | [optional] 
**end_time** | **datetime** | Date and time when Discovery finished | [optional] 
**total_certificates_discovered** | **int** | Number of certificates that are discovered | [optional] [default to 0]
**connector_uuid** | **str** | UUID of the Discovery Provider | 
**connector_name** | **str** | Name of the Discovery Provider | 

## Example

```python
from pyCZERTAINLY.models.discovery_history_dto import DiscoveryHistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryHistoryDto from a JSON string
discovery_history_dto_instance = DiscoveryHistoryDto.from_json(json)
# print the JSON string representation of the object
print(DiscoveryHistoryDto.to_json())

# convert the object into a dict
discovery_history_dto_dict = discovery_history_dto_instance.to_dict()
# create an instance of DiscoveryHistoryDto from a dict
discovery_history_dto_from_dict = DiscoveryHistoryDto.from_dict(discovery_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


