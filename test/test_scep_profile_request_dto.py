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

from pyCZERTAINLY.models.scep_profile_request_dto import ScepProfileRequestDto

class TestScepProfileRequestDto(unittest.TestCase):
    """ScepProfileRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScepProfileRequestDto:
        """Test ScepProfileRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScepProfileRequestDto`
        """
        model = ScepProfileRequestDto()
        if include_optional:
            return ScepProfileRequestDto(
                description = 'Sample description',
                ra_profile_uuid = '6b55de1c-844f-11ec-a8a3-0242ac120002',
                issue_certificate_attributes = [
                    pyCZERTAINLY.models.request_attribute_dto.RequestAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        content_type = 'string', 
                        content = [
                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = pyCZERTAINLY.models.data.data(), )
                            ], )
                    ],
                ca_certificate_uuid = '',
                custom_attributes = [
                    pyCZERTAINLY.models.request_attribute_dto.RequestAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        content_type = 'string', 
                        content = [
                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = pyCZERTAINLY.models.data.data(), )
                            ], )
                    ],
                renewal_threshold = 56,
                include_ca_certificate = True,
                include_ca_certificate_chain = True,
                challenge_password = '',
                enable_intune = True,
                intune_tenant = '',
                intune_application_id = '',
                intune_application_key = '',
                name = 'Profile Name 1'
            )
        else:
            return ScepProfileRequestDto(
                issue_certificate_attributes = [
                    pyCZERTAINLY.models.request_attribute_dto.RequestAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        content_type = 'string', 
                        content = [
                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                reference = '', 
                                data = pyCZERTAINLY.models.data.data(), )
                            ], )
                    ],
                ca_certificate_uuid = '',
                name = 'Profile Name 1',
        )
        """

    def testScepProfileRequestDto(self):
        """Test ScepProfileRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
