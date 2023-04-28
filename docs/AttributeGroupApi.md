# swagger_client.AttributeGroupApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attribute_groups_get**](AttributeGroupApi.md#attribute_groups_get) | **GET** /api/rest/v1/attribute-groups/{code} | Get an attribute group
[**attribute_groups_get_list**](AttributeGroupApi.md#attribute_groups_get_list) | **GET** /api/rest/v1/attribute-groups | Get list of attribute groups
[**attribute_groups_patch**](AttributeGroupApi.md#attribute_groups_patch) | **PATCH** /api/rest/v1/attribute-groups/{code} | Update/create an attribute group
[**attribute_groups_post**](AttributeGroupApi.md#attribute_groups_post) | **POST** /api/rest/v1/attribute-groups | Create a new attribute group
[**several_attribute_groups_patch**](AttributeGroupApi.md#several_attribute_groups_patch) | **PATCH** /api/rest/v1/attribute-groups | Update/create several attribute groups

# **attribute_groups_get**
> InlineResponse20011 attribute_groups_get(authorization, code)

Get an attribute group

This endpoint allows you to get the information about a given attribute group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeGroupApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Get an attribute group
    api_response = api_instance.attribute_groups_get(authorization, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeGroupApi->attribute_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_groups_get_list**
> AttributeGroups attribute_groups_get_list(authorization, search=search, page=page, limit=limit, with_count=with_count)

Get list of attribute groups

This endpoint allows you to get a list of attribute groups. Attribute groups are paginated and sorted by code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeGroupApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
search = 'search_example' # str | Filter attribute groups, for more details see the <a href=\"/documentation/filter.html#filter-attribute-groups\">Filters</a> section. (optional)
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get list of attribute groups
    api_response = api_instance.attribute_groups_get_list(authorization, search=search, page=page, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeGroupApi->attribute_groups_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **search** | **str**| Filter attribute groups, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-attribute-groups\&quot;&gt;Filters&lt;/a&gt; section. | [optional] 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**AttributeGroups**](AttributeGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_groups_patch**
> attribute_groups_patch(body, code)

Update/create an attribute group

This endpoint allows you to update a given attribute group. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no attribute group exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeGroupApi()
body = swagger_client.AttributegroupsCodeBody() # AttributegroupsCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create an attribute group
    api_instance.attribute_groups_patch(body, code)
except ApiException as e:
    print("Exception when calling AttributeGroupApi->attribute_groups_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributegroupsCodeBody**](AttributegroupsCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attribute_groups_post**
> attribute_groups_post(body=body)

Create a new attribute group

This endpoint allows you to create a new attribute group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeGroupApi()
body = swagger_client.V1AttributegroupsBody() # V1AttributegroupsBody |  (optional)

try:
    # Create a new attribute group
    api_instance.attribute_groups_post(body=body)
except ApiException as e:
    print("Exception when calling AttributeGroupApi->attribute_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AttributegroupsBody**](V1AttributegroupsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **several_attribute_groups_patch**
> InlineResponse200 several_attribute_groups_patch(body=body)

Update/create several attribute groups

This endpoint allows you to update and/or create several attribute groups at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeGroupApi()
body = swagger_client.V1AttributegroupsBody1() # V1AttributegroupsBody1 |  (optional)

try:
    # Update/create several attribute groups
    api_response = api_instance.several_attribute_groups_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeGroupApi->several_attribute_groups_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AttributegroupsBody1**](V1AttributegroupsBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

