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

from pyCZERTAINLY.models.action_request_dto import ActionRequestDto

class TestActionRequestDto(unittest.TestCase):
    """ActionRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionRequestDto:
        """Test ActionRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionRequestDto`
        """
        model = ActionRequestDto()
        if include_optional:
            return ActionRequestDto(
                name = '',
                description = '',
                resource = 'NONE',
                executions_uuids = [
                    ''
                    ]
            )
        else:
            return ActionRequestDto(
                name = '',
                resource = 'NONE',
                executions_uuids = [
                    ''
                    ],
        )
        """

    def testActionRequestDto(self):
        """Test ActionRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
