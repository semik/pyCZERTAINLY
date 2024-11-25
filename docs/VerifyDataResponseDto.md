# VerifyDataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verifications** | [**List[VerificationResponseData]**](VerificationResponseData.md) | Signatures | 

## Example

```python
from openapi_client.models.verify_data_response_dto import VerifyDataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyDataResponseDto from a JSON string
verify_data_response_dto_instance = VerifyDataResponseDto.from_json(json)
# print the JSON string representation of the object
print(VerifyDataResponseDto.to_json())

# convert the object into a dict
verify_data_response_dto_dict = verify_data_response_dto_instance.to_dict()
# create an instance of VerifyDataResponseDto from a dict
verify_data_response_dto_from_dict = VerifyDataResponseDto.from_dict(verify_data_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


