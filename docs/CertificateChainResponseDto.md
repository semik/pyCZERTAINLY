# CertificateChainResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete_chain** | **bool** | Indicator whether the chain returned is complete | 
**certificates** | [**List[CertificateDetailDto]**](CertificateDetailDto.md) | List of certificates in the chain | 

## Example

```python
from pyCZERTAINLY.models.certificate_chain_response_dto import CertificateChainResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateChainResponseDto from a JSON string
certificate_chain_response_dto_instance = CertificateChainResponseDto.from_json(json)
# print the JSON string representation of the object
print(CertificateChainResponseDto.to_json())

# convert the object into a dict
certificate_chain_response_dto_dict = certificate_chain_response_dto_instance.to_dict()
# create an instance of CertificateChainResponseDto from a dict
certificate_chain_response_dto_from_dict = CertificateChainResponseDto.from_dict(certificate_chain_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


