# UserApprovalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.user_approval_dto import UserApprovalDto

# TODO update the JSON string below
json = "{}"
# create an instance of UserApprovalDto from a JSON string
user_approval_dto_instance = UserApprovalDto.from_json(json)
# print the JSON string representation of the object
print(UserApprovalDto.to_json())

# convert the object into a dict
user_approval_dto_dict = user_approval_dto_instance.to_dict()
# create an instance of UserApprovalDto from a dict
user_approval_dto_from_dict = UserApprovalDto.from_dict(user_approval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


