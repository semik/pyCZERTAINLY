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

from pyCZERTAINLY.models.certificate_in_location_dto import CertificateInLocationDto

class TestCertificateInLocationDto(unittest.TestCase):
    """CertificateInLocationDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificateInLocationDto:
        """Test CertificateInLocationDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateInLocationDto`
        """
        model = CertificateInLocationDto()
        if include_optional:
            return CertificateInLocationDto(
                certificate_uuid = '',
                state = 'requested',
                validation_status = 'not_checked',
                common_name = '',
                serial_number = '',
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
                push_attributes = [
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
                csr_attributes = [
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
                with_key = True
            )
        else:
            return CertificateInLocationDto(
                certificate_uuid = '',
                state = 'requested',
                validation_status = 'not_checked',
                common_name = '',
                serial_number = '',
        )
        """

    def testCertificateInLocationDto(self):
        """Test CertificateInLocationDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
