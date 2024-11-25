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

from pyCZERTAINLY.models.execution_item_request_dto import ExecutionItemRequestDto

class TestExecutionItemRequestDto(unittest.TestCase):
    """ExecutionItemRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExecutionItemRequestDto:
        """Test ExecutionItemRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExecutionItemRequestDto`
        """
        model = ExecutionItemRequestDto()
        if include_optional:
            return ExecutionItemRequestDto(
                field_source = 'meta',
                field_identifier = '',
                data = None
            )
        else:
            return ExecutionItemRequestDto(
                field_source = 'meta',
                field_identifier = '',
        )
        """

    def testExecutionItemRequestDto(self):
        """Test ExecutionItemRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
