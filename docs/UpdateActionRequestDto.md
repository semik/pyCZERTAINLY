# UpdateActionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the action | [optional] 
**executions_uuids** | **List[str]** | List of UUIDs of existing executions to add to the action | 

## Example

```python
from pyCZERTAINLY.models.update_action_request_dto import UpdateActionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateActionRequestDto from a JSON string
update_action_request_dto_instance = UpdateActionRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateActionRequestDto.to_json())

# convert the object into a dict
update_action_request_dto_dict = update_action_request_dto_instance.to_dict()
# create an instance of UpdateActionRequestDto from a dict
update_action_request_dto_from_dict = UpdateActionRequestDto.from_dict(update_action_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


