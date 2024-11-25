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

from openapi_client.models.compliance_groups_dto import ComplianceGroupsDto

class TestComplianceGroupsDto(unittest.TestCase):
    """ComplianceGroupsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ComplianceGroupsDto:
        """Test ComplianceGroupsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ComplianceGroupsDto`
        """
        model = ComplianceGroupsDto()
        if include_optional:
            return ComplianceGroupsDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                description = 'Sample group description'
            )
        else:
            return ComplianceGroupsDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
        )
        """

    def testComplianceGroupsDto(self):
        """Test ComplianceGroupsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
