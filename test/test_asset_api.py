# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.asset_api import AssetApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAssetApi(unittest.TestCase):
    """AssetApi unit test stubs"""

    def setUp(self):
        self.api = AssetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_assets_code(self):
        """Test case for delete_assets_code

        Delete an asset  # noqa: E501
        """
        pass

    def test_get_assets(self):
        """Test case for get_assets

        Get the list of the assets of a given asset family  # noqa: E501
        """
        pass

    def test_get_assets_code(self):
        """Test case for get_assets_code

        Get an asset of a given asset family  # noqa: E501
        """
        pass

    def test_patch_asset_code(self):
        """Test case for patch_asset_code

        Update/create an asset  # noqa: E501
        """
        pass

    def test_patch_assets(self):
        """Test case for patch_assets

        Update/create several assets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
