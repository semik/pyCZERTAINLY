# AddTokenProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Token Profile name | 
**description** | **str** | Token Profile description | [optional] 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to create Token Profile | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | [optional] [default to False]
**usage** | [**List[KeyUsage]**](KeyUsage.md) | Usages for the Key | [optional] 

## Example

```python
from pyCZERTAINLY.models.add_token_profile_request_dto import AddTokenProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddTokenProfileRequestDto from a JSON string
add_token_profile_request_dto_instance = AddTokenProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(AddTokenProfileRequestDto.to_json())

# convert the object into a dict
add_token_profile_request_dto_dict = add_token_profile_request_dto_instance.to_dict()
# create an instance of AddTokenProfileRequestDto from a dict
add_token_profile_request_dto_from_dict = AddTokenProfileRequestDto.from_dict(add_token_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


