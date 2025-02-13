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

from pyCZERTAINLY.models.code_block_attribute_content_data import CodeBlockAttributeContentData

class TestCodeBlockAttributeContentData(unittest.TestCase):
    """CodeBlockAttributeContentData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodeBlockAttributeContentData:
        """Test CodeBlockAttributeContentData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodeBlockAttributeContentData`
        """
        model = CodeBlockAttributeContentData()
        if include_optional:
            return CodeBlockAttributeContentData(
                language = 'JAVA, PHP, C, etc',
                code = ''
            )
        else:
            return CodeBlockAttributeContentData(
                language = 'JAVA, PHP, C, etc',
                code = '',
        )
        """

    def testCodeBlockAttributeContentData(self):
        """Test CodeBlockAttributeContentData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
