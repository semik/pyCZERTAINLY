# openapi_client.LocationManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_location**](LocationManagementApi.md#add_location) | **POST** /v1/entities/{entityUuid}/locations | Add Location
[**delete_location**](LocationManagementApi.md#delete_location) | **DELETE** /v1/entities/{entityUuid}/locations/{locationUuid} | Delete Location
[**disable_location**](LocationManagementApi.md#disable_location) | **PATCH** /v1/entities/{entityUuid}/locations/{locationUuid}/disable | Disable Location
[**edit_location**](LocationManagementApi.md#edit_location) | **PUT** /v1/entities/{entityUuid}/locations/{locationUuid} | Edit Location
[**enable_location**](LocationManagementApi.md#enable_location) | **PATCH** /v1/entities/{entityUuid}/locations/{locationUuid}/enable | Enable Location
[**get_location**](LocationManagementApi.md#get_location) | **GET** /v1/entities/{entityUuid}/locations/{locationUuid} | Get Location Details
[**get_searchable_field_information**](LocationManagementApi.md#get_searchable_field_information) | **GET** /v1/locations/search | Get Locations searchable fields information
[**issue_certificate_to_location**](LocationManagementApi.md#issue_certificate_to_location) | **POST** /v1/entities/{entityUuid}/locations/{locationUuid}/certificates | Issue Certificate to Location
[**list_csr_attributes**](LocationManagementApi.md#list_csr_attributes) | **GET** /v1/entities/{entityUuid}/locations/{locationUuid}/attributes/issue | Get CSR Attributes
[**list_locations**](LocationManagementApi.md#list_locations) | **POST** /v1/locations | List Locations
[**list_push_attributes**](LocationManagementApi.md#list_push_attributes) | **GET** /v1/entities/{entityUuid}/locations/{locationUuid}/attributes/push | Get push Attributes
[**push_certificate**](LocationManagementApi.md#push_certificate) | **PUT** /v1/entities/{entityUuid}/locations/{locationUuid}/certificates/{certificateUuid} | Push Certificate to Location
[**remove_certificate**](LocationManagementApi.md#remove_certificate) | **DELETE** /v1/entities/{entityUuid}/locations/{locationUuid}/certificates/{certificateUuid} | Remove Certificate from Location
[**renew_certificate_in_location**](LocationManagementApi.md#renew_certificate_in_location) | **PATCH** /v1/entities/{entityUuid}/locations/{locationUuid}/certificates/{certificateUuid} | Renew Certificate in Location
[**update_location_content**](LocationManagementApi.md#update_location_content) | **PUT** /v1/entities/{entityUuid}/locations/{locationUuid}/sync | Sync Location content


# **add_location**
> UuidDto add_location(entity_uuid, add_location_request_dto)

Add Location

### Example


```python
import openapi_client
from openapi_client.models.add_location_request_dto import AddLocationRequestDto
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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    add_location_request_dto = openapi_client.AddLocationRequestDto() # AddLocationRequestDto | 

    try:
        # Add Location
        api_response = api_instance.add_location(entity_uuid, add_location_request_dto)
        print("The response of LocationManagementApi->add_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->add_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **add_location_request_dto** | [**AddLocationRequestDto**](AddLocationRequestDto.md)|  | 

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
**201** | Location added |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location**
> delete_location(entity_uuid, location_uuid)

Delete Location

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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID

    try:
        # Delete Location
        api_instance.delete_location(entity_uuid, location_uuid)
    except Exception as e:
        print("Exception when calling LocationManagementApi->delete_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 

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
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**204** | Location deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_location**
> disable_location(entity_uuid, location_uuid)

Disable Location

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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID

    try:
        # Disable Location
        api_instance.disable_location(entity_uuid, location_uuid)
    except Exception as e:
        print("Exception when calling LocationManagementApi->disable_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 

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
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**204** | Location disabled |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_location**
> LocationDto edit_location(entity_uuid, location_uuid, edit_location_request_dto)

Edit Location

### Example


```python
import openapi_client
from openapi_client.models.edit_location_request_dto import EditLocationRequestDto
from openapi_client.models.location_dto import LocationDto
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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID
    edit_location_request_dto = openapi_client.EditLocationRequestDto() # EditLocationRequestDto | 

    try:
        # Edit Location
        api_response = api_instance.edit_location(entity_uuid, location_uuid, edit_location_request_dto)
        print("The response of LocationManagementApi->edit_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->edit_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 
 **edit_location_request_dto** | [**EditLocationRequestDto**](EditLocationRequestDto.md)|  | 

### Return type

[**LocationDto**](LocationDto.md)

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
**204** | Location updated |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_location**
> enable_location(entity_uuid, location_uuid)

Enable Location

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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID

    try:
        # Enable Location
        api_instance.enable_location(entity_uuid, location_uuid)
    except Exception as e:
        print("Exception when calling LocationManagementApi->enable_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 

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
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**204** | Location enabled |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location**
> LocationDto get_location(entity_uuid, location_uuid)

Get Location Details

### Example


```python
import openapi_client
from openapi_client.models.location_dto import LocationDto
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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID

    try:
        # Get Location Details
        api_response = api_instance.get_location(entity_uuid, location_uuid)
        print("The response of LocationManagementApi->get_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->get_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 

### Return type

[**LocationDto**](LocationDto.md)

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
**200** | Location detail retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_searchable_field_information**
> List[SearchFieldDataByGroupDto] get_searchable_field_information()

Get Locations searchable fields information

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
    api_instance = openapi_client.LocationManagementApi(api_client)

    try:
        # Get Locations searchable fields information
        api_response = api_instance.get_searchable_field_information()
        print("The response of LocationManagementApi->get_searchable_field_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->get_searchable_field_information: %s\n" % e)
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
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Locations searchable field information retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_certificate_to_location**
> LocationDto issue_certificate_to_location(entity_uuid, location_uuid, issue_to_location_request_dto)

Issue Certificate to Location

### Example


```python
import openapi_client
from openapi_client.models.issue_to_location_request_dto import IssueToLocationRequestDto
from openapi_client.models.location_dto import LocationDto
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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID
    issue_to_location_request_dto = openapi_client.IssueToLocationRequestDto() # IssueToLocationRequestDto | 

    try:
        # Issue Certificate to Location
        api_response = api_instance.issue_certificate_to_location(entity_uuid, location_uuid, issue_to_location_request_dto)
        print("The response of LocationManagementApi->issue_certificate_to_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->issue_certificate_to_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 
 **issue_to_location_request_dto** | [**IssueToLocationRequestDto**](IssueToLocationRequestDto.md)|  | 

### Return type

[**LocationDto**](LocationDto.md)

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
**200** | Certificate issued |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_csr_attributes**
> List[BaseAttributeDto] list_csr_attributes(entity_uuid, location_uuid)

Get CSR Attributes

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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID

    try:
        # Get CSR Attributes
        api_response = api_instance.list_csr_attributes(entity_uuid, location_uuid)
        print("The response of LocationManagementApi->list_csr_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->list_csr_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 

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
**200** | CSR Attributes list obtained |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_locations**
> LocationsResponseDto list_locations(search_request_dto)

List Locations

### Example


```python
import openapi_client
from openapi_client.models.locations_response_dto import LocationsResponseDto
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
    api_instance = openapi_client.LocationManagementApi(api_client)
    search_request_dto = openapi_client.SearchRequestDto() # SearchRequestDto | 

    try:
        # List Locations
        api_response = api_instance.list_locations(search_request_dto)
        print("The response of LocationManagementApi->list_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->list_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request_dto** | [**SearchRequestDto**](SearchRequestDto.md)|  | 

### Return type

[**LocationsResponseDto**](LocationsResponseDto.md)

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
**200** | Locations retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_push_attributes**
> List[BaseAttributeDto] list_push_attributes(entity_uuid, location_uuid)

Get push Attributes

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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID

    try:
        # Get push Attributes
        api_response = api_instance.list_push_attributes(entity_uuid, location_uuid)
        print("The response of LocationManagementApi->list_push_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->list_push_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Push attributes list obtained |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_certificate**
> LocationDto push_certificate(entity_uuid, location_uuid, certificate_uuid, push_to_location_request_dto)

Push Certificate to Location

### Example


```python
import openapi_client
from openapi_client.models.location_dto import LocationDto
from openapi_client.models.push_to_location_request_dto import PushToLocationRequestDto
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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID
    certificate_uuid = 'certificate_uuid_example' # str | Certificate UUID
    push_to_location_request_dto = openapi_client.PushToLocationRequestDto() # PushToLocationRequestDto | 

    try:
        # Push Certificate to Location
        api_response = api_instance.push_certificate(entity_uuid, location_uuid, certificate_uuid, push_to_location_request_dto)
        print("The response of LocationManagementApi->push_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->push_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 
 **certificate_uuid** | **str**| Certificate UUID | 
 **push_to_location_request_dto** | [**PushToLocationRequestDto**](PushToLocationRequestDto.md)|  | 

### Return type

[**LocationDto**](LocationDto.md)

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
**200** | Certificate pushed |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_certificate**
> LocationDto remove_certificate(entity_uuid, location_uuid, certificate_uuid)

Remove Certificate from Location

### Example


```python
import openapi_client
from openapi_client.models.location_dto import LocationDto
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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID
    certificate_uuid = 'certificate_uuid_example' # str | Certificate UUID

    try:
        # Remove Certificate from Location
        api_response = api_instance.remove_certificate(entity_uuid, location_uuid, certificate_uuid)
        print("The response of LocationManagementApi->remove_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->remove_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 
 **certificate_uuid** | **str**| Certificate UUID | 

### Return type

[**LocationDto**](LocationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate removed |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_certificate_in_location**
> LocationDto renew_certificate_in_location(entity_uuid, location_uuid, certificate_uuid)

Renew Certificate in Location

### Example


```python
import openapi_client
from openapi_client.models.location_dto import LocationDto
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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID
    certificate_uuid = 'certificate_uuid_example' # str | Certificate UUID

    try:
        # Renew Certificate in Location
        api_response = api_instance.renew_certificate_in_location(entity_uuid, location_uuid, certificate_uuid)
        print("The response of LocationManagementApi->renew_certificate_in_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->renew_certificate_in_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 
 **certificate_uuid** | **str**| Certificate UUID | 

### Return type

[**LocationDto**](LocationDto.md)

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
**200** | Content updated |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location_content**
> LocationDto update_location_content(entity_uuid, location_uuid)

Sync Location content

### Example


```python
import openapi_client
from openapi_client.models.location_dto import LocationDto
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
    api_instance = openapi_client.LocationManagementApi(api_client)
    entity_uuid = 'entity_uuid_example' # str | Entity UUID
    location_uuid = 'location_uuid_example' # str | Location UUID

    try:
        # Sync Location content
        api_response = api_instance.update_location_content(entity_uuid, location_uuid)
        print("The response of LocationManagementApi->update_location_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationManagementApi->update_location_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**| Entity UUID | 
 **location_uuid** | **str**| Location UUID | 

### Return type

[**LocationDto**](LocationDto.md)

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
**200** | Content updated |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

