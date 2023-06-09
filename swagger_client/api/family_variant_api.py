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


class FamilyVariantApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_families_family_code_variants(self, authorization, family_code, **kwargs):  # noqa: E501
        """Get list of family variants  # noqa: E501

        This endpoint allows you to get a list of family variants. Family variants are paginated and sorted by code.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_families_family_code_variants(authorization, family_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str family_code: Code of the family (required)
        :param int page: Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
        :param int limit: Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
        :param bool with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
        :return: FamilyVariants
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_families_family_code_variants_with_http_info(authorization, family_code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_families_family_code_variants_with_http_info(authorization, family_code, **kwargs)  # noqa: E501
            return data

    def get_families_family_code_variants_with_http_info(self, authorization, family_code, **kwargs):  # noqa: E501
        """Get list of family variants  # noqa: E501

        This endpoint allows you to get a list of family variants. Family variants are paginated and sorted by code.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_families_family_code_variants_with_http_info(authorization, family_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str family_code: Code of the family (required)
        :param int page: Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
        :param int limit: Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
        :param bool with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
        :return: FamilyVariants
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'family_code', 'page', 'limit', 'with_count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_families_family_code_variants" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_families_family_code_variants`")  # noqa: E501
        # verify the required parameter 'family_code' is set
        if ('family_code' not in params or
                params['family_code'] is None):
            raise ValueError("Missing the required parameter `family_code` when calling `get_families_family_code_variants`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'family_code' in params:
            path_params['family_code'] = params['family_code']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'with_count' in params:
            query_params.append(('with_count', params['with_count']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'code', 'labels', 'variant_attribute_sets', 'message'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/rest/v1/families/{family_code}/variants', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FamilyVariants',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_families_family_code_variants_code(self, authorization, family_code, code, **kwargs):  # noqa: E501
        """Get a family variant  # noqa: E501

        This endpoint allows you to get the information about a given family variant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_families_family_code_variants_code(authorization, family_code, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str family_code: Code of the family (required)
        :param str code: Code of the resource (required)
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_families_family_code_variants_code_with_http_info(authorization, family_code, code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_families_family_code_variants_code_with_http_info(authorization, family_code, code, **kwargs)  # noqa: E501
            return data

    def get_families_family_code_variants_code_with_http_info(self, authorization, family_code, code, **kwargs):  # noqa: E501
        """Get a family variant  # noqa: E501

        This endpoint allows you to get the information about a given family variant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_families_family_code_variants_code_with_http_info(authorization, family_code, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Equal to 'Bearer xx', where 'xx' is the access token. (required)
        :param str family_code: Code of the family (required)
        :param str code: Code of the resource (required)
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'family_code', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_families_family_code_variants_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_families_family_code_variants_code`")  # noqa: E501
        # verify the required parameter 'family_code' is set
        if ('family_code' not in params or
                params['family_code'] is None):
            raise ValueError("Missing the required parameter `family_code` when calling `get_families_family_code_variants_code`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_families_family_code_variants_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'family_code' in params:
            path_params['family_code'] = params['family_code']  # noqa: E501
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
            '/api/rest/v1/families/{family_code}/variants/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_families_family_code_variants(self, family_code, **kwargs):  # noqa: E501
        """Update/create several family variants  # noqa: E501

        This endpoint allows you to update and/or create several family variants at once, for a given family.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_families_family_code_variants(family_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str family_code: Code of the family (required)
        :param FamilyCodeVariantsBody1 body:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_families_family_code_variants_with_http_info(family_code, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_families_family_code_variants_with_http_info(family_code, **kwargs)  # noqa: E501
            return data

    def patch_families_family_code_variants_with_http_info(self, family_code, **kwargs):  # noqa: E501
        """Update/create several family variants  # noqa: E501

        This endpoint allows you to update and/or create several family variants at once, for a given family.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_families_family_code_variants_with_http_info(family_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str family_code: Code of the family (required)
        :param FamilyCodeVariantsBody1 body:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['family_code', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_families_family_code_variants" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'family_code' is set
        if ('family_code' not in params or
                params['family_code'] is None):
            raise ValueError("Missing the required parameter `family_code` when calling `patch_families_family_code_variants`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'family_code' in params:
            path_params['family_code'] = params['family_code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'x-example-1', 'x-example-2', 'x-example-3', 'code', 'message'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/rest/v1/families/{family_code}/variants', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_families_family_code_variants_code(self, body, family_code, code, **kwargs):  # noqa: E501
        """Update/create a family variant  # noqa: E501

        This endpoint allows you to update a given family variant. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no family variant exists for the given code, it creates it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_families_family_code_variants_code(body, family_code, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VariantsCodeBody body: (required)
        :param str family_code: Code of the family (required)
        :param str code: Code of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_families_family_code_variants_code_with_http_info(body, family_code, code, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_families_family_code_variants_code_with_http_info(body, family_code, code, **kwargs)  # noqa: E501
            return data

    def patch_families_family_code_variants_code_with_http_info(self, body, family_code, code, **kwargs):  # noqa: E501
        """Update/create a family variant  # noqa: E501

        This endpoint allows you to update a given family variant. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no family variant exists for the given code, it creates it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_families_family_code_variants_code_with_http_info(body, family_code, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VariantsCodeBody body: (required)
        :param str family_code: Code of the family (required)
        :param str code: Code of the resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'family_code', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_families_family_code_variants_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_families_family_code_variants_code`")  # noqa: E501
        # verify the required parameter 'family_code' is set
        if ('family_code' not in params or
                params['family_code'] is None):
            raise ValueError("Missing the required parameter `family_code` when calling `patch_families_family_code_variants_code`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `patch_families_family_code_variants_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'family_code' in params:
            path_params['family_code'] = params['family_code']  # noqa: E501
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
            '/api/rest/v1/families/{family_code}/variants/{code}', 'PATCH',
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
