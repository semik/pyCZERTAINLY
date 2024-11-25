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

from pyCZERTAINLY.api.authority_management_api import AuthorityManagementApi


class TestAuthorityManagementApi(unittest.TestCase):
    """AuthorityManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthorityManagementApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_delete_authority_instance(self) -> None:
        """Test case for bulk_delete_authority_instance

        Delete multiple Authority instances
        """
        pass

    def test_create_authority_instance(self) -> None:
        """Test case for create_authority_instance

        Add Authority instance
        """
        pass

    def test_delete_authority_instance(self) -> None:
        """Test case for delete_authority_instance

        Delete Authority instance
        """
        pass

    def test_edit_authority_instance(self) -> None:
        """Test case for edit_authority_instance

        Edit Authority instance
        """
        pass

    def test_force_delete_authority_instances(self) -> None:
        """Test case for force_delete_authority_instances

        Force delete multiple Authority instances
        """
        pass

    def test_get_authority_instance(self) -> None:
        """Test case for get_authority_instance

        Details of an Authority instance
        """
        pass

    def test_list_authority_instances(self) -> None:
        """Test case for list_authority_instances

        List of available Authority instances
        """
        pass

    def test_list_cas_in_profile(self) -> None:
        """Test case for list_cas_in_profile

        """
        pass

    def test_list_certificate_profiles(self) -> None:
        """Test case for list_certificate_profiles

        """
        pass

    def test_list_entity_profiles(self) -> None:
        """Test case for list_entity_profiles

        """
        pass

    def test_list_ra_profile_attributes(self) -> None:
        """Test case for list_ra_profile_attributes

        List RA Profile Attributes
        """
        pass

    def test_validate_ra_profile_attributes(self) -> None:
        """Test case for validate_ra_profile_attributes

        Validate RA Profile Attributes
        """
        pass


if __name__ == '__main__':
    unittest.main()
