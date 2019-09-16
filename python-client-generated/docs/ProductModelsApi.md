# swagger_client.ProductModelsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product_model**](ProductModelsApi.md#delete_product_model) | **DELETE** /api/ProductModels/{id} | 
[**get_product_model**](ProductModelsApi.md#get_product_model) | **GET** /api/ProductModels | 
[**get_product_model_0**](ProductModelsApi.md#get_product_model_0) | **GET** /api/ProductModels/{id} | 
[**post_product_model**](ProductModelsApi.md#post_product_model) | **POST** /api/ProductModels | 
[**put_product_model**](ProductModelsApi.md#put_product_model) | **PUT** /api/ProductModels/{id} | 


# **delete_product_model**
> delete_product_model(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelsApi()
id = 56 # int | 

try:
    api_instance.delete_product_model(id)
except ApiException as e:
    print("Exception when calling ProductModelsApi->delete_product_model: %s\n" % e)
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

# **get_product_model**
> list[ProductModel] get_product_model()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelsApi()

try:
    api_response = api_instance.get_product_model()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductModelsApi->get_product_model: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProductModel]**](ProductModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_model_0**
> get_product_model_0(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelsApi()
id = 56 # int | 

try:
    api_instance.get_product_model_0(id)
except ApiException as e:
    print("Exception when calling ProductModelsApi->get_product_model_0: %s\n" % e)
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

# **post_product_model**
> post_product_model(product_model=product_model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelsApi()
product_model = swagger_client.ProductModel() # ProductModel |  (optional)

try:
    api_instance.post_product_model(product_model=product_model)
except ApiException as e:
    print("Exception when calling ProductModelsApi->post_product_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_model** | [**ProductModel**](ProductModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_product_model**
> put_product_model(id, product_model=product_model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductModelsApi()
id = 56 # int | 
product_model = swagger_client.ProductModel() # ProductModel |  (optional)

try:
    api_instance.put_product_model(id, product_model=product_model)
except ApiException as e:
    print("Exception when calling ProductModelsApi->put_product_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **product_model** | [**ProductModel**](ProductModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

