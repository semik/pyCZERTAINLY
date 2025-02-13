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

from pyCZERTAINLY.models.custom_attribute_definition_dto import CustomAttributeDefinitionDto

class TestCustomAttributeDefinitionDto(unittest.TestCase):
    """CustomAttributeDefinitionDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomAttributeDefinitionDto:
        """Test CustomAttributeDefinitionDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomAttributeDefinitionDto`
        """
        model = CustomAttributeDefinitionDto()
        if include_optional:
            return CustomAttributeDefinitionDto(
                uuid = '',
                name = '',
                content_type = 'string',
                description = '',
                enabled = True,
                resources = [
                    'NONE'
                    ]
            )
        else:
            return CustomAttributeDefinitionDto(
                uuid = '',
                name = '',
                content_type = 'string',
                description = '',
                resources = [
                    'NONE'
                    ],
        )
        """

    def testCustomAttributeDefinitionDto(self):
        """Test CustomAttributeDefinitionDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
