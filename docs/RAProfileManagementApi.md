# openapi_client.RAProfileManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_acme_for_ra_profile**](RAProfileManagementApi.md#activate_acme_for_ra_profile) | **PATCH** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/protocols/acme/activate/{acmeProfileUuid} | Activate ACME for RA Profile
[**activate_cmp_for_ra_profile**](RAProfileManagementApi.md#activate_cmp_for_ra_profile) | **PATCH** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/protocols/cmp/activate/{cmpProfileUuid} | Activate CMP for RA Profile
[**activate_scep_for_ra_profile**](RAProfileManagementApi.md#activate_scep_for_ra_profile) | **PATCH** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/protocols/scep/activate/{scepProfileUuid} | Activate SCEP for RA Profile
[**associate_ra_profile_with_approval_profile**](RAProfileManagementApi.md#associate_ra_profile_with_approval_profile) | **PATCH** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/approvalProfiles/{approvalProfileUuid} | Associated RA profile with the Approval profile
[**bulk_delete_ra_profile**](RAProfileManagementApi.md#bulk_delete_ra_profile) | **DELETE** /v1/raProfiles | Delete multiple RA Profiles
[**bulk_disable_ra_profile**](RAProfileManagementApi.md#bulk_disable_ra_profile) | **PATCH** /v1/raProfiles/disable | Disable multiple RA Profiles
[**bulk_enable_ra_profile**](RAProfileManagementApi.md#bulk_enable_ra_profile) | **PATCH** /v1/raProfiles/enable | Enable multiple RA Profiles
[**check_ra_profile_compliance**](RAProfileManagementApi.md#check_ra_profile_compliance) | **POST** /v1/raProfiles/compliance | Initiate Certificate Compliance Check
[**create_ra_profile**](RAProfileManagementApi.md#create_ra_profile) | **POST** /v1/authorities/{authorityUuid}/raProfiles | Create RA Profile
[**deactivate_acme_for_ra_profile**](RAProfileManagementApi.md#deactivate_acme_for_ra_profile) | **PATCH** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/protocols/acme/deactivate | Deactivate ACME for RA Profile
[**deactivate_cmp_for_ra_profile**](RAProfileManagementApi.md#deactivate_cmp_for_ra_profile) | **PATCH** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/protocols/cmp/deactivate | Deactivate CMP for RA Profile
[**deactivate_scep_for_ra_profile**](RAProfileManagementApi.md#deactivate_scep_for_ra_profile) | **PATCH** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/protocols/scep/deactivate | Deactivate SCEP for RA Profile
[**delete_ra_profile**](RAProfileManagementApi.md#delete_ra_profile) | **DELETE** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid} | Delete RA Profile
[**delete_ra_profile_without_authority**](RAProfileManagementApi.md#delete_ra_profile_without_authority) | **DELETE** /v1/raProfiles/{raProfileUuid} | Delete RA Profile
[**disable_ra_profile**](RAProfileManagementApi.md#disable_ra_profile) | **PATCH** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/disable | Disable RA Profiles
[**disassociate_ra_profile_from_approval_profile**](RAProfileManagementApi.md#disassociate_ra_profile_from_approval_profile) | **DELETE** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/approvalProfiles/{approvalProfileUuid} | Disassociated RA profile with the Approval profile
[**edit_ra_profile**](RAProfileManagementApi.md#edit_ra_profile) | **PUT** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid} | Edit RA Profile
[**enable_ra_profile**](RAProfileManagementApi.md#enable_ra_profile) | **PATCH** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/enable | Enable RA Profiles
[**get_acme_for_ra_profile**](RAProfileManagementApi.md#get_acme_for_ra_profile) | **GET** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/protocols/acme | Get ACME details for RA Profile
[**get_associated_approval_profiles**](RAProfileManagementApi.md#get_associated_approval_profiles) | **GET** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/approvalProfiles | List of Approval profiles associated with the RAProfile
[**get_associated_compliance_profiles**](RAProfileManagementApi.md#get_associated_compliance_profiles) | **GET** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/complianceProfiles | Get Compliance Profiles for an RA Profile
[**get_authority_certificate_chain**](RAProfileManagementApi.md#get_authority_certificate_chain) | **GET** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/caCertificates | Retrieve certificates of authority belonging to RA profile
[**get_cmp_for_ra_profile**](RAProfileManagementApi.md#get_cmp_for_ra_profile) | **GET** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/protocols/cmp | Get CMP details for RA Profile
[**get_ra_profile**](RAProfileManagementApi.md#get_ra_profile) | **GET** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid} | Details of RA Profile
[**get_ra_profile_without_authority**](RAProfileManagementApi.md#get_ra_profile_without_authority) | **GET** /v1/raProfiles/{raProfileUuid} | Details of RA Profile
[**get_scep_for_ra_profile**](RAProfileManagementApi.md#get_scep_for_ra_profile) | **GET** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/protocols/scep | Get SCEP details for RA Profile
[**list_ra_profile_issue_certificate_attributes**](RAProfileManagementApi.md#list_ra_profile_issue_certificate_attributes) | **GET** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/attributes/issue | Get issue Certificate Attributes
[**list_ra_profile_revoke_certificate_attributes**](RAProfileManagementApi.md#list_ra_profile_revoke_certificate_attributes) | **GET** /v1/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/attributes/revoke | Get revocation Attributes
[**list_ra_profiles**](RAProfileManagementApi.md#list_ra_profiles) | **GET** /v1/raProfiles | List of available RA Profiles


# **activate_acme_for_ra_profile**
> RaProfileAcmeDetailResponseDto activate_acme_for_ra_profile(authority_uuid, ra_profile_uuid, acme_profile_uuid, activate_acme_for_ra_profile_request_dto)

Activate ACME for RA Profile

### Example


```python
import openapi_client
from openapi_client.models.activate_acme_for_ra_profile_request_dto import ActivateAcmeForRaProfileRequestDto
from openapi_client.models.ra_profile_acme_detail_response_dto import RaProfileAcmeDetailResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    acme_profile_uuid = 'acme_profile_uuid_example' # str | ACME Profile UUID
    activate_acme_for_ra_profile_request_dto = openapi_client.ActivateAcmeForRaProfileRequestDto() # ActivateAcmeForRaProfileRequestDto | 

    try:
        # Activate ACME for RA Profile
        api_response = api_instance.activate_acme_for_ra_profile(authority_uuid, ra_profile_uuid, acme_profile_uuid, activate_acme_for_ra_profile_request_dto)
        print("The response of RAProfileManagementApi->activate_acme_for_ra_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->activate_acme_for_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
 **acme_profile_uuid** | **str**| ACME Profile UUID | 
 **activate_acme_for_ra_profile_request_dto** | [**ActivateAcmeForRaProfileRequestDto**](ActivateAcmeForRaProfileRequestDto.md)|  | 

### Return type

[**RaProfileAcmeDetailResponseDto**](RaProfileAcmeDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | ACME activated |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_cmp_for_ra_profile**
> RaProfileCmpDetailResponseDto activate_cmp_for_ra_profile(authority_uuid, ra_profile_uuid, cmp_profile_uuid, activate_cmp_for_ra_profile_request_dto)

Activate CMP for RA Profile

### Example


```python
import openapi_client
from openapi_client.models.activate_cmp_for_ra_profile_request_dto import ActivateCmpForRaProfileRequestDto
from openapi_client.models.ra_profile_cmp_detail_response_dto import RaProfileCmpDetailResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    cmp_profile_uuid = 'cmp_profile_uuid_example' # str | CMP Profile UUID
    activate_cmp_for_ra_profile_request_dto = openapi_client.ActivateCmpForRaProfileRequestDto() # ActivateCmpForRaProfileRequestDto | 

    try:
        # Activate CMP for RA Profile
        api_response = api_instance.activate_cmp_for_ra_profile(authority_uuid, ra_profile_uuid, cmp_profile_uuid, activate_cmp_for_ra_profile_request_dto)
        print("The response of RAProfileManagementApi->activate_cmp_for_ra_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->activate_cmp_for_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
 **cmp_profile_uuid** | **str**| CMP Profile UUID | 
 **activate_cmp_for_ra_profile_request_dto** | [**ActivateCmpForRaProfileRequestDto**](ActivateCmpForRaProfileRequestDto.md)|  | 

### Return type

[**RaProfileCmpDetailResponseDto**](RaProfileCmpDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**204** | CMP activated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_scep_for_ra_profile**
> RaProfileScepDetailResponseDto activate_scep_for_ra_profile(authority_uuid, ra_profile_uuid, scep_profile_uuid, activate_scep_for_ra_profile_request_dto)

Activate SCEP for RA Profile

### Example


```python
import openapi_client
from openapi_client.models.activate_scep_for_ra_profile_request_dto import ActivateScepForRaProfileRequestDto
from openapi_client.models.ra_profile_scep_detail_response_dto import RaProfileScepDetailResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    scep_profile_uuid = 'scep_profile_uuid_example' # str | SCEP Profile UUID
    activate_scep_for_ra_profile_request_dto = openapi_client.ActivateScepForRaProfileRequestDto() # ActivateScepForRaProfileRequestDto | 

    try:
        # Activate SCEP for RA Profile
        api_response = api_instance.activate_scep_for_ra_profile(authority_uuid, ra_profile_uuid, scep_profile_uuid, activate_scep_for_ra_profile_request_dto)
        print("The response of RAProfileManagementApi->activate_scep_for_ra_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->activate_scep_for_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
 **scep_profile_uuid** | **str**| SCEP Profile UUID | 
 **activate_scep_for_ra_profile_request_dto** | [**ActivateScepForRaProfileRequestDto**](ActivateScepForRaProfileRequestDto.md)|  | 

### Return type

[**RaProfileScepDetailResponseDto**](RaProfileScepDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**204** | SCEP activated |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_ra_profile_with_approval_profile**
> associate_ra_profile_with_approval_profile(authority_uuid, ra_profile_uuid, approval_profile_uuid)

Associated RA profile with the Approval profile

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA profile UUID
    approval_profile_uuid = 'approval_profile_uuid_example' # str | Approval profile UUID

    try:
        # Associated RA profile with the Approval profile
        api_instance.associate_ra_profile_with_approval_profile(authority_uuid, ra_profile_uuid, approval_profile_uuid)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->associate_ra_profile_with_approval_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority instance UUID | 
 **ra_profile_uuid** | **str**| RA profile UUID | 
 **approval_profile_uuid** | **str**| Approval profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**200** | Approval profile associated with the RA profile |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_ra_profile**
> bulk_delete_ra_profile(request_body)

Delete multiple RA Profiles

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | RA Profile UUIDs

    try:
        # Delete multiple RA Profiles
        api_instance.bulk_delete_ra_profile(request_body)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->bulk_delete_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| RA Profile UUIDs | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**204** | RA Profiles deleted |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_disable_ra_profile**
> bulk_disable_ra_profile(request_body)

Disable multiple RA Profiles

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | RA Profile UUIDs

    try:
        # Disable multiple RA Profiles
        api_instance.bulk_disable_ra_profile(request_body)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->bulk_disable_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| RA Profile UUIDs | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | RA Profiles disabled |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_ra_profile**
> bulk_enable_ra_profile(request_body)

Enable multiple RA Profiles

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | RA Profile UUIDs

    try:
        # Enable multiple RA Profiles
        api_instance.bulk_enable_ra_profile(request_body)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->bulk_enable_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| RA Profile UUIDs | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**204** | RA Profiles enabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_ra_profile_compliance**
> check_ra_profile_compliance(request_body)

Initiate Certificate Compliance Check

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | RA Profile UUIDs

    try:
        # Initiate Certificate Compliance Check
        api_instance.check_ra_profile_compliance(request_body)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->check_ra_profile_compliance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| RA Profile UUIDs | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**204** | Compliance check initiated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ra_profile**
> UuidDto create_ra_profile(authority_uuid, add_ra_profile_request_dto)

Create RA Profile

### Example


```python
import openapi_client
from openapi_client.models.add_ra_profile_request_dto import AddRaProfileRequestDto
from openapi_client.models.uuid_dto import UuidDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    add_ra_profile_request_dto = openapi_client.AddRaProfileRequestDto() # AddRaProfileRequestDto | 

    try:
        # Create RA Profile
        api_response = api_instance.create_ra_profile(authority_uuid, add_ra_profile_request_dto)
        print("The response of RAProfileManagementApi->create_ra_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->create_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **add_ra_profile_request_dto** | [**AddRaProfileRequestDto**](AddRaProfileRequestDto.md)|  | 

### Return type

[**UuidDto**](UuidDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**201** | RA Profile added |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_acme_for_ra_profile**
> deactivate_acme_for_ra_profile(authority_uuid, ra_profile_uuid)

Deactivate ACME for RA Profile

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Deactivate ACME for RA Profile
        api_instance.deactivate_acme_for_ra_profile(authority_uuid, ra_profile_uuid)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->deactivate_acme_for_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**204** | ACME deactivated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_cmp_for_ra_profile**
> deactivate_cmp_for_ra_profile(authority_uuid, ra_profile_uuid)

Deactivate CMP for RA Profile

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Deactivate CMP for RA Profile
        api_instance.deactivate_cmp_for_ra_profile(authority_uuid, ra_profile_uuid)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->deactivate_cmp_for_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**204** | CMP deactivated |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_scep_for_ra_profile**
> deactivate_scep_for_ra_profile(authority_uuid, ra_profile_uuid)

Deactivate SCEP for RA Profile

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Deactivate SCEP for RA Profile
        api_instance.deactivate_scep_for_ra_profile(authority_uuid, ra_profile_uuid)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->deactivate_scep_for_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | SCEP deactivated |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ra_profile**
> delete_ra_profile(authority_uuid, ra_profile_uuid)

Delete RA Profile

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Delete RA Profile
        api_instance.delete_ra_profile(authority_uuid, ra_profile_uuid)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->delete_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | RA Profile deleted |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ra_profile_without_authority**
> delete_ra_profile_without_authority(ra_profile_uuid)

Delete RA Profile

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Delete RA Profile
        api_instance.delete_ra_profile_without_authority(ra_profile_uuid)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->delete_ra_profile_without_authority: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | RA Profile deleted |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_ra_profile**
> disable_ra_profile(authority_uuid, ra_profile_uuid)

Disable RA Profiles

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Disable RA Profiles
        api_instance.disable_ra_profile(authority_uuid, ra_profile_uuid)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->disable_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**204** | RA Profile disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disassociate_ra_profile_from_approval_profile**
> disassociate_ra_profile_from_approval_profile(authority_uuid, ra_profile_uuid, approval_profile_uuid)

Disassociated RA profile with the Approval profile

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA profile UUID
    approval_profile_uuid = 'approval_profile_uuid_example' # str | Approval profile UUID

    try:
        # Disassociated RA profile with the Approval profile
        api_instance.disassociate_ra_profile_from_approval_profile(authority_uuid, ra_profile_uuid, approval_profile_uuid)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->disassociate_ra_profile_from_approval_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority instance UUID | 
 **ra_profile_uuid** | **str**| RA profile UUID | 
 **approval_profile_uuid** | **str**| Approval profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**200** | Approval profile disassociated from the RA profile |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_ra_profile**
> RaProfileDto edit_ra_profile(authority_uuid, ra_profile_uuid, edit_ra_profile_request_dto)

Edit RA Profile

### Example


```python
import openapi_client
from openapi_client.models.edit_ra_profile_request_dto import EditRaProfileRequestDto
from openapi_client.models.ra_profile_dto import RaProfileDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    edit_ra_profile_request_dto = openapi_client.EditRaProfileRequestDto() # EditRaProfileRequestDto | 

    try:
        # Edit RA Profile
        api_response = api_instance.edit_ra_profile(authority_uuid, ra_profile_uuid, edit_ra_profile_request_dto)
        print("The response of RAProfileManagementApi->edit_ra_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->edit_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
 **edit_ra_profile_request_dto** | [**EditRaProfileRequestDto**](EditRaProfileRequestDto.md)|  | 

### Return type

[**RaProfileDto**](RaProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**204** | RA Profile updated |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_ra_profile**
> enable_ra_profile(authority_uuid, ra_profile_uuid)

Enable RA Profiles

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Enable RA Profiles
        api_instance.enable_ra_profile(authority_uuid, ra_profile_uuid)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->enable_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**204** | RA Profile enabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acme_for_ra_profile**
> RaProfileAcmeDetailResponseDto get_acme_for_ra_profile(authority_uuid, ra_profile_uuid)

Get ACME details for RA Profile

### Example


```python
import openapi_client
from openapi_client.models.ra_profile_acme_detail_response_dto import RaProfileAcmeDetailResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Get ACME details for RA Profile
        api_response = api_instance.get_acme_for_ra_profile(authority_uuid, ra_profile_uuid)
        print("The response of RAProfileManagementApi->get_acme_for_ra_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->get_acme_for_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

[**RaProfileAcmeDetailResponseDto**](RaProfileAcmeDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**204** | ACME details retrieved |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associated_approval_profiles**
> List[ApprovalProfileDto] get_associated_approval_profiles(authority_uuid, ra_profile_uuid)

List of Approval profiles associated with the RAProfile

### Example


```python
import openapi_client
from openapi_client.models.approval_profile_dto import ApprovalProfileDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA profile UUID

    try:
        # List of Approval profiles associated with the RAProfile
        api_response = api_instance.get_associated_approval_profiles(authority_uuid, ra_profile_uuid)
        print("The response of RAProfileManagementApi->get_associated_approval_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->get_associated_approval_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority instance UUID | 
 **ra_profile_uuid** | **str**| RA profile UUID | 

### Return type

[**List[ApprovalProfileDto]**](ApprovalProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | Approval profiles retrieved |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associated_compliance_profiles**
> List[SimplifiedComplianceProfileDto] get_associated_compliance_profiles(authority_uuid, ra_profile_uuid)

Get Compliance Profiles for an RA Profile

### Example


```python
import openapi_client
from openapi_client.models.simplified_compliance_profile_dto import SimplifiedComplianceProfileDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Get Compliance Profiles for an RA Profile
        api_response = api_instance.get_associated_compliance_profiles(authority_uuid, ra_profile_uuid)
        print("The response of RAProfileManagementApi->get_associated_compliance_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->get_associated_compliance_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

[**List[SimplifiedComplianceProfileDto]**](SimplifiedComplianceProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Compliance Profiles retrieved |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authority_certificate_chain**
> List[CertificateDetailDto] get_authority_certificate_chain(authority_uuid, ra_profile_uuid)

Retrieve certificates of authority belonging to RA profile

### Example


```python
import openapi_client
from openapi_client.models.certificate_detail_dto import CertificateDetailDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA profile UUID

    try:
        # Retrieve certificates of authority belonging to RA profile
        api_response = api_instance.get_authority_certificate_chain(authority_uuid, ra_profile_uuid)
        print("The response of RAProfileManagementApi->get_authority_certificate_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->get_authority_certificate_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority instance UUID | 
 **ra_profile_uuid** | **str**| RA profile UUID | 

### Return type

[**List[CertificateDetailDto]**](CertificateDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**200** | Approval profile associated with the RA profile |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cmp_for_ra_profile**
> RaProfileCmpDetailResponseDto get_cmp_for_ra_profile(authority_uuid, ra_profile_uuid)

Get CMP details for RA Profile

### Example


```python
import openapi_client
from openapi_client.models.ra_profile_cmp_detail_response_dto import RaProfileCmpDetailResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Get CMP details for RA Profile
        api_response = api_instance.get_cmp_for_ra_profile(authority_uuid, ra_profile_uuid)
        print("The response of RAProfileManagementApi->get_cmp_for_ra_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->get_cmp_for_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

[**RaProfileCmpDetailResponseDto**](RaProfileCmpDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | CMP details retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ra_profile**
> RaProfileDto get_ra_profile(authority_uuid, ra_profile_uuid)

Details of RA Profile

### Example


```python
import openapi_client
from openapi_client.models.ra_profile_dto import RaProfileDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Details of RA Profile
        api_response = api_instance.get_ra_profile(authority_uuid, ra_profile_uuid)
        print("The response of RAProfileManagementApi->get_ra_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->get_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

[**RaProfileDto**](RaProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | RA Profile details retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ra_profile_without_authority**
> RaProfileDto get_ra_profile_without_authority(ra_profile_uuid)

Details of RA Profile

### Example


```python
import openapi_client
from openapi_client.models.ra_profile_dto import RaProfileDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Details of RA Profile
        api_response = api_instance.get_ra_profile_without_authority(ra_profile_uuid)
        print("The response of RAProfileManagementApi->get_ra_profile_without_authority:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->get_ra_profile_without_authority: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

[**RaProfileDto**](RaProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | RA Profile details retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scep_for_ra_profile**
> RaProfileScepDetailResponseDto get_scep_for_ra_profile(authority_uuid, ra_profile_uuid)

Get SCEP details for RA Profile

### Example


```python
import openapi_client
from openapi_client.models.ra_profile_scep_detail_response_dto import RaProfileScepDetailResponseDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Get SCEP details for RA Profile
        api_response = api_instance.get_scep_for_ra_profile(authority_uuid, ra_profile_uuid)
        print("The response of RAProfileManagementApi->get_scep_for_ra_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->get_scep_for_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

[**RaProfileScepDetailResponseDto**](RaProfileScepDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**204** | SCEP details retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ra_profile_issue_certificate_attributes**
> List[BaseAttributeDto] list_ra_profile_issue_certificate_attributes(authority_uuid, ra_profile_uuid)

Get issue Certificate Attributes

### Example


```python
import openapi_client
from openapi_client.models.base_attribute_dto import BaseAttributeDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Get issue Certificate Attributes
        api_response = api_instance.list_ra_profile_issue_certificate_attributes(authority_uuid, ra_profile_uuid)
        print("The response of RAProfileManagementApi->list_ra_profile_issue_certificate_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->list_ra_profile_issue_certificate_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

[**List[BaseAttributeDto]**](BaseAttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**200** | Issue certificate attributes list obtained |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ra_profile_revoke_certificate_attributes**
> List[BaseAttributeDto] list_ra_profile_revoke_certificate_attributes(authority_uuid, ra_profile_uuid)

Get revocation Attributes

### Example


```python
import openapi_client
from openapi_client.models.base_attribute_dto import BaseAttributeDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Get revocation Attributes
        api_response = api_instance.list_ra_profile_revoke_certificate_attributes(authority_uuid, ra_profile_uuid)
        print("The response of RAProfileManagementApi->list_ra_profile_revoke_certificate_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->list_ra_profile_revoke_certificate_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 

### Return type

[**List[BaseAttributeDto]**](BaseAttributeDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Revocation attributes list obtained |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ra_profiles**
> List[RaProfileDto] list_ra_profiles(enabled=enabled)

List of available RA Profiles

### Example


```python
import openapi_client
from openapi_client.models.ra_profile_dto import RaProfileDto
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RAProfileManagementApi(api_client)
    enabled = True # bool |  (optional)

    try:
        # List of available RA Profiles
        api_response = api_instance.list_ra_profiles(enabled=enabled)
        print("The response of RAProfileManagementApi->list_ra_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAProfileManagementApi->list_ra_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**|  | [optional] 

### Return type

[**List[RaProfileDto]**](RaProfileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | RA Profiles retrieved |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

