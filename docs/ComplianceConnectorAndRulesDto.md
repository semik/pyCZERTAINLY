# ComplianceConnectorAndRulesDto

List of rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_name** | **str** | Name of the Compliance Provider | [optional] 
**connector_uuid** | **str** | UUID of the Compliance Provider | [optional] 
**kind** | **str** | Kind of the Compliance Provider | [optional] 
**rules** | [**List[ComplianceRulesDto]**](ComplianceRulesDto.md) | Rules associated | [optional] 

## Example

```python
from pyCZERTAINLY.models.compliance_connector_and_rules_dto import ComplianceConnectorAndRulesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceConnectorAndRulesDto from a JSON string
compliance_connector_and_rules_dto_instance = ComplianceConnectorAndRulesDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceConnectorAndRulesDto.to_json())

# convert the object into a dict
compliance_connector_and_rules_dto_dict = compliance_connector_and_rules_dto_instance.to_dict()
# create an instance of ComplianceConnectorAndRulesDto from a dict
compliance_connector_and_rules_dto_from_dict = ComplianceConnectorAndRulesDto.from_dict(compliance_connector_and_rules_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


