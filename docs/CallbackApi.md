# pyCZERTAINLY.CallbackApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callback**](CallbackApi.md#callback) | **POST** /v1/connectors/{uuid}/{functionGroup}/{kind}/callback | Connector Callback API
[**resource_callback**](CallbackApi.md#resource_callback) | **POST** /v1/{resource}/{parentObjectUuid}/callback | Resource Callback API


# **callback**
> object callback(uuid, function_group, kind, request_attribute_callback)

Connector Callback API

API to trigger the Callback for Connector.

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.request_attribute_callback import RequestAttributeCallback
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
    api_instance = pyCZERTAINLY.CallbackApi(api_client)
    uuid = 'uuid_example' # str | Connector UUID
    function_group = 'function_group_example' # str | Function Group
    kind = 'kind_example' # str | Kind
    request_attribute_callback = pyCZERTAINLY.RequestAttributeCallback() # RequestAttributeCallback | 

    try:
        # Connector Callback API
        api_response = api_instance.callback(uuid, function_group, kind, request_attribute_callback)
        print("The response of CallbackApi->callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbackApi->callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Connector UUID | 
 **function_group** | **str**| Function Group | 
 **kind** | **str**| Kind | 
 **request_attribute_callback** | [**RequestAttributeCallback**](RequestAttributeCallback.md)|  | 

### Return type

**object**

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Callback executed |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_callback**
> object resource_callback(resource, parent_object_uuid, request_attribute_callback)

Resource Callback API

API to trigger the Callback for resource.

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.request_attribute_callback import RequestAttributeCallback
from pyCZERTAINLY.models.resource import Resource
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
    api_instance = pyCZERTAINLY.CallbackApi(api_client)
    resource = pyCZERTAINLY.Resource() # Resource | Name of the resource
    parent_object_uuid = 'parent_object_uuid_example' # str | Parent Object UUID
    request_attribute_callback = pyCZERTAINLY.RequestAttributeCallback() # RequestAttributeCallback | 

    try:
        # Resource Callback API
        api_response = api_instance.resource_callback(resource, parent_object_uuid, request_attribute_callback)
        print("The response of CallbackApi->resource_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallbackApi->resource_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | [**Resource**](.md)| Name of the resource | 
 **parent_object_uuid** | **str**| Parent Object UUID | 
 **request_attribute_callback** | [**RequestAttributeCallback**](RequestAttributeCallback.md)|  | 

### Return type

**object**

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Callback executed |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

