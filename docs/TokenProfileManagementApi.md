# openapi_client.TokenProfileManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_profile**](TokenProfileManagementApi.md#create_token_profile) | **POST** /v1/tokens/{tokenInstanceUuid}/tokenProfiles | Create Token Profile
[**delete_ra_profile_without_token_instance**](TokenProfileManagementApi.md#delete_ra_profile_without_token_instance) | **DELETE** /v1/tokenProfiles/{uuid} | Delete Token Profile
[**delete_token_profile**](TokenProfileManagementApi.md#delete_token_profile) | **DELETE** /v1/tokens/{tokenInstanceUuid}/tokenProfiles/{uuid} | Delete Token Profile
[**delete_token_profiles**](TokenProfileManagementApi.md#delete_token_profiles) | **DELETE** /v1/tokenProfiles | Delete multiple Token Profiles
[**disable_token_profile**](TokenProfileManagementApi.md#disable_token_profile) | **PATCH** /v1/tokens/{tokenInstanceUuid}/tokenProfiles/{uuid}/disable | Disable Token Profile
[**disable_token_profiles**](TokenProfileManagementApi.md#disable_token_profiles) | **PATCH** /v1/tokenProfiles/disable | Disable multiple Token Profiles
[**edit_token_profile**](TokenProfileManagementApi.md#edit_token_profile) | **PUT** /v1/tokens/{tokenInstanceUuid}/tokenProfiles/{uuid} | Edit Token Profile
[**enable_token_profile**](TokenProfileManagementApi.md#enable_token_profile) | **PATCH** /v1/tokens/{tokenInstanceUuid}/tokenProfiles/{uuid}/enable | Enable Token Profile
[**enable_token_profiles**](TokenProfileManagementApi.md#enable_token_profiles) | **PATCH** /v1/tokenProfiles/enable | Enable multiple Token Profiles
[**get_token_profile**](TokenProfileManagementApi.md#get_token_profile) | **GET** /v1/tokens/{tokenInstanceUuid}/tokenProfiles/{uuid} | Details of Token Profile
[**list_token_profiles**](TokenProfileManagementApi.md#list_token_profiles) | **GET** /v1/tokenProfiles | List of available Token Profiles
[**update_key_usages**](TokenProfileManagementApi.md#update_key_usages) | **PUT** /v1/tokens/{tokenInstanceUuid}/tokenProfiles/{tokenProfileUuid}/usages | Update Key Usage
[**update_keys_usages**](TokenProfileManagementApi.md#update_keys_usages) | **PUT** /v1/tokens/usages | Update Key Usages for Multiple Token Profiles


# **create_token_profile**
> TokenProfileDetailDto create_token_profile(token_instance_uuid, add_token_profile_request_dto)

Create Token Profile

### Example


```python
import openapi_client
from openapi_client.models.add_token_profile_request_dto import AddTokenProfileRequestDto
from openapi_client.models.token_profile_detail_dto import TokenProfileDetailDto
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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    add_token_profile_request_dto = openapi_client.AddTokenProfileRequestDto() # AddTokenProfileRequestDto | 

    try:
        # Create Token Profile
        api_response = api_instance.create_token_profile(token_instance_uuid, add_token_profile_request_dto)
        print("The response of TokenProfileManagementApi->create_token_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->create_token_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **add_token_profile_request_dto** | [**AddTokenProfileRequestDto**](AddTokenProfileRequestDto.md)|  | 

### Return type

[**TokenProfileDetailDto**](TokenProfileDetailDto.md)

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
**201** | Token Profile added |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ra_profile_without_token_instance**
> delete_ra_profile_without_token_instance(uuid)

Delete Token Profile

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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    uuid = 'uuid_example' # str | Token Profile UUID

    try:
        # Delete Token Profile
        api_instance.delete_ra_profile_without_token_instance(uuid)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->delete_ra_profile_without_token_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Token Profile UUID | 

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
**204** | Token Profile deleted |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_profile**
> delete_token_profile(token_instance_uuid, uuid)

Delete Token Profile

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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Token Profile UUID

    try:
        # Delete Token Profile
        api_instance.delete_token_profile(token_instance_uuid, uuid)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->delete_token_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Token Profile UUID | 

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
**204** | Token Profile deleted |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_profiles**
> delete_token_profiles(request_body)

Delete multiple Token Profiles

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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Token Profile UUIDs

    try:
        # Delete multiple Token Profiles
        api_instance.delete_token_profiles(request_body)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->delete_token_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Token Profile UUIDs | 

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
**204** | Token Profiles deleted |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_token_profile**
> disable_token_profile(token_instance_uuid, uuid)

Disable Token Profile

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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Token Profile UUID

    try:
        # Disable Token Profile
        api_instance.disable_token_profile(token_instance_uuid, uuid)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->disable_token_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Token Profile UUID | 

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
**204** | Token Profile disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_token_profiles**
> disable_token_profiles(request_body)

Disable multiple Token Profiles

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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Token Profile UUIDs

    try:
        # Disable multiple Token Profiles
        api_instance.disable_token_profiles(request_body)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->disable_token_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Token Profile UUIDs | 

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
**204** | Token Profiles disabled |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_token_profile**
> TokenProfileDetailDto edit_token_profile(token_instance_uuid, uuid, edit_token_profile_request_dto)

Edit Token Profile

### Example


```python
import openapi_client
from openapi_client.models.edit_token_profile_request_dto import EditTokenProfileRequestDto
from openapi_client.models.token_profile_detail_dto import TokenProfileDetailDto
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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Token Profile UUID
    edit_token_profile_request_dto = openapi_client.EditTokenProfileRequestDto() # EditTokenProfileRequestDto | 

    try:
        # Edit Token Profile
        api_response = api_instance.edit_token_profile(token_instance_uuid, uuid, edit_token_profile_request_dto)
        print("The response of TokenProfileManagementApi->edit_token_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->edit_token_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Token Profile UUID | 
 **edit_token_profile_request_dto** | [**EditTokenProfileRequestDto**](EditTokenProfileRequestDto.md)|  | 

### Return type

[**TokenProfileDetailDto**](TokenProfileDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**204** | Token Profile updated |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_token_profile**
> enable_token_profile(token_instance_uuid, uuid)

Enable Token Profile

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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Token Profile UUID

    try:
        # Enable Token Profile
        api_instance.enable_token_profile(token_instance_uuid, uuid)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->enable_token_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Token Profile UUID | 

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
**204** | Token Profile enabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_token_profiles**
> enable_token_profiles(request_body)

Enable multiple Token Profiles

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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Token Profile UUIDs

    try:
        # Enable multiple Token Profiles
        api_instance.enable_token_profiles(request_body)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->enable_token_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Token Profile UUIDs | 

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
**204** | Token Profiles enabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_profile**
> TokenProfileDetailDto get_token_profile(token_instance_uuid, uuid)

Details of Token Profile

### Example


```python
import openapi_client
from openapi_client.models.token_profile_detail_dto import TokenProfileDetailDto
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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Token Profile UUID

    try:
        # Details of Token Profile
        api_response = api_instance.get_token_profile(token_instance_uuid, uuid)
        print("The response of TokenProfileManagementApi->get_token_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->get_token_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Token Profile UUID | 

### Return type

[**TokenProfileDetailDto**](TokenProfileDetailDto.md)

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
**200** | Token Profile details retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_token_profiles**
> List[TokenProfileDto] list_token_profiles(enabled=enabled)

List of available Token Profiles

### Example


```python
import openapi_client
from openapi_client.models.token_profile_dto import TokenProfileDto
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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    enabled = True # bool |  (optional)

    try:
        # List of available Token Profiles
        api_response = api_instance.list_token_profiles(enabled=enabled)
        print("The response of TokenProfileManagementApi->list_token_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->list_token_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**|  | [optional] 

### Return type

[**List[TokenProfileDto]**](TokenProfileDto.md)

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
**200** | Token Profiles retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key_usages**
> update_key_usages(token_instance_uuid, token_profile_uuid, token_profile_key_usage_request_dto)

Update Key Usage

### Example


```python
import openapi_client
from openapi_client.models.token_profile_key_usage_request_dto import TokenProfileKeyUsageRequestDto
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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    token_profile_uuid = 'token_profile_uuid_example' # str | Token Profile UUID
    token_profile_key_usage_request_dto = openapi_client.TokenProfileKeyUsageRequestDto() # TokenProfileKeyUsageRequestDto | 

    try:
        # Update Key Usage
        api_instance.update_key_usages(token_instance_uuid, token_profile_uuid, token_profile_key_usage_request_dto)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->update_key_usages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **token_profile_uuid** | **str**| Token Profile UUID | 
 **token_profile_key_usage_request_dto** | [**TokenProfileKeyUsageRequestDto**](TokenProfileKeyUsageRequestDto.md)|  | 

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
**204** | Key Usages Updated |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_keys_usages**
> update_keys_usages(bulk_token_profile_key_usage_request_dto)

Update Key Usages for Multiple Token Profiles

### Example


```python
import openapi_client
from openapi_client.models.bulk_token_profile_key_usage_request_dto import BulkTokenProfileKeyUsageRequestDto
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
    api_instance = openapi_client.TokenProfileManagementApi(api_client)
    bulk_token_profile_key_usage_request_dto = openapi_client.BulkTokenProfileKeyUsageRequestDto() # BulkTokenProfileKeyUsageRequestDto | 

    try:
        # Update Key Usages for Multiple Token Profiles
        api_instance.update_keys_usages(bulk_token_profile_key_usage_request_dto)
    except Exception as e:
        print("Exception when calling TokenProfileManagementApi->update_keys_usages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_token_profile_key_usage_request_dto** | [**BulkTokenProfileKeyUsageRequestDto**](BulkTokenProfileKeyUsageRequestDto.md)|  | 

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
**204** | Key Usages Updated |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

