# ComplianceRuleDeletionRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **str** | UUID of the Compliance Provider | 
**kind** | **str** | Kind of the Compliance Provider | 
**rule_uuid** | **str** | UUID of the rule | 

## Example

```python
from openapi_client.models.compliance_rule_deletion_request_dto import ComplianceRuleDeletionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRuleDeletionRequestDto from a JSON string
compliance_rule_deletion_request_dto_instance = ComplianceRuleDeletionRequestDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceRuleDeletionRequestDto.to_json())

# convert the object into a dict
compliance_rule_deletion_request_dto_dict = compliance_rule_deletion_request_dto_instance.to_dict()
# create an instance of ComplianceRuleDeletionRequestDto from a dict
compliance_rule_deletion_request_dto_from_dict = ComplianceRuleDeletionRequestDto.from_dict(compliance_rule_deletion_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


