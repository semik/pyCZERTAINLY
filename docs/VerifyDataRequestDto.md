# VerifyDataRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of signature Attributes | 
**data** | [**List[SignatureRequestData]**](SignatureRequestData.md) | Data to be signed | 
**signatures** | [**List[SignatureRequestData]**](SignatureRequestData.md) | Signatures to verify | 

## Example

```python
from pyCZERTAINLY.models.verify_data_request_dto import VerifyDataRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyDataRequestDto from a JSON string
verify_data_request_dto_instance = VerifyDataRequestDto.from_json(json)
# print the JSON string representation of the object
print(VerifyDataRequestDto.to_json())

# convert the object into a dict
verify_data_request_dto_dict = verify_data_request_dto_instance.to_dict()
# create an instance of VerifyDataRequestDto from a dict
verify_data_request_dto_from_dict = VerifyDataRequestDto.from_dict(verify_data_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


