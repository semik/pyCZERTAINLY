# ApprovalProfileUpdateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the Approval profile | [optional] 
**expiry** | **int** | Expiration of the Approval profile in hours | [optional] 
**approval_steps** | [**List[ApprovalStepRequestDto]**](ApprovalStepRequestDto.md) | List of Approval steps for the Approval profile | 

## Example

```python
from openapi_client.models.approval_profile_update_request_dto import ApprovalProfileUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalProfileUpdateRequestDto from a JSON string
approval_profile_update_request_dto_instance = ApprovalProfileUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalProfileUpdateRequestDto.to_json())

# convert the object into a dict
approval_profile_update_request_dto_dict = approval_profile_update_request_dto_instance.to_dict()
# create an instance of ApprovalProfileUpdateRequestDto from a dict
approval_profile_update_request_dto_from_dict = ApprovalProfileUpdateRequestDto.from_dict(approval_profile_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


