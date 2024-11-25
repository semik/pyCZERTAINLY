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

from openapi_client.api.audit_log_api import AuditLogApi


class TestAuditLogApi(unittest.TestCase):
    """AuditLogApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuditLogApi()

    def tearDown(self) -> None:
        pass

    def test_export_audit_logs(self) -> None:
        """Test case for export_audit_logs

        Export Audit logs
        """
        pass

    def test_get_searchable_field_information5(self) -> None:
        """Test case for get_searchable_field_information5

        Get Audit logs searchable fields information
        """
        pass

    def test_list_audit_logs(self) -> None:
        """Test case for list_audit_logs

        List Audit logs
        """
        pass

    def test_purge_audit_logs(self) -> None:
        """Test case for purge_audit_logs

        Purge Audit logs
        """
        pass


if __name__ == '__main__':
    unittest.main()
