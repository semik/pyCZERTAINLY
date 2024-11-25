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

from openapi_client.models.add_location_request_dto import AddLocationRequestDto

class TestAddLocationRequestDto(unittest.TestCase):
    """AddLocationRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddLocationRequestDto:
        """Test AddLocationRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddLocationRequestDto`
        """
        model = AddLocationRequestDto()
        if include_optional:
            return AddLocationRequestDto(
                name = '',
                description = '',
                attributes = [
                    openapi_client.models.request_attribute_dto.RequestAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        content_type = 'string', 
                        content = [
                            openapi_client.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = openapi_client.models.data.data(), )
                            ], )
                    ],
                custom_attributes = [
                    openapi_client.models.request_attribute_dto.RequestAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        content_type = 'string', 
                        content = [
                            openapi_client.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = openapi_client.models.data.data(), )
                            ], )
                    ],
                enabled = True
            )
        else:
            return AddLocationRequestDto(
                name = '',
                attributes = [
                    openapi_client.models.request_attribute_dto.RequestAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        content_type = 'string', 
                        content = [
                            openapi_client.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = openapi_client.models.data.data(), )
                            ], )
                    ],
        )
        """

    def testAddLocationRequestDto(self):
        """Test AddLocationRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
