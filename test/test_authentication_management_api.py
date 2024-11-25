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

from openapi_client.api.authentication_management_api import AuthenticationManagementApi


class TestAuthenticationManagementApi(unittest.TestCase):
    """AuthenticationManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthenticationManagementApi()

    def tearDown(self) -> None:
        pass

    def test_get_auth_resources(self) -> None:
        """Test case for get_auth_resources

        Get Auth Resources
        """
        pass

    def test_get_objects_for_resource(self) -> None:
        """Test case for get_objects_for_resource

        Get List of objects for Object Access
        """
        pass

    def test_profile(self) -> None:
        """Test case for profile

        Profile Authorization
        """
        pass

    def test_update_user_profile(self) -> None:
        """Test case for update_user_profile

        Update User Profile
        """
        pass


if __name__ == '__main__':
    unittest.main()
