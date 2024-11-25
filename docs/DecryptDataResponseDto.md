# DecryptDataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decrypted_data** | [**List[CipherResponseData]**](CipherResponseData.md) | Decrypted data | 

## Example

```python
from pyCZERTAINLY.models.decrypt_data_response_dto import DecryptDataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptDataResponseDto from a JSON string
decrypt_data_response_dto_instance = DecryptDataResponseDto.from_json(json)
# print the JSON string representation of the object
print(DecryptDataResponseDto.to_json())

# convert the object into a dict
decrypt_data_response_dto_dict = decrypt_data_response_dto_instance.to_dict()
# create an instance of DecryptDataResponseDto from a dict
decrypt_data_response_dto_from_dict = DecryptDataResponseDto.from_dict(decrypt_data_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


