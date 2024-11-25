# ApprovalUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**history** | **bool** |  | [optional] 

## Example

```python
from pyCZERTAINLY.models.approval_user_dto import ApprovalUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalUserDto from a JSON string
approval_user_dto_instance = ApprovalUserDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalUserDto.to_json())

# convert the object into a dict
approval_user_dto_dict = approval_user_dto_instance.to_dict()
# create an instance of ApprovalUserDto from a dict
approval_user_dto_from_dict = ApprovalUserDto.from_dict(approval_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


