# openapi_client.CredentialManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_credential**](CredentialManagementApi.md#bulk_delete_credential) | **DELETE** /v1/credentials | Delete multiple Credentials
[**create_credential**](CredentialManagementApi.md#create_credential) | **POST** /v1/credentials | Add Credential
[**delete_credential**](CredentialManagementApi.md#delete_credential) | **DELETE** /v1/credentials/{uuid} | Delete Credential
[**disable_credential**](CredentialManagementApi.md#disable_credential) | **PATCH** /v1/credentials/{uuid}/disable | Disable Credential
[**edit_credential**](CredentialManagementApi.md#edit_credential) | **PUT** /v1/credentials/{uuid} | Edit Credential
[**enable_credential**](CredentialManagementApi.md#enable_credential) | **PATCH** /v1/credentials/{uuid}/enable | Enable Credential
[**get_credential**](CredentialManagementApi.md#get_credential) | **GET** /v1/credentials/{uuid} | Details of a Credentials
[**list_credentials**](CredentialManagementApi.md#list_credentials) | **GET** /v1/credentials | List of All Credentials


# **bulk_delete_credential**
> bulk_delete_credential(request_body)

Delete multiple Credentials

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
    api_instance = openapi_client.CredentialManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Credential UUIDs

    try:
        # Delete multiple Credentials
        api_instance.bulk_delete_credential(request_body)
    except Exception as e:
        print("Exception when calling CredentialManagementApi->bulk_delete_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Credential UUIDs | 

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
**200** | Credentials deleted |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credential**
> UuidDto create_credential(credential_request_dto)

Add Credential

### Example


```python
import openapi_client
from openapi_client.models.credential_request_dto import CredentialRequestDto
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
    api_instance = openapi_client.CredentialManagementApi(api_client)
    credential_request_dto = openapi_client.CredentialRequestDto() # CredentialRequestDto | 

    try:
        # Add Credential
        api_response = api_instance.create_credential(credential_request_dto)
        print("The response of CredentialManagementApi->create_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialManagementApi->create_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_request_dto** | [**CredentialRequestDto**](CredentialRequestDto.md)|  | 

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
**403** | Forbidden |  -  |
**201** | New Credential added |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credential**
> delete_credential(uuid)

Delete Credential

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
    api_instance = openapi_client.CredentialManagementApi(api_client)
    uuid = 'uuid_example' # str | Credential UUID

    try:
        # Delete Credential
        api_instance.delete_credential(uuid)
    except Exception as e:
        print("Exception when calling CredentialManagementApi->delete_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Credential UUID | 

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
**204** | Credential deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_credential**
> disable_credential(uuid)

Disable Credential

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
    api_instance = openapi_client.CredentialManagementApi(api_client)
    uuid = 'uuid_example' # str | Credential UUID

    try:
        # Disable Credential
        api_instance.disable_credential(uuid)
    except Exception as e:
        print("Exception when calling CredentialManagementApi->disable_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Credential UUID | 

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
**204** | Credential disabled |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_credential**
> CredentialDto edit_credential(uuid, credential_update_request_dto)

Edit Credential

### Example


```python
import openapi_client
from openapi_client.models.credential_dto import CredentialDto
from openapi_client.models.credential_update_request_dto import CredentialUpdateRequestDto
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
    api_instance = openapi_client.CredentialManagementApi(api_client)
    uuid = 'uuid_example' # str | Credential UUID
    credential_update_request_dto = openapi_client.CredentialUpdateRequestDto() # CredentialUpdateRequestDto | 

    try:
        # Edit Credential
        api_response = api_instance.edit_credential(uuid, credential_update_request_dto)
        print("The response of CredentialManagementApi->edit_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialManagementApi->edit_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Credential UUID | 
 **credential_update_request_dto** | [**CredentialUpdateRequestDto**](CredentialUpdateRequestDto.md)|  | 

### Return type

[**CredentialDto**](CredentialDto.md)

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
**200** | Credential updated |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_credential**
> enable_credential(uuid)

Enable Credential

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
    api_instance = openapi_client.CredentialManagementApi(api_client)
    uuid = 'uuid_example' # str | Credential UUID

    try:
        # Enable Credential
        api_instance.enable_credential(uuid)
    except Exception as e:
        print("Exception when calling CredentialManagementApi->enable_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Credential UUID | 

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
**204** | Credential enabled |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential**
> CredentialDto get_credential(uuid)

Details of a Credentials

### Example


```python
import openapi_client
from openapi_client.models.credential_dto import CredentialDto
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
    api_instance = openapi_client.CredentialManagementApi(api_client)
    uuid = 'uuid_example' # str | Credential UUID

    try:
        # Details of a Credentials
        api_response = api_instance.get_credential(uuid)
        print("The response of CredentialManagementApi->get_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialManagementApi->get_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Credential UUID | 

### Return type

[**CredentialDto**](CredentialDto.md)

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
**200** | Credential details retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credentials**
> List[CredentialDto] list_credentials()

List of All Credentials

### Example


```python
import openapi_client
from openapi_client.models.credential_dto import CredentialDto
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
    api_instance = openapi_client.CredentialManagementApi(api_client)

    try:
        # List of All Credentials
        api_response = api_instance.list_credentials()
        print("The response of CredentialManagementApi->list_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialManagementApi->list_credentials: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CredentialDto]**](CredentialDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all Credentials |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

