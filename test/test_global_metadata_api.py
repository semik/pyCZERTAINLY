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

from pyCZERTAINLY.api.global_metadata_api import GlobalMetadataApi


class TestGlobalMetadataApi(unittest.TestCase):
    """GlobalMetadataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GlobalMetadataApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_delete_global_metadata(self) -> None:
        """Test case for bulk_delete_global_metadata

        Delete multiple Global Metadata
        """
        pass

    def test_create_global_metadata(self) -> None:
        """Test case for create_global_metadata

        Create Global Metadata
        """
        pass

    def test_delete_global_metadata(self) -> None:
        """Test case for delete_global_metadata

        Delete Global Metadata
        """
        pass

    def test_edit_global_metadata(self) -> None:
        """Test case for edit_global_metadata

        Edit Global Metadata
        """
        pass

    def test_get_connector_metadata(self) -> None:
        """Test case for get_connector_metadata

        Get Available Connector Metadata
        """
        pass

    def test_get_global_metadata(self) -> None:
        """Test case for get_global_metadata

        Global Metadata details
        """
        pass

    def test_list_global_metadata(self) -> None:
        """Test case for list_global_metadata

        List Global Metadata
        """
        pass

    def test_promote_connector_metadata(self) -> None:
        """Test case for promote_connector_metadata

        Promote Connector Metadata to Global Metadata
        """
        pass


if __name__ == '__main__':
    unittest.main()
