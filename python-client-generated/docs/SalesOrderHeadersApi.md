# swagger_client.SalesOrderHeadersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_order_header**](SalesOrderHeadersApi.md#delete_sales_order_header) | **DELETE** /api/SalesOrderHeaders/{id} | 
[**get_sales_order_header**](SalesOrderHeadersApi.md#get_sales_order_header) | **GET** /api/SalesOrderHeaders | 
[**get_sales_order_header_0**](SalesOrderHeadersApi.md#get_sales_order_header_0) | **GET** /api/SalesOrderHeaders/{id} | 
[**post_sales_order_header**](SalesOrderHeadersApi.md#post_sales_order_header) | **POST** /api/SalesOrderHeaders | 
[**put_sales_order_header**](SalesOrderHeadersApi.md#put_sales_order_header) | **PUT** /api/SalesOrderHeaders/{id} | 


# **delete_sales_order_header**
> delete_sales_order_header(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderHeadersApi()
id = 56 # int | 

try:
    api_instance.delete_sales_order_header(id)
except ApiException as e:
    print("Exception when calling SalesOrderHeadersApi->delete_sales_order_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_order_header**
> list[SalesOrderHeader] get_sales_order_header()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderHeadersApi()

try:
    api_response = api_instance.get_sales_order_header()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderHeadersApi->get_sales_order_header: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SalesOrderHeader]**](SalesOrderHeader.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_order_header_0**
> get_sales_order_header_0(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderHeadersApi()
id = 56 # int | 

try:
    api_instance.get_sales_order_header_0(id)
except ApiException as e:
    print("Exception when calling SalesOrderHeadersApi->get_sales_order_header_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_order_header**
> post_sales_order_header(sales_order_header=sales_order_header)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderHeadersApi()
sales_order_header = swagger_client.SalesOrderHeader() # SalesOrderHeader |  (optional)

try:
    api_instance.post_sales_order_header(sales_order_header=sales_order_header)
except ApiException as e:
    print("Exception when calling SalesOrderHeadersApi->post_sales_order_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_order_header** | [**SalesOrderHeader**](SalesOrderHeader.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_order_header**
> put_sales_order_header(id, sales_order_header=sales_order_header)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderHeadersApi()
id = 56 # int | 
sales_order_header = swagger_client.SalesOrderHeader() # SalesOrderHeader |  (optional)

try:
    api_instance.put_sales_order_header(id, sales_order_header=sales_order_header)
except ApiException as e:
    print("Exception when calling SalesOrderHeadersApi->put_sales_order_header: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **sales_order_header** | [**SalesOrderHeader**](SalesOrderHeader.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

