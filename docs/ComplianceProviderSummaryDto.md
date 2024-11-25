# ComplianceProviderSummaryDto

Rules summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_name** | **str** | Name of the Compliance Provider | 
**number_of_rules** | **int** | Number of rules for the Provider | [optional] 
**number_of_groups** | **int** | Number of groups for the Provider | [optional] 

## Example

```python
from pyCZERTAINLY.models.compliance_provider_summary_dto import ComplianceProviderSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceProviderSummaryDto from a JSON string
compliance_provider_summary_dto_instance = ComplianceProviderSummaryDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceProviderSummaryDto.to_json())

# convert the object into a dict
compliance_provider_summary_dto_dict = compliance_provider_summary_dto_instance.to_dict()
# create an instance of ComplianceProviderSummaryDto from a dict
compliance_provider_summary_dto_from_dict = ComplianceProviderSummaryDto.from_dict(compliance_provider_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


