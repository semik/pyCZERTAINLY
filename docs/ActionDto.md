# ActionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the action | [optional] 
**resource** | [**Resource**](Resource.md) |  | 

## Example

```python
from pyCZERTAINLY.models.action_dto import ActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDto from a JSON string
action_dto_instance = ActionDto.from_json(json)
# print the JSON string representation of the object
print(ActionDto.to_json())

# convert the object into a dict
action_dto_dict = action_dto_instance.to_dict()
# create an instance of ActionDto from a dict
action_dto_from_dict = ActionDto.from_dict(action_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


