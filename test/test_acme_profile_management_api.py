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

from pyCZERTAINLY.api.acme_profile_management_api import ACMEProfileManagementApi


class TestACMEProfileManagementApi(unittest.TestCase):
    """ACMEProfileManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ACMEProfileManagementApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_delete_acme_profile(self) -> None:
        """Test case for bulk_delete_acme_profile

        Delete multiple ACME Profiles
        """
        pass

    def test_bulk_disable_acme_profile(self) -> None:
        """Test case for bulk_disable_acme_profile

        Disable multiple ACME Profile
        """
        pass

    def test_bulk_enable_acme_profile(self) -> None:
        """Test case for bulk_enable_acme_profile

        Enable multiple ACME Profiles
        """
        pass

    def test_create_acme_profile(self) -> None:
        """Test case for create_acme_profile

        Create ACME Profile
        """
        pass

    def test_delete_acme_profile(self) -> None:
        """Test case for delete_acme_profile

        Delete ACME Profile
        """
        pass

    def test_disable_acme_profile(self) -> None:
        """Test case for disable_acme_profile

        Disable ACME Profile
        """
        pass

    def test_edit_acme_profile(self) -> None:
        """Test case for edit_acme_profile

        Edit ACME Profile
        """
        pass

    def test_enable_acme_profile(self) -> None:
        """Test case for enable_acme_profile

        Enable ACME Profile
        """
        pass

    def test_force_delete_acme_profiles(self) -> None:
        """Test case for force_delete_acme_profiles

        Force delete multiple ACME Profiles
        """
        pass

    def test_get_acme_profile(self) -> None:
        """Test case for get_acme_profile

        Get details of ACME Profile
        """
        pass

    def test_list_acme_profiles(self) -> None:
        """Test case for list_acme_profiles

        Get list of ACME Profiles
        """
        pass

    def test_update_ra_profile2(self) -> None:
        """Test case for update_ra_profile2

        Update RA Profile for ACME Profile
        """
        pass


if __name__ == '__main__':
    unittest.main()
