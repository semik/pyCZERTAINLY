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

from openapi_client.api.external_notification_management_api import ExternalNotificationManagementApi


class TestExternalNotificationManagementApi(unittest.TestCase):
    """ExternalNotificationManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExternalNotificationManagementApi()

    def tearDown(self) -> None:
        pass

    def test_create_notification_instance(self) -> None:
        """Test case for create_notification_instance

        Add Notification instance
        """
        pass

    def test_delete_notification_instance(self) -> None:
        """Test case for delete_notification_instance

        Delete Notification instance
        """
        pass

    def test_edit_notification_instance(self) -> None:
        """Test case for edit_notification_instance

        Edit Notification instance
        """
        pass

    def test_get_notification_instance(self) -> None:
        """Test case for get_notification_instance

        Details of an Notification instance
        """
        pass

    def test_list_mapping_attributes(self) -> None:
        """Test case for list_mapping_attributes

        List of mapping attributes
        """
        pass

    def test_list_notification_instances(self) -> None:
        """Test case for list_notification_instances

        List of available Notification instances
        """
        pass


if __name__ == '__main__':
    unittest.main()
