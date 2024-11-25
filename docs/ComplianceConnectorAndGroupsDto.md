# ComplianceConnectorAndGroupsDto

List of groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_name** | **str** | Name of the Compliance Provider | [optional] 
**connector_uuid** | **str** | UUID of the Compliance Provider | [optional] 
**kind** | **str** | Kind of the Compliance Provider | [optional] 
**groups** | [**List[ComplianceGroupsDto]**](ComplianceGroupsDto.md) | Groups associated | [optional] 

## Example

```python
from pyCZERTAINLY.models.compliance_connector_and_groups_dto import ComplianceConnectorAndGroupsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceConnectorAndGroupsDto from a JSON string
compliance_connector_and_groups_dto_instance = ComplianceConnectorAndGroupsDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceConnectorAndGroupsDto.to_json())

# convert the object into a dict
compliance_connector_and_groups_dto_dict = compliance_connector_and_groups_dto_instance.to_dict()
# create an instance of ComplianceConnectorAndGroupsDto from a dict
compliance_connector_and_groups_dto_from_dict = ComplianceConnectorAndGroupsDto.from_dict(compliance_connector_and_groups_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


