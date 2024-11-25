# pyCZERTAINLY.SCEPProfileManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_scep_profile**](SCEPProfileManagementApi.md#bulk_delete_scep_profile) | **DELETE** /v1/scepProfiles/delete | Delete multiple SCEP Profiles
[**bulk_disable_scep_profile**](SCEPProfileManagementApi.md#bulk_disable_scep_profile) | **PATCH** /v1/scepProfiles/disable | Disable multiple SCEP Profile
[**bulk_enable_scep_profile**](SCEPProfileManagementApi.md#bulk_enable_scep_profile) | **PATCH** /v1/scepProfiles/enable | Enable multiple SCEP Profiles
[**create_scep_profile**](SCEPProfileManagementApi.md#create_scep_profile) | **POST** /v1/scepProfiles | Create SCEP Profile
[**delete_scep_profile**](SCEPProfileManagementApi.md#delete_scep_profile) | **DELETE** /v1/scepProfiles/{uuid} | Delete SCEP Profile
[**disable_scep_profile**](SCEPProfileManagementApi.md#disable_scep_profile) | **PATCH** /v1/scepProfiles/{uuid}/disable | Disable SCEP Profile
[**edit_scep_profile**](SCEPProfileManagementApi.md#edit_scep_profile) | **PUT** /v1/scepProfiles/{uuid} | Edit SCEP Profile
[**enable_scep_profile**](SCEPProfileManagementApi.md#enable_scep_profile) | **PATCH** /v1/scepProfiles/{uuid}/enable | Enable SCEP Profile
[**force_delete_scep_profiles**](SCEPProfileManagementApi.md#force_delete_scep_profiles) | **DELETE** /v1/scepProfiles/delete/force | Force delete multiple SCEP Profiles
[**get_scep_profile**](SCEPProfileManagementApi.md#get_scep_profile) | **GET** /v1/scepProfiles/{uuid} | Get details of SCEP Profile
[**list_scep_ca_certificates**](SCEPProfileManagementApi.md#list_scep_ca_certificates) | **GET** /v1/scepProfiles/caCertificates | Get list of certificates eligible for CA certificate of SCEP requests
[**list_scep_profiles**](SCEPProfileManagementApi.md#list_scep_profiles) | **GET** /v1/scepProfiles | Get list of SCEP Profiles
[**update_ra_profile**](SCEPProfileManagementApi.md#update_ra_profile) | **PATCH** /v1/scepProfiles/{uuid}/raProfiles/{raProfileUuid} | Update RA Profile for SCEP Profile


# **bulk_delete_scep_profile**
> List[BulkActionMessageDto] bulk_delete_scep_profile(request_body)

Delete multiple SCEP Profiles

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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | SCEP Profile UUIDs

    try:
        # Delete multiple SCEP Profiles
        api_response = api_instance.bulk_delete_scep_profile(request_body)
        print("The response of SCEPProfileManagementApi->bulk_delete_scep_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->bulk_delete_scep_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| SCEP Profile UUIDs | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | SCEP Profiles deleted |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_disable_scep_profile**
> bulk_disable_scep_profile(request_body)

Disable multiple SCEP Profile

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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | SCEP Profile UUIDs

    try:
        # Disable multiple SCEP Profile
        api_instance.bulk_disable_scep_profile(request_body)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->bulk_disable_scep_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| SCEP Profile UUIDs | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**204** | SCEP Profiles disabled |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_scep_profile**
> bulk_enable_scep_profile(request_body)

Enable multiple SCEP Profiles

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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | SCEP Profile UUIDs

    try:
        # Enable multiple SCEP Profiles
        api_instance.bulk_enable_scep_profile(request_body)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->bulk_enable_scep_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| SCEP Profile UUIDs | 

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
**204** | SCEP Profiles enabled |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scep_profile**
> ScepProfileDetailDto create_scep_profile(scep_profile_request_dto)

Create SCEP Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.scep_profile_detail_dto import ScepProfileDetailDto
from pyCZERTAINLY.models.scep_profile_request_dto import ScepProfileRequestDto
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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    scep_profile_request_dto = pyCZERTAINLY.ScepProfileRequestDto() # ScepProfileRequestDto | 

    try:
        # Create SCEP Profile
        api_response = api_instance.create_scep_profile(scep_profile_request_dto)
        print("The response of SCEPProfileManagementApi->create_scep_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->create_scep_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scep_profile_request_dto** | [**ScepProfileRequestDto**](ScepProfileRequestDto.md)|  | 

### Return type

[**ScepProfileDetailDto**](ScepProfileDetailDto.md)

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
**500** | Internal Server Error |  -  |
**201** | SCEP Profile created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scep_profile**
> delete_scep_profile(uuid)

Delete SCEP Profile

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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | SCEP Profile UUID

    try:
        # Delete SCEP Profile
        api_instance.delete_scep_profile(uuid)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->delete_scep_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| SCEP Profile UUID | 

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
**403** | Forbidden |  -  |
**204** | SCEP Profile deleted |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_scep_profile**
> disable_scep_profile(uuid)

Disable SCEP Profile

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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | SCEP Profile UUID

    try:
        # Disable SCEP Profile
        api_instance.disable_scep_profile(uuid)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->disable_scep_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| SCEP Profile UUID | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | SCEP Profile disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_scep_profile**
> ScepProfileDetailDto edit_scep_profile(uuid, scep_profile_edit_request_dto)

Edit SCEP Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.scep_profile_detail_dto import ScepProfileDetailDto
from pyCZERTAINLY.models.scep_profile_edit_request_dto import ScepProfileEditRequestDto
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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | SCEP Profile UUID
    scep_profile_edit_request_dto = pyCZERTAINLY.ScepProfileEditRequestDto() # ScepProfileEditRequestDto | 

    try:
        # Edit SCEP Profile
        api_response = api_instance.edit_scep_profile(uuid, scep_profile_edit_request_dto)
        print("The response of SCEPProfileManagementApi->edit_scep_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->edit_scep_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| SCEP Profile UUID | 
 **scep_profile_edit_request_dto** | [**ScepProfileEditRequestDto**](ScepProfileEditRequestDto.md)|  | 

### Return type

[**ScepProfileDetailDto**](ScepProfileDetailDto.md)

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
**200** | SCEP Profile updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_scep_profile**
> enable_scep_profile(uuid)

Enable SCEP Profile

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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | SCEP Profile UUID

    try:
        # Enable SCEP Profile
        api_instance.enable_scep_profile(uuid)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->enable_scep_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| SCEP Profile UUID | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | SCEP Profile enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_scep_profiles**
> List[BulkActionMessageDto] force_delete_scep_profiles(request_body)

Force delete multiple SCEP Profiles

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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | SCEP Profile UUIDs

    try:
        # Force delete multiple SCEP Profiles
        api_response = api_instance.force_delete_scep_profiles(request_body)
        print("The response of SCEPProfileManagementApi->force_delete_scep_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->force_delete_scep_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| SCEP Profile UUIDs | 

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
**200** | SCEP Profiles forced to delete |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scep_profile**
> ScepProfileDetailDto get_scep_profile(uuid)

Get details of SCEP Profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.scep_profile_detail_dto import ScepProfileDetailDto
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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | SCEP Profile UUID

    try:
        # Get details of SCEP Profile
        api_response = api_instance.get_scep_profile(uuid)
        print("The response of SCEPProfileManagementApi->get_scep_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->get_scep_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| SCEP Profile UUID | 

### Return type

[**ScepProfileDetailDto**](ScepProfileDetailDto.md)

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
**200** | SCEP Profile details retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scep_ca_certificates**
> List[CertificateDto] list_scep_ca_certificates(intune_enabled)

Get list of certificates eligible for CA certificate of SCEP requests

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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    intune_enabled = True # bool | flag to return certificates that are eligible for Intune integration

    try:
        # Get list of certificates eligible for CA certificate of SCEP requests
        api_response = api_instance.list_scep_ca_certificates(intune_enabled)
        print("The response of SCEPProfileManagementApi->list_scep_ca_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->list_scep_ca_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intune_enabled** | **bool**| flag to return certificates that are eligible for Intune integration | 

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
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | List of CA certificates retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scep_profiles**
> List[ScepProfileDto] list_scep_profiles()

Get list of SCEP Profiles

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.scep_profile_dto import ScepProfileDto
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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)

    try:
        # Get list of SCEP Profiles
        api_response = api_instance.list_scep_profiles()
        print("The response of SCEPProfileManagementApi->list_scep_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->list_scep_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ScepProfileDto]**](ScepProfileDto.md)

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
**200** | SCEP Profile list retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ra_profile**
> update_ra_profile(uuid, ra_profile_uuid)

Update RA Profile for SCEP Profile

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
    api_instance = pyCZERTAINLY.SCEPProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | SCEP Profile UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Update RA Profile for SCEP Profile
        api_instance.update_ra_profile(uuid, ra_profile_uuid)
    except Exception as e:
        print("Exception when calling SCEPProfileManagementApi->update_ra_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| SCEP Profile UUID | 
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

