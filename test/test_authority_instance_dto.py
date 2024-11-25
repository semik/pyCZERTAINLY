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

from openapi_client.models.authority_instance_dto import AuthorityInstanceDto

class TestAuthorityInstanceDto(unittest.TestCase):
    """AuthorityInstanceDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthorityInstanceDto:
        """Test AuthorityInstanceDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthorityInstanceDto`
        """
        model = AuthorityInstanceDto()
        if include_optional:
            return AuthorityInstanceDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                attributes = [
                    openapi_client.models.response_attribute_dto.ResponseAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        label = 'Attribute Name', 
                        type = 'data', 
                        content_type = 'string', 
                        content = [
                            openapi_client.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = openapi_client.models.data.data(), )
                            ], )
                    ],
                custom_attributes = [
                    openapi_client.models.response_attribute_dto.ResponseAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        label = 'Attribute Name', 
                        type = 'data', 
                        content_type = 'string', 
                        content = [
                            openapi_client.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = openapi_client.models.data.data(), )
                            ], )
                    ],
                status = '',
                connector_uuid = '',
                connector_name = '',
                kind = 'LegacyEjbca, ADCS, etc.'
            )
        else:
            return AuthorityInstanceDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                attributes = [
                    openapi_client.models.response_attribute_dto.ResponseAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        label = 'Attribute Name', 
                        type = 'data', 
                        content_type = 'string', 
                        content = [
                            openapi_client.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = openapi_client.models.data.data(), )
                            ], )
                    ],
                status = '',
                connector_uuid = '',
                connector_name = '',
                kind = 'LegacyEjbca, ADCS, etc.',
        )
        """

    def testAuthorityInstanceDto(self):
        """Test AuthorityInstanceDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
