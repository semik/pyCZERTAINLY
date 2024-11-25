# ActivateCmpForRaProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to issue Certificate | 
**revoke_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to revoke Certificate | 

## Example

```python
from pyCZERTAINLY.models.activate_cmp_for_ra_profile_request_dto import ActivateCmpForRaProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateCmpForRaProfileRequestDto from a JSON string
activate_cmp_for_ra_profile_request_dto_instance = ActivateCmpForRaProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(ActivateCmpForRaProfileRequestDto.to_json())

# convert the object into a dict
activate_cmp_for_ra_profile_request_dto_dict = activate_cmp_for_ra_profile_request_dto_instance.to_dict()
# create an instance of ActivateCmpForRaProfileRequestDto from a dict
activate_cmp_for_ra_profile_request_dto_from_dict = ActivateCmpForRaProfileRequestDto.from_dict(activate_cmp_for_ra_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


