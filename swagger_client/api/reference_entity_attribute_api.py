# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ReferenceEntityAttributeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_reference_entities_code_attributes(self, authorization, reference_entity_code, **kwargs):  # noqa: E501
        """Get the list of attributes of a given reference entity  # noqa: E501

        This endpoint allows you to get the list of attributes of a given reference entity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reference_entities_code_attributes(authorization, reference_entity_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str reference_entity_code: Code of the reference entity (required)
        :return: list[InlineResponse20021]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_reference_entities_code_attributes_with_http_info(authorization, reference_entity_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_reference_entities_code_attributes_with_http_info(authorization, reference_entity_code, **kwargs)  # noqa: E501
            return data

    def get_reference_entities_code_attributes_with_http_info(self, authorization, reference_entity_code, **kwargs):  # noqa: E501
        """Get the list of attributes of a given reference entity  # noqa: E501

        This endpoint allows you to get the list of attributes of a given reference entity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reference_entities_code_attributes_with_http_info(authorization, reference_entity_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str reference_entity_code: Code of the reference entity (required)
        :return: list[InlineResponse20021]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'reference_entity_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reference_entities_code_attributes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_reference_entities_code_attributes`")  # noqa: E501
        # verify the required parameter 'reference_entity_code' is set
        if ('reference_entity_code' not in params or
                params['reference_entity_code'] is None):
            raise ValueError("Missing the required parameter `reference_entity_code` when calling `get_reference_entities_code_attributes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reference_entity_code' in params:
            path_params['reference_entity_code'] = params['reference_entity_code']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'code', 'message'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/rest/v1/reference-entities/{reference_entity_code}/attributes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20021]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_reference_entity_attributes_code(self, authorization, reference_entity_code, code, **kwargs):  # noqa: E501
        """Get an attribute of a given reference entity  # noqa: E501

        This endpoint allows you to get the information about a given attribute for a given reference entity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reference_entity_attributes_code(authorization, reference_entity_code, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str reference_entity_code: Code of the reference entity (required)
        :param str code: Code of the resource (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_reference_entity_attributes_code_with_http_info(authorization, reference_entity_code, code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_reference_entity_attributes_code_with_http_info(authorization, reference_entity_code, code, **kwargs)  # noqa: E501
            return data

    def get_reference_entity_attributes_code_with_http_info(self, authorization, reference_entity_code, code, **kwargs):  # noqa: E501
        """Get an attribute of a given reference entity  # noqa: E501

        This endpoint allows you to get the information about a given attribute for a given reference entity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reference_entity_attributes_code_with_http_info(authorization, reference_entity_code, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str reference_entity_code: Code of the reference entity (required)
        :param str code: Code of the resource (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'reference_entity_code', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reference_entity_attributes_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_reference_entity_attributes_code`")  # noqa: E501
        # verify the required parameter 'reference_entity_code' is set
        if ('reference_entity_code' not in params or
                params['reference_entity_code'] is None):
            raise ValueError("Missing the required parameter `reference_entity_code` when calling `get_reference_entity_attributes_code`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_reference_entity_attributes_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reference_entity_code' in params:
            path_params['reference_entity_code'] = params['reference_entity_code']  # noqa: E501
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'code', 'message'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/rest/v1/reference-entities/{reference_entity_code}/attributes/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20022',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_reference_entity_attributes_code(self, body, reference_entity_code, code, **kwargs):  # noqa: E501
        """Update/create an attribute of a given reference entity  # noqa: E501

        This endpoint allows you to update a given attribute for a given renference entity. Note that if the attribute does not already exist for the given reference entity, it creates it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_reference_entity_attributes_code(body, reference_entity_code, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AttributesCodeBody1 body: (required)
        :param str reference_entity_code: Code of the reference entity (required)
        :param str code: Code of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_reference_entity_attributes_code_with_http_info(body, reference_entity_code, code, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_reference_entity_attributes_code_with_http_info(body, reference_entity_code, code, **kwargs)  # noqa: E501
            return data

    def patch_reference_entity_attributes_code_with_http_info(self, body, reference_entity_code, code, **kwargs):  # noqa: E501
        """Update/create an attribute of a given reference entity  # noqa: E501

        This endpoint allows you to update a given attribute for a given renference entity. Note that if the attribute does not already exist for the given reference entity, it creates it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_reference_entity_attributes_code_with_http_info(body, reference_entity_code, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AttributesCodeBody1 body: (required)
        :param str reference_entity_code: Code of the reference entity (required)
        :param str code: Code of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'reference_entity_code', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_reference_entity_attributes_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_reference_entity_attributes_code`")  # noqa: E501
        # verify the required parameter 'reference_entity_code' is set
        if ('reference_entity_code' not in params or
                params['reference_entity_code'] is None):
            raise ValueError("Missing the required parameter `reference_entity_code` when calling `patch_reference_entity_attributes_code`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `patch_reference_entity_attributes_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reference_entity_code' in params:
            path_params['reference_entity_code'] = params['reference_entity_code']  # noqa: E501
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'code', 'message', '_links'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/rest/v1/reference-entities/{reference_entity_code}/attributes/{code}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
