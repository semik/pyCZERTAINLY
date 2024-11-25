# ComplianceRulesDto

Rules associated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the rule | [optional] 
**certificate_type** | [**CertificateType**](CertificateType.md) |  | 
**attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | Attributes of the rule | [optional] 

## Example

```python
from openapi_client.models.compliance_rules_dto import ComplianceRulesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRulesDto from a JSON string
compliance_rules_dto_instance = ComplianceRulesDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceRulesDto.to_json())

# convert the object into a dict
compliance_rules_dto_dict = compliance_rules_dto_instance.to_dict()
# create an instance of ComplianceRulesDto from a dict
compliance_rules_dto_from_dict = ComplianceRulesDto.from_dict(compliance_rules_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


