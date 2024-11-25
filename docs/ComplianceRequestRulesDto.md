# ComplianceRequestRulesDto

Rules for new Compliance Profiles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the rule | 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | Attributes for the rule | [optional] 

## Example

```python
from pyCZERTAINLY.models.compliance_request_rules_dto import ComplianceRequestRulesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRequestRulesDto from a JSON string
compliance_request_rules_dto_instance = ComplianceRequestRulesDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceRequestRulesDto.to_json())

# convert the object into a dict
compliance_request_rules_dto_dict = compliance_request_rules_dto_instance.to_dict()
# create an instance of ComplianceRequestRulesDto from a dict
compliance_request_rules_dto_from_dict = ComplianceRequestRulesDto.from_dict(compliance_request_rules_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


