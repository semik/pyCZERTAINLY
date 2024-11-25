# openapi_client.ACMEProfileManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_acme_profile**](ACMEProfileManagementApi.md#bulk_delete_acme_profile) | **DELETE** /v1/acmeProfiles/delete | Delete multiple ACME Profiles
[**bulk_disable_acme_profile**](ACMEProfileManagementApi.md#bulk_disable_acme_profile) | **PATCH** /v1/acmeProfiles/disable | Disable multiple ACME Profile
[**bulk_enable_acme_profile**](ACMEProfileManagementApi.md#bulk_enable_acme_profile) | **PATCH** /v1/acmeProfiles/enable | Enable multiple ACME Profiles
[**create_acme_profile**](ACMEProfileManagementApi.md#create_acme_profile) | **POST** /v1/acmeProfiles | Create ACME Profile
[**delete_acme_profile**](ACMEProfileManagementApi.md#delete_acme_profile) | **DELETE** /v1/acmeProfiles/{uuid} | Delete ACME Profile
[**disable_acme_profile**](ACMEProfileManagementApi.md#disable_acme_profile) | **PATCH** /v1/acmeProfiles/{uuid}/disable | Disable ACME Profile
[**edit_acme_profile**](ACMEProfileManagementApi.md#edit_acme_profile) | **PUT** /v1/acmeProfiles/{uuid} | Edit ACME Profile
[**enable_acme_profile**](ACMEProfileManagementApi.md#enable_acme_profile) | **PATCH** /v1/acmeProfiles/{uuid}/enable | Enable ACME Profile
[**force_delete_acme_profiles**](ACMEProfileManagementApi.md#force_delete_acme_profiles) | **DELETE** /v1/acmeProfiles/delete/force | Force delete multiple ACME Profiles
[**get_acme_profile**](ACMEProfileManagementApi.md#get_acme_profile) | **GET** /v1/acmeProfiles/{uuid} | Get details of ACME Profile
[**list_acme_profiles**](ACMEProfileManagementApi.md#list_acme_profiles) | **GET** /v1/acmeProfiles | Get list of ACME Profiles
[**update_ra_profile2**](ACMEProfileManagementApi.md#update_ra_profile2) | **PATCH** /v1/acmeProfiles/{uuid}/raprofile/{raProfileUuid} | Update RA Profile for ACME Profile


# **bulk_delete_acme_profile**
> List[BulkActionMessageDto] bulk_delete_acme_profile(request_body)

Delete multiple ACME Profiles

### Example


```python
import openapi_client
from openapi_client.models.bulk_action_message_dto import BulkActionMessageDto
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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | ACME Profile UUIDs

    try:
        # Delete multiple ACME Profiles
        api_response = api_instance.bulk_delete_acme_profile(request_body)
        print("The response of ACMEProfileManagementApi->bulk_delete_acme_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->bulk_delete_acme_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| ACME Profile UUIDs | 

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
**500** | Internal Server Error |  -  |
**200** | ACME Profiles deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_disable_acme_profile**
> bulk_disable_acme_profile(request_body)

Disable multiple ACME Profile

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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | ACME Profile UUIDs

    try:
        # Disable multiple ACME Profile
        api_instance.bulk_disable_acme_profile(request_body)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->bulk_disable_acme_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| ACME Profile UUIDs | 

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
**200** | ACME Profiles disabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_acme_profile**
> bulk_enable_acme_profile(request_body)

Enable multiple ACME Profiles

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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | ACME Profile UUIDs

    try:
        # Enable multiple ACME Profiles
        api_instance.bulk_enable_acme_profile(request_body)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->bulk_enable_acme_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| ACME Profile UUIDs | 

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
**200** | ACME Profiles enabled |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_acme_profile**
> UuidDto create_acme_profile(acme_profile_request_dto)

Create ACME Profile

### Example


```python
import openapi_client
from openapi_client.models.acme_profile_request_dto import AcmeProfileRequestDto
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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    acme_profile_request_dto = openapi_client.AcmeProfileRequestDto() # AcmeProfileRequestDto | 

    try:
        # Create ACME Profile
        api_response = api_instance.create_acme_profile(acme_profile_request_dto)
        print("The response of ACMEProfileManagementApi->create_acme_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->create_acme_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acme_profile_request_dto** | [**AcmeProfileRequestDto**](AcmeProfileRequestDto.md)|  | 

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
**201** | ACME Profile created |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_acme_profile**
> delete_acme_profile(uuid)

Delete ACME Profile

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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | ACME Profile UUID

    try:
        # Delete ACME Profile
        api_instance.delete_acme_profile(uuid)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->delete_acme_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ACME Profile UUID | 

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
**204** | ACME Profile deleted |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_acme_profile**
> disable_acme_profile(uuid)

Disable ACME Profile

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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | ACME Profile UUID

    try:
        # Disable ACME Profile
        api_instance.disable_acme_profile(uuid)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->disable_acme_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ACME Profile UUID | 

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
**200** | ACME Profile disabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_acme_profile**
> AcmeProfileDto edit_acme_profile(uuid, acme_profile_edit_request_dto)

Edit ACME Profile

### Example


```python
import openapi_client
from openapi_client.models.acme_profile_dto import AcmeProfileDto
from openapi_client.models.acme_profile_edit_request_dto import AcmeProfileEditRequestDto
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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | ACME Profile UUID
    acme_profile_edit_request_dto = openapi_client.AcmeProfileEditRequestDto() # AcmeProfileEditRequestDto | 

    try:
        # Edit ACME Profile
        api_response = api_instance.edit_acme_profile(uuid, acme_profile_edit_request_dto)
        print("The response of ACMEProfileManagementApi->edit_acme_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->edit_acme_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ACME Profile UUID | 
 **acme_profile_edit_request_dto** | [**AcmeProfileEditRequestDto**](AcmeProfileEditRequestDto.md)|  | 

### Return type

[**AcmeProfileDto**](AcmeProfileDto.md)

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
**200** | ACME Profile updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_acme_profile**
> enable_acme_profile(uuid)

Enable ACME Profile

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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | ACME Profile UUID

    try:
        # Enable ACME Profile
        api_instance.enable_acme_profile(uuid)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->enable_acme_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ACME Profile UUID | 

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
**200** | ACME Profile enabled |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_acme_profiles**
> List[BulkActionMessageDto] force_delete_acme_profiles(request_body)

Force delete multiple ACME Profiles

### Example


```python
import openapi_client
from openapi_client.models.bulk_action_message_dto import BulkActionMessageDto
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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | ACME Profile UUIDs

    try:
        # Force delete multiple ACME Profiles
        api_response = api_instance.force_delete_acme_profiles(request_body)
        print("The response of ACMEProfileManagementApi->force_delete_acme_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->force_delete_acme_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| ACME Profile UUIDs | 

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
**200** | ACME Profiles forced to delete |  -  |
**500** | Internal Server Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acme_profile**
> AcmeProfileDto get_acme_profile(uuid)

Get details of ACME Profile

### Example


```python
import openapi_client
from openapi_client.models.acme_profile_dto import AcmeProfileDto
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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | ACME Profile UUID

    try:
        # Get details of ACME Profile
        api_response = api_instance.get_acme_profile(uuid)
        print("The response of ACMEProfileManagementApi->get_acme_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->get_acme_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ACME Profile UUID | 

### Return type

[**AcmeProfileDto**](AcmeProfileDto.md)

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
**200** | ACME Profile details retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_acme_profiles**
> List[AcmeProfileListDto] list_acme_profiles()

Get list of ACME Profiles

### Example


```python
import openapi_client
from openapi_client.models.acme_profile_list_dto import AcmeProfileListDto
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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)

    try:
        # Get list of ACME Profiles
        api_response = api_instance.list_acme_profiles()
        print("The response of ACMEProfileManagementApi->list_acme_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->list_acme_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AcmeProfileListDto]**](AcmeProfileListDto.md)

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
**200** | ACME Profile list retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ra_profile2**
> update_ra_profile2(uuid, ra_profile_uuid)

Update RA Profile for ACME Profile

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
    api_instance = openapi_client.ACMEProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | ACME Profile UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Update RA Profile for ACME Profile
        api_instance.update_ra_profile2(uuid, ra_profile_uuid)
    except Exception as e:
        print("Exception when calling ACMEProfileManagementApi->update_ra_profile2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| ACME Profile UUID | 
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

