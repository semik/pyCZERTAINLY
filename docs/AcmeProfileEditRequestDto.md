# AcmeProfileEditRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the ACME Profile | [optional] 
**terms_of_service_url** | **str** | Terms of Service URL | [optional] 
**website_url** | **str** | Website URL | [optional] 
**dns_resolver_ip** | **str** | DNS Resolver IP address | [optional] [default to 'System Default']
**dns_resolver_port** | **str** | DNS Resolver port number | [optional] [default to '53']
**ra_profile_uuid** | **str** | RA Profile UUID | [optional] 
**retry_interval** | **int** | Retry interval for the Orders | [optional] [default to 30]
**terms_of_service_change_disable** | **bool** | Disable new Orders due to change in Terms of Service | [optional] [default to False]
**terms_of_service_change_url** | **str** | Changes of Terms of Service URL | [optional] 
**validity** | **int** | Order Validity | [optional] [default to 36000]
**issue_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to issue Certificate | 
**revoke_certificate_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Attributes to revoke Certificate | 
**require_contact** | **bool** | Require contact information for new Account | [optional] [default to False]
**require_terms_of_service** | **bool** | Require new Account to agree on Terms of Service | [optional] [default to False]
**custom_attributes** | [**List[RequestAttributeDto]**](RequestAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.acme_profile_edit_request_dto import AcmeProfileEditRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AcmeProfileEditRequestDto from a JSON string
acme_profile_edit_request_dto_instance = AcmeProfileEditRequestDto.from_json(json)
# print the JSON string representation of the object
print(AcmeProfileEditRequestDto.to_json())

# convert the object into a dict
acme_profile_edit_request_dto_dict = acme_profile_edit_request_dto_instance.to_dict()
# create an instance of AcmeProfileEditRequestDto from a dict
acme_profile_edit_request_dto_from_dict = AcmeProfileEditRequestDto.from_dict(acme_profile_edit_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


