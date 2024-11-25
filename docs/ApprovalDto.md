# ApprovalDto

List of the Approvals

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_uuid** | **str** | UUID of the Approval | 
**creator_uuid** | **str** | UUID of the user that requested approval | 
**creator_username** | **str** | Username of the user that requested approval | [optional] 
**version** | **int** | Version of the Approval profile | 
**created_at** | **datetime** | Creation date of the Approval | 
**expiry_at** | **datetime** | Expiry date of the Approval | 
**closed_at** | **datetime** | Date of resolution of the Approval | [optional] 
**status** | **str** | Status of the Approval | 
**resource** | [**Resource**](Resource.md) |  | 
**resource_action** | **str** | Resource action of the Approval | 
**object_uuid** | **str** | UUID of the target object of the Approval | 
**approval_profile_name** | **str** | Name of the Approval profile | 
**approval_profile_uuid** | **str** | UUID of the Approval profile | 

## Example

```python
from openapi_client.models.approval_dto import ApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalDto from a JSON string
approval_dto_instance = ApprovalDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalDto.to_json())

# convert the object into a dict
approval_dto_dict = approval_dto_instance.to_dict()
# create an instance of ApprovalDto from a dict
approval_dto_from_dict = ApprovalDto.from_dict(approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


