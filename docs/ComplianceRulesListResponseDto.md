# ComplianceRulesListResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_name** | **str** | Name of the Compliance Provider | 
**connector_uuid** | **str** | UUID of the Compliance Provider | 
**kind** | **str** | Kind of the Compliance Provider | 
**rules** | [**List[ComplianceRulesResponseDto]**](ComplianceRulesResponseDto.md) | Rules from Compliance Provider | 

## Example

```python
from pyCZERTAINLY.models.compliance_rules_list_response_dto import ComplianceRulesListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRulesListResponseDto from a JSON string
compliance_rules_list_response_dto_instance = ComplianceRulesListResponseDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceRulesListResponseDto.to_json())

# convert the object into a dict
compliance_rules_list_response_dto_dict = compliance_rules_list_response_dto_instance.to_dict()
# create an instance of ComplianceRulesListResponseDto from a dict
compliance_rules_list_response_dto_from_dict = ComplianceRulesListResponseDto.from_dict(compliance_rules_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


