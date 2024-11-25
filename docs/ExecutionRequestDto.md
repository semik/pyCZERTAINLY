# ExecutionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the execution | 
**description** | **str** | Description of the execution | [optional] 
**type** | [**ExecutionType**](ExecutionType.md) |  | 
**resource** | [**Resource**](Resource.md) |  | 
**items** | [**List[ExecutionItemRequestDto]**](ExecutionItemRequestDto.md) | List of the execution items to add to execution | 

## Example

```python
from openapi_client.models.execution_request_dto import ExecutionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionRequestDto from a JSON string
execution_request_dto_instance = ExecutionRequestDto.from_json(json)
# print the JSON string representation of the object
print(ExecutionRequestDto.to_json())

# convert the object into a dict
execution_request_dto_dict = execution_request_dto_instance.to_dict()
# create an instance of ExecutionRequestDto from a dict
execution_request_dto_from_dict = ExecutionRequestDto.from_dict(execution_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


