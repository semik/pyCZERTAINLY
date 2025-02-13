# coding: utf-8

"""
    CZERTAINLY Core API

    REST API for CZERTAINLY Core

    The version of the OpenAPI document: 2.13.2-SNAPSHOT
    Contact: info@czertainly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyCZERTAINLY.api.connector_authentication_api import ConnectorAuthenticationApi


class TestConnectorAuthenticationApi(unittest.TestCase):
    """ConnectorAuthenticationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorAuthenticationApi()

    def tearDown(self) -> None:
        pass

    def test_get_api_key_auth_attributes(self) -> None:
        """Test case for get_api_key_auth_attributes

        Get API Key auth Attributes
        """
        pass

    def test_get_authentication_types(self) -> None:
        """Test case for get_authentication_types

        Get list of Authentication Types
        """
        pass

    def test_get_basic_auth_attributes(self) -> None:
        """Test case for get_basic_auth_attributes

        Get basic auth Attributes
        """
        pass

    def test_get_certificate_attributes(self) -> None:
        """Test case for get_certificate_attributes

        Get Attributes for certificate auth
        """
        pass

    def test_get_jwt_auth_attributes(self) -> None:
        """Test case for get_jwt_auth_attributes

        Get JWT auth Attributes
        """
        pass

    def test_validate_api_key_auth_attributes(self) -> None:
        """Test case for validate_api_key_auth_attributes

        Validate API Key Attributes
        """
        pass

    def test_validate_basic_auth_attributes(self) -> None:
        """Test case for validate_basic_auth_attributes

        Validate basic auth Attributes
        """
        pass

    def test_validate_certificate_attributes(self) -> None:
        """Test case for validate_certificate_attributes

        Validate certificate auth Attributes
        """
        pass

    def test_validate_jwt_auth_attributes(self) -> None:
        """Test case for validate_jwt_auth_attributes

        Validate JWT auth Attributes
        """
        pass


if __name__ == '__main__':
    unittest.main()
