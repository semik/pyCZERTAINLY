# UpdateKeyUsageRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | [**List[KeyUsage]**](KeyUsage.md) | Usages for the Key | 
**uuids** | **List[str]** | List of UUIDs of the key Items. If not provided, the usage will be updated to all the itemsin the key | [optional] 

## Example

```python
from openapi_client.models.update_key_usage_request_dto import UpdateKeyUsageRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKeyUsageRequestDto from a JSON string
update_key_usage_request_dto_instance = UpdateKeyUsageRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateKeyUsageRequestDto.to_json())

# convert the object into a dict
update_key_usage_request_dto_dict = update_key_usage_request_dto_instance.to_dict()
# create an instance of UpdateKeyUsageRequestDto from a dict
update_key_usage_request_dto_from_dict = UpdateKeyUsageRequestDto.from_dict(update_key_usage_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


