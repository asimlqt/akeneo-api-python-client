# swagger_client.ReferenceEntityApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reference_entities**](ReferenceEntityApi.md#get_reference_entities) | **GET** /api/rest/v1/reference-entities | Get list of reference entities
[**get_reference_entities_code**](ReferenceEntityApi.md#get_reference_entities_code) | **GET** /api/rest/v1/reference-entities/{code} | Get a reference entity
[**patch_reference_entity_code**](ReferenceEntityApi.md#patch_reference_entity_code) | **PATCH** /api/rest/v1/reference-entities/{code} | Update/create a reference entity

# **get_reference_entities**
> ReferenceEntities get_reference_entities(authorization, search_after=search_after)

Get list of reference entities

This endpoint allows you to get a list of reference entities. Reference entities are paginated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
search_after = 'cursor to the first page' # str | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to cursor to the first page)

try:
    # Get list of reference entities
    api_response = api_instance.get_reference_entities(authorization, search_after=search_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceEntityApi->get_reference_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **search_after** | **str**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page]

### Return type

[**ReferenceEntities**](ReferenceEntities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_entities_code**
> InlineResponse20020 get_reference_entities_code(authorization, code)

Get a reference entity

This endpoint allows you to get the information about a given reference entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityApi()
authorization = 'authorization_example' # str | Equal to 'Bearer xx', where 'xx' is the access token.
code = 'code_example' # str | Code of the resource

try:
    # Get a reference entity
    api_response = api_instance.get_reference_entities_code(authorization, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceEntityApi->get_reference_entities_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Equal to &#x27;Bearer xx&#x27;, where &#x27;xx&#x27; is the access token. | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_reference_entity_code**
> patch_reference_entity_code(body, code)

Update/create a reference entity

This endpoint allows you to update a given reference entity. Note that if the reference entity does not already exist, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityApi()
body = swagger_client.ReferenceentitiesCodeBody() # ReferenceentitiesCodeBody | 
code = 'code_example' # str | Code of the resource

try:
    # Update/create a reference entity
    api_instance.patch_reference_entity_code(body, code)
except ApiException as e:
    print("Exception when calling ReferenceEntityApi->patch_reference_entity_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReferenceentitiesCodeBody**](ReferenceentitiesCodeBody.md)|  | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

