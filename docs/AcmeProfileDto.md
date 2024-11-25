# AcmeProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Object identifier | 
**name** | **str** | Object Name | 
**enabled** | **bool** | Enabled flag - true &#x3D; enabled; false &#x3D; disabled | 
**description** | **str** | ACME Profile description | [optional] 
**terms_of_service_url** | **str** | Terms of Service URL | [optional] 
**website_url** | **str** | Website URL | [optional] 
**dns_resolver_ip** | **str** | DNS Resolver IP address | [optional] 
**dns_resolver_port** | **str** | DNS Resolver port number | [optional] 
**ra_profile** | [**SimplifiedRaProfileDto**](SimplifiedRaProfileDto.md) |  | [optional] 
**retry_interval** | **int** | Retry interval for ACME client requests | [optional] 
**terms_of_service_change_disable** | **bool** | Disable new Orders (change in Terms of Service) | [optional] 
**validity** | **int** | Order validity | [optional] 
**directory_url** | **str** | ACME Directory URL | [optional] 
**terms_of_service_change_url** | **str** | Changes of Terms of Service URL | [optional] 
**require_contact** | **bool** | Require Contact information for new Account | [optional] 
**require_terms_of_service** | **bool** | Require new Account to agree on Terms of Service | [optional] 
**issue_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to issue a Certificate | [optional] 
**revoke_certificate_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Attributes to revoke a Certificate | [optional] 
**custom_attributes** | [**List[ResponseAttributeDto]**](ResponseAttributeDto.md) | List of Custom Attributes | [optional] 

## Example

```python
from pyCZERTAINLY.models.acme_profile_dto import AcmeProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of AcmeProfileDto from a JSON string
acme_profile_dto_instance = AcmeProfileDto.from_json(json)
# print the JSON string representation of the object
print(AcmeProfileDto.to_json())

# convert the object into a dict
acme_profile_dto_dict = acme_profile_dto_instance.to_dict()
# create an instance of AcmeProfileDto from a dict
acme_profile_dto_from_dict = AcmeProfileDto.from_dict(acme_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


