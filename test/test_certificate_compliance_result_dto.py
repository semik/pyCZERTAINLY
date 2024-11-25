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

from pyCZERTAINLY.models.certificate_compliance_result_dto import CertificateComplianceResultDto

class TestCertificateComplianceResultDto(unittest.TestCase):
    """CertificateComplianceResultDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificateComplianceResultDto:
        """Test CertificateComplianceResultDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateComplianceResultDto`
        """
        model = CertificateComplianceResultDto()
        if include_optional:
            return CertificateComplianceResultDto(
                connector_name = 'Provider1',
                rule_name = 'RuleName',
                rule_description = 'Description sample',
                status = 'nok',
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
                    ]
            )
        else:
            return CertificateComplianceResultDto(
                connector_name = 'Provider1',
                rule_name = 'RuleName',
                rule_description = 'Description sample',
                status = 'nok',
        )
        """

    def testCertificateComplianceResultDto(self):
        """Test CertificateComplianceResultDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
