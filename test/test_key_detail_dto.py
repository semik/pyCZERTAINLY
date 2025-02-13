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

from pyCZERTAINLY.models.key_detail_dto import KeyDetailDto

class TestKeyDetailDto(unittest.TestCase):
    """KeyDetailDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeyDetailDto:
        """Test KeyDetailDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeyDetailDto`
        """
        model = KeyDetailDto()
        if include_optional:
            return KeyDetailDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                description = '',
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                token_profile_uuid = '',
                token_profile_name = '',
                token_instance_uuid = '',
                token_instance_name = '',
                custom_attributes = [
                    pyCZERTAINLY.models.response_attribute_dto.ResponseAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        label = 'Attribute Name', 
                        type = 'data', 
                        content_type = 'string', 
                        content = [
                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = pyCZERTAINLY.models.data.data(), )
                            ], )
                    ],
                attributes = [
                    pyCZERTAINLY.models.response_attribute_dto.ResponseAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        label = 'Attribute Name', 
                        type = 'data', 
                        content_type = 'string', 
                        content = [
                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = pyCZERTAINLY.models.data.data(), )
                            ], )
                    ],
                owner = '',
                owner_uuid = '',
                groups = [
                    pyCZERTAINLY.models.group_dto.GroupDto(
                        uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                        name = 'Name', 
                        description = '', 
                        email = '', 
                        custom_attributes = [
                            pyCZERTAINLY.models.response_attribute_dto.ResponseAttributeDto(
                                uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                name = 'Attribute', 
                                label = 'Attribute Name', 
                                type = 'data', 
                                content_type = 'string', 
                                content = [
                                    pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                        reference = '', 
                                        data = pyCZERTAINLY.models.data.data(), )
                                    ], )
                            ], )
                    ],
                items = [
                    pyCZERTAINLY.models.key_item_detail_dto.KeyItemDetailDto(
                        uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                        name = 'Name', 
                        key_reference_uuid = '', 
                        type = 'Secret', 
                        key_algorithm = 'RSA', 
                        format = 'Raw', 
                        key_data = '', 
                        length = 56, 
                        metadata = [
                            pyCZERTAINLY.models.metadata_response_dto.MetadataResponseDto(
                                connector_uuid = '', 
                                connector_name = '', 
                                source_object_type = 'NONE', 
                                items = [
                                    pyCZERTAINLY.models.response_metadata_dto.ResponseMetadataDto(
                                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                        name = 'Attribute', 
                                        label = 'Attribute Name', 
                                        type = 'data', 
                                        content_type = 'string', 
                                        content = [
                                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                                reference = '', 
                                                data = pyCZERTAINLY.models.data.data(), )
                                            ], 
                                        source_objects = [
                                            pyCZERTAINLY.models.name_and_uuid_dto.NameAndUuidDto(
                                                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                                name = 'Name', )
                                            ], )
                                    ], )
                            ], 
                        usage = [
                            'sign'
                            ], 
                        enabled = True, 
                        state = 'pre-active', 
                        reason = 'disclosure', )
                    ],
                associations = [
                    pyCZERTAINLY.models.key_association_dto.KeyAssociationDto(
                        uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                        name = 'Name', 
                        resource = 'NONE', )
                    ]
            )
        else:
            return KeyDetailDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                description = '',
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                token_instance_uuid = '',
                token_instance_name = '',
                attributes = [
                    pyCZERTAINLY.models.response_attribute_dto.ResponseAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        label = 'Attribute Name', 
                        type = 'data', 
                        content_type = 'string', 
                        content = [
                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = pyCZERTAINLY.models.data.data(), )
                            ], )
                    ],
                items = [
                    pyCZERTAINLY.models.key_item_detail_dto.KeyItemDetailDto(
                        uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                        name = 'Name', 
                        key_reference_uuid = '', 
                        type = 'Secret', 
                        key_algorithm = 'RSA', 
                        format = 'Raw', 
                        key_data = '', 
                        length = 56, 
                        metadata = [
                            pyCZERTAINLY.models.metadata_response_dto.MetadataResponseDto(
                                connector_uuid = '', 
                                connector_name = '', 
                                source_object_type = 'NONE', 
                                items = [
                                    pyCZERTAINLY.models.response_metadata_dto.ResponseMetadataDto(
                                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                        name = 'Attribute', 
                                        label = 'Attribute Name', 
                                        type = 'data', 
                                        content_type = 'string', 
                                        content = [
                                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                                reference = '', 
                                                data = pyCZERTAINLY.models.data.data(), )
                                            ], 
                                        source_objects = [
                                            pyCZERTAINLY.models.name_and_uuid_dto.NameAndUuidDto(
                                                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                                name = 'Name', )
                                            ], )
                                    ], )
                            ], 
                        usage = [
                            'sign'
                            ], 
                        enabled = True, 
                        state = 'pre-active', 
                        reason = 'disclosure', )
                    ],
        )
        """

    def testKeyDetailDto(self):
        """Test KeyDetailDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
