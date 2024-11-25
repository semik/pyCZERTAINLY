# SimplifiedRaProfileDto

RA Profile associated to the Certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**authority_instance_uuid** | **str** | Authority Instance UUID | [optional] 

## Example

```python
from openapi_client.models.simplified_ra_profile_dto import SimplifiedRaProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedRaProfileDto from a JSON string
simplified_ra_profile_dto_instance = SimplifiedRaProfileDto.from_json(json)
# print the JSON string representation of the object
print(SimplifiedRaProfileDto.to_json())

# convert the object into a dict
simplified_ra_profile_dto_dict = simplified_ra_profile_dto_instance.to_dict()
# create an instance of SimplifiedRaProfileDto from a dict
simplified_ra_profile_dto_from_dict = SimplifiedRaProfileDto.from_dict(simplified_ra_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


