# ActivateScepForRaProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to issue Certificate | 

## Example

```python
from pyCZERTAINLY.models.activate_scep_for_ra_profile_request_dto import ActivateScepForRaProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateScepForRaProfileRequestDto from a JSON string
activate_scep_for_ra_profile_request_dto_instance = ActivateScepForRaProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(ActivateScepForRaProfileRequestDto.to_json())

# convert the object into a dict
activate_scep_for_ra_profile_request_dto_dict = activate_scep_for_ra_profile_request_dto_instance.to_dict()
# create an instance of ActivateScepForRaProfileRequestDto from a dict
activate_scep_for_ra_profile_request_dto_from_dict = ActivateScepForRaProfileRequestDto.from_dict(activate_scep_for_ra_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


