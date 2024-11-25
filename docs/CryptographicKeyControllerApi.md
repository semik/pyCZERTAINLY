# openapi_client.CryptographicKeyControllerApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compromise_key**](CryptographicKeyControllerApi.md#compromise_key) | **PATCH** /v1/tokens/{tokenInstanceUuid}/keys/{uuid}/compromise | Mark Key and its Items as Compromised
[**compromise_key_items**](CryptographicKeyControllerApi.md#compromise_key_items) | **PATCH** /v1/keys/items/compromise | Mark Multiple Key Items as Compromised
[**compromise_keys**](CryptographicKeyControllerApi.md#compromise_keys) | **PATCH** /v1/keys/compromise | Mark Multiple Key and all its Items as Compromised
[**create_key**](CryptographicKeyControllerApi.md#create_key) | **POST** /v1/tokens/{tokenInstanceUuid}/tokenProfiles/{tokenProfileUuid}/keys/{type} | Create a new Cryptographic Key
[**delete_key**](CryptographicKeyControllerApi.md#delete_key) | **DELETE** /v1/tokens/{tokenInstanceUuid}/keys/{uuid} | Delete Cryptographic Key
[**delete_key_items**](CryptographicKeyControllerApi.md#delete_key_items) | **DELETE** /v1/keys/items | Delete Multiple Cryptographic Key Items
[**delete_keys**](CryptographicKeyControllerApi.md#delete_keys) | **DELETE** /v1/keys | Delete Multiple Cryptographic Key
[**destroy_key**](CryptographicKeyControllerApi.md#destroy_key) | **PATCH** /v1/tokens/{tokenInstanceUuid}/keys/{uuid}/destroy | Destroy Cryptographic Key
[**destroy_key_items**](CryptographicKeyControllerApi.md#destroy_key_items) | **PATCH** /v1/keys/items/destroy | Destroy Multiple Cryptographic Key items
[**destroy_keys**](CryptographicKeyControllerApi.md#destroy_keys) | **PATCH** /v1/keys/destroy | Destroy Multiple Cryptographic Key and its items
[**disable_key**](CryptographicKeyControllerApi.md#disable_key) | **PATCH** /v1/tokens/{tokenInstanceUuid}/keys/{uuid}/disable | Disable Key
[**disable_key_items**](CryptographicKeyControllerApi.md#disable_key_items) | **PATCH** /v1/keys/items/disable | Disable multiple Key Items
[**disable_keys**](CryptographicKeyControllerApi.md#disable_keys) | **PATCH** /v1/keys/disable | Disable multiple Keys
[**edit_key**](CryptographicKeyControllerApi.md#edit_key) | **PUT** /v1/tokens/{tokenInstanceUuid}/keys/{uuid} | Edit Key
[**enable_key**](CryptographicKeyControllerApi.md#enable_key) | **PATCH** /v1/tokens/{tokenInstanceUuid}/keys/{uuid}/enable | Enable Key
[**enable_key_items**](CryptographicKeyControllerApi.md#enable_key_items) | **PATCH** /v1/keys/items/enable | Enable multiple Key Items
[**enable_keys**](CryptographicKeyControllerApi.md#enable_keys) | **PATCH** /v1/keys/enable | Enable multiple Keys
[**get_event_history**](CryptographicKeyControllerApi.md#get_event_history) | **GET** /v1/tokens/{tokenInstanceUuid}/keys/{uuid}/items/{keyItemUuid}/history | Get Key Item event history
[**get_key**](CryptographicKeyControllerApi.md#get_key) | **GET** /v1/tokens/{tokenInstanceUuid}/keys/{uuid} | Get Cryptographic Key Detail
[**get_key_item**](CryptographicKeyControllerApi.md#get_key_item) | **GET** /v1/tokens/{tokenInstanceUuid}/keys/{uuid}/items/{keyItemUuid} | Get Cryptographic Key Detail
[**get_searchable_field_information1**](CryptographicKeyControllerApi.md#get_searchable_field_information1) | **GET** /v1/keys/search | Get CryptographicKey searchable fields information
[**list_create_key_attributes**](CryptographicKeyControllerApi.md#list_create_key_attributes) | **GET** /v1/tokens/{tokenInstanceUuid}/tokenProfiles/{tokenProfileUuid}/keys/{type}/attributes | List of Attributes to create a Key
[**list_cryptographic_keys**](CryptographicKeyControllerApi.md#list_cryptographic_keys) | **POST** /v1/keys | List cryptographic keys
[**list_key_pairs**](CryptographicKeyControllerApi.md#list_key_pairs) | **GET** /v1/keys/pairs | List Cryptographic Keys with full Key Pairs
[**sync_keys**](CryptographicKeyControllerApi.md#sync_keys) | **PATCH** /v1/tokens/{tokenInstanceUuid}/sync | Sync Keys from connector
[**update_key_item_usages**](CryptographicKeyControllerApi.md#update_key_item_usages) | **PUT** /v1/keys/items/usages | Update Key Usages for Multiple Key Items
[**update_key_usages1**](CryptographicKeyControllerApi.md#update_key_usages1) | **PUT** /v1/tokens/{tokenInstanceUuid}/keys/{uuid}/usages | Update Key Usage
[**update_keys_usages1**](CryptographicKeyControllerApi.md#update_keys_usages1) | **PUT** /v1/keys/usages | Update Key Usages for Multiple Keys


# **compromise_key**
> compromise_key(token_instance_uuid, uuid, compromise_key_request_dto)

Mark Key and its Items as Compromised

If the request body is provided with the UUID of the items of Key, then only those itemswill be compromised. Else all the sub items of the key will be compromised

### Example


```python
import openapi_client
from openapi_client.models.compromise_key_request_dto import CompromiseKeyRequestDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Key UUID
    compromise_key_request_dto = openapi_client.CompromiseKeyRequestDto() # CompromiseKeyRequestDto | 

    try:
        # Mark Key and its Items as Compromised
        api_instance.compromise_key(token_instance_uuid, uuid, compromise_key_request_dto)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->compromise_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Key UUID | 
 **compromise_key_request_dto** | [**CompromiseKeyRequestDto**](CompromiseKeyRequestDto.md)|  | 

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
**204** | Key marked as compromised |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compromise_key_items**
> compromise_key_items(bulk_compromise_key_item_request_dto)

Mark Multiple Key Items as Compromised

This API can be used to mark multiple keys items to be marked as compromised.

### Example


```python
import openapi_client
from openapi_client.models.bulk_compromise_key_item_request_dto import BulkCompromiseKeyItemRequestDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    bulk_compromise_key_item_request_dto = openapi_client.BulkCompromiseKeyItemRequestDto() # BulkCompromiseKeyItemRequestDto | 

    try:
        # Mark Multiple Key Items as Compromised
        api_instance.compromise_key_items(bulk_compromise_key_item_request_dto)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->compromise_key_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_compromise_key_item_request_dto** | [**BulkCompromiseKeyItemRequestDto**](BulkCompromiseKeyItemRequestDto.md)|  | 

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
**204** | Key Items marked as compromised |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compromise_keys**
> compromise_keys(bulk_compromise_key_request_dto)

Mark Multiple Key and all its Items as Compromised

This API can be used to mark multiple keys and its sub items to be marked as compromised.Specific part of the key cannot be mentioned in this API

### Example


```python
import openapi_client
from openapi_client.models.bulk_compromise_key_request_dto import BulkCompromiseKeyRequestDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    bulk_compromise_key_request_dto = openapi_client.BulkCompromiseKeyRequestDto() # BulkCompromiseKeyRequestDto | 

    try:
        # Mark Multiple Key and all its Items as Compromised
        api_instance.compromise_keys(bulk_compromise_key_request_dto)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->compromise_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_compromise_key_request_dto** | [**BulkCompromiseKeyRequestDto**](BulkCompromiseKeyRequestDto.md)|  | 

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
**204** | Key marked as compromised |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_key**
> KeyDetailDto create_key(token_instance_uuid, token_profile_uuid, type, key_request_dto)

Create a new Cryptographic Key

### Example


```python
import openapi_client
from openapi_client.models.key_detail_dto import KeyDetailDto
from openapi_client.models.key_request_dto import KeyRequestDto
from openapi_client.models.key_request_type import KeyRequestType
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | UUID of the Token Instance
    token_profile_uuid = 'token_profile_uuid_example' # str | UUID of the Token Profile
    type = openapi_client.KeyRequestType() # KeyRequestType | Type of the key to be created
    key_request_dto = openapi_client.KeyRequestDto() # KeyRequestDto | 

    try:
        # Create a new Cryptographic Key
        api_response = api_instance.create_key(token_instance_uuid, token_profile_uuid, type, key_request_dto)
        print("The response of CryptographicKeyControllerApi->create_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->create_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| UUID of the Token Instance | 
 **token_profile_uuid** | **str**| UUID of the Token Profile | 
 **type** | [**KeyRequestType**](.md)| Type of the key to be created | 
 **key_request_dto** | [**KeyRequestDto**](KeyRequestDto.md)|  | 

### Return type

[**KeyDetailDto**](KeyDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**201** | Cryptographic Key Created Successfully |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key**
> delete_key(token_instance_uuid, uuid, request_body=request_body)

Delete Cryptographic Key

If the request body provided, only those key items will be deleted. If the request body is not provided or given empty, then the entire key will be destroyed

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Key UUID
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key Item UUIDs (optional)

    try:
        # Delete Cryptographic Key
        api_instance.delete_key(token_instance_uuid, uuid, request_body=request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->delete_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Key UUID | 
 **request_body** | [**List[str]**](str.md)| Key Item UUIDs | [optional] 

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
**204** | Key deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_items**
> delete_key_items(request_body)

Delete Multiple Cryptographic Key Items

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key Items UUIDs

    try:
        # Delete Multiple Cryptographic Key Items
        api_instance.delete_key_items(request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->delete_key_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Key Items UUIDs | 

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
**204** | Key Items deleted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_keys**
> delete_keys(request_body)

Delete Multiple Cryptographic Key

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key UUIDs

    try:
        # Delete Multiple Cryptographic Key
        api_instance.delete_keys(request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->delete_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Key UUIDs | 

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
**204** | Keys deleted |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_key**
> destroy_key(token_instance_uuid, uuid, request_body=request_body)

Destroy Cryptographic Key

If the request body provided, only those key items will be destroyed. If the request body is not provided or given empty, then the entire key will be destroyed

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Key UUID
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key UUIDs (optional)

    try:
        # Destroy Cryptographic Key
        api_instance.destroy_key(token_instance_uuid, uuid, request_body=request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->destroy_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Key UUID | 
 **request_body** | [**List[str]**](str.md)| Key UUIDs | [optional] 

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
**204** | Keys destroyed |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_key_items**
> destroy_key_items(request_body)

Destroy Multiple Cryptographic Key items

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key Item UUIDs

    try:
        # Destroy Multiple Cryptographic Key items
        api_instance.destroy_key_items(request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->destroy_key_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Key Item UUIDs | 

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
**204** | Keys Items destroyed |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_keys**
> destroy_keys(request_body)

Destroy Multiple Cryptographic Key and its items

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key UUIDs

    try:
        # Destroy Multiple Cryptographic Key and its items
        api_instance.destroy_keys(request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->destroy_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Key UUIDs | 

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
**204** | Keys destroyed |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_key**
> disable_key(token_instance_uuid, uuid, request_body=request_body)

Disable Key

If the request body provided, only those key items will be disabled. If the request body is not provided or given empty, then the entire key will be disabled

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Key UUID
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key Item UUIDs (optional)

    try:
        # Disable Key
        api_instance.disable_key(token_instance_uuid, uuid, request_body=request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->disable_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Key UUID | 
 **request_body** | [**List[str]**](str.md)| Key Item UUIDs | [optional] 

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
**204** | Key disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_key_items**
> disable_key_items(request_body)

Disable multiple Key Items

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key Item UUIDs

    try:
        # Disable multiple Key Items
        api_instance.disable_key_items(request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->disable_key_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Key Item UUIDs | 

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
**204** | Key Items disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_keys**
> disable_keys(request_body)

Disable multiple Keys

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key UUIDs

    try:
        # Disable multiple Keys
        api_instance.disable_keys(request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->disable_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Key UUIDs | 

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
**204** | Keys disabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_key**
> KeyDetailDto edit_key(token_instance_uuid, uuid, edit_key_request_dto)

Edit Key

### Example


```python
import openapi_client
from openapi_client.models.edit_key_request_dto import EditKeyRequestDto
from openapi_client.models.key_detail_dto import KeyDetailDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Key UUID
    edit_key_request_dto = openapi_client.EditKeyRequestDto() # EditKeyRequestDto | 

    try:
        # Edit Key
        api_response = api_instance.edit_key(token_instance_uuid, uuid, edit_key_request_dto)
        print("The response of CryptographicKeyControllerApi->edit_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->edit_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Key UUID | 
 **edit_key_request_dto** | [**EditKeyRequestDto**](EditKeyRequestDto.md)|  | 

### Return type

[**KeyDetailDto**](KeyDetailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**204** | Key updated |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_key**
> enable_key(token_instance_uuid, uuid, request_body=request_body)

Enable Key

If the request body provided, only those key items will be enabled. If the request body is not provided or given empty, then the entire key will be enabled

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Key UUID
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key Item UUIDs (optional)

    try:
        # Enable Key
        api_instance.enable_key(token_instance_uuid, uuid, request_body=request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->enable_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Key UUID | 
 **request_body** | [**List[str]**](str.md)| Key Item UUIDs | [optional] 

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
**204** | Key enabled |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_key_items**
> enable_key_items(request_body)

Enable multiple Key Items

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key Item UUIDs

    try:
        # Enable multiple Key Items
        api_instance.enable_key_items(request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->enable_key_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Key Item UUIDs | 

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
**204** | Key Items enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_keys**
> enable_keys(request_body)

Enable multiple Keys

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Key UUIDs

    try:
        # Enable multiple Keys
        api_instance.enable_keys(request_body)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->enable_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Key UUIDs | 

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
**204** | Keys enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_history**
> List[KeyEventHistoryDto] get_event_history(token_instance_uuid, uuid, key_item_uuid)

Get Key Item event history

### Example


```python
import openapi_client
from openapi_client.models.key_event_history_dto import KeyEventHistoryDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Key UUID
    key_item_uuid = 'key_item_uuid_example' # str | Key Item UUID

    try:
        # Get Key Item event history
        api_response = api_instance.get_event_history(token_instance_uuid, uuid, key_item_uuid)
        print("The response of CryptographicKeyControllerApi->get_event_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->get_event_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Key UUID | 
 **key_item_uuid** | **str**| Key Item UUID | 

### Return type

[**List[KeyEventHistoryDto]**](KeyEventHistoryDto.md)

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
**200** | Certificate event history retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key**
> KeyDetailDto get_key(token_instance_uuid, uuid)

Get Cryptographic Key Detail

### Example


```python
import openapi_client
from openapi_client.models.key_detail_dto import KeyDetailDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | UUID of the Token Instance
    uuid = 'uuid_example' # str | UUID of the Key

    try:
        # Get Cryptographic Key Detail
        api_response = api_instance.get_key(token_instance_uuid, uuid)
        print("The response of CryptographicKeyControllerApi->get_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->get_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| UUID of the Token Instance | 
 **uuid** | **str**| UUID of the Key | 

### Return type

[**KeyDetailDto**](KeyDetailDto.md)

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
**200** | Cryptographic Key Detail retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_item**
> KeyItemDetailDto get_key_item(token_instance_uuid, uuid, key_item_uuid)

Get Cryptographic Key Detail

### Example


```python
import openapi_client
from openapi_client.models.key_item_detail_dto import KeyItemDetailDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | UUID of the Token Instance
    uuid = 'uuid_example' # str | UUID of the Key
    key_item_uuid = 'key_item_uuid_example' # str | UUID of the Key Item

    try:
        # Get Cryptographic Key Detail
        api_response = api_instance.get_key_item(token_instance_uuid, uuid, key_item_uuid)
        print("The response of CryptographicKeyControllerApi->get_key_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->get_key_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| UUID of the Token Instance | 
 **uuid** | **str**| UUID of the Key | 
 **key_item_uuid** | **str**| UUID of the Key Item | 

### Return type

[**KeyItemDetailDto**](KeyItemDetailDto.md)

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
**200** | Cryptographic Key Detail retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_searchable_field_information1**
> List[SearchFieldDataByGroupDto] get_searchable_field_information1()

Get CryptographicKey searchable fields information

### Example


```python
import openapi_client
from openapi_client.models.search_field_data_by_group_dto import SearchFieldDataByGroupDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)

    try:
        # Get CryptographicKey searchable fields information
        api_response = api_instance.get_searchable_field_information1()
        print("The response of CryptographicKeyControllerApi->get_searchable_field_information1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->get_searchable_field_information1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SearchFieldDataByGroupDto]**](SearchFieldDataByGroupDto.md)

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
**200** | CryptographicKey searchable field information retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_create_key_attributes**
> List[BaseAttributeDto] list_create_key_attributes(token_instance_uuid, token_profile_uuid, type)

List of Attributes to create a Key

### Example


```python
import openapi_client
from openapi_client.models.base_attribute_dto import BaseAttributeDto
from openapi_client.models.key_request_type import KeyRequestType
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    token_profile_uuid = 'token_profile_uuid_example' # str | Token Profile UUID
    type = openapi_client.KeyRequestType() # KeyRequestType | Type of the key to be created

    try:
        # List of Attributes to create a Key
        api_response = api_instance.list_create_key_attributes(token_instance_uuid, token_profile_uuid, type)
        print("The response of CryptographicKeyControllerApi->list_create_key_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->list_create_key_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **token_profile_uuid** | **str**| Token Profile UUID | 
 **type** | [**KeyRequestType**](.md)| Type of the key to be created | 

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

# **list_cryptographic_keys**
> CryptographicKeyResponseDto list_cryptographic_keys(search_request_dto)

List cryptographic keys

### Example


```python
import openapi_client
from openapi_client.models.cryptographic_key_response_dto import CryptographicKeyResponseDto
from openapi_client.models.search_request_dto import SearchRequestDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    search_request_dto = openapi_client.SearchRequestDto() # SearchRequestDto | 

    try:
        # List cryptographic keys
        api_response = api_instance.list_cryptographic_keys(search_request_dto)
        print("The response of CryptographicKeyControllerApi->list_cryptographic_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->list_cryptographic_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request_dto** | [**SearchRequestDto**](SearchRequestDto.md)|  | 

### Return type

[**CryptographicKeyResponseDto**](CryptographicKeyResponseDto.md)

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
**200** | List of all the cryptographic keys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_key_pairs**
> List[KeyDto] list_key_pairs(token_profile_uuid=token_profile_uuid)

List Cryptographic Keys with full Key Pairs

This API contains the logic to get the keys that contains the full key pair (private and public Key)

### Example


```python
import openapi_client
from openapi_client.models.key_dto import KeyDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_profile_uuid = 'token_profile_uuid_example' # str |  (optional)

    try:
        # List Cryptographic Keys with full Key Pairs
        api_response = api_instance.list_key_pairs(token_profile_uuid=token_profile_uuid)
        print("The response of CryptographicKeyControllerApi->list_key_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->list_key_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_profile_uuid** | **str**|  | [optional] 

### Return type

[**List[KeyDto]**](KeyDto.md)

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
**200** | Cryptographic Keys retrieved |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_keys**
> sync_keys(token_instance_uuid)

Sync Keys from connector

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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID

    try:
        # Sync Keys from connector
        api_instance.sync_keys(token_instance_uuid)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->sync_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 

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
**204** | Key sync completed |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key_item_usages**
> update_key_item_usages(bulk_key_item_usage_request_dto)

Update Key Usages for Multiple Key Items

Update the key usages for multiple keys Items

### Example


```python
import openapi_client
from openapi_client.models.bulk_key_item_usage_request_dto import BulkKeyItemUsageRequestDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    bulk_key_item_usage_request_dto = openapi_client.BulkKeyItemUsageRequestDto() # BulkKeyItemUsageRequestDto | 

    try:
        # Update Key Usages for Multiple Key Items
        api_instance.update_key_item_usages(bulk_key_item_usage_request_dto)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->update_key_item_usages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_key_item_usage_request_dto** | [**BulkKeyItemUsageRequestDto**](BulkKeyItemUsageRequestDto.md)|  | 

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
**204** | Key Items Usages Updated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key_usages1**
> update_key_usages1(token_instance_uuid, uuid, update_key_usage_request_dto)

Update Key Usage

If the request body provided, only those key items will be updated. If the request body is not provided or given empty, then the entire key will be updated

### Example


```python
import openapi_client
from openapi_client.models.update_key_usage_request_dto import UpdateKeyUsageRequestDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    token_instance_uuid = 'token_instance_uuid_example' # str | Token Instance UUID
    uuid = 'uuid_example' # str | Key UUID
    update_key_usage_request_dto = openapi_client.UpdateKeyUsageRequestDto() # UpdateKeyUsageRequestDto | 

    try:
        # Update Key Usage
        api_instance.update_key_usages1(token_instance_uuid, uuid, update_key_usage_request_dto)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->update_key_usages1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_instance_uuid** | **str**| Token Instance UUID | 
 **uuid** | **str**| Key UUID | 
 **update_key_usage_request_dto** | [**UpdateKeyUsageRequestDto**](UpdateKeyUsageRequestDto.md)|  | 

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
**204** | Keys Usages Updates |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_keys_usages1**
> update_keys_usages1(bulk_key_usage_request_dto)

Update Key Usages for Multiple Keys

Update the key usages for multiple keys and all the items inside it

### Example


```python
import openapi_client
from openapi_client.models.bulk_key_usage_request_dto import BulkKeyUsageRequestDto
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
    api_instance = openapi_client.CryptographicKeyControllerApi(api_client)
    bulk_key_usage_request_dto = openapi_client.BulkKeyUsageRequestDto() # BulkKeyUsageRequestDto | 

    try:
        # Update Key Usages for Multiple Keys
        api_instance.update_keys_usages1(bulk_key_usage_request_dto)
    except Exception as e:
        print("Exception when calling CryptographicKeyControllerApi->update_keys_usages1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_key_usage_request_dto** | [**BulkKeyUsageRequestDto**](BulkKeyUsageRequestDto.md)|  | 

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
**204** | Keys Usages Updated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

