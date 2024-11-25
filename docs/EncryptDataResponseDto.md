# EncryptDataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_data** | [**List[CipherResponseData]**](CipherResponseData.md) | Encrypted data | 

## Example

```python
from pyCZERTAINLY.models.encrypt_data_response_dto import EncryptDataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptDataResponseDto from a JSON string
encrypt_data_response_dto_instance = EncryptDataResponseDto.from_json(json)
# print the JSON string representation of the object
print(EncryptDataResponseDto.to_json())

# convert the object into a dict
encrypt_data_response_dto_dict = encrypt_data_response_dto_instance.to_dict()
# create an instance of EncryptDataResponseDto from a dict
encrypt_data_response_dto_from_dict = EncryptDataResponseDto.from_dict(encrypt_data_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


