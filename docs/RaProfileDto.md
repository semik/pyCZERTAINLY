# RaProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of RA Profile | [optional] 
**authority_instance_uuid** | **str** | UUID of Authority provider | 
**authority_instance_name** | **str** | Name of Authority instance | 
**legacy_authority** | **bool** | Has Authority of legacy authority provider | [optional] 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of RA Profiles attributes | [optional] 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 
**enabled_protocols** | **List[str]** | List of protocols enabled | [optional] 

## Example

```python
from pyCZERTAINLY.models.ra_profile_dto import RaProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of RaProfileDto from a JSON string
ra_profile_dto_instance = RaProfileDto.from_json(json)
# print the JSON string representation of the object
print(RaProfileDto.to_json())

# convert the object into a dict
ra_profile_dto_dict = ra_profile_dto_instance.to_dict()
# create an instance of RaProfileDto from a dict
ra_profile_dto_from_dict = RaProfileDto.from_dict(ra_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


