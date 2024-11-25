# AcmeAccountResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the Account | 
**uuid** | **str** | UUID of the Account | 
**enabled** | **bool** | Enabled flag. enabled&#x3D;true, disabled&#x3D;false | 
**total_orders** | **int** | Order count for the Account | 
**successful_orders** | **int** | Number of successful Orders | 
**failed_orders** | **int** | Number of failed Orders | 
**pending_orders** | **int** | Number of pending Orders | 
**valid_orders** | **int** | Number of valid Orders | 
**processing_orders** | **int** | Number of processing Orders | 
**status** | [**AccountStatus**](AccountStatus.md) |  | 
**contact** | **List[str]** | Contact information | 
**terms_of_service_agreed** | **bool** | Terms of Service Agreed | 
**ra_profile** | [**SimplifiedRaProfileDto**](SimplifiedRaProfileDto.md) |  | 
**acme_profile_name** | **str** | Name of the ACME Profile | 
**acme_profile_uuid** | **str** | UUID of the ACME Profile | 

## Example

```python
from openapi_client.models.acme_account_response_dto import AcmeAccountResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AcmeAccountResponseDto from a JSON string
acme_account_response_dto_instance = AcmeAccountResponseDto.from_json(json)
# print the JSON string representation of the object
print(AcmeAccountResponseDto.to_json())

# convert the object into a dict
acme_account_response_dto_dict = acme_account_response_dto_instance.to_dict()
# create an instance of AcmeAccountResponseDto from a dict
acme_account_response_dto_from_dict = AcmeAccountResponseDto.from_dict(acme_account_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


