# ApprovalStepRequestDto

List of Approval steps for the Approval profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **str** | UUID of the responsible user to approve action in approval step | [optional] 
**role_uuid** | **str** | UUID of the responsible role of the users to approve action in approval step | [optional] 
**group_uuid** | **str** | UUID of the responsible group of the users to approve action in approval step | [optional] 
**description** | **str** | Description of the approval step | [optional] 
**order** | **int** | Order of the position in the approval steps flow | 
**required_approvals** | **int** | Count of the required approvals for the approval step, by default there is 1 approval needed. | [optional] 

## Example

```python
from openapi_client.models.approval_step_request_dto import ApprovalStepRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalStepRequestDto from a JSON string
approval_step_request_dto_instance = ApprovalStepRequestDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalStepRequestDto.to_json())

# convert the object into a dict
approval_step_request_dto_dict = approval_step_request_dto_instance.to_dict()
# create an instance of ApprovalStepRequestDto from a dict
approval_step_request_dto_from_dict = ApprovalStepRequestDto.from_dict(approval_step_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


