# AddRaProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | RA Profile name | 
**description** | **str** | RA Profile description | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to create RA Profile | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | [optional] [default to False]

## Example

```python
from pyCZERTAINLY.models.add_ra_profile_request_dto import AddRaProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddRaProfileRequestDto from a JSON string
add_ra_profile_request_dto_instance = AddRaProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(AddRaProfileRequestDto.to_json())

# convert the object into a dict
add_ra_profile_request_dto_dict = add_ra_profile_request_dto_instance.to_dict()
# create an instance of AddRaProfileRequestDto from a dict
add_ra_profile_request_dto_from_dict = AddRaProfileRequestDto.from_dict(add_ra_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


