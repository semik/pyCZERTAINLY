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

from pyCZERTAINLY.api.role_management_api import RoleManagementApi


class TestRoleManagementApi(unittest.TestCase):
    """RoleManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RoleManagementApi()

    def tearDown(self) -> None:
        pass

    def test_add_resource_permission_objects(self) -> None:
        """Test case for add_resource_permission_objects

        Add Resource Objects to a Role
        """
        pass

    def test_create_role(self) -> None:
        """Test case for create_role

        Create Role
        """
        pass

    def test_delete_role(self) -> None:
        """Test case for delete_role

        Delete Role
        """
        pass

    def test_get_resource_permission_objects(self) -> None:
        """Test case for get_resource_permission_objects

        Get Resource Objects of a Role
        """
        pass

    def test_get_role(self) -> None:
        """Test case for get_role

        Get role details
        """
        pass

    def test_get_role_permissions(self) -> None:
        """Test case for get_role_permissions

        Get Permissions of a Role
        """
        pass

    def test_get_role_resource_permissions(self) -> None:
        """Test case for get_role_resource_permissions

        Get Resources of a Role
        """
        pass

    def test_get_role_users(self) -> None:
        """Test case for get_role_users

        Get Role Users
        """
        pass

    def test_list_roles(self) -> None:
        """Test case for list_roles

        List Roles
        """
        pass

    def test_remove_resource_permission_objects(self) -> None:
        """Test case for remove_resource_permission_objects

        Update Resource Objects to a Role
        """
        pass

    def test_save_permissions(self) -> None:
        """Test case for save_permissions

        Add permissions to Role
        """
        pass

    def test_update_resource_permission_objects(self) -> None:
        """Test case for update_resource_permission_objects

        Update Resource Objects to a Role
        """
        pass

    def test_update_role(self) -> None:
        """Test case for update_role

        Update Role
        """
        pass

    def test_update_users(self) -> None:
        """Test case for update_users

        Add users to Role
        """
        pass


if __name__ == '__main__':
    unittest.main()
