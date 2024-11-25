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

from pyCZERTAINLY.models.global_metadata_definition_detail_dto import GlobalMetadataDefinitionDetailDto

class TestGlobalMetadataDefinitionDetailDto(unittest.TestCase):
    """GlobalMetadataDefinitionDetailDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GlobalMetadataDefinitionDetailDto:
        """Test GlobalMetadataDefinitionDetailDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GlobalMetadataDefinitionDetailDto`
        """
        model = GlobalMetadataDefinitionDetailDto()
        if include_optional:
            return GlobalMetadataDefinitionDetailDto(
                uuid = '',
                name = '',
                content_type = 'string',
                description = '',
                enabled = True,
                type = 'data',
                label = 'Attribute Name',
                visible = True,
                group = 'requiredAttributes'
            )
        else:
            return GlobalMetadataDefinitionDetailDto(
                uuid = '',
                name = '',
                content_type = 'string',
                description = '',
                type = 'data',
                label = 'Attribute Name',
        )
        """

    def testGlobalMetadataDefinitionDetailDto(self):
        """Test GlobalMetadataDefinitionDetailDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
