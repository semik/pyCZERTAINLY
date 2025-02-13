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

from pyCZERTAINLY.api.location_management_api import LocationManagementApi


class TestLocationManagementApi(unittest.TestCase):
    """LocationManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LocationManagementApi()

    def tearDown(self) -> None:
        pass

    def test_add_location(self) -> None:
        """Test case for add_location

        Add Location
        """
        pass

    def test_delete_location(self) -> None:
        """Test case for delete_location

        Delete Location
        """
        pass

    def test_disable_location(self) -> None:
        """Test case for disable_location

        Disable Location
        """
        pass

    def test_edit_location(self) -> None:
        """Test case for edit_location

        Edit Location
        """
        pass

    def test_enable_location(self) -> None:
        """Test case for enable_location

        Enable Location
        """
        pass

    def test_get_location(self) -> None:
        """Test case for get_location

        Get Location Details
        """
        pass

    def test_get_searchable_field_information(self) -> None:
        """Test case for get_searchable_field_information

        Get Locations searchable fields information
        """
        pass

    def test_issue_certificate_to_location(self) -> None:
        """Test case for issue_certificate_to_location

        Issue Certificate to Location
        """
        pass

    def test_list_csr_attributes(self) -> None:
        """Test case for list_csr_attributes

        Get CSR Attributes
        """
        pass

    def test_list_locations(self) -> None:
        """Test case for list_locations

        List Locations
        """
        pass

    def test_list_push_attributes(self) -> None:
        """Test case for list_push_attributes

        Get push Attributes
        """
        pass

    def test_push_certificate(self) -> None:
        """Test case for push_certificate

        Push Certificate to Location
        """
        pass

    def test_remove_certificate(self) -> None:
        """Test case for remove_certificate

        Remove Certificate from Location
        """
        pass

    def test_renew_certificate_in_location(self) -> None:
        """Test case for renew_certificate_in_location

        Renew Certificate in Location
        """
        pass

    def test_update_location_content(self) -> None:
        """Test case for update_location_content

        Sync Location content
        """
        pass


if __name__ == '__main__':
    unittest.main()
