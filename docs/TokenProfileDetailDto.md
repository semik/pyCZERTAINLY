# TokenProfileDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of Token Profile | [optional] 
**token_instance_uuid** | **str** | UUID of Token Instance | 
**token_instance_name** | **str** | Name of Token instance | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Token Profile attributes | 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 
**token_instance_status** | [**TokenInstanceStatus**](TokenInstanceStatus.md) |  | 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**usages** | [**List[KeyUsage]**](KeyUsage.md) | Usages for the Keys assoiated to the profile | 

## Example

```python
from pyCZERTAINLY.models.token_profile_detail_dto import TokenProfileDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of TokenProfileDetailDto from a JSON string
token_profile_detail_dto_instance = TokenProfileDetailDto.from_json(json)
# print the JSON string representation of the object
print(TokenProfileDetailDto.to_json())

# convert the object into a dict
token_profile_detail_dto_dict = token_profile_detail_dto_instance.to_dict()
# create an instance of TokenProfileDetailDto from a dict
token_profile_detail_dto_from_dict = TokenProfileDetailDto.from_dict(token_profile_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


