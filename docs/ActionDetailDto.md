# ActionDetailDto

List of Action Groups in the Rule Trigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the action | [optional] 
**resource** | [**Resource**](Resource.md) |  | 
**executions** | [**List[ExecutionDto]**](ExecutionDto.md) | List of executions | 

## Example

```python
from openapi_client.models.action_detail_dto import ActionDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDetailDto from a JSON string
action_detail_dto_instance = ActionDetailDto.from_json(json)
# print the JSON string representation of the object
print(ActionDetailDto.to_json())

# convert the object into a dict
action_detail_dto_dict = action_detail_dto_instance.to_dict()
# create an instance of ActionDetailDto from a dict
action_detail_dto_from_dict = ActionDetailDto.from_dict(action_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


