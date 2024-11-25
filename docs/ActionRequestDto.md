# ActionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the action | 
**description** | **str** | Description of the action | [optional] 
**resource** | [**Resource**](Resource.md) |  | 
**executions_uuids** | **List[str]** | List of UUIDs of existing executions to add to the action | 

## Example

```python
from pyCZERTAINLY.models.action_request_dto import ActionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRequestDto from a JSON string
action_request_dto_instance = ActionRequestDto.from_json(json)
# print the JSON string representation of the object
print(ActionRequestDto.to_json())

# convert the object into a dict
action_request_dto_dict = action_request_dto_instance.to_dict()
# create an instance of ActionRequestDto from a dict
action_request_dto_from_dict = ActionRequestDto.from_dict(action_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


