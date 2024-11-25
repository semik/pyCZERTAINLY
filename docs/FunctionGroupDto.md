# FunctionGroupDto

List of Function Groups implemented by the Connector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_group_code** | [**FunctionGroupCode**](FunctionGroupCode.md) |  | 
**kinds** | **List[str]** | List of supported functional group kinds | 
**end_points** | [**List[EndpointDto]**](EndpointDto.md) | List of end points related to functional group | 
**uuid** | **str** | UUID of the Function Group | 
**name** | **str** | Function Group Name | 

## Example

```python
from pyCZERTAINLY.models.function_group_dto import FunctionGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionGroupDto from a JSON string
function_group_dto_instance = FunctionGroupDto.from_json(json)
# print the JSON string representation of the object
print(FunctionGroupDto.to_json())

# convert the object into a dict
function_group_dto_dict = function_group_dto_instance.to_dict()
# create an instance of FunctionGroupDto from a dict
function_group_dto_from_dict = FunctionGroupDto.from_dict(function_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


