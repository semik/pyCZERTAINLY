# TriggerHistoryRecordDto

List of records for each action that has not been performed and each condition that has not been evaluated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message with cause of action/condition failure. | 
**condition** | [**ConditionDto**](ConditionDto.md) |  | [optional] 
**execution** | [**ExecutionDto**](ExecutionDto.md) |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.trigger_history_record_dto import TriggerHistoryRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerHistoryRecordDto from a JSON string
trigger_history_record_dto_instance = TriggerHistoryRecordDto.from_json(json)
# print the JSON string representation of the object
print(TriggerHistoryRecordDto.to_json())

# convert the object into a dict
trigger_history_record_dto_dict = trigger_history_record_dto_instance.to_dict()
# create an instance of TriggerHistoryRecordDto from a dict
trigger_history_record_dto_from_dict = TriggerHistoryRecordDto.from_dict(trigger_history_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


