# AddUserRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username of the user | 
**description** | **str** | Description of the user | [optional] 
**first_name** | **str** | First name of the user | [optional] 
**last_name** | **str** | Last name of the user | [optional] 
**email** | **str** | Email of the user | [optional] 
**group_uuids** | **List[str]** | Groups UUIDs of the user | [optional] 
**enabled** | **bool** | Status of the user. True &#x3D; Enabled, False &#x3D; Disabled | [optional] 
**certificate_data** | **str** | Base64 Content of the user certificate | [optional] 
**certificate_uuid** | **str** | UUID of the existing certificate in the Inventory | [optional] 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.add_user_request_dto import AddUserRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserRequestDto from a JSON string
add_user_request_dto_instance = AddUserRequestDto.from_json(json)
# print the JSON string representation of the object
print(AddUserRequestDto.to_json())

# convert the object into a dict
add_user_request_dto_dict = add_user_request_dto_instance.to_dict()
# create an instance of AddUserRequestDto from a dict
add_user_request_dto_from_dict = AddUserRequestDto.from_dict(add_user_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


