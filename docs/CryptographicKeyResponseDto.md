# CryptographicKeyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cryptographic_keys** | [**List[KeyItemDto]**](KeyItemDto.md) | Cryptographic Keys | 
**items_per_page** | **int** | Number of entries per page | 
**page_number** | **int** | Page number for the request | 
**total_pages** | **int** | Number of pages available | 
**total_items** | **int** | Number of items available | 

## Example

```python
from pyCZERTAINLY.models.cryptographic_key_response_dto import CryptographicKeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CryptographicKeyResponseDto from a JSON string
cryptographic_key_response_dto_instance = CryptographicKeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(CryptographicKeyResponseDto.to_json())

# convert the object into a dict
cryptographic_key_response_dto_dict = cryptographic_key_response_dto_instance.to_dict()
# create an instance of CryptographicKeyResponseDto from a dict
cryptographic_key_response_dto_from_dict = CryptographicKeyResponseDto.from_dict(cryptographic_key_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


