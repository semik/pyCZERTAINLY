# ClientCertificateDataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_data** | **str** | Base64 encoded Certificate content | [optional] 
**uuid** | **str** | UUID of Certificate | 

## Example

```python
from pyCZERTAINLY.models.client_certificate_data_response_dto import ClientCertificateDataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificateDataResponseDto from a JSON string
client_certificate_data_response_dto_instance = ClientCertificateDataResponseDto.from_json(json)
# print the JSON string representation of the object
print(ClientCertificateDataResponseDto.to_json())

# convert the object into a dict
client_certificate_data_response_dto_dict = client_certificate_data_response_dto_instance.to_dict()
# create an instance of ClientCertificateDataResponseDto from a dict
client_certificate_data_response_dto_from_dict = ClientCertificateDataResponseDto.from_dict(client_certificate_data_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


