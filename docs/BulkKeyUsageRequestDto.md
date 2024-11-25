# BulkKeyUsageRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | [**List[KeyUsage]**](KeyUsage.md) | Usages for the Key | 
**uuids** | **List[str]** | Key UUIDs | 

## Example

```python
from openapi_client.models.bulk_key_usage_request_dto import BulkKeyUsageRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkKeyUsageRequestDto from a JSON string
bulk_key_usage_request_dto_instance = BulkKeyUsageRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkKeyUsageRequestDto.to_json())

# convert the object into a dict
bulk_key_usage_request_dto_dict = bulk_key_usage_request_dto_instance.to_dict()
# create an instance of BulkKeyUsageRequestDto from a dict
bulk_key_usage_request_dto_from_dict = BulkKeyUsageRequestDto.from_dict(bulk_key_usage_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


