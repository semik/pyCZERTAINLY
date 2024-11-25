# ComplianceGroupsDto

Groups associated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the group | [optional] 

## Example

```python
from openapi_client.models.compliance_groups_dto import ComplianceGroupsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceGroupsDto from a JSON string
compliance_groups_dto_instance = ComplianceGroupsDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceGroupsDto.to_json())

# convert the object into a dict
compliance_groups_dto_dict = compliance_groups_dto_instance.to_dict()
# create an instance of ComplianceGroupsDto from a dict
compliance_groups_dto_from_dict = ComplianceGroupsDto.from_dict(compliance_groups_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


