# pyCZERTAINLY.ApprovalProfileInventoryApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_approval_profile**](ApprovalProfileInventoryApi.md#create_approval_profile) | **POST** /v1/approvalProfiles | Create a Approval profile
[**delete_approval_profile**](ApprovalProfileInventoryApi.md#delete_approval_profile) | **DELETE** /v1/approvalProfiles/{uuid} | Delete an approval profile
[**disable_approval_profile**](ApprovalProfileInventoryApi.md#disable_approval_profile) | **PATCH** /v1/approvalProfiles/{uuid}/disable | Disabling of Approval profile
[**edit_approval_profile**](ApprovalProfileInventoryApi.md#edit_approval_profile) | **PUT** /v1/approvalProfiles/{uuid} | Edit an Approval profile
[**enable_approval_profile**](ApprovalProfileInventoryApi.md#enable_approval_profile) | **PATCH** /v1/approvalProfiles/{uuid}/enable | Enabling of Approval profile
[**get_approval_profile**](ApprovalProfileInventoryApi.md#get_approval_profile) | **GET** /v1/approvalProfiles/{uuid} | Get Approval Profile Details
[**list_approval_profiles**](ApprovalProfileInventoryApi.md#list_approval_profiles) | **GET** /v1/approvalProfiles | List Approval Profiles


# **create_approval_profile**
> UuidDto create_approval_profile(approval_profile_request_dto)

Create a Approval profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.approval_profile_request_dto import ApprovalProfileRequestDto
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
    api_instance = pyCZERTAINLY.ApprovalProfileInventoryApi(api_client)
    approval_profile_request_dto = pyCZERTAINLY.ApprovalProfileRequestDto() # ApprovalProfileRequestDto | 

    try:
        # Create a Approval profile
        api_response = api_instance.create_approval_profile(approval_profile_request_dto)
        print("The response of ApprovalProfileInventoryApi->create_approval_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalProfileInventoryApi->create_approval_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approval_profile_request_dto** | [**ApprovalProfileRequestDto**](ApprovalProfileRequestDto.md)|  | 

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
**200** | New Approval profile created |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_approval_profile**
> delete_approval_profile(uuid)

Delete an approval profile

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
    api_instance = pyCZERTAINLY.ApprovalProfileInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval profile UUID

    try:
        # Delete an approval profile
        api_instance.delete_approval_profile(uuid)
    except Exception as e:
        print("Exception when calling ApprovalProfileInventoryApi->delete_approval_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval profile UUID | 

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
**204** | Approval profile deleted |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_approval_profile**
> disable_approval_profile(uuid)

Disabling of Approval profile

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
    api_instance = pyCZERTAINLY.ApprovalProfileInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval profile UUID

    try:
        # Disabling of Approval profile
        api_instance.disable_approval_profile(uuid)
    except Exception as e:
        print("Exception when calling ApprovalProfileInventoryApi->disable_approval_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**204** | Approval profile disabled |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_approval_profile**
> object edit_approval_profile(uuid, approval_profile_update_request_dto)

Edit an Approval profile

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.approval_profile_update_request_dto import ApprovalProfileUpdateRequestDto
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
    api_instance = pyCZERTAINLY.ApprovalProfileInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval profile UUID
    approval_profile_update_request_dto = pyCZERTAINLY.ApprovalProfileUpdateRequestDto() # ApprovalProfileUpdateRequestDto | 

    try:
        # Edit an Approval profile
        api_response = api_instance.edit_approval_profile(uuid, approval_profile_update_request_dto)
        print("The response of ApprovalProfileInventoryApi->edit_approval_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalProfileInventoryApi->edit_approval_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval profile UUID | 
 **approval_profile_update_request_dto** | [**ApprovalProfileUpdateRequestDto**](ApprovalProfileUpdateRequestDto.md)|  | 

### Return type

**object**

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | Approval profile updated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_approval_profile**
> enable_approval_profile(uuid)

Enabling of Approval profile

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
    api_instance = pyCZERTAINLY.ApprovalProfileInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval profile UUID

    try:
        # Enabling of Approval profile
        api_instance.enable_approval_profile(uuid)
    except Exception as e:
        print("Exception when calling ApprovalProfileInventoryApi->enable_approval_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval profile UUID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Approval profile enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_profile**
> ApprovalProfileDetailDto get_approval_profile(uuid, approval_profile_for_version_dto)

Get Approval Profile Details

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.approval_profile_detail_dto import ApprovalProfileDetailDto
from pyCZERTAINLY.models.approval_profile_for_version_dto import ApprovalProfileForVersionDto
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
    api_instance = pyCZERTAINLY.ApprovalProfileInventoryApi(api_client)
    uuid = 'uuid_example' # str | Approval profile UUID
    approval_profile_for_version_dto = pyCZERTAINLY.ApprovalProfileForVersionDto() # ApprovalProfileForVersionDto | Select specific version of the approval profile

    try:
        # Get Approval Profile Details
        api_response = api_instance.get_approval_profile(uuid, approval_profile_for_version_dto)
        print("The response of ApprovalProfileInventoryApi->get_approval_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalProfileInventoryApi->get_approval_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Approval profile UUID | 
 **approval_profile_for_version_dto** | [**ApprovalProfileForVersionDto**](.md)| Select specific version of the approval profile | 

### Return type

[**ApprovalProfileDetailDto**](ApprovalProfileDetailDto.md)

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
**200** | Approval profile retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_approval_profiles**
> ApprovalProfileResponseDto list_approval_profiles(pagination_request_dto)

List Approval Profiles

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.approval_profile_response_dto import ApprovalProfileResponseDto
from pyCZERTAINLY.models.pagination_request_dto import PaginationRequestDto
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
    api_instance = pyCZERTAINLY.ApprovalProfileInventoryApi(api_client)
    pagination_request_dto = pyCZERTAINLY.PaginationRequestDto() # PaginationRequestDto | 

    try:
        # List Approval Profiles
        api_response = api_instance.list_approval_profiles(pagination_request_dto)
        print("The response of ApprovalProfileInventoryApi->list_approval_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalProfileInventoryApi->list_approval_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination_request_dto** | [**PaginationRequestDto**](.md)|  | 

### Return type

[**ApprovalProfileResponseDto**](ApprovalProfileResponseDto.md)

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
**200** | List of all the approval profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

