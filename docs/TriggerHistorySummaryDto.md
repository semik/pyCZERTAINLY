# TriggerHistorySummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_resource** | [**Resource**](Resource.md) |  | 
**association_object_uuid** | **str** | UUID of the object associated with triggers. | 
**objects_resource** | [**Resource**](Resource.md) |  | 
**objects_evaluated** | **int** | Number of objects evaluated. | 
**objects_matched** | **int** | Number of objects matched at least by one trigger. | 
**objects_ignored** | **int** | Number of objects matched by ignore triggers. | 
**objects** | [**List[TriggerHistoryObjectSummaryDto]**](TriggerHistoryObjectSummaryDto.md) | List of history of objects that triggers has been evaluated on. | 

## Example

```python
from openapi_client.models.trigger_history_summary_dto import TriggerHistorySummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerHistorySummaryDto from a JSON string
trigger_history_summary_dto_instance = TriggerHistorySummaryDto.from_json(json)
# print the JSON string representation of the object
print(TriggerHistorySummaryDto.to_json())

# convert the object into a dict
trigger_history_summary_dto_dict = trigger_history_summary_dto_instance.to_dict()
# create an instance of TriggerHistorySummaryDto from a dict
trigger_history_summary_dto_from_dict = TriggerHistorySummaryDto.from_dict(trigger_history_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


