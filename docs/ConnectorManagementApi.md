# pyCZERTAINLY.ConnectorManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve**](ConnectorManagementApi.md#approve) | **PUT** /v1/connectors/{uuid}/approve | Approve a Connector
[**bulk_approve**](ConnectorManagementApi.md#bulk_approve) | **PUT** /v1/connectors/approve | Approve multiple Connector
[**bulk_delete_connector**](ConnectorManagementApi.md#bulk_delete_connector) | **DELETE** /v1/connectors | Delete multiple Connectors
[**bulk_reconnect**](ConnectorManagementApi.md#bulk_reconnect) | **PUT** /v1/connectors/reconnect | Reconnect multiple Connectors
[**check_health**](ConnectorManagementApi.md#check_health) | **GET** /v1/connectors/{uuid}/health | Check Health of a Connector
[**connect**](ConnectorManagementApi.md#connect) | **PUT** /v1/connectors/connect | Connect to a Connector
[**create_connector**](ConnectorManagementApi.md#create_connector) | **POST** /v1/connectors | Create a new Connector
[**delete_connector**](ConnectorManagementApi.md#delete_connector) | **DELETE** /v1/connectors/{uuid} | Delete a Connector
[**edit_connector**](ConnectorManagementApi.md#edit_connector) | **PUT** /v1/connectors/{uuid} | Edit a Connector
[**force_delete_connector**](ConnectorManagementApi.md#force_delete_connector) | **DELETE** /v1/connectors/force | Force Delete multiple Connectors
[**get_attributes**](ConnectorManagementApi.md#get_attributes) | **GET** /v1/connectors/{uuid}/attributes/{functionGroup}/{kind} | Get Attributes from a Connector
[**get_attributes_all**](ConnectorManagementApi.md#get_attributes_all) | **GET** /v1/connectors/{uuid}/attributes | Get attributes of all Function Groups
[**get_connector**](ConnectorManagementApi.md#get_connector) | **GET** /v1/connectors/{uuid} | Get details of a Connector
[**list_connectors**](ConnectorManagementApi.md#list_connectors) | **GET** /v1/connectors | List Connectors by Function Group and Kind
[**reconnect**](ConnectorManagementApi.md#reconnect) | **PUT** /v1/connectors/{uuid}/reconnect | Reconnect to a Connector
[**validate_attributes**](ConnectorManagementApi.md#validate_attributes) | **POST** /v1/connectors/{uuid}/{functionGroup}/{kind}/validate | Validate Attributes


# **approve**
> approve(uuid)

Approve a Connector

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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID

    try:
        # Approve a Connector
        api_instance.approve(uuid)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 

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
**200** | Connector Approved |  -  |
**503** | Connector Communication Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_approve**
> bulk_approve(request_body)

Approve multiple Connector

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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Connector UUIDs

    try:
        # Approve multiple Connector
        api_instance.bulk_approve(request_body)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->bulk_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Connector UUIDs | 

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
**200** | Approve multiple Connectors |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_connector**
> List[BulkActionMessageDto] bulk_delete_connector(request_body)

Delete multiple Connectors

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.bulk_action_message_dto import BulkActionMessageDto
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Connector UUIDs

    try:
        # Delete multiple Connectors
        api_response = api_instance.bulk_delete_connector(request_body)
        print("The response of ConnectorManagementApi->bulk_delete_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->bulk_delete_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Connector UUIDs | 

### Return type

[**List[BulkActionMessageDto]**](BulkActionMessageDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connectors deleted |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_reconnect**
> bulk_reconnect(request_body)

Reconnect multiple Connectors

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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Connector UUIDs

    try:
        # Reconnect multiple Connectors
        api_instance.bulk_reconnect(request_body)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->bulk_reconnect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Connector UUIDs | 

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
**204** | Reconnect multiple Connectors initiated |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_health**
> HealthDto check_health(uuid)

Check Health of a Connector

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.health_dto import HealthDto
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID

    try:
        # Check Health of a Connector
        api_response = api_instance.check_health(uuid)
        print("The response of ConnectorManagementApi->check_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->check_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 

### Return type

[**HealthDto**](HealthDto.md)

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
**200** | Health check completed |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect**
> List[ConnectDto] connect(connect_request_dto)

Connect to a Connector

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.connect_dto import ConnectDto
from pyCZERTAINLY.models.connect_request_dto import ConnectRequestDto
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    connect_request_dto = pyCZERTAINLY.ConnectRequestDto() # ConnectRequestDto | 

    try:
        # Connect to a Connector
        api_response = api_instance.connect(connect_request_dto)
        print("The response of ConnectorManagementApi->connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_request_dto** | [**ConnectRequestDto**](ConnectRequestDto.md)|  | 

### Return type

[**List[ConnectDto]**](ConnectDto.md)

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
**200** | Connector connected |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connector**
> UuidDto create_connector(connector_request_dto)

Create a new Connector

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.connector_request_dto import ConnectorRequestDto
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    connector_request_dto = pyCZERTAINLY.ConnectorRequestDto() # ConnectorRequestDto | 

    try:
        # Create a new Connector
        api_response = api_instance.create_connector(connector_request_dto)
        print("The response of ConnectorManagementApi->create_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->create_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_request_dto** | [**ConnectorRequestDto**](ConnectorRequestDto.md)|  | 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | New Connector created |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connector**
> delete_connector(uuid)

Delete a Connector

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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID

    try:
        # Delete a Connector
        api_instance.delete_connector(uuid)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->delete_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 

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
**204** | Connector deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_connector**
> ConnectorDto edit_connector(uuid, connector_update_request_dto)

Edit a Connector

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.connector_dto import ConnectorDto
from pyCZERTAINLY.models.connector_update_request_dto import ConnectorUpdateRequestDto
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID
    connector_update_request_dto = pyCZERTAINLY.ConnectorUpdateRequestDto() # ConnectorUpdateRequestDto | 

    try:
        # Edit a Connector
        api_response = api_instance.edit_connector(uuid, connector_update_request_dto)
        print("The response of ConnectorManagementApi->edit_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->edit_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 
 **connector_update_request_dto** | [**ConnectorUpdateRequestDto**](ConnectorUpdateRequestDto.md)|  | 

### Return type

[**ConnectorDto**](ConnectorDto.md)

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
**200** | Connector updated |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_connector**
> List[BulkActionMessageDto] force_delete_connector(request_body)

Force Delete multiple Connectors

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.bulk_action_message_dto import BulkActionMessageDto
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Connector UUIDs

    try:
        # Force Delete multiple Connectors
        api_response = api_instance.force_delete_connector(request_body)
        print("The response of ConnectorManagementApi->force_delete_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->force_delete_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Connector UUIDs | 

### Return type

[**List[BulkActionMessageDto]**](BulkActionMessageDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connectors deleted |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> List[BaseAttributeDto] get_attributes(uuid, function_group, kind)

Get Attributes from a Connector

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.base_attribute_dto import BaseAttributeDto
from pyCZERTAINLY.models.function_group_code import FunctionGroupCode
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID
    function_group = pyCZERTAINLY.FunctionGroupCode() # FunctionGroupCode | Function Group name
    kind = 'kind_example' # str | Kind

    try:
        # Get Attributes from a Connector
        api_response = api_instance.get_attributes(uuid, function_group, kind)
        print("The response of ConnectorManagementApi->get_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->get_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 
 **function_group** | [**FunctionGroupCode**](.md)| Function Group name | 
 **kind** | **str**| Kind | 

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
**502** | Connector Error |  -  |
**200** | Attributes received |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_all**
> Dict[str, Dict[str, List[BaseAttributeDto]]] get_attributes_all(uuid)

Get attributes of all Function Groups

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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID

    try:
        # Get attributes of all Function Groups
        api_response = api_instance.get_attributes_all(uuid)
        print("The response of ConnectorManagementApi->get_attributes_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->get_attributes_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 

### Return type

**Dict[str, Dict[str, List[BaseAttributeDto]]]**

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
**200** | Attributes received |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector**
> ConnectorDto get_connector(uuid)

Get details of a Connector

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.connector_dto import ConnectorDto
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID

    try:
        # Get details of a Connector
        api_response = api_instance.get_connector(uuid)
        print("The response of ConnectorManagementApi->get_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->get_connector: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 

### Return type

[**ConnectorDto**](ConnectorDto.md)

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
**200** | Connector details retrieved |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectors**
> List[ConnectorDto] list_connectors(function_group=function_group, kind=kind, status=status)

List Connectors by Function Group and Kind

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.connector_dto import ConnectorDto
from pyCZERTAINLY.models.connector_status import ConnectorStatus
from pyCZERTAINLY.models.function_group_code import FunctionGroupCode
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    function_group = pyCZERTAINLY.FunctionGroupCode() # FunctionGroupCode |  (optional)
    kind = 'kind_example' # str |  (optional)
    status = pyCZERTAINLY.ConnectorStatus() # ConnectorStatus |  (optional)

    try:
        # List Connectors by Function Group and Kind
        api_response = api_instance.list_connectors(function_group=function_group, kind=kind, status=status)
        print("The response of ConnectorManagementApi->list_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->list_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_group** | [**FunctionGroupCode**](.md)|  | [optional] 
 **kind** | **str**|  | [optional] 
 **status** | [**ConnectorStatus**](.md)|  | [optional] 

### Return type

[**List[ConnectorDto]**](ConnectorDto.md)

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
**200** | List all Connectors |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reconnect**
> List[ConnectDto] reconnect(uuid)

Reconnect to a Connector

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.connect_dto import ConnectDto
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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID

    try:
        # Reconnect to a Connector
        api_response = api_instance.reconnect(uuid)
        print("The response of ConnectorManagementApi->reconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->reconnect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 

### Return type

[**List[ConnectDto]**](ConnectDto.md)

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
**200** | Reconnect to a Connector |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_attributes**
> validate_attributes(uuid, function_group, kind, request_attribute_dto)

Validate Attributes

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
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID
    function_group = 'function_group_example' # str | Function Group name
    kind = 'kind_example' # str | Kind
    request_attribute_dto = [pyCZERTAINLY.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Validate Attributes
        api_instance.validate_attributes(uuid, function_group, kind, request_attribute_dto)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->validate_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 
 **function_group** | **str**| Function Group name | 
 **kind** | **str**| Kind | 
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
**200** | Attributes Validated |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

