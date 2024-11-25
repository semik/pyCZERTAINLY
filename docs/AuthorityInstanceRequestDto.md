# AuthorityInstanceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Authority instance name | 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Authority instance Attributes | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**connector_uuid** | **str** | UUID of Authority provider | 
**kind** | **str** | Authority instance Kind | 

## Example

```python
from pyCZERTAINLY.models.authority_instance_request_dto import AuthorityInstanceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorityInstanceRequestDto from a JSON string
authority_instance_request_dto_instance = AuthorityInstanceRequestDto.from_json(json)
# print the JSON string representation of the object
print(AuthorityInstanceRequestDto.to_json())

# convert the object into a dict
authority_instance_request_dto_dict = authority_instance_request_dto_instance.to_dict()
# create an instance of AuthorityInstanceRequestDto from a dict
authority_instance_request_dto_from_dict = AuthorityInstanceRequestDto.from_dict(authority_instance_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


