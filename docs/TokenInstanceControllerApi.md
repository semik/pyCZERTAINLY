# openapi_client.TokenInstanceControllerApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_token_instance**](TokenInstanceControllerApi.md#activate_token_instance) | **PATCH** /v1/tokens/{uuid}/activate | Activate Token Instance
[**create_token_instance**](TokenInstanceControllerApi.md#create_token_instance) | **POST** /v1/tokens | Create a new Token Instance
[**deactivate_token_instance**](TokenInstanceControllerApi.md#deactivate_token_instance) | **PATCH** /v1/tokens/{uuid}/deactivate | Deactivate Token Instance
[**delete_token_instance**](TokenInstanceControllerApi.md#delete_token_instance) | **DELETE** /v1/tokens/{uuid} | 
[**delete_token_instance1**](TokenInstanceControllerApi.md#delete_token_instance1) | **DELETE** /v1/tokens/delete | 
[**get_token_instance**](TokenInstanceControllerApi.md#get_token_instance) | **GET** /v1/tokens/{uuid} | Get Token Instance Detail
[**list_token_instance_activation_attributes**](TokenInstanceControllerApi.md#list_token_instance_activation_attributes) | **GET** /v1/tokens/{uuid}/activate/attributes | List Token activation Attributes
[**list_token_instances**](TokenInstanceControllerApi.md#list_token_instances) | **GET** /v1/tokens | List Token Instances
[**list_token_profile_attributes**](TokenInstanceControllerApi.md#list_token_profile_attributes) | **GET** /v1/tokens/{uuid}/tokenProfiles/attributes | List Token Profile Attributes
[**reload_status**](TokenInstanceControllerApi.md#reload_status) | **PATCH** /v1/tokens/{uuid} | Reload Token Instance status
[**update_token_instance**](TokenInstanceControllerApi.md#update_token_instance) | **PUT** /v1/tokens/{uuid} | Update Token Instance


# **activate_token_instance**
> activate_token_instance(uuid, request_attribute_dto)

Activate Token Instance

### Example


```python
import openapi_client
from openapi_client.models.request_attribute_dto import RequestAttributeDto
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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    uuid = 'uuid_example' # str | Token Instance UUID
    request_attribute_dto = [openapi_client.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Activate Token Instance
        api_instance.activate_token_instance(uuid, request_attribute_dto)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->activate_token_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Token Instance UUID | 
 **request_attribute_dto** | [**List[RequestAttributeDto]**](RequestAttributeDto.md)|  | 

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
**204** | Token Instance Activated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token_instance**
> TokenInstanceDetailDto create_token_instance(token_instance_request_dto)

Create a new Token Instance

### Example


```python
import openapi_client
from openapi_client.models.token_instance_detail_dto import TokenInstanceDetailDto
from openapi_client.models.token_instance_request_dto import TokenInstanceRequestDto
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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    token_instance_request_dto = openapi_client.TokenInstanceRequestDto() # TokenInstanceRequestDto | 

    try:
        # Create a new Token Instance
        api_response = api_instance.create_token_instance(token_instance_request_dto)
        print("The response of TokenInstanceControllerApi->create_token_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->create_token_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_request_dto** | [**TokenInstanceRequestDto**](TokenInstanceRequestDto.md)|  | 

### Return type

[**TokenInstanceDetailDto**](TokenInstanceDetailDto.md)

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
**201** | Token Instance Created Successfully |  -  |
**500** | Internal Server Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_token_instance**
> deactivate_token_instance(uuid)

Deactivate Token Instance

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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    uuid = 'uuid_example' # str | Token Instance UUID

    try:
        # Deactivate Token Instance
        api_instance.deactivate_token_instance(uuid)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->deactivate_token_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Token Instance UUID | 

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
**204** | Token Instance Deactivated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_instance**
> delete_token_instance(uuid)



Delete Token Instance

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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    uuid = 'uuid_example' # str | Token Instance UUID

    try:
        api_instance.delete_token_instance(uuid)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->delete_token_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Token Instance UUID | 

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
**204** | Token Instance deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_instance1**
> delete_token_instance1(request_body)



Delete multiple Token Instance

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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Token Instance UUIDs

    try:
        api_instance.delete_token_instance1(request_body)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->delete_token_instance1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Token Instance UUIDs | 

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
**500** | Internal Server Error |  -  |
**204** | Token Instances deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_instance**
> TokenInstanceDetailDto get_token_instance(uuid)

Get Token Instance Detail

### Example


```python
import openapi_client
from openapi_client.models.token_instance_detail_dto import TokenInstanceDetailDto
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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the Token Instance

    try:
        # Get Token Instance Detail
        api_response = api_instance.get_token_instance(uuid)
        print("The response of TokenInstanceControllerApi->get_token_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->get_token_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the Token Instance | 

### Return type

[**TokenInstanceDetailDto**](TokenInstanceDetailDto.md)

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
**200** | Token Instance Detail retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_token_instance_activation_attributes**
> List[BaseAttributeDto] list_token_instance_activation_attributes(uuid)

List Token activation Attributes

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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    uuid = 'uuid_example' # str | Token Instance UUID

    try:
        # List Token activation Attributes
        api_response = api_instance.list_token_instance_activation_attributes(uuid)
        print("The response of TokenInstanceControllerApi->list_token_instance_activation_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->list_token_instance_activation_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Token Instance UUID | 

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
**200** | Token activation Attributes retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_token_instances**
> List[TokenInstanceDto] list_token_instances()

List Token Instances

### Example


```python
import openapi_client
from openapi_client.models.token_instance_dto import TokenInstanceDto
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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)

    try:
        # List Token Instances
        api_response = api_instance.list_token_instances()
        print("The response of TokenInstanceControllerApi->list_token_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->list_token_instances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TokenInstanceDto]**](TokenInstanceDto.md)

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
**200** | Token Instances retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_token_profile_attributes**
> List[BaseAttributeDto] list_token_profile_attributes(uuid)

List Token Profile Attributes

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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    uuid = 'uuid_example' # str | Token instance UUID

    try:
        # List Token Profile Attributes
        api_response = api_instance.list_token_profile_attributes(uuid)
        print("The response of TokenInstanceControllerApi->list_token_profile_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->list_token_profile_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Token instance UUID | 

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
**200** | Token Profile Attributes retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_status**
> TokenInstanceDetailDto reload_status(uuid)

Reload Token Instance status

### Example


```python
import openapi_client
from openapi_client.models.token_instance_detail_dto import TokenInstanceDetailDto
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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the Token Instance

    try:
        # Reload Token Instance status
        api_response = api_instance.reload_status(uuid)
        print("The response of TokenInstanceControllerApi->reload_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->reload_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the Token Instance | 

### Return type

[**TokenInstanceDetailDto**](TokenInstanceDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token Instance Status Reloaded from Connector |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token_instance**
> TokenInstanceDetailDto update_token_instance(uuid, token_instance_request_dto)

Update Token Instance

### Example


```python
import openapi_client
from openapi_client.models.token_instance_detail_dto import TokenInstanceDetailDto
from openapi_client.models.token_instance_request_dto import TokenInstanceRequestDto
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
    api_instance = openapi_client.TokenInstanceControllerApi(api_client)
    uuid = 'uuid_example' # str | Token Instance UUID
    token_instance_request_dto = openapi_client.TokenInstanceRequestDto() # TokenInstanceRequestDto | 

    try:
        # Update Token Instance
        api_response = api_instance.update_token_instance(uuid, token_instance_request_dto)
        print("The response of TokenInstanceControllerApi->update_token_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenInstanceControllerApi->update_token_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Token Instance UUID | 
 **token_instance_request_dto** | [**TokenInstanceRequestDto**](TokenInstanceRequestDto.md)|  | 

### Return type

[**TokenInstanceDetailDto**](TokenInstanceDetailDto.md)

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
**200** | Token Instance Updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

