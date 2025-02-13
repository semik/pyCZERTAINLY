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

from pyCZERTAINLY.models.search_field_data_by_group_dto import SearchFieldDataByGroupDto

class TestSearchFieldDataByGroupDto(unittest.TestCase):
    """SearchFieldDataByGroupDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchFieldDataByGroupDto:
        """Test SearchFieldDataByGroupDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchFieldDataByGroupDto`
        """
        model = SearchFieldDataByGroupDto()
        if include_optional:
            return SearchFieldDataByGroupDto(
                filter_field_source = 'meta',
                search_field_data = [
                    pyCZERTAINLY.models.search_field_data_dto.SearchFieldDataDto(
                        field_identifier = '', 
                        field_label = '', 
                        type = 'string', 
                        conditions = [
                            'EQUALS'
                            ], 
                        platform_enum = 'Resource', 
                        attribute_content_type = 'string', 
                        value = pyCZERTAINLY.models.value.value(), 
                        multi_value = True, )
                    ]
            )
        else:
            return SearchFieldDataByGroupDto(
                filter_field_source = 'meta',
        )
        """

    def testSearchFieldDataByGroupDto(self):
        """Test SearchFieldDataByGroupDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
