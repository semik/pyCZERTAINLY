# VerificationResponseData

Signatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | Data to be signed or verified | 
**identifier** | **str** | Custom identifier of the data, that should be the same as in the request, if available | [optional] 
**details** | **object** | Additional details for the result, for example reason, etc. | [optional] 

## Example

```python
from pyCZERTAINLY.models.verification_response_data import VerificationResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationResponseData from a JSON string
verification_response_data_instance = VerificationResponseData.from_json(json)
# print the JSON string representation of the object
print(VerificationResponseData.to_json())

# convert the object into a dict
verification_response_data_dict = verification_response_data_instance.to_dict()
# create an instance of VerificationResponseData from a dict
verification_response_data_from_dict = VerificationResponseData.from_dict(verification_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


