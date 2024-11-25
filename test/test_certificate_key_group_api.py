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

from openapi_client.api.certificate_key_group_api import CertificateKeyGroupApi


class TestCertificateKeyGroupApi(unittest.TestCase):
    """CertificateKeyGroupApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CertificateKeyGroupApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_delete_group(self) -> None:
        """Test case for bulk_delete_group

        Delete multiple Groups
        """
        pass

    def test_create_group(self) -> None:
        """Test case for create_group

        Create Group
        """
        pass

    def test_delete_group(self) -> None:
        """Test case for delete_group

        Delete Group
        """
        pass

    def test_edit_group(self) -> None:
        """Test case for edit_group

        Edit Group
        """
        pass

    def test_get_group(self) -> None:
        """Test case for get_group

        Group details
        """
        pass

    def test_list_groups(self) -> None:
        """Test case for list_groups

        List Groups
        """
        pass


if __name__ == '__main__':
    unittest.main()
