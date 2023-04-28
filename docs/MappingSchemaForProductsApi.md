# swagger_client.MappingSchemaForProductsApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_app_catalogs_mapping_schema_product**](MappingSchemaForProductsApi.md#delete_app_catalogs_mapping_schema_product) | **DELETE** /api/rest/v1/catalogs/{id}/mapping-schemas/product | Delete the product mapping schema related to a catalog
[**get_app_catalogs_mapping_schema_product**](MappingSchemaForProductsApi.md#get_app_catalogs_mapping_schema_product) | **GET** /api/rest/v1/catalogs/{id}/mapping-schemas/product | Get the product mapping schema related to a catalog
[**put_app_catalogs_mapping_schema_product**](MappingSchemaForProductsApi.md#put_app_catalogs_mapping_schema_product) | **PUT** /api/rest/v1/catalogs/{id}/mapping-schemas/product | Create or update the product mapping schema related to a catalog

# **delete_app_catalogs_mapping_schema_product**
> delete_app_catalogs_mapping_schema_product(id)

Delete the product mapping schema related to a catalog

This endpoint allows you to delete the product mapping schema related to a catalog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingSchemaForProductsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Catalog ID

try:
    # Delete the product mapping schema related to a catalog
    api_instance.delete_app_catalogs_mapping_schema_product(id)
except ApiException as e:
    print("Exception when calling MappingSchemaForProductsApi->delete_app_catalogs_mapping_schema_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Catalog ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_catalogs_mapping_schema_product**
> InlineResponse20038 get_app_catalogs_mapping_schema_product(authorization, id)

Get the product mapping schema related to a catalog

This endpoint allows you to retrieve the product mapping schema related to a catalog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingSchemaForProductsApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Catalog ID

try:
    # Get the product mapping schema related to a catalog
    api_response = api_instance.get_app_catalogs_mapping_schema_product(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingSchemaForProductsApi->get_app_catalogs_mapping_schema_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **id** | [**str**](.md)| Catalog ID | 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_app_catalogs_mapping_schema_product**
> put_app_catalogs_mapping_schema_product(id, body=body)

Create or update the product mapping schema related to a catalog

This endpoint allows you to create or update the product mapping schema related to a catalog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingSchemaForProductsApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Catalog ID
body = swagger_client.MappingschemasProductBody() # MappingschemasProductBody |  (optional)

try:
    # Create or update the product mapping schema related to a catalog
    api_instance.put_app_catalogs_mapping_schema_product(id, body=body)
except ApiException as e:
    print("Exception when calling MappingSchemaForProductsApi->put_app_catalogs_mapping_schema_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Catalog ID | 
 **body** | [**MappingschemasProductBody**](MappingschemasProductBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

