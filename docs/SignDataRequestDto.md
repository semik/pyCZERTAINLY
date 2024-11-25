# SignDataRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of signature Attributes | 
**data** | [**List[SignatureRequestData]**](SignatureRequestData.md) | Data to be signed | 

## Example

```python
from openapi_client.models.sign_data_request_dto import SignDataRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SignDataRequestDto from a JSON string
sign_data_request_dto_instance = SignDataRequestDto.from_json(json)
# print the JSON string representation of the object
print(SignDataRequestDto.to_json())

# convert the object into a dict
sign_data_request_dto_dict = sign_data_request_dto_instance.to_dict()
# create an instance of SignDataRequestDto from a dict
sign_data_request_dto_from_dict = SignDataRequestDto.from_dict(sign_data_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


