# IssueToLocationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ra_profile_uuid** | **str** | RA Profile UUID | 
**csr_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of CSR Attributes for Location | 
**issue_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of certificate issue Attributes for RA Profile | 
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 
**certificate_custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Certificate Custom Attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.issue_to_location_request_dto import IssueToLocationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of IssueToLocationRequestDto from a JSON string
issue_to_location_request_dto_instance = IssueToLocationRequestDto.from_json(json)
# print the JSON string representation of the object
print(IssueToLocationRequestDto.to_json())

# convert the object into a dict
issue_to_location_request_dto_dict = issue_to_location_request_dto_instance.to_dict()
# create an instance of IssueToLocationRequestDto from a dict
issue_to_location_request_dto_from_dict = IssueToLocationRequestDto.from_dict(issue_to_location_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


