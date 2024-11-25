# openapi_client.LocalOperationsApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_admin**](LocalOperationsApi.md#add_admin) | **POST** /v1/local/admins | Create Administrator


# **add_admin**
> UserDetailDto add_admin(add_user_request_dto)

Create Administrator

### Example


```python
import openapi_client
from openapi_client.models.add_user_request_dto import AddUserRequestDto
from openapi_client.models.user_detail_dto import UserDetailDto
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
    api_instance = openapi_client.LocalOperationsApi(api_client)
    add_user_request_dto = openapi_client.AddUserRequestDto() # AddUserRequestDto | 

    try:
        # Create Administrator
        api_response = api_instance.add_admin(add_user_request_dto)
        print("The response of LocalOperationsApi->add_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalOperationsApi->add_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_request_dto** | [**AddUserRequestDto**](AddUserRequestDto.md)|  | 

### Return type

[**UserDetailDto**](UserDetailDto.md)

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
**200** | Admin created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

