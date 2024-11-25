# CipherResponseData

Encrypted data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Base64 encoded encrypted/decrypted data | 
**identifier** | **str** | Custom identifier of the data, that should be the same as in the request, if available | [optional] 
**details** | **object** | Additional details of the data, for example, the data type, error handling, etc. | [optional] 

## Example

```python
from pyCZERTAINLY.models.cipher_response_data import CipherResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CipherResponseData from a JSON string
cipher_response_data_instance = CipherResponseData.from_json(json)
# print the JSON string representation of the object
print(CipherResponseData.to_json())

# convert the object into a dict
cipher_response_data_dict = cipher_response_data_instance.to_dict()
# create an instance of CipherResponseData from a dict
cipher_response_data_from_dict = CipherResponseData.from_dict(cipher_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


