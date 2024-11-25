# ApprovalProfileResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_per_page** | **int** | Number of entries per page | 
**page_number** | **int** | Page number for the request | 
**total_pages** | **int** | Number of pages available | 
**total_items** | **int** | Number of items available | 
**approval_profiles** | [**List[ApprovalProfileDto]**](ApprovalProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.approval_profile_response_dto import ApprovalProfileResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalProfileResponseDto from a JSON string
approval_profile_response_dto_instance = ApprovalProfileResponseDto.from_json(json)
# print the JSON string representation of the object
print(ApprovalProfileResponseDto.to_json())

# convert the object into a dict
approval_profile_response_dto_dict = approval_profile_response_dto_instance.to_dict()
# create an instance of ApprovalProfileResponseDto from a dict
approval_profile_response_dto_from_dict = ApprovalProfileResponseDto.from_dict(approval_profile_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


