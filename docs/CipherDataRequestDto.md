# CipherDataRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cipher_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of cipher Attributes | 
**cipher_data** | [**List[CipherRequestData]**](CipherRequestData.md) | Encrypted/decrypted data | 

## Example

```python
from openapi_client.models.cipher_data_request_dto import CipherDataRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CipherDataRequestDto from a JSON string
cipher_data_request_dto_instance = CipherDataRequestDto.from_json(json)
# print the JSON string representation of the object
print(CipherDataRequestDto.to_json())

# convert the object into a dict
cipher_data_request_dto_dict = cipher_data_request_dto_instance.to_dict()
# create an instance of CipherDataRequestDto from a dict
cipher_data_request_dto_from_dict = CipherDataRequestDto.from_dict(cipher_data_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


