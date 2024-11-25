# UpdateExecutionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the execution | [optional] 
**items** | [**List[ExecutionItemRequestDto]**](ExecutionItemRequestDto.md) | List of the execution items to add to execution | 

## Example

```python
from openapi_client.models.update_execution_request_dto import UpdateExecutionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExecutionRequestDto from a JSON string
update_execution_request_dto_instance = UpdateExecutionRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateExecutionRequestDto.to_json())

# convert the object into a dict
update_execution_request_dto_dict = update_execution_request_dto_instance.to_dict()
# create an instance of UpdateExecutionRequestDto from a dict
update_execution_request_dto_from_dict = UpdateExecutionRequestDto.from_dict(update_execution_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


