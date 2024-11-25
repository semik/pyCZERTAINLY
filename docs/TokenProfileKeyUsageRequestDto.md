# TokenProfileKeyUsageRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | [**List[KeyUsage]**](KeyUsage.md) | Usages for the Key | 

## Example

```python
from pyCZERTAINLY.models.token_profile_key_usage_request_dto import TokenProfileKeyUsageRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TokenProfileKeyUsageRequestDto from a JSON string
token_profile_key_usage_request_dto_instance = TokenProfileKeyUsageRequestDto.from_json(json)
# print the JSON string representation of the object
print(TokenProfileKeyUsageRequestDto.to_json())

# convert the object into a dict
token_profile_key_usage_request_dto_dict = token_profile_key_usage_request_dto_instance.to_dict()
# create an instance of TokenProfileKeyUsageRequestDto from a dict
token_profile_key_usage_request_dto_from_dict = TokenProfileKeyUsageRequestDto.from_dict(token_profile_key_usage_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


