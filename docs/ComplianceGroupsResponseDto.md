# ComplianceGroupsResponseDto

Groups from Compliance Provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the group | 
**name** | **str** | Name of the group | 
**description** | **str** | Description of the group | [optional] 

## Example

```python
from openapi_client.models.compliance_groups_response_dto import ComplianceGroupsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceGroupsResponseDto from a JSON string
compliance_groups_response_dto_instance = ComplianceGroupsResponseDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceGroupsResponseDto.to_json())

# convert the object into a dict
compliance_groups_response_dto_dict = compliance_groups_response_dto_instance.to_dict()
# create an instance of ComplianceGroupsResponseDto from a dict
compliance_groups_response_dto_from_dict = ComplianceGroupsResponseDto.from_dict(compliance_groups_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


