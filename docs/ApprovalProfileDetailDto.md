# ApprovalProfileDetailDto


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
**approval_steps** | [**List[ApprovalStepDto]**](ApprovalStepDto.md) | List of Approval steps for the Approval profile | 

## Example

```python
from pyCZERTAINLY.models.approval_profile_detail_dto import ApprovalProfileDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalProfileDetailDto from a JSON string
approval_profile_detail_dto_instance = ApprovalProfileDetailDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalProfileDetailDto.to_json())

# convert the object into a dict
approval_profile_detail_dto_dict = approval_profile_detail_dto_instance.to_dict()
# create an instance of ApprovalProfileDetailDto from a dict
approval_profile_detail_dto_from_dict = ApprovalProfileDetailDto.from_dict(approval_profile_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


