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

from pyCZERTAINLY.models.compliance_profile_rule_dto import ComplianceProfileRuleDto

class TestComplianceProfileRuleDto(unittest.TestCase):
    """ComplianceProfileRuleDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComplianceProfileRuleDto:
        """Test ComplianceProfileRuleDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComplianceProfileRuleDto`
        """
        model = ComplianceProfileRuleDto()
        if include_optional:
            return ComplianceProfileRuleDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                description = 'Sample rule description',
                connector_name = '',
                connector_uuid = '',
                kind = '',
                group_uuid = '',
                certificate_type = 'X.509',
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
                compliance_profile_uuid = '',
                compliance_profile_name = ''
            )
        else:
            return ComplianceProfileRuleDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                connector_name = '',
                connector_uuid = '',
                kind = '',
                certificate_type = 'X.509',
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
                compliance_profile_uuid = '',
                compliance_profile_name = '',
        )
        """

    def testComplianceProfileRuleDto(self):
        """Test ComplianceProfileRuleDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
