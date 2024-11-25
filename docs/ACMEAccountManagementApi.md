# openapi_client.ACMEAccountManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_disable_acme_account**](ACMEAccountManagementApi.md#bulk_disable_acme_account) | **PATCH** /v1/acmeAccounts/disable | Disable multiple ACME Accounts
[**bulk_enable_acme_account**](ACMEAccountManagementApi.md#bulk_enable_acme_account) | **PATCH** /v1/acmeAccounts/enable | Enable multiple ACME Accounts
[**bulk_revoke_acme_account**](ACMEAccountManagementApi.md#bulk_revoke_acme_account) | **PUT** /v1/acmeAccounts/revoke | Revoke multiple ACME Accounts
[**disable_acme_account**](ACMEAccountManagementApi.md#disable_acme_account) | **PATCH** /v1/acmeProfiles/{acmeProfileUuid}/acmeAccounts/{acmeAccountUuid}/disable | Disable ACME Account
[**enable_acme_account**](ACMEAccountManagementApi.md#enable_acme_account) | **PATCH** /v1/acmeProfiles/{acmeProfileUuid}/acmeAccounts/{acmeAccountUuid}/enable | Enable ACME Account
[**get_acme_account**](ACMEAccountManagementApi.md#get_acme_account) | **GET** /v1/acmeProfiles/{acmeProfileUuid}/acmeAccounts/{acmeAccountUuid} | Details of ACME Account
[**list_acme_accounts**](ACMEAccountManagementApi.md#list_acme_accounts) | **GET** /v1/acmeAccounts | List ACME Accounts
[**revoke_acme_account**](ACMEAccountManagementApi.md#revoke_acme_account) | **POST** /v1/acmeProfiles/{acmeProfileUuid}/acmeAccounts/{acmeAccountUuid} | Revoke ACME Account


# **bulk_disable_acme_account**
> bulk_disable_acme_account(request_body)

Disable multiple ACME Accounts

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
    api_instance = openapi_client.ACMEAccountManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | ACME Account UUIDs

    try:
        # Disable multiple ACME Accounts
        api_instance.bulk_disable_acme_account(request_body)
    except Exception as e:
        print("Exception when calling ACMEAccountManagementApi->bulk_disable_acme_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| ACME Account UUIDs | 

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
**204** | ACME Accounts disabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_acme_account**
> bulk_enable_acme_account(request_body)

Enable multiple ACME Accounts

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
    api_instance = openapi_client.ACMEAccountManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | ACME Account UUIDs

    try:
        # Enable multiple ACME Accounts
        api_instance.bulk_enable_acme_account(request_body)
    except Exception as e:
        print("Exception when calling ACMEAccountManagementApi->bulk_enable_acme_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| ACME Account UUIDs | 

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
**204** | ACME Accounts enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_revoke_acme_account**
> bulk_revoke_acme_account(request_body)

Revoke multiple ACME Accounts

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
    api_instance = openapi_client.ACMEAccountManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | ACME Account UUIDs

    try:
        # Revoke multiple ACME Accounts
        api_instance.bulk_revoke_acme_account(request_body)
    except Exception as e:
        print("Exception when calling ACMEAccountManagementApi->bulk_revoke_acme_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| ACME Account UUIDs | 

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
**204** | ACME Accounts revoked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_acme_account**
> disable_acme_account(acme_profile_uuid, acme_account_uuid)

Disable ACME Account

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
    api_instance = openapi_client.ACMEAccountManagementApi(api_client)
    acme_profile_uuid = 'acme_profile_uuid_example' # str | ACME Profile UUID
    acme_account_uuid = 'acme_account_uuid_example' # str | ACME Account UUID

    try:
        # Disable ACME Account
        api_instance.disable_acme_account(acme_profile_uuid, acme_account_uuid)
    except Exception as e:
        print("Exception when calling ACMEAccountManagementApi->disable_acme_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acme_profile_uuid** | **str**| ACME Profile UUID | 
 **acme_account_uuid** | **str**| ACME Account UUID | 

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
**204** | ACME Account disabled |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_acme_account**
> enable_acme_account(acme_profile_uuid, acme_account_uuid)

Enable ACME Account

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
    api_instance = openapi_client.ACMEAccountManagementApi(api_client)
    acme_profile_uuid = 'acme_profile_uuid_example' # str | ACME Profile UUID
    acme_account_uuid = 'acme_account_uuid_example' # str | ACME Account UUID

    try:
        # Enable ACME Account
        api_instance.enable_acme_account(acme_profile_uuid, acme_account_uuid)
    except Exception as e:
        print("Exception when calling ACMEAccountManagementApi->enable_acme_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acme_profile_uuid** | **str**| ACME Profile UUID | 
 **acme_account_uuid** | **str**| ACME Account UUID | 

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
**204** | ACME Account enabled |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acme_account**
> AcmeAccountResponseDto get_acme_account(acme_profile_uuid, acme_account_uuid)

Details of ACME Account

### Example


```python
import openapi_client
from openapi_client.models.acme_account_response_dto import AcmeAccountResponseDto
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
    api_instance = openapi_client.ACMEAccountManagementApi(api_client)
    acme_profile_uuid = 'acme_profile_uuid_example' # str | ACME Profile UUID
    acme_account_uuid = 'acme_account_uuid_example' # str | ACME Account UUID

    try:
        # Details of ACME Account
        api_response = api_instance.get_acme_account(acme_profile_uuid, acme_account_uuid)
        print("The response of ACMEAccountManagementApi->get_acme_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACMEAccountManagementApi->get_acme_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acme_profile_uuid** | **str**| ACME Profile UUID | 
 **acme_account_uuid** | **str**| ACME Account UUID | 

### Return type

[**AcmeAccountResponseDto**](AcmeAccountResponseDto.md)

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
**200** | ACME Account details retrieved |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_acme_accounts**
> List[AcmeAccountListResponseDto] list_acme_accounts()

List ACME Accounts

### Example


```python
import openapi_client
from openapi_client.models.acme_account_list_response_dto import AcmeAccountListResponseDto
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
    api_instance = openapi_client.ACMEAccountManagementApi(api_client)

    try:
        # List ACME Accounts
        api_response = api_instance.list_acme_accounts()
        print("The response of ACMEAccountManagementApi->list_acme_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACMEAccountManagementApi->list_acme_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AcmeAccountListResponseDto]**](AcmeAccountListResponseDto.md)

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
**200** | ACME Accounts list retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_acme_account**
> revoke_acme_account(acme_profile_uuid, acme_account_uuid)

Revoke ACME Account

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
    api_instance = openapi_client.ACMEAccountManagementApi(api_client)
    acme_profile_uuid = 'acme_profile_uuid_example' # str | ACME Profile UUID
    acme_account_uuid = 'acme_account_uuid_example' # str | ACME Account UUID

    try:
        # Revoke ACME Account
        api_instance.revoke_acme_account(acme_profile_uuid, acme_account_uuid)
    except Exception as e:
        print("Exception when calling ACMEAccountManagementApi->revoke_acme_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acme_profile_uuid** | **str**| ACME Profile UUID | 
 **acme_account_uuid** | **str**| ACME Account UUID | 

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
**204** | ACME Account revoked |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

