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

from pyCZERTAINLY.models.key_association_dto import KeyAssociationDto

class TestKeyAssociationDto(unittest.TestCase):
    """KeyAssociationDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeyAssociationDto:
        """Test KeyAssociationDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeyAssociationDto`
        """
        model = KeyAssociationDto()
        if include_optional:
            return KeyAssociationDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                resource = 'NONE'
            )
        else:
            return KeyAssociationDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                resource = 'NONE',
        )
        """

    def testKeyAssociationDto(self):
        """Test KeyAssociationDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
