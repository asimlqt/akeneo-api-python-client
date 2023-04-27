# swagger_client.ProductIdentifierApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_products_code**](ProductIdentifierApi.md#delete_products_code) | **DELETE** /api/rest/v1/products/{code} | Delete a product
[**get_draft_code**](ProductIdentifierApi.md#get_draft_code) | **GET** /api/rest/v1/products/{code}/draft | Get a draft
[**get_products**](ProductIdentifierApi.md#get_products) | **GET** /api/rest/v1/products | Get list of products
[**get_products_code**](ProductIdentifierApi.md#get_products_code) | **GET** /api/rest/v1/products/{code} | Get a product
[**patch_products**](ProductIdentifierApi.md#patch_products) | **PATCH** /api/rest/v1/products | Update/create several products
[**patch_products_code**](ProductIdentifierApi.md#patch_products_code) | **PATCH** /api/rest/v1/products/{code} | Update/create a product
[**post_products**](ProductIdentifierApi.md#post_products) | **POST** /api/rest/v1/products | Create a new product
[**post_proposal**](ProductIdentifierApi.md#post_proposal) | **POST** /api/rest/v1/products/{code}/proposal | Submit a draft for approval

# **delete_products_code**
> delete_products_code(code)

Delete a product

This endpoint allows you to delete a given product. In the Enterprise Edition, since the 2.0, permissions based on your user groups are applied to the product you try to delete.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductIdentifierApi()
code = 'code_example' # str | Code of the resource

try:
    # Delete a product
    api_instance.delete_products_code(code)
except ApiException as e:
    print("Exception when calling ProductIdentifierApi->delete_products_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft_code**
> InlineResponse2001 get_draft_code(code)

Get a draft

This endpoint allows you to get the information about a given draft.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductIdentifierApi()
code = 'code_example' # str | Code of the resource

try:
    # Get a draft
    api_response = api_instance.get_draft_code(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductIdentifierApi->get_draft_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> Products get_products(authorization, search=search, scope=scope, locales=locales, attributes=attributes, pagination_type=pagination_type, page=page, search_after=search_after, limit=limit, with_count=with_count, with_attribute_options=with_attribute_options, with_quality_scores=with_quality_scores, with_completenesses=with_completenesses)

Get list of products

This endpoint allows you to get a list of products. Products are paginated and they can be filtered. In the Enterprise Edition, since the 2.0, permissions based on your user groups are applied to the set of products you request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductIdentifierApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
search = 'search_example' # str | Filter products, for more details see the <a href=\"/documentation/filter.html\">Filters</a> section (optional)
scope = 'scope_example' # str | Filter product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#via-channel\">Filter product values via channel</a> section (optional)
locales = 'locales_example' # str | Filter product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#via-locale\">Filter product values via locale</a> section (optional)
attributes = 'attributes_example' # str | Filter product values to only return those concerning the given attributes, for more details see the <a href=\"/documentation/filter.html#filter-product-values\">Filter on product values</a> section (optional)
pagination_type = 'page' # str | Pagination method type, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to page)
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
search_after = 'cursor to the first page' # str | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to cursor to the first page)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)
with_attribute_options = false # bool | Return labels of attribute options in the response. (Only available since the 5.0 version) (optional) (default to false)
with_quality_scores = false # bool | Return product quality scores in the response. (Only available since the 5.0 version) (optional) (default to false)
with_completenesses = false # bool | Return product completenesses in the response. (Only available since the 6.0 version) (optional) (default to false)

try:
    # Get list of products
    api_response = api_instance.get_products(authorization, search=search, scope=scope, locales=locales, attributes=attributes, pagination_type=pagination_type, page=page, search_after=search_after, limit=limit, with_count=with_count, with_attribute_options=with_attribute_options, with_quality_scores=with_quality_scores, with_completenesses=with_completenesses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductIdentifierApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **search** | **str**| Filter products, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section | [optional] 
 **scope** | **str**| Filter product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-channel\&quot;&gt;Filter product values via channel&lt;/a&gt; section | [optional] 
 **locales** | **str**| Filter product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-locale\&quot;&gt;Filter product values via locale&lt;/a&gt; section | [optional] 
 **attributes** | **str**| Filter product values to only return those concerning the given attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-product-values\&quot;&gt;Filter on product values&lt;/a&gt; section | [optional] 
 **pagination_type** | **str**| Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to page]
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **search_after** | **str**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]
 **with_attribute_options** | **bool**| Return labels of attribute options in the response. (Only available since the 5.0 version) | [optional] [default to false]
 **with_quality_scores** | **bool**| Return product quality scores in the response. (Only available since the 5.0 version) | [optional] [default to false]
 **with_completenesses** | **bool**| Return product completenesses in the response. (Only available since the 6.0 version) | [optional] [default to false]

### Return type

[**Products**](Products.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products_code**
> InlineResponse2001 get_products_code(authorization, code, with_attribute_options=with_attribute_options, with_quality_scores=with_quality_scores, with_completenesses=with_completenesses)

Get a product

This endpoint allows you to get the information about a given product. In the Entreprise Edition, since the v2.0, permissions based on your user groups are applied to the product you request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductIdentifierApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource
with_attribute_options = false # bool | Return labels of attribute options in the response. (Only available since the 5.0 version) (optional) (default to false)
with_quality_scores = false # bool | Return product quality scores in the response. (Only available since the 5.0 version) (optional) (default to false)
with_completenesses = false # bool | Return product completenesses in the response. (Only available since the 6.0 version) (optional) (default to false)

try:
    # Get a product
    api_response = api_instance.get_products_code(authorization, code, with_attribute_options=with_attribute_options, with_quality_scores=with_quality_scores, with_completenesses=with_completenesses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductIdentifierApi->get_products_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 
 **with_attribute_options** | **bool**| Return labels of attribute options in the response. (Only available since the 5.0 version) | [optional] [default to false]
 **with_quality_scores** | **bool**| Return product quality scores in the response. (Only available since the 5.0 version) | [optional] [default to false]
 **with_completenesses** | **bool**| Return product completenesses in the response. (Only available since the 6.0 version) | [optional] [default to false]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_products**
> InlineResponse200 patch_products(body=body)

Update/create several products

This endpoint allows you to update and/or create several products at once. Learn more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no product exists for the given identifier, it creates it. In the Enterprise Edition, since the v2.0, permissions based on your user groups are applied to the products you try to update. It may result in the creation of drafts if you only have edit rights through the product's categories.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductIdentifierApi()
body = swagger_client.V1ProductsBody1() # V1ProductsBody1 |  (optional)

try:
    # Update/create several products
    api_response = api_instance.patch_products(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductIdentifierApi->patch_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ProductsBody1**](V1ProductsBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_products_code**
> patch_products_code(body, code)

Update/create a product

This endpoint allows you to update a given product. Learn more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no product exists for the given identifier, it creates it. In the Entreprise Edition, since the v2.0, permissions based on your user groups are applied to the product you try to update. It may result in the creation of a draft if you only have edit rights through the product's categories.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductIdentifierApi()
body = swagger_client.ProductsCodeBody() # ProductsCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create a product
    api_instance.patch_products_code(body, code)
except ApiException as e:
    print("Exception when calling ProductIdentifierApi->patch_products_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductsCodeBody**](ProductsCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_products**
> post_products(body=body)

Create a new product

This endpoint allows you to create a new product. In the Enterprise Edition, since the v2.0, permissions based on your user groups are applied to the product you try to create.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductIdentifierApi()
body = swagger_client.V1ProductsBody() # V1ProductsBody |  (optional)

try:
    # Create a new product
    api_instance.post_products(body=body)
except ApiException as e:
    print("Exception when calling ProductIdentifierApi->post_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ProductsBody**](V1ProductsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_proposal**
> post_proposal(code)

Submit a draft for approval

This endpoint allows you to submit a draft for approval.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductIdentifierApi()
code = 'code_example' # str | Code of the resource

try:
    # Submit a draft for approval
    api_instance.post_proposal(code)
except ApiException as e:
    print("Exception when calling ProductIdentifierApi->post_proposal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

