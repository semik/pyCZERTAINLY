# pyCZERTAINLY.ConnectorAuthenticationApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_key_auth_attributes**](ConnectorAuthenticationApi.md#get_api_key_auth_attributes) | **GET** /v1/connectors/auth/attributes/apiKey | Get API Key auth Attributes
[**get_authentication_types**](ConnectorAuthenticationApi.md#get_authentication_types) | **GET** /v1/connectors/auth/types | Get list of Authentication Types
[**get_basic_auth_attributes**](ConnectorAuthenticationApi.md#get_basic_auth_attributes) | **GET** /v1/connectors/auth/attributes/basic | Get basic auth Attributes
[**get_certificate_attributes**](ConnectorAuthenticationApi.md#get_certificate_attributes) | **GET** /v1/connectors/auth/attributes/certificate | Get Attributes for certificate auth
[**get_jwt_auth_attributes**](ConnectorAuthenticationApi.md#get_jwt_auth_attributes) | **GET** /v1/connectors/auth/attributes/jwt | Get JWT auth Attributes
[**validate_api_key_auth_attributes**](ConnectorAuthenticationApi.md#validate_api_key_auth_attributes) | **POST** /v1/connectors/auth/attributes/apiKey/validate | Validate API Key Attributes
[**validate_basic_auth_attributes**](ConnectorAuthenticationApi.md#validate_basic_auth_attributes) | **POST** /v1/connectors/auth/attributes/basic/validate | Validate basic auth Attributes
[**validate_certificate_attributes**](ConnectorAuthenticationApi.md#validate_certificate_attributes) | **POST** /v1/connectors/auth/attributes/certificate/validate | Validate certificate auth Attributes
[**validate_jwt_auth_attributes**](ConnectorAuthenticationApi.md#validate_jwt_auth_attributes) | **POST** /v1/connectors/auth/attributes/jwt/validate | Validate JWT auth Attributes


# **get_api_key_auth_attributes**
> List[BaseAttributeDto] get_api_key_auth_attributes()

Get API Key auth Attributes

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.base_attribute_dto import BaseAttributeDto
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
    api_instance = pyCZERTAINLY.ConnectorAuthenticationApi(api_client)

    try:
        # Get API Key auth Attributes
        api_response = api_instance.get_api_key_auth_attributes()
        print("The response of ConnectorAuthenticationApi->get_api_key_auth_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorAuthenticationApi->get_api_key_auth_attributes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Attributes retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_types**
> List[str] get_authentication_types()

Get list of Authentication Types

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
    api_instance = pyCZERTAINLY.ConnectorAuthenticationApi(api_client)

    try:
        # Get list of Authentication Types
        api_response = api_instance.get_authentication_types()
        print("The response of ConnectorAuthenticationApi->get_authentication_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorAuthenticationApi->get_authentication_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

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
**200** | Auth Types retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_basic_auth_attributes**
> List[BaseAttributeDto] get_basic_auth_attributes()

Get basic auth Attributes

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.base_attribute_dto import BaseAttributeDto
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
    api_instance = pyCZERTAINLY.ConnectorAuthenticationApi(api_client)

    try:
        # Get basic auth Attributes
        api_response = api_instance.get_basic_auth_attributes()
        print("The response of ConnectorAuthenticationApi->get_basic_auth_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorAuthenticationApi->get_basic_auth_attributes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Attributes retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_attributes**
> List[BaseAttributeDto] get_certificate_attributes()

Get Attributes for certificate auth

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.base_attribute_dto import BaseAttributeDto
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
    api_instance = pyCZERTAINLY.ConnectorAuthenticationApi(api_client)

    try:
        # Get Attributes for certificate auth
        api_response = api_instance.get_certificate_attributes()
        print("The response of ConnectorAuthenticationApi->get_certificate_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorAuthenticationApi->get_certificate_attributes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Attributes retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwt_auth_attributes**
> List[BaseAttributeDto] get_jwt_auth_attributes()

Get JWT auth Attributes

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.base_attribute_dto import BaseAttributeDto
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
    api_instance = pyCZERTAINLY.ConnectorAuthenticationApi(api_client)

    try:
        # Get JWT auth Attributes
        api_response = api_instance.get_jwt_auth_attributes()
        print("The response of ConnectorAuthenticationApi->get_jwt_auth_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorAuthenticationApi->get_jwt_auth_attributes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Attributes retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_api_key_auth_attributes**
> validate_api_key_auth_attributes(request_attribute_dto)

Validate API Key Attributes

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.request_attribute_dto import RequestAttributeDto
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
    api_instance = pyCZERTAINLY.ConnectorAuthenticationApi(api_client)
    request_attribute_dto = [pyCZERTAINLY.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Validate API Key Attributes
        api_instance.validate_api_key_auth_attributes(request_attribute_dto)
    except Exception as e:
        print("Exception when calling ConnectorAuthenticationApi->validate_api_key_auth_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**500** | Internal Server Error |  -  |
**200** | Attributes validated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_basic_auth_attributes**
> validate_basic_auth_attributes(request_attribute_dto)

Validate basic auth Attributes

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.request_attribute_dto import RequestAttributeDto
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
    api_instance = pyCZERTAINLY.ConnectorAuthenticationApi(api_client)
    request_attribute_dto = [pyCZERTAINLY.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Validate basic auth Attributes
        api_instance.validate_basic_auth_attributes(request_attribute_dto)
    except Exception as e:
        print("Exception when calling ConnectorAuthenticationApi->validate_basic_auth_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**500** | Internal Server Error |  -  |
**200** | Attributes validated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_certificate_attributes**
> validate_certificate_attributes(request_attribute_dto)

Validate certificate auth Attributes

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.request_attribute_dto import RequestAttributeDto
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
    api_instance = pyCZERTAINLY.ConnectorAuthenticationApi(api_client)
    request_attribute_dto = [pyCZERTAINLY.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Validate certificate auth Attributes
        api_instance.validate_certificate_attributes(request_attribute_dto)
    except Exception as e:
        print("Exception when calling ConnectorAuthenticationApi->validate_certificate_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**500** | Internal Server Error |  -  |
**200** | Attributes validated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_jwt_auth_attributes**
> validate_jwt_auth_attributes(request_attribute_dto)

Validate JWT auth Attributes

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.request_attribute_dto import RequestAttributeDto
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
    api_instance = pyCZERTAINLY.ConnectorAuthenticationApi(api_client)
    request_attribute_dto = [pyCZERTAINLY.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Validate JWT auth Attributes
        api_instance.validate_jwt_auth_attributes(request_attribute_dto)
    except Exception as e:
        print("Exception when calling ConnectorAuthenticationApi->validate_jwt_auth_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**500** | Internal Server Error |  -  |
**200** | Attributes validated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

