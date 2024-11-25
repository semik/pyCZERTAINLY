# ComplianceGroupRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_uuid** | **str** | UUID of the Compliance Provider | 
**kind** | **str** | Kind of the Compliance Provider | 
**group_uuid** | **str** | UUID of the group | 

## Example

```python
from openapi_client.models.compliance_group_request_dto import ComplianceGroupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceGroupRequestDto from a JSON string
compliance_group_request_dto_instance = ComplianceGroupRequestDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceGroupRequestDto.to_json())

# convert the object into a dict
compliance_group_request_dto_dict = compliance_group_request_dto_instance.to_dict()
# create an instance of ComplianceGroupRequestDto from a dict
compliance_group_request_dto_from_dict = ComplianceGroupRequestDto.from_dict(compliance_group_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


