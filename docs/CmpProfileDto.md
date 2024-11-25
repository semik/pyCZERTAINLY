# CmpProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**variant** | **str** | Variant of the CMP Profile | 
**description** | **str** | CMP Profile description | [optional] 
**ra_profile** | [**SimplifiedRaProfileDto**](SimplifiedRaProfileDto.md) |  | [optional] 
**cmp_url** | **str** | CMP URL | [optional] 

## Example

```python
from pyCZERTAINLY.models.cmp_profile_dto import CmpProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of CmpProfileDto from a JSON string
cmp_profile_dto_instance = CmpProfileDto.from_json(json)
# print the JSON string representation of the object
print(CmpProfileDto.to_json())

# convert the object into a dict
cmp_profile_dto_dict = cmp_profile_dto_instance.to_dict()
# create an instance of CmpProfileDto from a dict
cmp_profile_dto_from_dict = CmpProfileDto.from_dict(cmp_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


