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

from pyCZERTAINLY.models.ra_profile_association_request_dto import RaProfileAssociationRequestDto

class TestRaProfileAssociationRequestDto(unittest.TestCase):
    """RaProfileAssociationRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RaProfileAssociationRequestDto:
        """Test RaProfileAssociationRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RaProfileAssociationRequestDto`
        """
        model = RaProfileAssociationRequestDto()
        if include_optional:
            return RaProfileAssociationRequestDto(
                ra_profile_uuids = ["18324af0-e95c-11ec-8fea-0242ac120002","18324c94-e95c-11ec-8fea-0242ac120002"]
            )
        else:
            return RaProfileAssociationRequestDto(
                ra_profile_uuids = ["18324af0-e95c-11ec-8fea-0242ac120002","18324c94-e95c-11ec-8fea-0242ac120002"],
        )
        """

    def testRaProfileAssociationRequestDto(self):
        """Test RaProfileAssociationRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
