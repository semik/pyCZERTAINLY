# SignDataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signatures** | [**List[SignatureResponseData]**](SignatureResponseData.md) | Signatures | 

## Example

```python
from openapi_client.models.sign_data_response_dto import SignDataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SignDataResponseDto from a JSON string
sign_data_response_dto_instance = SignDataResponseDto.from_json(json)
# print the JSON string representation of the object
print(SignDataResponseDto.to_json())

# convert the object into a dict
sign_data_response_dto_dict = sign_data_response_dto_instance.to_dict()
# create an instance of SignDataResponseDto from a dict
sign_data_response_dto_from_dict = SignDataResponseDto.from_dict(sign_data_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


