# ComplianceGroupsListResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_name** | **str** | Name of the Compliance Provider | 
**connector_uuid** | **str** | UUID of the Compliance Provider | 
**kind** | **str** | Kind of the Compliance Provider | 
**groups** | [**List[ComplianceGroupsResponseDto]**](ComplianceGroupsResponseDto.md) | Groups from Compliance Provider | 

## Example

```python
from openapi_client.models.compliance_groups_list_response_dto import ComplianceGroupsListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceGroupsListResponseDto from a JSON string
compliance_groups_list_response_dto_instance = ComplianceGroupsListResponseDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceGroupsListResponseDto.to_json())

# convert the object into a dict
compliance_groups_list_response_dto_dict = compliance_groups_list_response_dto_instance.to_dict()
# create an instance of ComplianceGroupsListResponseDto from a dict
compliance_groups_list_response_dto_from_dict = ComplianceGroupsListResponseDto.from_dict(compliance_groups_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


