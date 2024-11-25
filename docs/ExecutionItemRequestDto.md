# ExecutionItemRequestDto

List of the execution items to add to execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_source** | [**FilterFieldSource**](FilterFieldSource.md) |  | 
**field_identifier** | **str** | Field identifier of the execution item | 
**data** | **object** | Data of the execution item | [optional] 

## Example

```python
from pyCZERTAINLY.models.execution_item_request_dto import ExecutionItemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionItemRequestDto from a JSON string
execution_item_request_dto_instance = ExecutionItemRequestDto.from_json(json)
# print the JSON string representation of the object
print(ExecutionItemRequestDto.to_json())

# convert the object into a dict
execution_item_request_dto_dict = execution_item_request_dto_instance.to_dict()
# create an instance of ExecutionItemRequestDto from a dict
execution_item_request_dto_from_dict = ExecutionItemRequestDto.from_dict(execution_item_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


