# pyCZERTAINLY.EnumsApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_platform_enums**](EnumsApi.md#get_platform_enums) | **GET** /v1/enums | Get platform enums


# **get_platform_enums**
> Dict[str, Dict[str, EnumItemDto]] get_platform_enums()

Get platform enums

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.enum_item_dto import EnumItemDto
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
    api_instance = pyCZERTAINLY.EnumsApi(api_client)

    try:
        # Get platform enums
        api_response = api_instance.get_platform_enums()
        print("The response of EnumsApi->get_platform_enums:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnumsApi->get_platform_enums: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Dict[str, EnumItemDto]]**

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
**404** | Not Found |  -  |
**200** | Platform settings retrieved |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

