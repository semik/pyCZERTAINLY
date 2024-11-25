# ComplianceProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the Compliance Profile | [optional] 
**rules** | [**List[ComplianceConnectorAndRulesDto]**](ComplianceConnectorAndRulesDto.md) | List of rules | 
**groups** | [**List[ComplianceConnectorAndGroupsDto]**](ComplianceConnectorAndGroupsDto.md) | List of groups | 
**ra_profiles** | [**List[SimplifiedRaProfileDto]**](SimplifiedRaProfileDto.md) | List of associated RA Profiles | [optional] 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.compliance_profile_dto import ComplianceProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceProfileDto from a JSON string
compliance_profile_dto_instance = ComplianceProfileDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceProfileDto.to_json())

# convert the object into a dict
compliance_profile_dto_dict = compliance_profile_dto_instance.to_dict()
# create an instance of ComplianceProfileDto from a dict
compliance_profile_dto_from_dict = ComplianceProfileDto.from_dict(compliance_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


