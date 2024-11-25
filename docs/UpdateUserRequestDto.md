# UpdateUserRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the user | [optional] 
**first_name** | **str** | First name of the user | [optional] 
**last_name** | **str** | Last name of the user | [optional] 
**email** | **str** | Email of the user | 
**group_uuids** | **List[str]** | Groups UUIDs of the user (set to empty list to remove certificate from all groups) | [optional] 
**certificate_data** | **str** | Base64 Content of the admin certificate | [optional] 
**certificate_uuid** | **str** | UUID of the existing certificate in the Inventory. Mandatory if certificate is not provided | [optional] 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.update_user_request_dto import UpdateUserRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestDto from a JSON string
update_user_request_dto_instance = UpdateUserRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestDto.to_json())

# convert the object into a dict
update_user_request_dto_dict = update_user_request_dto_instance.to_dict()
# create an instance of UpdateUserRequestDto from a dict
update_user_request_dto_from_dict = UpdateUserRequestDto.from_dict(update_user_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


