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

from pyCZERTAINLY.models.approval_dto import ApprovalDto

class TestApprovalDto(unittest.TestCase):
    """ApprovalDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApprovalDto:
        """Test ApprovalDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApprovalDto`
        """
        model = ApprovalDto()
        if include_optional:
            return ApprovalDto(
                approval_uuid = '',
                creator_uuid = '',
                creator_username = '',
                version = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expiry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'PENDING',
                resource = 'NONE',
                resource_action = '',
                object_uuid = '',
                approval_profile_name = '',
                approval_profile_uuid = ''
            )
        else:
            return ApprovalDto(
                approval_uuid = '',
                creator_uuid = '',
                version = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expiry_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'PENDING',
                resource = 'NONE',
                resource_action = '',
                object_uuid = '',
                approval_profile_name = '',
                approval_profile_uuid = '',
        )
        """

    def testApprovalDto(self):
        """Test ApprovalDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
