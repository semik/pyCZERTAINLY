# ActivateAcmeForRaProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to issue Certificate | 
**revoke_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to revoke Certificate | 

## Example

```python
from openapi_client.models.activate_acme_for_ra_profile_request_dto import ActivateAcmeForRaProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateAcmeForRaProfileRequestDto from a JSON string
activate_acme_for_ra_profile_request_dto_instance = ActivateAcmeForRaProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(ActivateAcmeForRaProfileRequestDto.to_json())

# convert the object into a dict
activate_acme_for_ra_profile_request_dto_dict = activate_acme_for_ra_profile_request_dto_instance.to_dict()
# create an instance of ActivateAcmeForRaProfileRequestDto from a dict
activate_acme_for_ra_profile_request_dto_from_dict = ActivateAcmeForRaProfileRequestDto.from_dict(activate_acme_for_ra_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


