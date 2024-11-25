# RaProfileAssociationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ra_profile_uuids** | **List[str]** | List of UUIDs of RA Profiles to be associated | 

## Example

```python
from openapi_client.models.ra_profile_association_request_dto import RaProfileAssociationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RaProfileAssociationRequestDto from a JSON string
ra_profile_association_request_dto_instance = RaProfileAssociationRequestDto.from_json(json)
# print the JSON string representation of the object
print(RaProfileAssociationRequestDto.to_json())

# convert the object into a dict
ra_profile_association_request_dto_dict = ra_profile_association_request_dto_instance.to_dict()
# create an instance of RaProfileAssociationRequestDto from a dict
ra_profile_association_request_dto_from_dict = RaProfileAssociationRequestDto.from_dict(ra_profile_association_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


