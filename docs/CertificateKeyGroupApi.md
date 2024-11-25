# openapi_client.CertificateKeyGroupApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_group**](CertificateKeyGroupApi.md#bulk_delete_group) | **DELETE** /v1/groups | Delete multiple Groups
[**create_group**](CertificateKeyGroupApi.md#create_group) | **POST** /v1/groups | Create Group
[**delete_group**](CertificateKeyGroupApi.md#delete_group) | **DELETE** /v1/groups/{uuid} | Delete Group
[**edit_group**](CertificateKeyGroupApi.md#edit_group) | **PUT** /v1/groups/{uuid} | Edit Group
[**get_group**](CertificateKeyGroupApi.md#get_group) | **GET** /v1/groups/{uuid} | Group details
[**list_groups**](CertificateKeyGroupApi.md#list_groups) | **GET** /v1/groups | List Groups


# **bulk_delete_group**
> bulk_delete_group(request_body)

Delete multiple Groups

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
    api_instance = openapi_client.CertificateKeyGroupApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Group UUIDs

    try:
        # Delete multiple Groups
        api_instance.bulk_delete_group(request_body)
    except Exception as e:
        print("Exception when calling CertificateKeyGroupApi->bulk_delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Group UUIDs | 

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
**204** | Groups deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> UuidDto create_group(group_request_dto)

Create Group

### Example


```python
import openapi_client
from openapi_client.models.group_request_dto import GroupRequestDto
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
    api_instance = openapi_client.CertificateKeyGroupApi(api_client)
    group_request_dto = openapi_client.GroupRequestDto() # GroupRequestDto | 

    try:
        # Create Group
        api_response = api_instance.create_group(group_request_dto)
        print("The response of CertificateKeyGroupApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateKeyGroupApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_request_dto** | [**GroupRequestDto**](GroupRequestDto.md)|  | 

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
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**201** | Group created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(uuid)

Delete Group

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
    api_instance = openapi_client.CertificateKeyGroupApi(api_client)
    uuid = 'uuid_example' # str | Group UUID

    try:
        # Delete Group
        api_instance.delete_group(uuid)
    except Exception as e:
        print("Exception when calling CertificateKeyGroupApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Group UUID | 

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
**204** | Group deleted |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_group**
> GroupDto edit_group(uuid, group_request_dto)

Edit Group

### Example


```python
import openapi_client
from openapi_client.models.group_dto import GroupDto
from openapi_client.models.group_request_dto import GroupRequestDto
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
    api_instance = openapi_client.CertificateKeyGroupApi(api_client)
    uuid = 'uuid_example' # str | Group UUID
    group_request_dto = openapi_client.GroupRequestDto() # GroupRequestDto | 

    try:
        # Edit Group
        api_response = api_instance.edit_group(uuid, group_request_dto)
        print("The response of CertificateKeyGroupApi->edit_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateKeyGroupApi->edit_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Group UUID | 
 **group_request_dto** | [**GroupRequestDto**](GroupRequestDto.md)|  | 

### Return type

[**GroupDto**](GroupDto.md)

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
**200** | Group updated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> GroupDto get_group(uuid)

Group details

### Example


```python
import openapi_client
from openapi_client.models.group_dto import GroupDto
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
    api_instance = openapi_client.CertificateKeyGroupApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Group details
        api_response = api_instance.get_group(uuid)
        print("The response of CertificateKeyGroupApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateKeyGroupApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GroupDto**](GroupDto.md)

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
**200** | Group details retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> List[GroupDto] list_groups()

List Groups

### Example


```python
import openapi_client
from openapi_client.models.group_dto import GroupDto
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
    api_instance = openapi_client.CertificateKeyGroupApi(api_client)

    try:
        # List Groups
        api_response = api_instance.list_groups()
        print("The response of CertificateKeyGroupApi->list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateKeyGroupApi->list_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GroupDto]**](GroupDto.md)

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
**200** | list of available Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

