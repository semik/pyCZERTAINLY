# pyCZERTAINLY.GlobalMetadataApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_global_metadata**](GlobalMetadataApi.md#bulk_delete_global_metadata) | **DELETE** /v1/attributes/metadata | Delete multiple Global Metadata
[**create_global_metadata**](GlobalMetadataApi.md#create_global_metadata) | **POST** /v1/attributes/metadata | Create Global Metadata
[**delete_global_metadata**](GlobalMetadataApi.md#delete_global_metadata) | **DELETE** /v1/attributes/metadata/{uuid} | Delete Global Metadata
[**edit_global_metadata**](GlobalMetadataApi.md#edit_global_metadata) | **PUT** /v1/attributes/metadata/{uuid} | Edit Global Metadata
[**get_connector_metadata**](GlobalMetadataApi.md#get_connector_metadata) | **GET** /v1/attributes/metadata/promote | Get Available Connector Metadata
[**get_global_metadata**](GlobalMetadataApi.md#get_global_metadata) | **GET** /v1/attributes/metadata/{uuid} | Global Metadata details
[**list_global_metadata**](GlobalMetadataApi.md#list_global_metadata) | **GET** /v1/attributes/metadata | List Global Metadata
[**promote_connector_metadata**](GlobalMetadataApi.md#promote_connector_metadata) | **POST** /v1/attributes/metadata/promote | Promote Connector Metadata to Global Metadata


# **bulk_delete_global_metadata**
> bulk_delete_global_metadata(request_body)

Delete multiple Global Metadata

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
    api_instance = pyCZERTAINLY.GlobalMetadataApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Global Metadata UUIDs

    try:
        # Delete multiple Global Metadata
        api_instance.bulk_delete_global_metadata(request_body)
    except Exception as e:
        print("Exception when calling GlobalMetadataApi->bulk_delete_global_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Global Metadata UUIDs | 

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
**204** | Global Metadata deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_global_metadata**
> UuidDto create_global_metadata(global_metadata_create_request_dto)

Create Global Metadata

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.global_metadata_create_request_dto import GlobalMetadataCreateRequestDto
from pyCZERTAINLY.models.uuid_dto import UuidDto
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
    api_instance = pyCZERTAINLY.GlobalMetadataApi(api_client)
    global_metadata_create_request_dto = pyCZERTAINLY.GlobalMetadataCreateRequestDto() # GlobalMetadataCreateRequestDto | 

    try:
        # Create Global Metadata
        api_response = api_instance.create_global_metadata(global_metadata_create_request_dto)
        print("The response of GlobalMetadataApi->create_global_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMetadataApi->create_global_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_metadata_create_request_dto** | [**GlobalMetadataCreateRequestDto**](GlobalMetadataCreateRequestDto.md)|  | 

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
**201** | Global Metadata created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_global_metadata**
> delete_global_metadata(uuid)

Delete Global Metadata

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
    api_instance = pyCZERTAINLY.GlobalMetadataApi(api_client)
    uuid = 'uuid_example' # str | Global Metadata UUID

    try:
        # Delete Global Metadata
        api_instance.delete_global_metadata(uuid)
    except Exception as e:
        print("Exception when calling GlobalMetadataApi->delete_global_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Global Metadata UUID | 

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
**500** | Internal Server Error |  -  |
**204** | Global Metadata deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_global_metadata**
> GlobalMetadataDefinitionDetailDto edit_global_metadata(uuid, global_metadata_update_request_dto)

Edit Global Metadata

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.global_metadata_definition_detail_dto import GlobalMetadataDefinitionDetailDto
from pyCZERTAINLY.models.global_metadata_update_request_dto import GlobalMetadataUpdateRequestDto
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
    api_instance = pyCZERTAINLY.GlobalMetadataApi(api_client)
    uuid = 'uuid_example' # str | Global Metadata UUID
    global_metadata_update_request_dto = pyCZERTAINLY.GlobalMetadataUpdateRequestDto() # GlobalMetadataUpdateRequestDto | 

    try:
        # Edit Global Metadata
        api_response = api_instance.edit_global_metadata(uuid, global_metadata_update_request_dto)
        print("The response of GlobalMetadataApi->edit_global_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMetadataApi->edit_global_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Global Metadata UUID | 
 **global_metadata_update_request_dto** | [**GlobalMetadataUpdateRequestDto**](GlobalMetadataUpdateRequestDto.md)|  | 

### Return type

[**GlobalMetadataDefinitionDetailDto**](GlobalMetadataDefinitionDetailDto.md)

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
**200** | Global Metadata updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_metadata**
> List[ConnectorMetadataResponseDto] get_connector_metadata(connector_uuid=connector_uuid)

Get Available Connector Metadata

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.connector_metadata_response_dto import ConnectorMetadataResponseDto
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
    api_instance = pyCZERTAINLY.GlobalMetadataApi(api_client)
    connector_uuid = 'connector_uuid_example' # str |  (optional)

    try:
        # Get Available Connector Metadata
        api_response = api_instance.get_connector_metadata(connector_uuid=connector_uuid)
        print("The response of GlobalMetadataApi->get_connector_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMetadataApi->get_connector_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_uuid** | **str**|  | [optional] 

### Return type

[**List[ConnectorMetadataResponseDto]**](ConnectorMetadataResponseDto.md)

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
**204** | Connector Metadata retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_metadata**
> GlobalMetadataDefinitionDetailDto get_global_metadata(uuid)

Global Metadata details

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.global_metadata_definition_detail_dto import GlobalMetadataDefinitionDetailDto
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
    api_instance = pyCZERTAINLY.GlobalMetadataApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Global Metadata details
        api_response = api_instance.get_global_metadata(uuid)
        print("The response of GlobalMetadataApi->get_global_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMetadataApi->get_global_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GlobalMetadataDefinitionDetailDto**](GlobalMetadataDefinitionDetailDto.md)

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
**200** | Global Metadata details retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_global_metadata**
> List[AttributeDefinitionDto] list_global_metadata()

List Global Metadata

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.attribute_definition_dto import AttributeDefinitionDto
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
    api_instance = pyCZERTAINLY.GlobalMetadataApi(api_client)

    try:
        # List Global Metadata
        api_response = api_instance.list_global_metadata()
        print("The response of GlobalMetadataApi->list_global_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMetadataApi->list_global_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AttributeDefinitionDto]**](AttributeDefinitionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of available Global Metadata |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote_connector_metadata**
> GlobalMetadataDefinitionDetailDto promote_connector_metadata(connector_metadata_promotion_request_dto)

Promote Connector Metadata to Global Metadata

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.connector_metadata_promotion_request_dto import ConnectorMetadataPromotionRequestDto
from pyCZERTAINLY.models.global_metadata_definition_detail_dto import GlobalMetadataDefinitionDetailDto
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
    api_instance = pyCZERTAINLY.GlobalMetadataApi(api_client)
    connector_metadata_promotion_request_dto = pyCZERTAINLY.ConnectorMetadataPromotionRequestDto() # ConnectorMetadataPromotionRequestDto | 

    try:
        # Promote Connector Metadata to Global Metadata
        api_response = api_instance.promote_connector_metadata(connector_metadata_promotion_request_dto)
        print("The response of GlobalMetadataApi->promote_connector_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalMetadataApi->promote_connector_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_metadata_promotion_request_dto** | [**ConnectorMetadataPromotionRequestDto**](ConnectorMetadataPromotionRequestDto.md)|  | 

### Return type

[**GlobalMetadataDefinitionDetailDto**](GlobalMetadataDefinitionDetailDto.md)

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
**204** | Connector Metadata promoted to global metadata |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

