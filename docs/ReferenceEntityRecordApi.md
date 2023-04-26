# swagger_client.ReferenceEntityRecordApi

All URIs are relative to *http://demo.akeneo.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reference_entity_records**](ReferenceEntityRecordApi.md#get_reference_entity_records) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/records | Get the list of the records of a reference entity
[**get_reference_entity_records_code**](ReferenceEntityRecordApi.md#get_reference_entity_records_code) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/records/{code} | Get a record of a given reference entity
[**patch_reference_entity_records**](ReferenceEntityRecordApi.md#patch_reference_entity_records) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/records | Update/create several reference entity records
[**patch_reference_entity_records_code**](ReferenceEntityRecordApi.md#patch_reference_entity_records_code) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/records/{code} | Update/create a record of a given reference entity

# **get_reference_entity_records**
> ReferenceEntityRecord get_reference_entity_records(reference_entity_code, search=search, channel=channel, locales=locales, search_after=search_after)

Get the list of the records of a reference entity

This endpoint allows you to get a list of records of a given reference entity. Records are paginated and can be filtered.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityRecordApi()
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity
search = 'search_example' # str | Filter records of the reference entity, for more details see the <a href=\"/documentation/filter.html#filter-reference-entity-records\">Filters</a> section (optional)
channel = 'channel_example' # str | Filter attribute values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#record-values-by-channel\">Filter attribute values by channel</a> section (optional)
locales = 'locales_example' # str | Filter attribute values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#record-values-by-locale\">Filter attribute values by locale</a> section (optional)
search_after = 'cursor to the first page' # str | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to cursor to the first page)

try:
    # Get the list of the records of a reference entity
    api_response = api_instance.get_reference_entity_records(reference_entity_code, search=search, channel=channel, locales=locales, search_after=search_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceEntityRecordApi->get_reference_entity_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_entity_code** | **str**| Code of the reference entity | 
 **search** | **str**| Filter records of the reference entity, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-reference-entity-records\&quot;&gt;Filters&lt;/a&gt; section | [optional] 
 **channel** | **str**| Filter attribute values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#record-values-by-channel\&quot;&gt;Filter attribute values by channel&lt;/a&gt; section | [optional] 
 **locales** | **str**| Filter attribute values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#record-values-by-locale\&quot;&gt;Filter attribute values by locale&lt;/a&gt; section | [optional] 
 **search_after** | **str**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page]

### Return type

[**ReferenceEntityRecord**](ReferenceEntityRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, _embedded, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_entity_records_code**
> InlineResponse20026 get_reference_entity_records_code(reference_entity_code, code)

Get a record of a given reference entity

This endpoint allows you to get the information about a given record for a given reference entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityRecordApi()
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity
code = 'code_example' # str | Code of the resource

try:
    # Get a record of a given reference entity
    api_response = api_instance.get_reference_entity_records_code(reference_entity_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceEntityRecordApi->get_reference_entity_records_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_entity_code** | **str**| Code of the reference entity | 
 **code** | **str**| Code of the resource | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_reference_entity_records**
> list[InlineResponse20025] patch_reference_entity_records(body, reference_entity_code)

Update/create several reference entity records

This endpoint allows you to update and/or create several records of one given reference entity at once. Learn more about <a href=\"/documentation/update.html#patch-reference-entity-record-values\">Update behavior</a>. Note that if the record does not already exist for the given reference entity, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityRecordApi()
body = [swagger_client.ReferenceEntityCodeRecordsBody()] # list[ReferenceEntityCodeRecordsBody] | 
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity

try:
    # Update/create several reference entity records
    api_response = api_instance.patch_reference_entity_records(body, reference_entity_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceEntityRecordApi->patch_reference_entity_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ReferenceEntityCodeRecordsBody]**](ReferenceEntityCodeRecordsBody.md)|  | 
 **reference_entity_code** | **str**| Code of the reference entity | 

### Return type

[**list[InlineResponse20025]**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_reference_entity_records_code**
> patch_reference_entity_records_code(body, reference_entity_code, code)

Update/create a record of a given reference entity

This endpoint allows you to update a given record of a given renference entity. Learn more about <a href=\"/documentation/update.html#patch-reference-entity-record-values\">Update behavior</a>. Note that if the record does not already exist for the given reference entity, it creates it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceEntityRecordApi()
body = swagger_client.RecordsCodeBody() # RecordsCodeBody | 
reference_entity_code = 'reference_entity_code_example' # str | Code of the reference entity
code = 'code_example' # str | Code of the resource

try:
    # Update/create a record of a given reference entity
    api_instance.patch_reference_entity_records_code(body, reference_entity_code, code)
except ApiException as e:
    print("Exception when calling ReferenceEntityRecordApi->patch_reference_entity_records_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordsCodeBody**](RecordsCodeBody.md)|  | 
 **reference_entity_code** | **str**| Code of the reference entity | 
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, code, message, _links

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

