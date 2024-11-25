# AuthorityInstanceUpdateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Authority instance Attributes | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.authority_instance_update_request_dto import AuthorityInstanceUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorityInstanceUpdateRequestDto from a JSON string
authority_instance_update_request_dto_instance = AuthorityInstanceUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(AuthorityInstanceUpdateRequestDto.to_json())

# convert the object into a dict
authority_instance_update_request_dto_dict = authority_instance_update_request_dto_instance.to_dict()
# create an instance of AuthorityInstanceUpdateRequestDto from a dict
authority_instance_update_request_dto_from_dict = AuthorityInstanceUpdateRequestDto.from_dict(authority_instance_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


