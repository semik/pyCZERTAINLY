# AcmeAccountListResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the Account | 
**uuid** | **str** | UUID of the Account | 
**enabled** | **bool** | Enabled flag. true &#x3D; enabled, false&#x3D;disabled | 
**total_orders** | **int** | Total number of Orders | 
**status** | [**AccountStatus**](AccountStatus.md) |  | 
**ra_profile** | [**SimplifiedRaProfileDto**](SimplifiedRaProfileDto.md) |  | 
**acme_profile_name** | **str** | Name of the ACME Profile | 
**acme_profile_uuid** | **str** | UUID of the ACME Profile | 

## Example

```python
from openapi_client.models.acme_account_list_response_dto import AcmeAccountListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AcmeAccountListResponseDto from a JSON string
acme_account_list_response_dto_instance = AcmeAccountListResponseDto.from_json(json)
# print the JSON string representation of the object
print(AcmeAccountListResponseDto.to_json())

# convert the object into a dict
acme_account_list_response_dto_dict = acme_account_list_response_dto_instance.to_dict()
# create an instance of AcmeAccountListResponseDto from a dict
acme_account_list_response_dto_from_dict = AcmeAccountListResponseDto.from_dict(acme_account_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


