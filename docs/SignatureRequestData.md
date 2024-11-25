# SignatureRequestData

Signatures to verify

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Base64 encoded data to be signed or verified | 
**identifier** | **str** | Custom identifier of the data, that should be the same as in the request, if available | [optional] 

## Example

```python
from pyCZERTAINLY.models.signature_request_data import SignatureRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureRequestData from a JSON string
signature_request_data_instance = SignatureRequestData.from_json(json)
# print the JSON string representation of the object
print(SignatureRequestData.to_json())

# convert the object into a dict
signature_request_data_dict = signature_request_data_instance.to_dict()
# create an instance of SignatureRequestData from a dict
signature_request_data_from_dict = SignatureRequestData.from_dict(signature_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


