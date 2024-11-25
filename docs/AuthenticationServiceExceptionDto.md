# AuthenticationServiceExceptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | Status code of the HTTP Request | 
**code** | **str** | Code of the result | 
**message** | **str** | Exception message | 

## Example

```python
from pyCZERTAINLY.models.authentication_service_exception_dto import AuthenticationServiceExceptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationServiceExceptionDto from a JSON string
authentication_service_exception_dto_instance = AuthenticationServiceExceptionDto.from_json(json)
# print the JSON string representation of the object
print(AuthenticationServiceExceptionDto.to_json())

# convert the object into a dict
authentication_service_exception_dto_dict = authentication_service_exception_dto_instance.to_dict()
# create an instance of AuthenticationServiceExceptionDto from a dict
authentication_service_exception_dto_from_dict = AuthenticationServiceExceptionDto.from_dict(authentication_service_exception_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


