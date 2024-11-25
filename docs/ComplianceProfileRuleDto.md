# ComplianceProfileRuleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the rule | [optional] 
**connector_name** | **str** | Connector Name | 
**connector_uuid** | **str** | Connector UUID | 
**kind** | **str** | Connector Kind | 
**group_uuid** | **str** | Group UUID | [optional] 
**certificate_type** | [**CertificateType**](CertificateType.md) |  | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of attributes for the rule | 
**compliance_profile_uuid** | **str** | UUID of the Compliance Profile | 
**compliance_profile_name** | **str** | Name of the Compliance Profile | 

## Example

```python
from pyCZERTAINLY.models.compliance_profile_rule_dto import ComplianceProfileRuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceProfileRuleDto from a JSON string
compliance_profile_rule_dto_instance = ComplianceProfileRuleDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceProfileRuleDto.to_json())

# convert the object into a dict
compliance_profile_rule_dto_dict = compliance_profile_rule_dto_instance.to_dict()
# create an instance of ComplianceProfileRuleDto from a dict
compliance_profile_rule_dto_from_dict = ComplianceProfileRuleDto.from_dict(compliance_profile_rule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


