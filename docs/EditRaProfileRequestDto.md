# EditRaProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of RA Profile | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes for RA Profile | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | [optional] 

## Example

```python
from pyCZERTAINLY.models.edit_ra_profile_request_dto import EditRaProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditRaProfileRequestDto from a JSON string
edit_ra_profile_request_dto_instance = EditRaProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(EditRaProfileRequestDto.to_json())

# convert the object into a dict
edit_ra_profile_request_dto_dict = edit_ra_profile_request_dto_instance.to_dict()
# create an instance of EditRaProfileRequestDto from a dict
edit_ra_profile_request_dto_from_dict = EditRaProfileRequestDto.from_dict(edit_ra_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


