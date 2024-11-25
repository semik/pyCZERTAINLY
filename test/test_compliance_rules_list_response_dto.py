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

from openapi_client.models.compliance_rules_list_response_dto import ComplianceRulesListResponseDto

class TestComplianceRulesListResponseDto(unittest.TestCase):
    """ComplianceRulesListResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComplianceRulesListResponseDto:
        """Test ComplianceRulesListResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComplianceRulesListResponseDto`
        """
        model = ComplianceRulesListResponseDto()
        if include_optional:
            return ComplianceRulesListResponseDto(
                connector_name = 'Provider1',
                connector_uuid = 'c35bc88c-d0ef-11ec-9d64-0242ac120003',
                kind = 'Kind1',
                rules = [
                    openapi_client.models.compliance_rules_response_dto.ComplianceRulesResponseDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        group_uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Rule1', 
                        certificate_type = 'X.509', 
                        attributes = [
                            openapi_client.models.base_attribute_dto.BaseAttributeDto(
                                uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                name = 'Attribute', 
                                description = '', 
                                type = 'data', 
                                content = openapi_client.models.content.content(), )
                            ], 
                        description = 'Sample rule description', )
                    ]
            )
        else:
            return ComplianceRulesListResponseDto(
                connector_name = 'Provider1',
                connector_uuid = 'c35bc88c-d0ef-11ec-9d64-0242ac120003',
                kind = 'Kind1',
                rules = [
                    openapi_client.models.compliance_rules_response_dto.ComplianceRulesResponseDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        group_uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Rule1', 
                        certificate_type = 'X.509', 
                        attributes = [
                            openapi_client.models.base_attribute_dto.BaseAttributeDto(
                                uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                name = 'Attribute', 
                                description = '', 
                                type = 'data', 
                                content = openapi_client.models.content.content(), )
                            ], 
                        description = 'Sample rule description', )
                    ],
        )
        """

    def testComplianceRulesListResponseDto(self):
        """Test ComplianceRulesListResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
