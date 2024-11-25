# CompromiseKeyRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**KeyCompromiseReason**](KeyCompromiseReason.md) |  | 
**uuids** | **List[str]** | List of UUIDs of the key Items. If not provided, the usage will be updated to all the itemsin the key | [optional] 

## Example

```python
from openapi_client.models.compromise_key_request_dto import CompromiseKeyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CompromiseKeyRequestDto from a JSON string
compromise_key_request_dto_instance = CompromiseKeyRequestDto.from_json(json)
# print the JSON string representation of the object
print(CompromiseKeyRequestDto.to_json())

# convert the object into a dict
compromise_key_request_dto_dict = compromise_key_request_dto_instance.to_dict()
# create an instance of CompromiseKeyRequestDto from a dict
compromise_key_request_dto_from_dict = CompromiseKeyRequestDto.from_dict(compromise_key_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


