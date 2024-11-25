# SimplifiedComplianceProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**description** | **str** | Description of the Compliance Profile | [optional] 

## Example

```python
from openapi_client.models.simplified_compliance_profile_dto import SimplifiedComplianceProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedComplianceProfileDto from a JSON string
simplified_compliance_profile_dto_instance = SimplifiedComplianceProfileDto.from_json(json)
# print the JSON string representation of the object
print(SimplifiedComplianceProfileDto.to_json())

# convert the object into a dict
simplified_compliance_profile_dto_dict = simplified_compliance_profile_dto_instance.to_dict()
# create an instance of SimplifiedComplianceProfileDto from a dict
simplified_compliance_profile_dto_from_dict = SimplifiedComplianceProfileDto.from_dict(simplified_compliance_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


