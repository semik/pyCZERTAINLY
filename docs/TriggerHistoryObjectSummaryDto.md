# TriggerHistoryObjectSummaryDto

List of history of objects that triggers has been evaluated on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_uuid** | **str** | UUID of the object that the trigger has been evaluated on. | [optional] 
**reference_object_uuid** | **str** | Reference UUID of the object that the trigger has been evaluated on. | [optional] 
**matched** | **bool** | Was matched at least by one trigger. | 
**ignored** | **bool** | Was matched by ignore trigger. | 
**triggers** | [**List[TriggerHistoryObjectTriggerSummaryDto]**](TriggerHistoryObjectTriggerSummaryDto.md) | List of records for each trigger that has been evaluated. | 

## Example

```python
from openapi_client.models.trigger_history_object_summary_dto import TriggerHistoryObjectSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerHistoryObjectSummaryDto from a JSON string
trigger_history_object_summary_dto_instance = TriggerHistoryObjectSummaryDto.from_json(json)
# print the JSON string representation of the object
print(TriggerHistoryObjectSummaryDto.to_json())

# convert the object into a dict
trigger_history_object_summary_dto_dict = trigger_history_object_summary_dto_instance.to_dict()
# create an instance of TriggerHistoryObjectSummaryDto from a dict
trigger_history_object_summary_dto_from_dict = TriggerHistoryObjectSummaryDto.from_dict(trigger_history_object_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


