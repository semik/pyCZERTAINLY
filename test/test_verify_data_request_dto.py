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

from pyCZERTAINLY.models.verify_data_request_dto import VerifyDataRequestDto

class TestVerifyDataRequestDto(unittest.TestCase):
    """VerifyDataRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VerifyDataRequestDto:
        """Test VerifyDataRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VerifyDataRequestDto`
        """
        model = VerifyDataRequestDto()
        if include_optional:
            return VerifyDataRequestDto(
                signature_attributes = [
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
                data = [
                    pyCZERTAINLY.models.signature_request_data.SignatureRequestData(
                        data = '', 
                        identifier = 'customId', )
                    ],
                signatures = [
                    pyCZERTAINLY.models.signature_request_data.SignatureRequestData(
                        data = '', 
                        identifier = 'customId', )
                    ]
            )
        else:
            return VerifyDataRequestDto(
                signature_attributes = [
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
                data = [
                    pyCZERTAINLY.models.signature_request_data.SignatureRequestData(
                        data = '', 
                        identifier = 'customId', )
                    ],
                signatures = [
                    pyCZERTAINLY.models.signature_request_data.SignatureRequestData(
                        data = '', 
                        identifier = 'customId', )
                    ],
        )
        """

    def testVerifyDataRequestDto(self):
        """Test VerifyDataRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
