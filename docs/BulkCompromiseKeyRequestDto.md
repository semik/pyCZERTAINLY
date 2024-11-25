# BulkCompromiseKeyRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**KeyCompromiseReason**](KeyCompromiseReason.md) |  | 
**uuids** | **List[str]** | List of UUIDs of the keys. This will mark all the items inside the selected key as compromised | [optional] 

## Example

```python
from openapi_client.models.bulk_compromise_key_request_dto import BulkCompromiseKeyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCompromiseKeyRequestDto from a JSON string
bulk_compromise_key_request_dto_instance = BulkCompromiseKeyRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkCompromiseKeyRequestDto.to_json())

# convert the object into a dict
bulk_compromise_key_request_dto_dict = bulk_compromise_key_request_dto_instance.to_dict()
# create an instance of BulkCompromiseKeyRequestDto from a dict
bulk_compromise_key_request_dto_from_dict = BulkCompromiseKeyRequestDto.from_dict(bulk_compromise_key_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


