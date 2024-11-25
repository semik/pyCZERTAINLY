# AuthorityInstanceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Authority instance Attributes | 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 
**status** | **str** | Status of Authority instance | 
**connector_uuid** | **str** | UUID of Authority provider | 
**connector_name** | **str** | Name of Authority provider | 
**kind** | **str** | Authority Instance Kind | 

## Example

```python
from pyCZERTAINLY.models.authority_instance_dto import AuthorityInstanceDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorityInstanceDto from a JSON string
authority_instance_dto_instance = AuthorityInstanceDto.from_json(json)
# print the JSON string representation of the object
print(AuthorityInstanceDto.to_json())

# convert the object into a dict
authority_instance_dto_dict = authority_instance_dto_instance.to_dict()
# create an instance of AuthorityInstanceDto from a dict
authority_instance_dto_from_dict = AuthorityInstanceDto.from_dict(authority_instance_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


