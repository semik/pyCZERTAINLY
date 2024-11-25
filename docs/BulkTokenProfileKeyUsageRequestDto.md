# BulkTokenProfileKeyUsageRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | [**List[KeyUsage]**](KeyUsage.md) | Usages for the Key | 
**uuids** | **List[str]** | Token Profile UUIDs | 

## Example

```python
from pyCZERTAINLY.models.bulk_token_profile_key_usage_request_dto import BulkTokenProfileKeyUsageRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkTokenProfileKeyUsageRequestDto from a JSON string
bulk_token_profile_key_usage_request_dto_instance = BulkTokenProfileKeyUsageRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkTokenProfileKeyUsageRequestDto.to_json())

# convert the object into a dict
bulk_token_profile_key_usage_request_dto_dict = bulk_token_profile_key_usage_request_dto_instance.to_dict()
# create an instance of BulkTokenProfileKeyUsageRequestDto from a dict
bulk_token_profile_key_usage_request_dto_from_dict = BulkTokenProfileKeyUsageRequestDto.from_dict(bulk_token_profile_key_usage_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


