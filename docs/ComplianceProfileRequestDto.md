# ComplianceProfileRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Compliance Profile | 
**description** | **str** | Description of the Compliance Profile | [optional] 
**rules** | [**List[ComplianceProfileRulesRequestDto]**](ComplianceProfileRulesRequestDto.md) | Rules to be associated with the Compliance Profile. Profiles can be created without rules and can be added later | [optional] 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from openapi_client.models.compliance_profile_request_dto import ComplianceProfileRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceProfileRequestDto from a JSON string
compliance_profile_request_dto_instance = ComplianceProfileRequestDto.from_json(json)
# print the JSON string representation of the object
print(ComplianceProfileRequestDto.to_json())

# convert the object into a dict
compliance_profile_request_dto_dict = compliance_profile_request_dto_instance.to_dict()
# create an instance of ComplianceProfileRequestDto from a dict
compliance_profile_request_dto_from_dict = ComplianceProfileRequestDto.from_dict(compliance_profile_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


