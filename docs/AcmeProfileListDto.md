# AcmeProfileListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**description** | **str** | ACME Profile description | [optional] 
**ra_profile** | [**SimplifiedRaProfileDto**](SimplifiedRaProfileDto.md) |  | [optional] 
**directory_url** | **str** | URL of the ACME Directory | [optional] 

## Example

```python
from pyCZERTAINLY.models.acme_profile_list_dto import AcmeProfileListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AcmeProfileListDto from a JSON string
acme_profile_list_dto_instance = AcmeProfileListDto.from_json(json)
# print the JSON string representation of the object
print(AcmeProfileListDto.to_json())

# convert the object into a dict
acme_profile_list_dto_dict = acme_profile_list_dto_instance.to_dict()
# create an instance of AcmeProfileListDto from a dict
acme_profile_list_dto_from_dict = AcmeProfileListDto.from_dict(acme_profile_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


