# ApprovalProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Approval profile | 
**description** | **str** | Description of the Approval profile | [optional] 
**enabled** | **bool** | Enable of the Approval profile | 
**expiry** | **int** | Expiration of the Approval profile in hours | [optional] 
**approval_steps** | [**List[ApprovalStepRequestDto]**](ApprovalStepRequestDto.md) | List of Approval steps for the Approval profile | 

## Example

```python
from openapi_client.models.approval_profile_request_dto import ApprovalProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalProfileRequestDto from a JSON string
approval_profile_request_dto_instance = ApprovalProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalProfileRequestDto.to_json())

# convert the object into a dict
approval_profile_request_dto_dict = approval_profile_request_dto_instance.to_dict()
# create an instance of ApprovalProfileRequestDto from a dict
approval_profile_request_dto_from_dict = ApprovalProfileRequestDto.from_dict(approval_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


