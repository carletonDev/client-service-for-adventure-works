# swagger_client.SalesOrderDetailsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_order_detail**](SalesOrderDetailsApi.md#delete_sales_order_detail) | **DELETE** /api/SalesOrderDetails/{id} | 
[**get_sales_order_detail**](SalesOrderDetailsApi.md#get_sales_order_detail) | **GET** /api/SalesOrderDetails | 
[**get_sales_order_detail_0**](SalesOrderDetailsApi.md#get_sales_order_detail_0) | **GET** /api/SalesOrderDetails/{id} | 
[**post_sales_order_detail**](SalesOrderDetailsApi.md#post_sales_order_detail) | **POST** /api/SalesOrderDetails | 
[**put_sales_order_detail**](SalesOrderDetailsApi.md#put_sales_order_detail) | **PUT** /api/SalesOrderDetails/{id} | 


# **delete_sales_order_detail**
> delete_sales_order_detail(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderDetailsApi()
id = 56 # int | 

try:
    api_instance.delete_sales_order_detail(id)
except ApiException as e:
    print("Exception when calling SalesOrderDetailsApi->delete_sales_order_detail: %s\n" % e)
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

# **get_sales_order_detail**
> list[SalesOrderDetail] get_sales_order_detail()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderDetailsApi()

try:
    api_response = api_instance.get_sales_order_detail()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderDetailsApi->get_sales_order_detail: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SalesOrderDetail]**](SalesOrderDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_order_detail_0**
> get_sales_order_detail_0(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderDetailsApi()
id = 56 # int | 

try:
    api_instance.get_sales_order_detail_0(id)
except ApiException as e:
    print("Exception when calling SalesOrderDetailsApi->get_sales_order_detail_0: %s\n" % e)
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

# **post_sales_order_detail**
> post_sales_order_detail(sales_order_detail=sales_order_detail)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderDetailsApi()
sales_order_detail = swagger_client.SalesOrderDetail() # SalesOrderDetail |  (optional)

try:
    api_instance.post_sales_order_detail(sales_order_detail=sales_order_detail)
except ApiException as e:
    print("Exception when calling SalesOrderDetailsApi->post_sales_order_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_order_detail** | [**SalesOrderDetail**](SalesOrderDetail.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_order_detail**
> put_sales_order_detail(id, sales_order_detail=sales_order_detail)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderDetailsApi()
id = 56 # int | 
sales_order_detail = swagger_client.SalesOrderDetail() # SalesOrderDetail |  (optional)

try:
    api_instance.put_sales_order_detail(id, sales_order_detail=sales_order_detail)
except ApiException as e:
    print("Exception when calling SalesOrderDetailsApi->put_sales_order_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **sales_order_detail** | [**SalesOrderDetail**](SalesOrderDetail.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

