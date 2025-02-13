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

from pyCZERTAINLY.models.approval_step_dto import ApprovalStepDto

class TestApprovalStepDto(unittest.TestCase):
    """ApprovalStepDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApprovalStepDto:
        """Test ApprovalStepDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApprovalStepDto`
        """
        model = ApprovalStepDto()
        if include_optional:
            return ApprovalStepDto(
                user_uuid = '',
                role_uuid = '',
                group_uuid = '',
                description = '',
                order = 56,
                required_approvals = 56,
                uuid = '',
                username = '',
                role_name = '',
                group_name = ''
            )
        else:
            return ApprovalStepDto(
                order = 56,
                uuid = '',
        )
        """

    def testApprovalStepDto(self):
        """Test ApprovalStepDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
