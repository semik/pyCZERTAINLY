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

from pyCZERTAINLY.api.acme_account_management_api import ACMEAccountManagementApi


class TestACMEAccountManagementApi(unittest.TestCase):
    """ACMEAccountManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ACMEAccountManagementApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_disable_acme_account(self) -> None:
        """Test case for bulk_disable_acme_account

        Disable multiple ACME Accounts
        """
        pass

    def test_bulk_enable_acme_account(self) -> None:
        """Test case for bulk_enable_acme_account

        Enable multiple ACME Accounts
        """
        pass

    def test_bulk_revoke_acme_account(self) -> None:
        """Test case for bulk_revoke_acme_account

        Revoke multiple ACME Accounts
        """
        pass

    def test_disable_acme_account(self) -> None:
        """Test case for disable_acme_account

        Disable ACME Account
        """
        pass

    def test_enable_acme_account(self) -> None:
        """Test case for enable_acme_account

        Enable ACME Account
        """
        pass

    def test_get_acme_account(self) -> None:
        """Test case for get_acme_account

        Details of ACME Account
        """
        pass

    def test_list_acme_accounts(self) -> None:
        """Test case for list_acme_accounts

        List ACME Accounts
        """
        pass

    def test_revoke_acme_account(self) -> None:
        """Test case for revoke_acme_account

        Revoke ACME Account
        """
        pass


if __name__ == '__main__':
    unittest.main()
