# swagger_client.AssociationTypeApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**association_types_get**](AssociationTypeApi.md#association_types_get) | **GET** /api/rest/v1/association-types/{code} | Get an association type
[**association_types_get_list**](AssociationTypeApi.md#association_types_get_list) | **GET** /api/rest/v1/association-types | Get a list of association types
[**association_types_patch**](AssociationTypeApi.md#association_types_patch) | **PATCH** /api/rest/v1/association-types/{code} | Update/create an association type
[**association_types_post**](AssociationTypeApi.md#association_types_post) | **POST** /api/rest/v1/association-types | Create a new association type
[**several_association_types_patch**](AssociationTypeApi.md#several_association_types_patch) | **PATCH** /api/rest/v1/association-types | Update/create several association types

# **association_types_get**
> InlineResponse20012 association_types_get(authorization, code)

Get an association type

This endpoint allows you to get the information about a given association type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationTypeApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Get an association type
    api_response = api_instance.association_types_get(authorization, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationTypeApi->association_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **association_types_get_list**
> AssociationTypes association_types_get_list(authorization, page=page, limit=limit, with_count=with_count)

Get a list of association types

This endpoint allows you to get a list of association types. Association types are paginated and sorted by code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationTypeApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
with_count = false # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to false)

try:
    # Get a list of association types
    api_response = api_instance.association_types_get_list(authorization, page=page, limit=limit, with_count=with_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationTypeApi->association_types_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**AssociationTypes**](AssociationTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **association_types_patch**
> association_types_patch(body, code)

Update/create an association type

This endpoint allows you to update a given association type. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no association type exists for the given code, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationTypeApi()
body = swagger_client.AssociationtypesCodeBody() # AssociationtypesCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create an association type
    api_instance.association_types_patch(body, code)
except ApiException as e:
    print("Exception when calling AssociationTypeApi->association_types_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssociationtypesCodeBody**](AssociationtypesCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **association_types_post**
> association_types_post(body=body)

Create a new association type

This endpoint allows you to create a new association type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationTypeApi()
body = swagger_client.V1AssociationtypesBody() # V1AssociationtypesBody |  (optional)

try:
    # Create a new association type
    api_instance.association_types_post(body=body)
except ApiException as e:
    print("Exception when calling AssociationTypeApi->association_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AssociationtypesBody**](V1AssociationtypesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **several_association_types_patch**
> InlineResponse200 several_association_types_patch(body=body)

Update/create several association types

This endpoint allows you to update and/or create several association types at once.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssociationTypeApi()
body = swagger_client.V1AssociationtypesBody1() # V1AssociationtypesBody1 |  (optional)

try:
    # Update/create several association types
    api_response = api_instance.several_association_types_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssociationTypeApi->several_association_types_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1AssociationtypesBody1**](V1AssociationtypesBody1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

