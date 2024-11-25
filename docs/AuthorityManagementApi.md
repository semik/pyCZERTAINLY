# openapi_client.AuthorityManagementApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_authority_instance**](AuthorityManagementApi.md#bulk_delete_authority_instance) | **DELETE** /v1/authorities | Delete multiple Authority instances
[**create_authority_instance**](AuthorityManagementApi.md#create_authority_instance) | **POST** /v1/authorities | Add Authority instance
[**delete_authority_instance**](AuthorityManagementApi.md#delete_authority_instance) | **DELETE** /v1/authorities/{uuid} | Delete Authority instance
[**edit_authority_instance**](AuthorityManagementApi.md#edit_authority_instance) | **PUT** /v1/authorities/{uuid} | Edit Authority instance
[**force_delete_authority_instances**](AuthorityManagementApi.md#force_delete_authority_instances) | **DELETE** /v1/authorities/force | Force delete multiple Authority instances
[**get_authority_instance**](AuthorityManagementApi.md#get_authority_instance) | **GET** /v1/authorities/{uuid} | Details of an Authority instance
[**list_authority_instances**](AuthorityManagementApi.md#list_authority_instances) | **GET** /v1/authorities | List of available Authority instances
[**list_cas_in_profile**](AuthorityManagementApi.md#list_cas_in_profile) | **GET** /v1/authorities/{uuid}/endentityprofiles/{endEntityProfileId}/cas | 
[**list_certificate_profiles**](AuthorityManagementApi.md#list_certificate_profiles) | **GET** /v1/authorities/{uuid}/endentityprofiles/{endEntityProfileId}/certificateprofiles | 
[**list_entity_profiles**](AuthorityManagementApi.md#list_entity_profiles) | **GET** /v1/authorities/{uuid}/endentityprofiles | 
[**list_ra_profile_attributes**](AuthorityManagementApi.md#list_ra_profile_attributes) | **GET** /v1/authorities/{uuid}/attributes/raProfile | List RA Profile Attributes
[**validate_ra_profile_attributes**](AuthorityManagementApi.md#validate_ra_profile_attributes) | **POST** /v1/authorities/{uuid}/attributes/raProfile/validate | Validate RA Profile Attributes


# **bulk_delete_authority_instance**
> List[BulkActionMessageDto] bulk_delete_authority_instance(request_body)

Delete multiple Authority instances

### Example


```python
import openapi_client
from openapi_client.models.bulk_action_message_dto import BulkActionMessageDto
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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Authority Instance UUIDs

    try:
        # Delete multiple Authority instances
        api_response = api_instance.bulk_delete_authority_instance(request_body)
        print("The response of AuthorityManagementApi->bulk_delete_authority_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->bulk_delete_authority_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Authority Instance UUIDs | 

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
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**200** | Authority instances deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authority_instance**
> UuidDto create_authority_instance(authority_instance_request_dto)

Add Authority instance

### Example


```python
import openapi_client
from openapi_client.models.authority_instance_request_dto import AuthorityInstanceRequestDto
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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    authority_instance_request_dto = openapi_client.AuthorityInstanceRequestDto() # AuthorityInstanceRequestDto | 

    try:
        # Add Authority instance
        api_response = api_instance.create_authority_instance(authority_instance_request_dto)
        print("The response of AuthorityManagementApi->create_authority_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->create_authority_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authority_instance_request_dto** | [**AuthorityInstanceRequestDto**](AuthorityInstanceRequestDto.md)|  | 

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
**201** | New Authority instance added |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authority_instance**
> delete_authority_instance(uuid)

Delete Authority instance

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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    uuid = 'uuid_example' # str | Authority instance UUID

    try:
        # Delete Authority instance
        api_instance.delete_authority_instance(uuid)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->delete_authority_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Authority instance UUID | 

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
**204** | Authority instance deleted |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_authority_instance**
> AuthorityInstanceDto edit_authority_instance(uuid, authority_instance_update_request_dto)

Edit Authority instance

### Example


```python
import openapi_client
from openapi_client.models.authority_instance_dto import AuthorityInstanceDto
from openapi_client.models.authority_instance_update_request_dto import AuthorityInstanceUpdateRequestDto
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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    uuid = 'uuid_example' # str | Authority instance UUID
    authority_instance_update_request_dto = openapi_client.AuthorityInstanceUpdateRequestDto() # AuthorityInstanceUpdateRequestDto | 

    try:
        # Edit Authority instance
        api_response = api_instance.edit_authority_instance(uuid, authority_instance_update_request_dto)
        print("The response of AuthorityManagementApi->edit_authority_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->edit_authority_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Authority instance UUID | 
 **authority_instance_update_request_dto** | [**AuthorityInstanceUpdateRequestDto**](AuthorityInstanceUpdateRequestDto.md)|  | 

### Return type

[**AuthorityInstanceDto**](AuthorityInstanceDto.md)

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
**200** | Authority instance details updated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_authority_instances**
> List[BulkActionMessageDto] force_delete_authority_instances(request_body)

Force delete multiple Authority instances

### Example


```python
import openapi_client
from openapi_client.models.bulk_action_message_dto import BulkActionMessageDto
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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Force delete multiple Authority instances
        api_response = api_instance.force_delete_authority_instances(request_body)
        print("The response of AuthorityManagementApi->force_delete_authority_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->force_delete_authority_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

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
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Authority instances forced to delete |  -  |
**503** | Connector Communication Error |  -  |
**422** | Unprocessible Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authority_instance**
> AuthorityInstanceDto get_authority_instance(uuid)

Details of an Authority instance

### Example


```python
import openapi_client
from openapi_client.models.authority_instance_dto import AuthorityInstanceDto
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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    uuid = 'uuid_example' # str | Authority instance UUID

    try:
        # Details of an Authority instance
        api_response = api_instance.get_authority_instance(uuid)
        print("The response of AuthorityManagementApi->get_authority_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->get_authority_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Authority instance UUID | 

### Return type

[**AuthorityInstanceDto**](AuthorityInstanceDto.md)

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
**200** | Authority instance details retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authority_instances**
> List[AuthorityInstanceDto] list_authority_instances()

List of available Authority instances

### Example


```python
import openapi_client
from openapi_client.models.authority_instance_dto import AuthorityInstanceDto
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
    api_instance = openapi_client.AuthorityManagementApi(api_client)

    try:
        # List of available Authority instances
        api_response = api_instance.list_authority_instances()
        print("The response of AuthorityManagementApi->list_authority_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->list_authority_instances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AuthorityInstanceDto]**](AuthorityInstanceDto.md)

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
**200** | List of Authority instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cas_in_profile**
> List[NameAndIdDto] list_cas_in_profile(uuid, end_entity_profile_id)



### Example


```python
import openapi_client
from openapi_client.models.name_and_id_dto import NameAndIdDto
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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    uuid = 'uuid_example' # str | Authority instance UUID
    end_entity_profile_id = 56 # int | 

    try:
        api_response = api_instance.list_cas_in_profile(uuid, end_entity_profile_id)
        print("The response of AuthorityManagementApi->list_cas_in_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->list_cas_in_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Authority instance UUID | 
 **end_entity_profile_id** | **int**|  | 

### Return type

[**List[NameAndIdDto]**](NameAndIdDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CAs in Profile retrieved |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificate_profiles**
> List[NameAndIdDto] list_certificate_profiles(uuid, end_entity_profile_id)



### Example


```python
import openapi_client
from openapi_client.models.name_and_id_dto import NameAndIdDto
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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    uuid = 'uuid_example' # str | Authority instance UUID
    end_entity_profile_id = 56 # int | 

    try:
        api_response = api_instance.list_certificate_profiles(uuid, end_entity_profile_id)
        print("The response of AuthorityManagementApi->list_certificate_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->list_certificate_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Authority instance UUID | 
 **end_entity_profile_id** | **int**|  | 

### Return type

[**List[NameAndIdDto]**](NameAndIdDto.md)

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
**200** | Certificate profiles retrieved |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_profiles**
> List[NameAndIdDto] list_entity_profiles(uuid)



### Example


```python
import openapi_client
from openapi_client.models.name_and_id_dto import NameAndIdDto
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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    uuid = 'uuid_example' # str | Authority instance UUID

    try:
        api_response = api_instance.list_entity_profiles(uuid)
        print("The response of AuthorityManagementApi->list_entity_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->list_entity_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Authority instance UUID | 

### Return type

[**List[NameAndIdDto]**](NameAndIdDto.md)

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
**200** | Entity profiles retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ra_profile_attributes**
> List[BaseAttributeDto] list_ra_profile_attributes(uuid)

List RA Profile Attributes

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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    uuid = 'uuid_example' # str | Authority instance UUID

    try:
        # List RA Profile Attributes
        api_response = api_instance.list_ra_profile_attributes(uuid)
        print("The response of AuthorityManagementApi->list_ra_profile_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->list_ra_profile_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Authority instance UUID | 

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
**200** | Attribute information retrieved |  -  |
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_ra_profile_attributes**
> validate_ra_profile_attributes(uuid, request_attribute_dto)

Validate RA Profile Attributes

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
    api_instance = openapi_client.AuthorityManagementApi(api_client)
    uuid = 'uuid_example' # str | Authority instance UUID
    request_attribute_dto = [openapi_client.RequestAttributeDto()] # List[RequestAttributeDto] | 

    try:
        # Validate RA Profile Attributes
        api_instance.validate_ra_profile_attributes(uuid, request_attribute_dto)
    except Exception as e:
        print("Exception when calling AuthorityManagementApi->validate_ra_profile_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Authority instance UUID | 
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
**200** | Attribute information validated |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

