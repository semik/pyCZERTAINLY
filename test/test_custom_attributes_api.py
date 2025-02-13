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

from pyCZERTAINLY.api.custom_attributes_api import CustomAttributesApi


class TestCustomAttributesApi(unittest.TestCase):
    """CustomAttributesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CustomAttributesApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_delete_custom_attributes(self) -> None:
        """Test case for bulk_delete_custom_attributes

        Delete multiple Custom Attributes
        """
        pass

    def test_bulk_disable_custom_attributes(self) -> None:
        """Test case for bulk_disable_custom_attributes

        Disable multiple Custom Attributes
        """
        pass

    def test_bulk_enable_custom_attributes(self) -> None:
        """Test case for bulk_enable_custom_attributes

        Enable multiple Custom Attributes
        """
        pass

    def test_create_custom_attribute(self) -> None:
        """Test case for create_custom_attribute

        Create Custom Attribute
        """
        pass

    def test_delete_attribute_content_for_resource(self) -> None:
        """Test case for delete_attribute_content_for_resource

        Delete Value of a Custom Attribute for a Resource
        """
        pass

    def test_delete_custom_attribute(self) -> None:
        """Test case for delete_custom_attribute

        Delete Custom Attribute
        """
        pass

    def test_disable_custom_attribute(self) -> None:
        """Test case for disable_custom_attribute

        Disable Custom Attribute
        """
        pass

    def test_edit_custom_attribute(self) -> None:
        """Test case for edit_custom_attribute

        Edit Custom Attribute
        """
        pass

    def test_enable_custom_attribute(self) -> None:
        """Test case for enable_custom_attribute

        Enable Custom Attribute
        """
        pass

    def test_get_custom_attribute(self) -> None:
        """Test case for get_custom_attribute

        Custom Attribute details
        """
        pass

    def test_get_resource_custom_attributes(self) -> None:
        """Test case for get_resource_custom_attributes

        Get Custom Attributes for a resource
        """
        pass

    def test_get_resources(self) -> None:
        """Test case for get_resources

        Get available resources for Custom Attributes
        """
        pass

    def test_list_custom_attributes(self) -> None:
        """Test case for list_custom_attributes

        List Custom Attributes
        """
        pass

    def test_update_attribute_content_for_resource(self) -> None:
        """Test case for update_attribute_content_for_resource

        Update Value of a Custom Attribute for a Resource
        """
        pass

    def test_update_resources(self) -> None:
        """Test case for update_resources

        Associate Custom Attribute to Resource
        """
        pass


if __name__ == '__main__':
    unittest.main()
