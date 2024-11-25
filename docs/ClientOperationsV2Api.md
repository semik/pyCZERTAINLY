# openapi_client.ClientOperationsV2Api

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issue_certificate**](ClientOperationsV2Api.md#issue_certificate) | **POST** /v2/operations/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/certificates | Issue Certificate
[**issue_requested_certificate**](ClientOperationsV2Api.md#issue_requested_certificate) | **POST** /v2/operations/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/certificates/{certificateUuid}/issue | Issue existing certificate with status Requested
[**list_issue_certificate_attributes**](ClientOperationsV2Api.md#list_issue_certificate_attributes) | **GET** /v2/operations/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/attributes/issue | Get issue Certificate Attributes
[**list_revoke_certificate_attributes**](ClientOperationsV2Api.md#list_revoke_certificate_attributes) | **GET** /v2/operations/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/attributes/revoke | Get revocation Attributes
[**rekey_certificate**](ClientOperationsV2Api.md#rekey_certificate) | **POST** /v2/operations/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/certificates/{certificateUuid}/rekey | Rekey Certificate
[**renew_certificate**](ClientOperationsV2Api.md#renew_certificate) | **POST** /v2/operations/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/certificates/{certificateUuid}/renew | Renew Certificate
[**revoke_certificate**](ClientOperationsV2Api.md#revoke_certificate) | **POST** /v2/operations/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/certificates/{certificateUuid}/revoke | Revoke Certificate
[**validate_issue_certificate_attributes**](ClientOperationsV2Api.md#validate_issue_certificate_attributes) | **POST** /v2/operations/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/attributes/issue/validate | Validate issue Certificate Attributes
[**validate_revoke_certificate_attributes**](ClientOperationsV2Api.md#validate_revoke_certificate_attributes) | **POST** /v2/operations/authorities/{authorityUuid}/raProfiles/{raProfileUuid}/attributes/revoke/validate | Validate revocation Attributes


# **issue_certificate**
> ClientCertificateDataResponseDto issue_certificate(authority_uuid, ra_profile_uuid, client_certificate_sign_request_dto)

Issue Certificate

### Example


```python
import openapi_client
from openapi_client.models.client_certificate_data_response_dto import ClientCertificateDataResponseDto
from openapi_client.models.client_certificate_sign_request_dto import ClientCertificateSignRequestDto
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
    api_instance = openapi_client.ClientOperationsV2Api(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    client_certificate_sign_request_dto = openapi_client.ClientCertificateSignRequestDto() # ClientCertificateSignRequestDto | 

    try:
        # Issue Certificate
        api_response = api_instance.issue_certificate(authority_uuid, ra_profile_uuid, client_certificate_sign_request_dto)
        print("The response of ClientOperationsV2Api->issue_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOperationsV2Api->issue_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
 **client_certificate_sign_request_dto** | [**ClientCertificateSignRequestDto**](ClientCertificateSignRequestDto.md)|  | 

### Return type

[**ClientCertificateDataResponseDto**](ClientCertificateDataResponseDto.md)

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
**200** | Certificate issued |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_requested_certificate**
> ClientCertificateDataResponseDto issue_requested_certificate(authority_uuid, ra_profile_uuid, certificate_uuid)

Issue existing certificate with status Requested

### Example


```python
import openapi_client
from openapi_client.models.client_certificate_data_response_dto import ClientCertificateDataResponseDto
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
    api_instance = openapi_client.ClientOperationsV2Api(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    certificate_uuid = 'certificate_uuid_example' # str | Certificate UUID

    try:
        # Issue existing certificate with status Requested
        api_response = api_instance.issue_requested_certificate(authority_uuid, ra_profile_uuid, certificate_uuid)
        print("The response of ClientOperationsV2Api->issue_requested_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOperationsV2Api->issue_requested_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
 **certificate_uuid** | **str**| Certificate UUID | 

### Return type

[**ClientCertificateDataResponseDto**](ClientCertificateDataResponseDto.md)

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
**200** | Certificate issued |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_issue_certificate_attributes**
> List[BaseAttributeDto] list_issue_certificate_attributes(authority_uuid, ra_profile_uuid)

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
    api_instance = openapi_client.ClientOperationsV2Api(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Get issue Certificate Attributes
        api_response = api_instance.list_issue_certificate_attributes(authority_uuid, ra_profile_uuid)
        print("The response of ClientOperationsV2Api->list_issue_certificate_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOperationsV2Api->list_issue_certificate_attributes: %s\n" % e)
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
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**200** | Attributes list obtained |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_revoke_certificate_attributes**
> List[BaseAttributeDto] list_revoke_certificate_attributes(authority_uuid, ra_profile_uuid)

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
    api_instance = openapi_client.ClientOperationsV2Api(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID

    try:
        # Get revocation Attributes
        api_response = api_instance.list_revoke_certificate_attributes(authority_uuid, ra_profile_uuid)
        print("The response of ClientOperationsV2Api->list_revoke_certificate_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOperationsV2Api->list_revoke_certificate_attributes: %s\n" % e)
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
**200** | Attributes obtained |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rekey_certificate**
> ClientCertificateDataResponseDto rekey_certificate(authority_uuid, ra_profile_uuid, certificate_uuid, client_certificate_rekey_request_dto)

Rekey Certificate

### Example


```python
import openapi_client
from openapi_client.models.client_certificate_data_response_dto import ClientCertificateDataResponseDto
from openapi_client.models.client_certificate_rekey_request_dto import ClientCertificateRekeyRequestDto
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
    api_instance = openapi_client.ClientOperationsV2Api(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    certificate_uuid = 'certificate_uuid_example' # str | Certificate UUID
    client_certificate_rekey_request_dto = openapi_client.ClientCertificateRekeyRequestDto() # ClientCertificateRekeyRequestDto | 

    try:
        # Rekey Certificate
        api_response = api_instance.rekey_certificate(authority_uuid, ra_profile_uuid, certificate_uuid, client_certificate_rekey_request_dto)
        print("The response of ClientOperationsV2Api->rekey_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOperationsV2Api->rekey_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
 **certificate_uuid** | **str**| Certificate UUID | 
 **client_certificate_rekey_request_dto** | [**ClientCertificateRekeyRequestDto**](ClientCertificateRekeyRequestDto.md)|  | 

### Return type

[**ClientCertificateDataResponseDto**](ClientCertificateDataResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate regenerated |  -  |
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_certificate**
> ClientCertificateDataResponseDto renew_certificate(authority_uuid, ra_profile_uuid, certificate_uuid, client_certificate_renew_request_dto)

Renew Certificate

### Example


```python
import openapi_client
from openapi_client.models.client_certificate_data_response_dto import ClientCertificateDataResponseDto
from openapi_client.models.client_certificate_renew_request_dto import ClientCertificateRenewRequestDto
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
    api_instance = openapi_client.ClientOperationsV2Api(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    certificate_uuid = 'certificate_uuid_example' # str | Certificate UUID
    client_certificate_renew_request_dto = openapi_client.ClientCertificateRenewRequestDto() # ClientCertificateRenewRequestDto | 

    try:
        # Renew Certificate
        api_response = api_instance.renew_certificate(authority_uuid, ra_profile_uuid, certificate_uuid, client_certificate_renew_request_dto)
        print("The response of ClientOperationsV2Api->renew_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientOperationsV2Api->renew_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
 **certificate_uuid** | **str**| Certificate UUID | 
 **client_certificate_renew_request_dto** | [**ClientCertificateRenewRequestDto**](ClientCertificateRenewRequestDto.md)|  | 

### Return type

[**ClientCertificateDataResponseDto**](ClientCertificateDataResponseDto.md)

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
**200** | Certificate renewed |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_certificate**
> revoke_certificate(authority_uuid, ra_profile_uuid, certificate_uuid, client_certificate_revocation_dto)

Revoke Certificate

### Example


```python
import openapi_client
from openapi_client.models.client_certificate_revocation_dto import ClientCertificateRevocationDto
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
    api_instance = openapi_client.ClientOperationsV2Api(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    certificate_uuid = 'certificate_uuid_example' # str | Certificate UUID
    client_certificate_revocation_dto = openapi_client.ClientCertificateRevocationDto() # ClientCertificateRevocationDto | 

    try:
        # Revoke Certificate
        api_instance.revoke_certificate(authority_uuid, ra_profile_uuid, certificate_uuid, client_certificate_revocation_dto)
    except Exception as e:
        print("Exception when calling ClientOperationsV2Api->revoke_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
 **certificate_uuid** | **str**| Certificate UUID | 
 **client_certificate_revocation_dto** | [**ClientCertificateRevocationDto**](ClientCertificateRevocationDto.md)|  | 

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
**204** | Certificate revoked |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_issue_certificate_attributes**
> validate_issue_certificate_attributes(authority_uuid, ra_profile_uuid, request_attribute_dto)

Validate issue Certificate Attributes

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
    api_instance = openapi_client.ClientOperationsV2Api(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    request_attribute_dto = [openapi_client.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Validate issue Certificate Attributes
        api_instance.validate_issue_certificate_attributes(authority_uuid, ra_profile_uuid, request_attribute_dto)
    except Exception as e:
        print("Exception when calling ClientOperationsV2Api->validate_issue_certificate_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
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
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Attributes validated |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_revoke_certificate_attributes**
> validate_revoke_certificate_attributes(authority_uuid, ra_profile_uuid, request_attribute_dto)

Validate revocation Attributes

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
    api_instance = openapi_client.ClientOperationsV2Api(api_client)
    authority_uuid = 'authority_uuid_example' # str | Authority Instance UUID
    ra_profile_uuid = 'ra_profile_uuid_example' # str | RA Profile UUID
    request_attribute_dto = [openapi_client.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Validate revocation Attributes
        api_instance.validate_revoke_certificate_attributes(authority_uuid, ra_profile_uuid, request_attribute_dto)
    except Exception as e:
        print("Exception when calling ClientOperationsV2Api->validate_revoke_certificate_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_uuid** | **str**| Authority Instance UUID | 
 **ra_profile_uuid** | **str**| RA Profile UUID | 
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
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Attributes validated |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

