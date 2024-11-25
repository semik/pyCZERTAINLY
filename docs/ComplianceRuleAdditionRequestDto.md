# ComplianceRuleAdditionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **str** | UUID of the Compliance Provider | 
**kind** | **str** | Kind of the Compliance Provider | 
**rule_uuid** | **str** | UUID of the rule | 
**attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | Attributes for the rule | [optional] 

## Example

```python
from openapi_client.models.compliance_rule_addition_request_dto import ComplianceRuleAdditionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleAdditionRequestDto from a JSON string
compliance_rule_addition_request_dto_instance = ComplianceRuleAdditionRequestDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceRuleAdditionRequestDto.to_json())

# convert the object into a dict
compliance_rule_addition_request_dto_dict = compliance_rule_addition_request_dto_instance.to_dict()
# create an instance of ComplianceRuleAdditionRequestDto from a dict
compliance_rule_addition_request_dto_from_dict = ComplianceRuleAdditionRequestDto.from_dict(compliance_rule_addition_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


