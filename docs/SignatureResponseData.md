# SignatureResponseData

Signatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Base64 encoded signature data | 
**identifier** | **str** | Custom identifier of the data, that should be the same as in the request, if available | [optional] 
**details** | **object** | Additional details of the data, for example, the data type, error handling, etc. | [optional] 

## Example

```python
from pyCZERTAINLY.models.signature_response_data import SignatureResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureResponseData from a JSON string
signature_response_data_instance = SignatureResponseData.from_json(json)
# print the JSON string representation of the object
print(SignatureResponseData.to_json())

# convert the object into a dict
signature_response_data_dict = signature_response_data_instance.to_dict()
# create an instance of SignatureResponseData from a dict
signature_response_data_from_dict = SignatureResponseData.from_dict(signature_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


