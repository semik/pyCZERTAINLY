# pyCZERTAINLY.ComplianceProfileManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](ComplianceProfileManagementApi.md#add_group) | **POST** /v1/complianceProfiles/{uuid}/groups | Add group to a Compliance Profile
[**add_rule**](ComplianceProfileManagementApi.md#add_rule) | **POST** /v1/complianceProfiles/{uuid}/rules | Add rule to a Compliance Profile
[**associate_profiles**](ComplianceProfileManagementApi.md#associate_profiles) | **PATCH** /v1/complianceProfiles/{uuid}/raProfiles/associate | Associate Compliance Profile to RA Profile
[**bulk_delete_compliance_profiles**](ComplianceProfileManagementApi.md#bulk_delete_compliance_profiles) | **DELETE** /v1/complianceProfiles | Delete multiple Compliance Profiles
[**check_compliance**](ComplianceProfileManagementApi.md#check_compliance) | **POST** /v1/complianceProfiles/compliance | Initiate Certificate Compliance Check
[**create_compliance_profile**](ComplianceProfileManagementApi.md#create_compliance_profile) | **POST** /v1/complianceProfiles | Add Compliance Profile
[**delete_compliance_profile**](ComplianceProfileManagementApi.md#delete_compliance_profile) | **DELETE** /v1/complianceProfiles/{uuid} | Delete Compliance Profile
[**disassociate_profiles**](ComplianceProfileManagementApi.md#disassociate_profiles) | **PATCH** /v1/complianceProfiles/{uuid}/raProfiles/disassociate | Disassociate Compliance Profile to RA Profile
[**force_delete_compliance_profiles**](ComplianceProfileManagementApi.md#force_delete_compliance_profiles) | **DELETE** /v1/complianceProfiles/force | Force delete Compliance Profiles
[**get_associated_ra_profiles**](ComplianceProfileManagementApi.md#get_associated_ra_profiles) | **GET** /v1/complianceProfiles/{uuid}/raProfiles | Get RA Profiles for a Compliance Profile
[**get_compliance_groups**](ComplianceProfileManagementApi.md#get_compliance_groups) | **GET** /v1/complianceProfiles/groups | Get Compliance groups
[**get_compliance_profile**](ComplianceProfileManagementApi.md#get_compliance_profile) | **GET** /v1/complianceProfiles/{uuid} | Details of a Compliance Profiles
[**get_compliance_rules**](ComplianceProfileManagementApi.md#get_compliance_rules) | **GET** /v1/complianceProfiles/rules | Get Compliance rules
[**list_compliance_profiles**](ComplianceProfileManagementApi.md#list_compliance_profiles) | **GET** /v1/complianceProfiles | List of available Compliance Profiles
[**remove_group**](ComplianceProfileManagementApi.md#remove_group) | **DELETE** /v1/complianceProfiles/{uuid}/groups | Delete group from a Compliance Profile
[**remove_rule**](ComplianceProfileManagementApi.md#remove_rule) | **DELETE** /v1/complianceProfiles/{uuid}/rules | Delete rule from a Compliance Profile


# **add_group**
> add_group(uuid, compliance_group_request_dto)

Add group to a Compliance Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.compliance_group_request_dto import ComplianceGroupRequestDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Compliance Profile UUID
    compliance_group_request_dto = pyCZERTAINLY.ComplianceGroupRequestDto() # ComplianceGroupRequestDto | 

    try:
        # Add group to a Compliance Profile
        api_instance.add_group(uuid, compliance_group_request_dto)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->add_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Compliance Profile UUID | 
 **compliance_group_request_dto** | [**ComplianceGroupRequestDto**](ComplianceGroupRequestDto.md)|  | 

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
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**204** | New group is deleted from the profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_rule**
> ComplianceProfileRuleDto add_rule(uuid, compliance_rule_addition_request_dto)

Add rule to a Compliance Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.compliance_profile_rule_dto import ComplianceProfileRuleDto
from pyCZERTAINLY.models.compliance_rule_addition_request_dto import ComplianceRuleAdditionRequestDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Compliance Profile UUID
    compliance_rule_addition_request_dto = pyCZERTAINLY.ComplianceRuleAdditionRequestDto() # ComplianceRuleAdditionRequestDto | 

    try:
        # Add rule to a Compliance Profile
        api_response = api_instance.add_rule(uuid, compliance_rule_addition_request_dto)
        print("The response of ComplianceProfileManagementApi->add_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->add_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Compliance Profile UUID | 
 **compliance_rule_addition_request_dto** | [**ComplianceRuleAdditionRequestDto**](ComplianceRuleAdditionRequestDto.md)|  | 

### Return type

[**ComplianceProfileRuleDto**](ComplianceProfileRuleDto.md)

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
**200** | New rule added to the profile |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **associate_profiles**
> associate_profiles(uuid, ra_profile_association_request_dto)

Associate Compliance Profile to RA Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.ra_profile_association_request_dto import RaProfileAssociationRequestDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Compliance Profile UUID
    ra_profile_association_request_dto = pyCZERTAINLY.RaProfileAssociationRequestDto() # RaProfileAssociationRequestDto | 

    try:
        # Associate Compliance Profile to RA Profile
        api_instance.associate_profiles(uuid, ra_profile_association_request_dto)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->associate_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Compliance Profile UUID | 
 **ra_profile_association_request_dto** | [**RaProfileAssociationRequestDto**](RaProfileAssociationRequestDto.md)|  | 

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
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**200** | RA Profile association successful |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_compliance_profiles**
> List[BulkActionMessageDto] bulk_delete_compliance_profiles(request_body)

Delete multiple Compliance Profiles

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.bulk_action_message_dto import BulkActionMessageDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Compliance Profile UUIDs

    try:
        # Delete multiple Compliance Profiles
        api_response = api_instance.bulk_delete_compliance_profiles(request_body)
        print("The response of ComplianceProfileManagementApi->bulk_delete_compliance_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->bulk_delete_compliance_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Compliance Profile UUIDs | 

### Return type

[**List[BulkActionMessageDto]**](BulkActionMessageDto.md)

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
**200** | Compliance Profiles deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_compliance**
> check_compliance(request_body)

Initiate Certificate Compliance Check

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | RA Profile UUIDs

    try:
        # Initiate Certificate Compliance Check
        api_instance.check_compliance(request_body)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->check_compliance: %s\n" % e)
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

# **create_compliance_profile**
> UuidDto create_compliance_profile(compliance_profile_request_dto)

Add Compliance Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.compliance_profile_request_dto import ComplianceProfileRequestDto
from pyCZERTAINLY.models.uuid_dto import UuidDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    compliance_profile_request_dto = pyCZERTAINLY.ComplianceProfileRequestDto() # ComplianceProfileRequestDto | 

    try:
        # Add Compliance Profile
        api_response = api_instance.create_compliance_profile(compliance_profile_request_dto)
        print("The response of ComplianceProfileManagementApi->create_compliance_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->create_compliance_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compliance_profile_request_dto** | [**ComplianceProfileRequestDto**](ComplianceProfileRequestDto.md)|  | 

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
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**201** | New Compliance profile added |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compliance_profile**
> delete_compliance_profile(uuid)

Delete Compliance Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Compliance Profile UUID

    try:
        # Delete Compliance Profile
        api_instance.delete_compliance_profile(uuid)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->delete_compliance_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Compliance Profile UUID | 

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
**204** | Compliance Profile deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disassociate_profiles**
> disassociate_profiles(uuid, ra_profile_association_request_dto)

Disassociate Compliance Profile to RA Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.ra_profile_association_request_dto import RaProfileAssociationRequestDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Compliance Profile UUID
    ra_profile_association_request_dto = pyCZERTAINLY.RaProfileAssociationRequestDto() # RaProfileAssociationRequestDto | 

    try:
        # Disassociate Compliance Profile to RA Profile
        api_instance.disassociate_profiles(uuid, ra_profile_association_request_dto)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->disassociate_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Compliance Profile UUID | 
 **ra_profile_association_request_dto** | [**RaProfileAssociationRequestDto**](RaProfileAssociationRequestDto.md)|  | 

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
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | RA Profile disassociation successful |  -  |
**503** | Connector Communication Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_compliance_profiles**
> List[BulkActionMessageDto] force_delete_compliance_profiles(request_body)

Force delete Compliance Profiles

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.bulk_action_message_dto import BulkActionMessageDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Force delete Compliance Profiles
        api_response = api_instance.force_delete_compliance_profiles(request_body)
        print("The response of ComplianceProfileManagementApi->force_delete_compliance_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->force_delete_compliance_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

[**List[BulkActionMessageDto]**](BulkActionMessageDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | Compliance Profiles forced to delete |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associated_ra_profiles**
> List[SimplifiedRaProfileDto] get_associated_ra_profiles(uuid)

Get RA Profiles for a Compliance Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.simplified_ra_profile_dto import SimplifiedRaProfileDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Compliance Profile UUID

    try:
        # Get RA Profiles for a Compliance Profile
        api_response = api_instance.get_associated_ra_profiles(uuid)
        print("The response of ComplianceProfileManagementApi->get_associated_ra_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->get_associated_ra_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Compliance Profile UUID | 

### Return type

[**List[SimplifiedRaProfileDto]**](SimplifiedRaProfileDto.md)

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

# **get_compliance_groups**
> List[ComplianceGroupsListResponseDto] get_compliance_groups(compliance_provider=compliance_provider, kind=kind)

Get Compliance groups

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.compliance_groups_list_response_dto import ComplianceGroupsListResponseDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    compliance_provider = 'compliance_provider_example' # str |  (optional)
    kind = 'kind_example' # str |  (optional)

    try:
        # Get Compliance groups
        api_response = api_instance.get_compliance_groups(compliance_provider=compliance_provider, kind=kind)
        print("The response of ComplianceProfileManagementApi->get_compliance_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->get_compliance_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compliance_provider** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 

### Return type

[**List[ComplianceGroupsListResponseDto]**](ComplianceGroupsListResponseDto.md)

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
**200** | Compliance groups retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_profile**
> ComplianceProfileDto get_compliance_profile(uuid)

Details of a Compliance Profiles

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.compliance_profile_dto import ComplianceProfileDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Compliance Profile UUID

    try:
        # Details of a Compliance Profiles
        api_response = api_instance.get_compliance_profile(uuid)
        print("The response of ComplianceProfileManagementApi->get_compliance_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->get_compliance_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Compliance Profile UUID | 

### Return type

[**ComplianceProfileDto**](ComplianceProfileDto.md)

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
**200** | Compliance Profile details retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_rules**
> List[ComplianceRulesListResponseDto] get_compliance_rules(compliance_provider=compliance_provider, kind=kind, certificate_type=certificate_type)

Get Compliance rules

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_type import CertificateType
from pyCZERTAINLY.models.compliance_rules_list_response_dto import ComplianceRulesListResponseDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    compliance_provider = 'compliance_provider_example' # str |  (optional)
    kind = 'kind_example' # str |  (optional)
    certificate_type = [pyCZERTAINLY.CertificateType()] # List[CertificateType] |  (optional)

    try:
        # Get Compliance rules
        api_response = api_instance.get_compliance_rules(compliance_provider=compliance_provider, kind=kind, certificate_type=certificate_type)
        print("The response of ComplianceProfileManagementApi->get_compliance_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->get_compliance_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compliance_provider** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **certificate_type** | [**List[CertificateType]**](CertificateType.md)|  | [optional] 

### Return type

[**List[ComplianceRulesListResponseDto]**](ComplianceRulesListResponseDto.md)

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
**200** | Compliance rules retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_profiles**
> List[ComplianceProfilesListDto] list_compliance_profiles()

List of available Compliance Profiles

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.compliance_profiles_list_dto import ComplianceProfilesListDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)

    try:
        # List of available Compliance Profiles
        api_response = api_instance.list_compliance_profiles()
        print("The response of ComplianceProfileManagementApi->list_compliance_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->list_compliance_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ComplianceProfilesListDto]**](ComplianceProfilesListDto.md)

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

# **remove_group**
> remove_group(uuid, compliance_group_request_dto)

Delete group from a Compliance Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.compliance_group_request_dto import ComplianceGroupRequestDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Compliance Profile UUID
    compliance_group_request_dto = pyCZERTAINLY.ComplianceGroupRequestDto() # ComplianceGroupRequestDto | 

    try:
        # Delete group from a Compliance Profile
        api_instance.remove_group(uuid, compliance_group_request_dto)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->remove_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Compliance Profile UUID | 
 **compliance_group_request_dto** | [**ComplianceGroupRequestDto**](ComplianceGroupRequestDto.md)|  | 

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
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**204** | New rule is added to the profile |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_rule**
> remove_rule(uuid, compliance_rule_deletion_request_dto)

Delete rule from a Compliance Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.compliance_rule_deletion_request_dto import ComplianceRuleDeletionRequestDto
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "http://localhost:45309"
)


# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ComplianceProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Compliance Profile UUID
    compliance_rule_deletion_request_dto = pyCZERTAINLY.ComplianceRuleDeletionRequestDto() # ComplianceRuleDeletionRequestDto | 

    try:
        # Delete rule from a Compliance Profile
        api_instance.remove_rule(uuid, compliance_rule_deletion_request_dto)
    except Exception as e:
        print("Exception when calling ComplianceProfileManagementApi->remove_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Compliance Profile UUID | 
 **compliance_rule_deletion_request_dto** | [**ComplianceRuleDeletionRequestDto**](ComplianceRuleDeletionRequestDto.md)|  | 

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
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | New group is added to the profile |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

