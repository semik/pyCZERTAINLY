# pyCZERTAINLY.CMPProfileManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_cmp_profile**](CMPProfileManagementApi.md#bulk_delete_cmp_profile) | **DELETE** /v1/cmpProfiles/delete | Delete multiple CMP Profiles
[**bulk_disable_cmp_profile**](CMPProfileManagementApi.md#bulk_disable_cmp_profile) | **PATCH** /v1/cmpProfiles/disable | Disable multiple CMP Profile
[**bulk_enable_cmp_profile**](CMPProfileManagementApi.md#bulk_enable_cmp_profile) | **PATCH** /v1/cmpProfiles/enable | Enable multiple CMP Profiles
[**create_cmp_profile**](CMPProfileManagementApi.md#create_cmp_profile) | **POST** /v1/cmpProfiles | Create CMP Profile
[**delete_cmp_profile**](CMPProfileManagementApi.md#delete_cmp_profile) | **DELETE** /v1/cmpProfiles/{cmpProfileUuid} | Delete CMP Profile
[**disable_cmp_profile**](CMPProfileManagementApi.md#disable_cmp_profile) | **PATCH** /v1/cmpProfiles/{cmpProfileUuid}/disable | Disable CMP Profile
[**edit_cmp_profile**](CMPProfileManagementApi.md#edit_cmp_profile) | **PUT** /v1/cmpProfiles/{cmpProfileUuid} | Edit CMP Profile
[**enable_cmp_profile**](CMPProfileManagementApi.md#enable_cmp_profile) | **PATCH** /v1/cmpProfiles/{cmpProfileUuid}/enable | Enable CMP Profile
[**force_delete_cmp_profiles**](CMPProfileManagementApi.md#force_delete_cmp_profiles) | **DELETE** /v1/cmpProfiles/delete/force | Force delete multiple CMP Profiles
[**get_cmp_profile**](CMPProfileManagementApi.md#get_cmp_profile) | **GET** /v1/cmpProfiles/{cmpProfileUuid} | Get details of CMP Profile
[**list_cmp_profiles**](CMPProfileManagementApi.md#list_cmp_profiles) | **GET** /v1/cmpProfiles | Get list of CMP Profiles
[**list_cmp_signing_certificates**](CMPProfileManagementApi.md#list_cmp_signing_certificates) | **GET** /v1/cmpProfiles/signingCertificates | Get list of certificates eligible for signing of CMP responses
[**update_ra_profile1**](CMPProfileManagementApi.md#update_ra_profile1) | **PATCH** /v1/cmpProfiles/{cmpProfileUuid}/raProfiles/{raProfileUuid} | Update RA Profile for CMP Profile


# **bulk_delete_cmp_profile**
> List[BulkActionMessageDto] bulk_delete_cmp_profile(request_body)

Delete multiple CMP Profiles

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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | CMP Profile UUIDs

    try:
        # Delete multiple CMP Profiles
        api_response = api_instance.bulk_delete_cmp_profile(request_body)
        print("The response of CMPProfileManagementApi->bulk_delete_cmp_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->bulk_delete_cmp_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| CMP Profile UUIDs | 

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
**200** | CMP Profiles deleted |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_disable_cmp_profile**
> bulk_disable_cmp_profile(request_body)

Disable multiple CMP Profile

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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | CMP Profile UUIDs

    try:
        # Disable multiple CMP Profile
        api_instance.bulk_disable_cmp_profile(request_body)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->bulk_disable_cmp_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| CMP Profile UUIDs | 

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
**204** | CMP Profiles disabled |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_cmp_profile**
> bulk_enable_cmp_profile(request_body)

Enable multiple CMP Profiles

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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | CMP Profile UUIDs

    try:
        # Enable multiple CMP Profiles
        api_instance.bulk_enable_cmp_profile(request_body)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->bulk_enable_cmp_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| CMP Profile UUIDs | 

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
**204** | CMP Profiles enabled |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cmp_profile**
> CmpProfileDetailDto create_cmp_profile(cmp_profile_request_dto)

Create CMP Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.cmp_profile_detail_dto import CmpProfileDetailDto
from pyCZERTAINLY.models.cmp_profile_request_dto import CmpProfileRequestDto
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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    cmp_profile_request_dto = pyCZERTAINLY.CmpProfileRequestDto() # CmpProfileRequestDto | 

    try:
        # Create CMP Profile
        api_response = api_instance.create_cmp_profile(cmp_profile_request_dto)
        print("The response of CMPProfileManagementApi->create_cmp_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->create_cmp_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_profile_request_dto** | [**CmpProfileRequestDto**](CmpProfileRequestDto.md)|  | 

### Return type

[**CmpProfileDetailDto**](CmpProfileDetailDto.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**201** | CMP Profile created |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cmp_profile**
> delete_cmp_profile(cmp_profile_uuid)

Delete CMP Profile

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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    cmp_profile_uuid = 'cmp_profile_uuid_example' # str | CMP Profile UUID

    try:
        # Delete CMP Profile
        api_instance.delete_cmp_profile(cmp_profile_uuid)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->delete_cmp_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_profile_uuid** | **str**| CMP Profile UUID | 

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
**204** | CMP Profile deleted |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_cmp_profile**
> disable_cmp_profile(cmp_profile_uuid)

Disable CMP Profile

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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    cmp_profile_uuid = 'cmp_profile_uuid_example' # str | CMP Profile UUID

    try:
        # Disable CMP Profile
        api_instance.disable_cmp_profile(cmp_profile_uuid)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->disable_cmp_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_profile_uuid** | **str**| CMP Profile UUID | 

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
**204** | CMP Profile disabled |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_cmp_profile**
> CmpProfileDetailDto edit_cmp_profile(cmp_profile_uuid, cmp_profile_edit_request_dto)

Edit CMP Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.cmp_profile_detail_dto import CmpProfileDetailDto
from pyCZERTAINLY.models.cmp_profile_edit_request_dto import CmpProfileEditRequestDto
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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    cmp_profile_uuid = 'cmp_profile_uuid_example' # str | CMP Profile UUID
    cmp_profile_edit_request_dto = pyCZERTAINLY.CmpProfileEditRequestDto() # CmpProfileEditRequestDto | 

    try:
        # Edit CMP Profile
        api_response = api_instance.edit_cmp_profile(cmp_profile_uuid, cmp_profile_edit_request_dto)
        print("The response of CMPProfileManagementApi->edit_cmp_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->edit_cmp_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_profile_uuid** | **str**| CMP Profile UUID | 
 **cmp_profile_edit_request_dto** | [**CmpProfileEditRequestDto**](CmpProfileEditRequestDto.md)|  | 

### Return type

[**CmpProfileDetailDto**](CmpProfileDetailDto.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | CMP Profile updated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_cmp_profile**
> enable_cmp_profile(cmp_profile_uuid)

Enable CMP Profile

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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    cmp_profile_uuid = 'cmp_profile_uuid_example' # str | CMP Profile UUID

    try:
        # Enable CMP Profile
        api_instance.enable_cmp_profile(cmp_profile_uuid)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->enable_cmp_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_profile_uuid** | **str**| CMP Profile UUID | 

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
**204** | CMP Profile enabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_cmp_profiles**
> List[BulkActionMessageDto] force_delete_cmp_profiles(request_body)

Force delete multiple CMP Profiles

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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | CMP Profile UUIDs

    try:
        # Force delete multiple CMP Profiles
        api_response = api_instance.force_delete_cmp_profiles(request_body)
        print("The response of CMPProfileManagementApi->force_delete_cmp_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->force_delete_cmp_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| CMP Profile UUIDs | 

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
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**200** | CMP Profiles forced to delete |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cmp_profile**
> CmpProfileDetailDto get_cmp_profile(cmp_profile_uuid)

Get details of CMP Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.cmp_profile_detail_dto import CmpProfileDetailDto
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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    cmp_profile_uuid = 'cmp_profile_uuid_example' # str | CMP Profile UUID

    try:
        # Get details of CMP Profile
        api_response = api_instance.get_cmp_profile(cmp_profile_uuid)
        print("The response of CMPProfileManagementApi->get_cmp_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->get_cmp_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_profile_uuid** | **str**| CMP Profile UUID | 

### Return type

[**CmpProfileDetailDto**](CmpProfileDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**200** | CMP Profile details retrieved |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cmp_profiles**
> List[CmpProfileDto] list_cmp_profiles()

Get list of CMP Profiles

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.cmp_profile_dto import CmpProfileDto
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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)

    try:
        # Get list of CMP Profiles
        api_response = api_instance.list_cmp_profiles()
        print("The response of CMPProfileManagementApi->list_cmp_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->list_cmp_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CmpProfileDto]**](CmpProfileDto.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | CMP Profile list retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cmp_signing_certificates**
> List[CertificateDto] list_cmp_signing_certificates()

Get list of certificates eligible for signing of CMP responses

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.certificate_dto import CertificateDto
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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)

    try:
        # Get list of certificates eligible for signing of CMP responses
        api_response = api_instance.list_cmp_signing_certificates()
        print("The response of CMPProfileManagementApi->list_cmp_signing_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->list_cmp_signing_certificates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CertificateDto]**](CertificateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of signing certificates retrieved |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ra_profile1**
> update_ra_profile1(cmp_profile_uuid, ra_profile_uuid)

Update RA Profile for CMP Profile

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
    api_instance = pyCZERTAINLY.CMPProfileManagementApi(api_client)
    cmp_profile_uuid = 'cmp_profile_uuid_example' # str | CMP Profile UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Update RA Profile for CMP Profile
        api_instance.update_ra_profile1(cmp_profile_uuid, ra_profile_uuid)
    except Exception as e:
        print("Exception when calling CMPProfileManagementApi->update_ra_profile1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cmp_profile_uuid** | **str**| CMP Profile UUID | 
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
**200** | RA Profile updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

