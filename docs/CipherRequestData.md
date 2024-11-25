# CipherRequestData

Encrypted/decrypted data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Base64 encoded encrypted/decrypted data | 
**identifier** | **str** | Custom identifier of the data, that should be the same as in the request, if available | [optional] 

## Example

```python
from pyCZERTAINLY.models.cipher_request_data import CipherRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CipherRequestData from a JSON string
cipher_request_data_instance = CipherRequestData.from_json(json)
# print the JSON string representation of the object
print(CipherRequestData.to_json())

# convert the object into a dict
cipher_request_data_dict = cipher_request_data_instance.to_dict()
# create an instance of CipherRequestData from a dict
cipher_request_data_from_dict = CipherRequestData.from_dict(cipher_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


