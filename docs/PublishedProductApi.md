# swagger_client.PublishedProductApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_published_products**](PublishedProductApi.md#get_published_products) | **GET** /api/rest/v1/published-products | Get list of published products
[**get_published_products_code**](PublishedProductApi.md#get_published_products_code) | **GET** /api/rest/v1/published-products/{code} | Get a published product

# **get_published_products**
> PublishedProducts get_published_products(authorization, search=search, scope=scope, locales=locales, attributes=attributes, pagination_type=pagination_type, page=page, search_after=search_after, limit=limit, with_count=with_count)

Get list of published products

This endpoint allows you to get a list of published products. Published products are paginated and they can be filtered.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishedProductApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
search = 'search_example' # str | Filter published products, for more details see the <a href=\"/documentation/filter.html\">Filters</a> section (optional)
scope = 'scope_example' # str | Filter published product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#filter-published-product-values\">Filter on published product values</a> section (optional)
locales = 'locales_example' # str | Filter published product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#filter-published-product-values\">Filter on published product values</a> section (optional)
attributes = 'attributes_example' # str | Filter published product values to only return those concerning the given attributes, for more details see the <a href=\"/documentation/filter.html#filter-product-values\">Filter on product values</a> section (optional)
pagination_type = 'page' # str | Pagination method type, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to page)
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
search_after = 'cursor to the first page' # str | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to cursor to the first page)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get list of published products
    api_response = api_instance.get_published_products(authorization, search=search, scope=scope, locales=locales, attributes=attributes, pagination_type=pagination_type, page=page, search_after=search_after, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishedProductApi->get_published_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **search** | **str**| Filter published products, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section | [optional] 
 **scope** | **str**| Filter published product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-published-product-values\&quot;&gt;Filter on published product values&lt;/a&gt; section | [optional] 
 **locales** | **str**| Filter published product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-published-product-values\&quot;&gt;Filter on published product values&lt;/a&gt; section | [optional] 
 **attributes** | **str**| Filter published product values to only return those concerning the given attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-product-values\&quot;&gt;Filter on product values&lt;/a&gt; section | [optional] 
 **pagination_type** | **str**| Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to page]
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **search_after** | **str**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**PublishedProducts**](PublishedProducts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_published_products_code**
> InlineResponse2005 get_published_products_code(authorization, code)

Get a published product

This endpoint allows you to get the information about a given published product.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublishedProductApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Get a published product
    api_response = api_instance.get_published_products_code(authorization, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublishedProductApi->get_published_products_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

