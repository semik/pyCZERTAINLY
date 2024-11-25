# pyCZERTAINLY.StatisticsDashboardApi

All URIs are relative to *http://localhost:45309*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics**](StatisticsDashboardApi.md#get_statistics) | **GET** /v1/statistics | Get Dashboard/Statistics Details


# **get_statistics**
> StatisticsDto get_statistics()

Get Dashboard/Statistics Details

### Example


```python
import pyCZERTAINLY
from pyCZERTAINLY.models.statistics_dto import StatisticsDto
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
    api_instance = pyCZERTAINLY.StatisticsDashboardApi(api_client)

    try:
        # Get Dashboard/Statistics Details
        api_response = api_instance.get_statistics()
        print("The response of StatisticsDashboardApi->get_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsDashboardApi->get_statistics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatisticsDto**](StatisticsDto.md)

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
**200** | Details retrieved |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

