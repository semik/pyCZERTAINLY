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

from openapi_client.models.metadata_attribute import MetadataAttribute

class TestMetadataAttribute(unittest.TestCase):
    """MetadataAttribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataAttribute:
        """Test MetadataAttribute
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetadataAttribute`
        """
        model = MetadataAttribute()
        if include_optional:
            return MetadataAttribute(
                uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003',
                name = 'Attribute',
                description = '',
                content = [
                    openapi_client.models.base_attribute_content_dto.BaseAttributeContentDto(
                        reference = '', 
                        data = openapi_client.models.data.data(), )
                    ],
                type = 'data',
                content_type = 'string',
                properties = openapi_client.models.metadata_attribute_properties.MetadataAttributeProperties(
                    label = 'Attribute Name', 
                    visible = True, 
                    group = 'requiredAttributes', 
                    global = True, 
                    overwrite = True, )
            )
        else:
            return MetadataAttribute(
                uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003',
                name = 'Attribute',
                content = [
                    openapi_client.models.base_attribute_content_dto.BaseAttributeContentDto(
                        reference = '', 
                        data = openapi_client.models.data.data(), )
                    ],
                type = 'data',
                content_type = 'string',
                properties = openapi_client.models.metadata_attribute_properties.MetadataAttributeProperties(
                    label = 'Attribute Name', 
                    visible = True, 
                    group = 'requiredAttributes', 
                    global = True, 
                    overwrite = True, ),
        )
        """

    def testMetadataAttribute(self):
        """Test MetadataAttribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
