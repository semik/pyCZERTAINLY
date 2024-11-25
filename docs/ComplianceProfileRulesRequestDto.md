# ComplianceProfileRulesRequestDto

Rules to be associated with the Compliance Profile. Profiles can be created without rules and can be added later

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **str** | UUID of the Compliance Provider | 
**kind** | **str** | Kind of the Compliance Provider | 
**rules** | [**List[ComplianceRequestRulesDto]**](ComplianceRequestRulesDto.md) | Rules for new Compliance Profiles | [optional] 
**groups** | **List[str]** | Groups for Compliance Profile | [optional] 

## Example

```python
from openapi_client.models.compliance_profile_rules_request_dto import ComplianceProfileRulesRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceProfileRulesRequestDto from a JSON string
compliance_profile_rules_request_dto_instance = ComplianceProfileRulesRequestDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceProfileRulesRequestDto.to_json())

# convert the object into a dict
compliance_profile_rules_request_dto_dict = compliance_profile_rules_request_dto_instance.to_dict()
# create an instance of ComplianceProfileRulesRequestDto from a dict
compliance_profile_rules_request_dto_from_dict = ComplianceProfileRulesRequestDto.from_dict(compliance_profile_rules_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


