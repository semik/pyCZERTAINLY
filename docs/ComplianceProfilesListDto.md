# ComplianceProfilesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Compliance Profile description | [optional] 
**rules** | [**List[ComplianceProviderSummaryDto]**](ComplianceProviderSummaryDto.md) | Rules summary | 

## Example

```python
from pyCZERTAINLY.models.compliance_profiles_list_dto import ComplianceProfilesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceProfilesListDto from a JSON string
compliance_profiles_list_dto_instance = ComplianceProfilesListDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceProfilesListDto.to_json())

# convert the object into a dict
compliance_profiles_list_dto_dict = compliance_profiles_list_dto_instance.to_dict()
# create an instance of ComplianceProfilesListDto from a dict
compliance_profiles_list_dto_from_dict = ComplianceProfilesListDto.from_dict(compliance_profiles_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


