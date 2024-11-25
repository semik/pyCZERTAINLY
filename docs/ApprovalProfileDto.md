# ApprovalProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the Approval profile | 
**name** | **str** | Name of the Approval profile | 
**version** | **int** | Version of the Approval profile | 
**description** | **str** | Description of the Approval profile | [optional] 
**enabled** | **bool** | Enable of the Approval profile | 
**expiry** | **int** | Expiration of the Approval profile in hours | [optional] 
**number_of_steps** | **int** | Number of the Approval profile steps | 
**associations** | **int** | Number of associated objects | 

## Example

```python
from openapi_client.models.approval_profile_dto import ApprovalProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalProfileDto from a JSON string
approval_profile_dto_instance = ApprovalProfileDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalProfileDto.to_json())

# convert the object into a dict
approval_profile_dto_dict = approval_profile_dto_instance.to_dict()
# create an instance of ApprovalProfileDto from a dict
approval_profile_dto_from_dict = ApprovalProfileDto.from_dict(approval_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


