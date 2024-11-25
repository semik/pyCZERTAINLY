# openapi_client.CryptographicOperationsControllerApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decrypt_data**](CryptographicOperationsControllerApi.md#decrypt_data) | **POST** /v1/operations/tokens/{tokenInstanceUuid}/tokenProfiles/{tokenProfileUuid}/keys/{uuid}/items/{keyItemUuid}/decrypt | Decrypt data using a Key
[**encrypt_data**](CryptographicOperationsControllerApi.md#encrypt_data) | **POST** /v1/operations/tokens/{tokenInstanceUuid}/tokenProfiles/{tokenProfileUuid}/keys/{uuid}/items/{keyItemUuid}/encrypt | Encrypt data using a Key
[**list_cipher_attributes**](CryptographicOperationsControllerApi.md#list_cipher_attributes) | **GET** /v1/operations/tokens/{tokenInstanceUuid}/tokenProfiles/{tokenProfileUuid}/keys/{uuid}/items/{keyItemUuid}/cipher/{algorithm}/attributes | List of cipher Attributes
[**list_random_attributes**](CryptographicOperationsControllerApi.md#list_random_attributes) | **GET** /v1/operations/tokens/{tokenInstanceUuid}/random/attributes | List of random generator Attributes
[**list_signature_attributes**](CryptographicOperationsControllerApi.md#list_signature_attributes) | **GET** /v1/operations/tokens/{tokenInstanceUuid}/tokenProfiles/{tokenProfileUuid}/keys/{uuid}/items/{keyItemUuid}/signature/{algorithm}/attributes | List of signature Attributes
[**random_data**](CryptographicOperationsControllerApi.md#random_data) | **POST** /v1/operations/tokens/{tokenInstanceUuid}/random | Generate random data
[**sign_data**](CryptographicOperationsControllerApi.md#sign_data) | **POST** /v1/operations/tokens/{tokenInstanceUuid}/tokenProfiles/{tokenProfileUuid}/keys/{uuid}/items/{keyItemUuid}/sign | Sign data using a Key
[**verify_data**](CryptographicOperationsControllerApi.md#verify_data) | **POST** /v1/operations/tokens/{tokenInstanceUuid}/tokenProfiles/{tokenProfileUuid}/keys/{uuid}/items/{keyItemUuid}/verify | Verify data using a Key


# **decrypt_data**
> DecryptDataResponseDto decrypt_data(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, cipher_data_request_dto)

Decrypt data using a Key

### Example


```python
import openapi_client
from openapi_client.models.cipher_data_request_dto import CipherDataRequestDto
from openapi_client.models.decrypt_data_response_dto import DecryptDataResponseDto
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
    api_instance = openapi_client.CryptographicOperationsControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    token_profile_uuid = 'token_profile_uuid_example' # str | Token Profile UUID
    uuid = 'uuid_example' # str | Key UUID
    key_item_uuid = 'key_item_uuid_example' # str | Key Item UUID
    cipher_data_request_dto = openapi_client.CipherDataRequestDto() # CipherDataRequestDto | 

    try:
        # Decrypt data using a Key
        api_response = api_instance.decrypt_data(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, cipher_data_request_dto)
        print("The response of CryptographicOperationsControllerApi->decrypt_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicOperationsControllerApi->decrypt_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **token_profile_uuid** | **str**| Token Profile UUID | 
 **uuid** | **str**| Key UUID | 
 **key_item_uuid** | **str**| Key Item UUID | 
 **cipher_data_request_dto** | [**CipherDataRequestDto**](CipherDataRequestDto.md)|  | 

### Return type

[**DecryptDataResponseDto**](DecryptDataResponseDto.md)

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
**500** | Internal Server Error |  -  |
**200** | Data decrypted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encrypt_data**
> EncryptDataResponseDto encrypt_data(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, cipher_data_request_dto)

Encrypt data using a Key

### Example


```python
import openapi_client
from openapi_client.models.cipher_data_request_dto import CipherDataRequestDto
from openapi_client.models.encrypt_data_response_dto import EncryptDataResponseDto
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
    api_instance = openapi_client.CryptographicOperationsControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    token_profile_uuid = 'token_profile_uuid_example' # str | Token Profile UUID
    uuid = 'uuid_example' # str | Key UUID
    key_item_uuid = 'key_item_uuid_example' # str | Key Item UUID
    cipher_data_request_dto = openapi_client.CipherDataRequestDto() # CipherDataRequestDto | 

    try:
        # Encrypt data using a Key
        api_response = api_instance.encrypt_data(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, cipher_data_request_dto)
        print("The response of CryptographicOperationsControllerApi->encrypt_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicOperationsControllerApi->encrypt_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **token_profile_uuid** | **str**| Token Profile UUID | 
 **uuid** | **str**| Key UUID | 
 **key_item_uuid** | **str**| Key Item UUID | 
 **cipher_data_request_dto** | [**CipherDataRequestDto**](CipherDataRequestDto.md)|  | 

### Return type

[**EncryptDataResponseDto**](EncryptDataResponseDto.md)

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
**200** | Data encrypted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cipher_attributes**
> List[BaseAttributeDto] list_cipher_attributes(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, algorithm)

List of cipher Attributes

### Example


```python
import openapi_client
from openapi_client.models.base_attribute_dto import BaseAttributeDto
from openapi_client.models.key_algorithm import KeyAlgorithm
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
    api_instance = openapi_client.CryptographicOperationsControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    token_profile_uuid = 'token_profile_uuid_example' # str | Token Profile UUID
    uuid = 'uuid_example' # str | Key UUID
    key_item_uuid = 'key_item_uuid_example' # str | Key Item UUID
    algorithm = openapi_client.KeyAlgorithm() # KeyAlgorithm | Cryptographic algorithm

    try:
        # List of cipher Attributes
        api_response = api_instance.list_cipher_attributes(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, algorithm)
        print("The response of CryptographicOperationsControllerApi->list_cipher_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicOperationsControllerApi->list_cipher_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **token_profile_uuid** | **str**| Token Profile UUID | 
 **uuid** | **str**| Key UUID | 
 **key_item_uuid** | **str**| Key Item UUID | 
 **algorithm** | [**KeyAlgorithm**](.md)| Cryptographic algorithm | 

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
**200** | List of Attributes retrieved |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_random_attributes**
> List[BaseAttributeDto] list_random_attributes(token_instance_uuid)

List of random generator Attributes

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
    api_instance = openapi_client.CryptographicOperationsControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID

    try:
        # List of random generator Attributes
        api_response = api_instance.list_random_attributes(token_instance_uuid)
        print("The response of CryptographicOperationsControllerApi->list_random_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicOperationsControllerApi->list_random_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 

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
**200** | List of Attributes retrieved |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_signature_attributes**
> List[BaseAttributeDto] list_signature_attributes(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, algorithm)

List of signature Attributes

### Example


```python
import openapi_client
from openapi_client.models.base_attribute_dto import BaseAttributeDto
from openapi_client.models.key_algorithm import KeyAlgorithm
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
    api_instance = openapi_client.CryptographicOperationsControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    token_profile_uuid = 'token_profile_uuid_example' # str | Token Profile UUID
    uuid = 'uuid_example' # str | Key instance UUID
    key_item_uuid = 'key_item_uuid_example' # str | Key Item UUID
    algorithm = openapi_client.KeyAlgorithm() # KeyAlgorithm | Cryptographic algorithm

    try:
        # List of signature Attributes
        api_response = api_instance.list_signature_attributes(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, algorithm)
        print("The response of CryptographicOperationsControllerApi->list_signature_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicOperationsControllerApi->list_signature_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **token_profile_uuid** | **str**| Token Profile UUID | 
 **uuid** | **str**| Key instance UUID | 
 **key_item_uuid** | **str**| Key Item UUID | 
 **algorithm** | [**KeyAlgorithm**](.md)| Cryptographic algorithm | 

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
**200** | List of Attributes retrieved |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **random_data**
> RandomDataResponseDto random_data(token_instance_uuid, random_data_request_dto)

Generate random data

### Example


```python
import openapi_client
from openapi_client.models.random_data_request_dto import RandomDataRequestDto
from openapi_client.models.random_data_response_dto import RandomDataResponseDto
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
    api_instance = openapi_client.CryptographicOperationsControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    random_data_request_dto = openapi_client.RandomDataRequestDto() # RandomDataRequestDto | 

    try:
        # Generate random data
        api_response = api_instance.random_data(token_instance_uuid, random_data_request_dto)
        print("The response of CryptographicOperationsControllerApi->random_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicOperationsControllerApi->random_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **random_data_request_dto** | [**RandomDataRequestDto**](RandomDataRequestDto.md)|  | 

### Return type

[**RandomDataResponseDto**](RandomDataResponseDto.md)

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
**500** | Internal Server Error |  -  |
**200** | Random data generated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_data**
> SignDataResponseDto sign_data(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, sign_data_request_dto)

Sign data using a Key

### Example


```python
import openapi_client
from openapi_client.models.sign_data_request_dto import SignDataRequestDto
from openapi_client.models.sign_data_response_dto import SignDataResponseDto
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
    api_instance = openapi_client.CryptographicOperationsControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    token_profile_uuid = 'token_profile_uuid_example' # str | Token Profile UUID
    uuid = 'uuid_example' # str | Key UUID
    key_item_uuid = 'key_item_uuid_example' # str | Key Item UUID
    sign_data_request_dto = openapi_client.SignDataRequestDto() # SignDataRequestDto | 

    try:
        # Sign data using a Key
        api_response = api_instance.sign_data(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, sign_data_request_dto)
        print("The response of CryptographicOperationsControllerApi->sign_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicOperationsControllerApi->sign_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **token_profile_uuid** | **str**| Token Profile UUID | 
 **uuid** | **str**| Key UUID | 
 **key_item_uuid** | **str**| Key Item UUID | 
 **sign_data_request_dto** | [**SignDataRequestDto**](SignDataRequestDto.md)|  | 

### Return type

[**SignDataResponseDto**](SignDataResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data signed |  -  |
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_data**
> VerifyDataResponseDto verify_data(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, verify_data_request_dto)

Verify data using a Key

### Example


```python
import openapi_client
from openapi_client.models.verify_data_request_dto import VerifyDataRequestDto
from openapi_client.models.verify_data_response_dto import VerifyDataResponseDto
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
    api_instance = openapi_client.CryptographicOperationsControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    token_profile_uuid = 'token_profile_uuid_example' # str | Token Profile UUID
    uuid = 'uuid_example' # str | Key UUID
    key_item_uuid = 'key_item_uuid_example' # str | Key Item UUID
    verify_data_request_dto = openapi_client.VerifyDataRequestDto() # VerifyDataRequestDto | 

    try:
        # Verify data using a Key
        api_response = api_instance.verify_data(token_instance_uuid, token_profile_uuid, uuid, key_item_uuid, verify_data_request_dto)
        print("The response of CryptographicOperationsControllerApi->verify_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicOperationsControllerApi->verify_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **token_profile_uuid** | **str**| Token Profile UUID | 
 **uuid** | **str**| Key UUID | 
 **key_item_uuid** | **str**| Key Item UUID | 
 **verify_data_request_dto** | [**VerifyDataRequestDto**](VerifyDataRequestDto.md)|  | 

### Return type

[**VerifyDataResponseDto**](VerifyDataResponseDto.md)

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
**500** | Internal Server Error |  -  |
**200** | Data decrypted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

