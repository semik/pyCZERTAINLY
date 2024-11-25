# ExecutionDto

List of executions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the execution | [optional] 
**type** | [**ExecutionType**](ExecutionType.md) |  | 
**resource** | [**Resource**](Resource.md) |  | 
**items** | [**List[ExecutionItemDto]**](ExecutionItemDto.md) | List of the execution items | 

## Example

```python
from pyCZERTAINLY.models.execution_dto import ExecutionDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionDto from a JSON string
execution_dto_instance = ExecutionDto.from_json(json)
# print the JSON string representation of the object
print(ExecutionDto.to_json())

# convert the object into a dict
execution_dto_dict = execution_dto_instance.to_dict()
# create an instance of ExecutionDto from a dict
execution_dto_from_dict = ExecutionDto.from_dict(execution_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


