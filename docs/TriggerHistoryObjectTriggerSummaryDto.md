# TriggerHistoryObjectTriggerSummaryDto

List of records for each trigger that has been evaluated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_uuid** | **str** | UUID of the object that the trigger has been evaluated on. | 
**trigger_name** | **str** | Reference UUID of the object that the trigger has been evaluated on. | 
**triggered_at** | **datetime** | Time at which has the trigger been triggered | 
**message** | **str** | Additional message.  | [optional] 
**records** | [**List[TriggerHistoryRecordDto]**](TriggerHistoryRecordDto.md) | List of records for each action that has not been performed and each condition that has not been evaluated. | 

## Example

```python
from pyCZERTAINLY.models.trigger_history_object_trigger_summary_dto import TriggerHistoryObjectTriggerSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerHistoryObjectTriggerSummaryDto from a JSON string
trigger_history_object_trigger_summary_dto_instance = TriggerHistoryObjectTriggerSummaryDto.from_json(json)
# print the JSON string representation of the object
print(TriggerHistoryObjectTriggerSummaryDto.to_json())

# convert the object into a dict
trigger_history_object_trigger_summary_dto_dict = trigger_history_object_trigger_summary_dto_instance.to_dict()
# create an instance of TriggerHistoryObjectTriggerSummaryDto from a dict
trigger_history_object_trigger_summary_dto_from_dict = TriggerHistoryObjectTriggerSummaryDto.from_dict(trigger_history_object_trigger_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


