# BulkCompromiseKeyItemRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**KeyCompromiseReason**](KeyCompromiseReason.md) |  | 
**uuids** | **List[str]** | List of Key Item UUID | [optional] 

## Example

```python
from openapi_client.models.bulk_compromise_key_item_request_dto import BulkCompromiseKeyItemRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCompromiseKeyItemRequestDto from a JSON string
bulk_compromise_key_item_request_dto_instance = BulkCompromiseKeyItemRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkCompromiseKeyItemRequestDto.to_json())

# convert the object into a dict
bulk_compromise_key_item_request_dto_dict = bulk_compromise_key_item_request_dto_instance.to_dict()
# create an instance of BulkCompromiseKeyItemRequestDto from a dict
bulk_compromise_key_item_request_dto_from_dict = BulkCompromiseKeyItemRequestDto.from_dict(bulk_compromise_key_item_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


