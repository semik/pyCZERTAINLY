# UserIdentificationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_content** | **str** | Base64 Content of the certificate | [optional] 
**authentication_token** | **str** | Authentication Token | [optional] 

## Example

```python
from pyCZERTAINLY.models.user_identification_request_dto import UserIdentificationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentificationRequestDto from a JSON string
user_identification_request_dto_instance = UserIdentificationRequestDto.from_json(json)
# print the JSON string representation of the object
print(UserIdentificationRequestDto.to_json())

# convert the object into a dict
user_identification_request_dto_dict = user_identification_request_dto_instance.to_dict()
# create an instance of UserIdentificationRequestDto from a dict
user_identification_request_dto_from_dict = UserIdentificationRequestDto.from_dict(user_identification_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


