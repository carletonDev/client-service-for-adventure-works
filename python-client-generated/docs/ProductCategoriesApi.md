# swagger_client.ProductCategoriesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product_category**](ProductCategoriesApi.md#delete_product_category) | **DELETE** /api/ProductCategories/{id} | 
[**get_product_category**](ProductCategoriesApi.md#get_product_category) | **GET** /api/ProductCategories | 
[**get_product_category_0**](ProductCategoriesApi.md#get_product_category_0) | **GET** /api/ProductCategories/{id} | 
[**post_product_category**](ProductCategoriesApi.md#post_product_category) | **POST** /api/ProductCategories | 
[**put_product_category**](ProductCategoriesApi.md#put_product_category) | **PUT** /api/ProductCategories/{id} | 


# **delete_product_category**
> delete_product_category(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductCategoriesApi()
id = 56 # int | 

try:
    api_instance.delete_product_category(id)
except ApiException as e:
    print("Exception when calling ProductCategoriesApi->delete_product_category: %s\n" % e)
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

# **get_product_category**
> list[ProductCategory] get_product_category()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductCategoriesApi()

try:
    api_response = api_instance.get_product_category()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductCategoriesApi->get_product_category: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProductCategory]**](ProductCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_category_0**
> get_product_category_0(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductCategoriesApi()
id = 56 # int | 

try:
    api_instance.get_product_category_0(id)
except ApiException as e:
    print("Exception when calling ProductCategoriesApi->get_product_category_0: %s\n" % e)
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

# **post_product_category**
> post_product_category(product_category=product_category)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductCategoriesApi()
product_category = swagger_client.ProductCategory() # ProductCategory |  (optional)

try:
    api_instance.post_product_category(product_category=product_category)
except ApiException as e:
    print("Exception when calling ProductCategoriesApi->post_product_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_category** | [**ProductCategory**](ProductCategory.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_product_category**
> put_product_category(id, product_category=product_category)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductCategoriesApi()
id = 56 # int | 
product_category = swagger_client.ProductCategory() # ProductCategory |  (optional)

try:
    api_instance.put_product_category(id, product_category=product_category)
except ApiException as e:
    print("Exception when calling ProductCategoriesApi->put_product_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **product_category** | [**ProductCategory**](ProductCategory.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

