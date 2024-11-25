# pyCZERTAINLY.EntityManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_instance**](EntityManagementApi.md#create_entity_instance) | **POST** /v1/entities | Add Entity instance
[**delete_entity_instance**](EntityManagementApi.md#delete_entity_instance) | **DELETE** /v1/entities/{entityUuid} | Delete Entity instance
[**edit_entity_instance**](EntityManagementApi.md#edit_entity_instance) | **PUT** /v1/entities/{entityUuid} | Edit Entity instance
[**get_entity_instance**](EntityManagementApi.md#get_entity_instance) | **GET** /v1/entities/{entityUuid} | Get Entity instance details
[**get_searchable_field_information2**](EntityManagementApi.md#get_searchable_field_information2) | **GET** /v1/entities/search | Get Entities searchable fields information
[**list_entity_instances**](EntityManagementApi.md#list_entity_instances) | **POST** /v1/entities/list | List Entity instances
[**list_location_attributes**](EntityManagementApi.md#list_location_attributes) | **GET** /v1/entities/{entityUuid}/attributes/location | List Location Attributes
[**validate_location_attributes**](EntityManagementApi.md#validate_location_attributes) | **POST** /v1/entities/{entityUuid}/attributes/location/validate | Validate Location Attributes


# **create_entity_instance**
> UuidDto create_entity_instance(entity_instance_request_dto)

Add Entity instance

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.entity_instance_request_dto import EntityInstanceRequestDto
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
    api_instance = pyCZERTAINLY.EntityManagementApi(api_client)
    entity_instance_request_dto = pyCZERTAINLY.EntityInstanceRequestDto() # EntityInstanceRequestDto | 

    try:
        # Add Entity instance
        api_response = api_instance.create_entity_instance(entity_instance_request_dto)
        print("The response of EntityManagementApi->create_entity_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityManagementApi->create_entity_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_instance_request_dto** | [**EntityInstanceRequestDto**](EntityInstanceRequestDto.md)|  | 

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
**201** | Entity instance created |  -  |
**422** | Unprocessable Entity |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_instance**
> delete_entity_instance(entity_uuid)

Delete Entity instance

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
    api_instance = pyCZERTAINLY.EntityManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity instance UUID

    try:
        # Delete Entity instance
        api_instance.delete_entity_instance(entity_uuid)
    except Exception as e:
        print("Exception when calling EntityManagementApi->delete_entity_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity instance UUID | 

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
**204** | Entity instance deleted |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_entity_instance**
> EntityInstanceDto edit_entity_instance(entity_uuid, entity_instance_update_request_dto)

Edit Entity instance

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.entity_instance_dto import EntityInstanceDto
from pyCZERTAINLY.models.entity_instance_update_request_dto import EntityInstanceUpdateRequestDto
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
    api_instance = pyCZERTAINLY.EntityManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity instance UUID
    entity_instance_update_request_dto = pyCZERTAINLY.EntityInstanceUpdateRequestDto() # EntityInstanceUpdateRequestDto | 

    try:
        # Edit Entity instance
        api_response = api_instance.edit_entity_instance(entity_uuid, entity_instance_update_request_dto)
        print("The response of EntityManagementApi->edit_entity_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityManagementApi->edit_entity_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity instance UUID | 
 **entity_instance_update_request_dto** | [**EntityInstanceUpdateRequestDto**](EntityInstanceUpdateRequestDto.md)|  | 

### Return type

[**EntityInstanceDto**](EntityInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**200** | Authority instance details updated |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_instance**
> EntityInstanceDto get_entity_instance(entity_uuid)

Get Entity instance details

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.entity_instance_dto import EntityInstanceDto
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
    api_instance = pyCZERTAINLY.EntityManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity instance UUID

    try:
        # Get Entity instance details
        api_response = api_instance.get_entity_instance(entity_uuid)
        print("The response of EntityManagementApi->get_entity_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityManagementApi->get_entity_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity instance UUID | 

### Return type

[**EntityInstanceDto**](EntityInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**200** | Authority instance details retrieved |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_searchable_field_information2**
> List[SearchFieldDataByGroupDto] get_searchable_field_information2()

Get Entities searchable fields information

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.search_field_data_by_group_dto import SearchFieldDataByGroupDto
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
    api_instance = pyCZERTAINLY.EntityManagementApi(api_client)

    try:
        # Get Entities searchable fields information
        api_response = api_instance.get_searchable_field_information2()
        print("The response of EntityManagementApi->get_searchable_field_information2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityManagementApi->get_searchable_field_information2: %s\n" % e)
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
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**404** | Not Found |  -  |
**200** | Entity searchable field information retrieved |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_instances**
> EntityInstanceResponseDto list_entity_instances(search_request_dto)

List Entity instances

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.entity_instance_response_dto import EntityInstanceResponseDto
from pyCZERTAINLY.models.search_request_dto import SearchRequestDto
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
    api_instance = pyCZERTAINLY.EntityManagementApi(api_client)
    search_request_dto = pyCZERTAINLY.SearchRequestDto() # SearchRequestDto | 

    try:
        # List Entity instances
        api_response = api_instance.list_entity_instances(search_request_dto)
        print("The response of EntityManagementApi->list_entity_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityManagementApi->list_entity_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request_dto** | [**SearchRequestDto**](SearchRequestDto.md)|  | 

### Return type

[**EntityInstanceResponseDto**](EntityInstanceResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**200** | List of Entity instances |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_location_attributes**
> List[BaseAttributeDto] list_location_attributes(entity_uuid)

List Location Attributes

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
    api_instance = pyCZERTAINLY.EntityManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity instance UUID

    try:
        # List Location Attributes
        api_response = api_instance.list_location_attributes(entity_uuid)
        print("The response of EntityManagementApi->list_location_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityManagementApi->list_location_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity instance UUID | 

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
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Location attributes retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_location_attributes**
> validate_location_attributes(entity_uuid, request_attribute_dto)

Validate Location Attributes

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
    api_instance = pyCZERTAINLY.EntityManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity instance UUID
    request_attribute_dto = [pyCZERTAINLY.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Validate Location Attributes
        api_instance.validate_location_attributes(entity_uuid, request_attribute_dto)
    except Exception as e:
        print("Exception when calling EntityManagementApi->validate_location_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity instance UUID | 
 **request_attribute_dto** | [**List[RequestAttributeDto]**](RequestAttributeDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Attributes validated |  -  |
**503** | Connector Communication Error |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

