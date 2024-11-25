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

from pyCZERTAINLY.models.compliance_rules_response_dto import ComplianceRulesResponseDto

class TestComplianceRulesResponseDto(unittest.TestCase):
    """ComplianceRulesResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComplianceRulesResponseDto:
        """Test ComplianceRulesResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComplianceRulesResponseDto`
        """
        model = ComplianceRulesResponseDto()
        if include_optional:
            return ComplianceRulesResponseDto(
                uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003',
                group_uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003',
                name = 'Rule1',
                certificate_type = 'X.509',
                attributes = [
                    pyCZERTAINLY.models.base_attribute_dto.BaseAttributeDto(
                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                        name = 'Attribute', 
                        description = '', 
                        type = 'data', 
                        content = pyCZERTAINLY.models.content.content(), )
                    ],
                description = 'Sample rule description'
            )
        else:
            return ComplianceRulesResponseDto(
                uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003',
                name = 'Rule1',
                certificate_type = 'X.509',
        )
        """

    def testComplianceRulesResponseDto(self):
        """Test ComplianceRulesResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
