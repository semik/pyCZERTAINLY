# ApprovalStepRecipientDto

List of the approval recipient related for this step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_recipient_uuid** | **str** | UUID of the approval recipient | 
**user_uuid** | **str** | UUID of the recipient user | 
**username** | **str** | Username of the recipient | [optional] 
**created_at** | **datetime** | Creating date of the approval recipient | 
**closed_at** | **datetime** | Resolution date of the approval recipient | [optional] 
**status** | **str** | Status of the approval recipient | 
**comment** | **str** | Comment of the approval recipient | [optional] 

## Example

```python
from openapi_client.models.approval_step_recipient_dto import ApprovalStepRecipientDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalStepRecipientDto from a JSON string
approval_step_recipient_dto_instance = ApprovalStepRecipientDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalStepRecipientDto.to_json())

# convert the object into a dict
approval_step_recipient_dto_dict = approval_step_recipient_dto_instance.to_dict()
# create an instance of ApprovalStepRecipientDto from a dict
approval_step_recipient_dto_from_dict = ApprovalStepRecipientDto.from_dict(approval_step_recipient_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


