# KeyEventHistoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the event | 
**key_uuid** | **str** | UUID of the Key | 
**created** | **datetime** | Event creation time | 
**created_by** | **str** | Created By | 
**event** | **str** | Event type | 
**status** | **str** | Event result | 
**message** | **str** | Event message | 
**additional_information** | **Dict[str, object]** | Additional information for the event | [optional] 

## Example

```python
from openapi_client.models.key_event_history_dto import KeyEventHistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeyEventHistoryDto from a JSON string
key_event_history_dto_instance = KeyEventHistoryDto.from_json(json)
# print the JSON string representation of the object
print(KeyEventHistoryDto.to_json())

# convert the object into a dict
key_event_history_dto_dict = key_event_history_dto_instance.to_dict()
# create an instance of KeyEventHistoryDto from a dict
key_event_history_dto_from_dict = KeyEventHistoryDto.from_dict(key_event_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


