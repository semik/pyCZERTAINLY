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

from pyCZERTAINLY.models.search_request_dto import SearchRequestDto

class TestSearchRequestDto(unittest.TestCase):
    """SearchRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchRequestDto:
        """Test SearchRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchRequestDto`
        """
        model = SearchRequestDto()
        if include_optional:
            return SearchRequestDto(
                filters = [
                    pyCZERTAINLY.models.search_filter_request_dto.SearchFilterRequestDto(
                        field_source = 'meta', 
                        field_identifier = '', 
                        condition = 'EQUALS', 
                        value = pyCZERTAINLY.models.value.value(), )
                    ],
                items_per_page = 56,
                page_number = 56
            )
        else:
            return SearchRequestDto(
        )
        """

    def testSearchRequestDto(self):
        """Test SearchRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
