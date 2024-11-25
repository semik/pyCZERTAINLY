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

from openapi_client.models.metadata_attribute_properties import MetadataAttributeProperties

class TestMetadataAttributeProperties(unittest.TestCase):
    """MetadataAttributeProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataAttributeProperties:
        """Test MetadataAttributeProperties
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetadataAttributeProperties`
        """
        model = MetadataAttributeProperties()
        if include_optional:
            return MetadataAttributeProperties(
                label = 'Attribute Name',
                visible = True,
                group = 'requiredAttributes',
                var_global = True,
                overwrite = True
            )
        else:
            return MetadataAttributeProperties(
                label = 'Attribute Name',
                visible = True,
        )
        """

    def testMetadataAttributeProperties(self):
        """Test MetadataAttributeProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
