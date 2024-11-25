# openapi_client.CustomAttributesApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_custom_attributes**](CustomAttributesApi.md#bulk_delete_custom_attributes) | **DELETE** /v1/attributes/custom | Delete multiple Custom Attributes
[**bulk_disable_custom_attributes**](CustomAttributesApi.md#bulk_disable_custom_attributes) | **PATCH** /v1/attributes/custom/disable | Disable multiple Custom Attributes
[**bulk_enable_custom_attributes**](CustomAttributesApi.md#bulk_enable_custom_attributes) | **PATCH** /v1/attributes/custom/enable | Enable multiple Custom Attributes
[**create_custom_attribute**](CustomAttributesApi.md#create_custom_attribute) | **POST** /v1/attributes/custom | Create Custom Attribute
[**delete_attribute_content_for_resource**](CustomAttributesApi.md#delete_attribute_content_for_resource) | **DELETE** /v1/attributes/custom/resources/{resourceName}/objects/{objectUuid}/{attributeUuid} | Delete Value of a Custom Attribute for a Resource
[**delete_custom_attribute**](CustomAttributesApi.md#delete_custom_attribute) | **DELETE** /v1/attributes/custom/{uuid} | Delete Custom Attribute
[**disable_custom_attribute**](CustomAttributesApi.md#disable_custom_attribute) | **PATCH** /v1/attributes/custom/{uuid}/disable | Disable Custom Attribute
[**edit_custom_attribute**](CustomAttributesApi.md#edit_custom_attribute) | **PUT** /v1/attributes/custom/{uuid} | Edit Custom Attribute
[**enable_custom_attribute**](CustomAttributesApi.md#enable_custom_attribute) | **PATCH** /v1/attributes/custom/{uuid}/enable | Enable Custom Attribute
[**get_custom_attribute**](CustomAttributesApi.md#get_custom_attribute) | **GET** /v1/attributes/custom/{uuid} | Custom Attribute details
[**get_resource_custom_attributes**](CustomAttributesApi.md#get_resource_custom_attributes) | **GET** /v1/attributes/custom/resources/{resource} | Get Custom Attributes for a resource
[**get_resources**](CustomAttributesApi.md#get_resources) | **GET** /v1/attributes/custom/resources | Get available resources for Custom Attributes
[**list_custom_attributes**](CustomAttributesApi.md#list_custom_attributes) | **GET** /v1/attributes/custom | List Custom Attributes
[**update_attribute_content_for_resource**](CustomAttributesApi.md#update_attribute_content_for_resource) | **PATCH** /v1/attributes/custom/resources/{resourceName}/objects/{objectUuid}/{attributeUuid} | Update Value of a Custom Attribute for a Resource
[**update_resources**](CustomAttributesApi.md#update_resources) | **PATCH** /v1/attributes/custom/{uuid}/resources | Associate Custom Attribute to Resource


# **bulk_delete_custom_attributes**
> bulk_delete_custom_attributes(request_body)

Delete multiple Custom Attributes

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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Attribute UUIDs

    try:
        # Delete multiple Custom Attributes
        api_instance.bulk_delete_custom_attributes(request_body)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->bulk_delete_custom_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Attribute UUIDs | 

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
**204** | Custom Attributes deleted |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_disable_custom_attributes**
> bulk_disable_custom_attributes(request_body)

Disable multiple Custom Attributes

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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Attribute UUIDs

    try:
        # Disable multiple Custom Attributes
        api_instance.bulk_disable_custom_attributes(request_body)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->bulk_disable_custom_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Attribute UUIDs | 

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
**204** | Custom Attributes disabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_custom_attributes**
> bulk_enable_custom_attributes(request_body)

Enable multiple Custom Attributes

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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    request_body = ["c2f685d4-6a3e-11ec-90d6-0242ac120003","b9b09548-a97c-4c6a-a06a-e4ee6fc2da98"] # List[str] | Attribute UUIDs

    try:
        # Enable multiple Custom Attributes
        api_instance.bulk_enable_custom_attributes(request_body)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->bulk_enable_custom_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)| Attribute UUIDs | 

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
**204** | Custom Attributes enabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_attribute**
> UuidDto create_custom_attribute(custom_attribute_create_request_dto)

Create Custom Attribute

### Example


```python
import openapi_client
from openapi_client.models.custom_attribute_create_request_dto import CustomAttributeCreateRequestDto
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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    custom_attribute_create_request_dto = openapi_client.CustomAttributeCreateRequestDto() # CustomAttributeCreateRequestDto | 

    try:
        # Create Custom Attribute
        api_response = api_instance.create_custom_attribute(custom_attribute_create_request_dto)
        print("The response of CustomAttributesApi->create_custom_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->create_custom_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_create_request_dto** | [**CustomAttributeCreateRequestDto**](CustomAttributeCreateRequestDto.md)|  | 

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
**201** | Custom Attribute created |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute_content_for_resource**
> List[ResponseAttributeDto] delete_attribute_content_for_resource(resource_name, object_uuid, attribute_uuid)

Delete Value of a Custom Attribute for a Resource

### Example


```python
import openapi_client
from openapi_client.models.resource import Resource
from openapi_client.models.response_attribute_dto import ResponseAttributeDto
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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    resource_name = openapi_client.Resource() # Resource | Resource Type
    object_uuid = 'object_uuid_example' # str | Object UUID
    attribute_uuid = 'attribute_uuid_example' # str | Custom Attribute UUID

    try:
        # Delete Value of a Custom Attribute for a Resource
        api_response = api_instance.delete_attribute_content_for_resource(resource_name, object_uuid, attribute_uuid)
        print("The response of CustomAttributesApi->delete_attribute_content_for_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->delete_attribute_content_for_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | [**Resource**](.md)| Resource Type | 
 **object_uuid** | **str**| Object UUID | 
 **attribute_uuid** | **str**| Custom Attribute UUID | 

### Return type

[**List[ResponseAttributeDto]**](ResponseAttributeDto.md)

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
**200** | Custom Attribute value deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_attribute**
> delete_custom_attribute(uuid)

Delete Custom Attribute

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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    uuid = 'uuid_example' # str | Custom Attribute UUID

    try:
        # Delete Custom Attribute
        api_instance.delete_custom_attribute(uuid)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->delete_custom_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Custom Attribute UUID | 

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
**204** | Custom Attribute deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_custom_attribute**
> disable_custom_attribute(uuid)

Disable Custom Attribute

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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    uuid = 'uuid_example' # str | Custom Attribute UUID

    try:
        # Disable Custom Attribute
        api_instance.disable_custom_attribute(uuid)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->disable_custom_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Custom Attribute UUID | 

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
**204** | Custom Attribute disabled |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_custom_attribute**
> CustomAttributeDefinitionDetailDto edit_custom_attribute(uuid, custom_attribute_update_request_dto)

Edit Custom Attribute

### Example


```python
import openapi_client
from openapi_client.models.custom_attribute_definition_detail_dto import CustomAttributeDefinitionDetailDto
from openapi_client.models.custom_attribute_update_request_dto import CustomAttributeUpdateRequestDto
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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    uuid = 'uuid_example' # str | Attribute UUID
    custom_attribute_update_request_dto = openapi_client.CustomAttributeUpdateRequestDto() # CustomAttributeUpdateRequestDto | 

    try:
        # Edit Custom Attribute
        api_response = api_instance.edit_custom_attribute(uuid, custom_attribute_update_request_dto)
        print("The response of CustomAttributesApi->edit_custom_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->edit_custom_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Attribute UUID | 
 **custom_attribute_update_request_dto** | [**CustomAttributeUpdateRequestDto**](CustomAttributeUpdateRequestDto.md)|  | 

### Return type

[**CustomAttributeDefinitionDetailDto**](CustomAttributeDefinitionDetailDto.md)

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
**200** | Custom Attribute updated |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_custom_attribute**
> enable_custom_attribute(uuid)

Enable Custom Attribute

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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    uuid = 'uuid_example' # str | Custom Attribute UUID

    try:
        # Enable Custom Attribute
        api_instance.enable_custom_attribute(uuid)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->enable_custom_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Custom Attribute UUID | 

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
**204** | Custom Attribute enabled |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_attribute**
> CustomAttributeDefinitionDetailDto get_custom_attribute(uuid)

Custom Attribute details

### Example


```python
import openapi_client
from openapi_client.models.custom_attribute_definition_detail_dto import CustomAttributeDefinitionDetailDto
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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Custom Attribute details
        api_response = api_instance.get_custom_attribute(uuid)
        print("The response of CustomAttributesApi->get_custom_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->get_custom_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**CustomAttributeDefinitionDetailDto**](CustomAttributeDefinitionDetailDto.md)

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
**200** | Custom Attribute details retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_custom_attributes**
> List[CustomAttribute] get_resource_custom_attributes(resource)

Get Custom Attributes for a resource

### Example


```python
import openapi_client
from openapi_client.models.custom_attribute import CustomAttribute
from openapi_client.models.resource import Resource
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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    resource = openapi_client.Resource() # Resource | Resource Name

    try:
        # Get Custom Attributes for a resource
        api_response = api_instance.get_resource_custom_attributes(resource)
        print("The response of CustomAttributesApi->get_resource_custom_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->get_resource_custom_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](.md)| Resource Name | 

### Return type

[**List[CustomAttribute]**](CustomAttribute.md)

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
**200** | Custom Attribute retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> List[Resource] get_resources()

Get available resources for Custom Attributes

### Example


```python
import openapi_client
from openapi_client.models.resource import Resource
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
    api_instance = openapi_client.CustomAttributesApi(api_client)

    try:
        # Get available resources for Custom Attributes
        api_response = api_instance.get_resources()
        print("The response of CustomAttributesApi->get_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->get_resources: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Resource]**](Resource.md)

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
**200** | Custom Attribute retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_attributes**
> List[CustomAttributeDefinitionDto] list_custom_attributes(attribute_content_type=attribute_content_type)

List Custom Attributes

### Example


```python
import openapi_client
from openapi_client.models.attribute_content_type import AttributeContentType
from openapi_client.models.custom_attribute_definition_dto import CustomAttributeDefinitionDto
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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    attribute_content_type = openapi_client.AttributeContentType() # AttributeContentType |  (optional)

    try:
        # List Custom Attributes
        api_response = api_instance.list_custom_attributes(attribute_content_type=attribute_content_type)
        print("The response of CustomAttributesApi->list_custom_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->list_custom_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_content_type** | [**AttributeContentType**](.md)|  | [optional] 

### Return type

[**List[CustomAttributeDefinitionDto]**](CustomAttributeDefinitionDto.md)

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
**200** | list of available Custom Attributes |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_content_for_resource**
> List[ResponseAttributeDto] update_attribute_content_for_resource(resource_name, object_uuid, attribute_uuid, base_attribute_content_dto)

Update Value of a Custom Attribute for a Resource

### Example


```python
import openapi_client
from openapi_client.models.base_attribute_content_dto import BaseAttributeContentDto
from openapi_client.models.resource import Resource
from openapi_client.models.response_attribute_dto import ResponseAttributeDto
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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    resource_name = openapi_client.Resource() # Resource | Resource Type
    object_uuid = 'object_uuid_example' # str | Object UUID
    attribute_uuid = 'attribute_uuid_example' # str | Custom Attribute UUID
    base_attribute_content_dto = [openapi_client.BaseAttributeContentDto()] # List[BaseAttributeContentDto] | 

    try:
        # Update Value of a Custom Attribute for a Resource
        api_response = api_instance.update_attribute_content_for_resource(resource_name, object_uuid, attribute_uuid, base_attribute_content_dto)
        print("The response of CustomAttributesApi->update_attribute_content_for_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->update_attribute_content_for_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | [**Resource**](.md)| Resource Type | 
 **object_uuid** | **str**| Object UUID | 
 **attribute_uuid** | **str**| Custom Attribute UUID | 
 **base_attribute_content_dto** | [**List[BaseAttributeContentDto]**](BaseAttributeContentDto.md)|  | 

### Return type

[**List[ResponseAttributeDto]**](ResponseAttributeDto.md)

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
**200** | Custom Attribute value updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resources**
> update_resources(uuid, request_body)

Associate Custom Attribute to Resource

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
    api_instance = openapi_client.CustomAttributesApi(api_client)
    uuid = 'uuid_example' # str | Custom Attribute UUID
    request_body = ["raProfiles","authorities"] # List[str] | List of Resources

    try:
        # Associate Custom Attribute to Resource
        api_instance.update_resources(uuid, request_body)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->update_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Custom Attribute UUID | 
 **request_body** | [**List[str]**](str.md)| List of Resources | 

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
**204** | Custom Attribute associated to the resources |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

