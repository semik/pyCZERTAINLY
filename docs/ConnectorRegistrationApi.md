# openapi_client.ConnectorRegistrationApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register**](ConnectorRegistrationApi.md#register) | **POST** /v1/connector/register | Register a Connector


# **register**
> UuidDto register(connector_request_dto)

Register a Connector

### Example


```python
import openapi_client
from openapi_client.models.connector_request_dto import ConnectorRequestDto
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
    api_instance = openapi_client.ConnectorRegistrationApi(api_client)
    connector_request_dto = openapi_client.ConnectorRequestDto() # ConnectorRequestDto | 

    try:
        # Register a Connector
        api_response = api_instance.register(connector_request_dto)
        print("The response of ConnectorRegistrationApi->register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorRegistrationApi->register: %s\n" % e)
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
**400** | Bad Request |  -  |
**502** | Connector Error |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**200** | Connector registration initiated |  -  |
**503** | Connector Communication Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

