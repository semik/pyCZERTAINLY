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

from pyCZERTAINLY.models.token_profile_key_usage_request_dto import TokenProfileKeyUsageRequestDto

class TestTokenProfileKeyUsageRequestDto(unittest.TestCase):
    """TokenProfileKeyUsageRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenProfileKeyUsageRequestDto:
        """Test TokenProfileKeyUsageRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenProfileKeyUsageRequestDto`
        """
        model = TokenProfileKeyUsageRequestDto()
        if include_optional:
            return TokenProfileKeyUsageRequestDto(
                usage = [
                    'sign'
                    ]
            )
        else:
            return TokenProfileKeyUsageRequestDto(
                usage = [
                    'sign'
                    ],
        )
        """

    def testTokenProfileKeyUsageRequestDto(self):
        """Test TokenProfileKeyUsageRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
