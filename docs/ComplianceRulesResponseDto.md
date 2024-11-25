# ComplianceRulesResponseDto

Rules from Compliance Provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the rule | 
**group_uuid** | **str** | UUID of the group to which the rule belongs to | [optional] 
**name** | **str** | Name of the rule | 
**certificate_type** | [**CertificateType**](CertificateType.md) |  | 
**attributes** | [**List[BaseAttributeDto]**](BaseAttributeDto.md) | Rule attributes | [optional] 
**description** | **str** | Description of the rule | [optional] 

## Example

```python
from openapi_client.models.compliance_rules_response_dto import ComplianceRulesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRulesResponseDto from a JSON string
compliance_rules_response_dto_instance = ComplianceRulesResponseDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceRulesResponseDto.to_json())

# convert the object into a dict
compliance_rules_response_dto_dict = compliance_rules_response_dto_instance.to_dict()
# create an instance of ComplianceRulesResponseDto from a dict
compliance_rules_response_dto_from_dict = ComplianceRulesResponseDto.from_dict(compliance_rules_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


