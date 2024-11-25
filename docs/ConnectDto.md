# ConnectDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_group** | [**FunctionGroupDto**](FunctionGroupDto.md) |  | 

## Example

```python
from pyCZERTAINLY.models.connect_dto import ConnectDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectDto from a JSON string
connect_dto_instance = ConnectDto.from_json(json)
# print the JSON string representation of the object
print(ConnectDto.to_json())

# convert the object into a dict
connect_dto_dict = connect_dto_instance.to_dict()
# create an instance of ConnectDto from a dict
connect_dto_from_dict = ConnectDto.from_dict(connect_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


