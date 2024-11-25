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

from openapi_client.models.role_permissions_request_dto import RolePermissionsRequestDto

class TestRolePermissionsRequestDto(unittest.TestCase):
    """RolePermissionsRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RolePermissionsRequestDto:
        """Test RolePermissionsRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RolePermissionsRequestDto`
        """
        model = RolePermissionsRequestDto()
        if include_optional:
            return RolePermissionsRequestDto(
                allow_all_resources = True,
                resources = [
                    openapi_client.models.resource_permissions_request_dto.ResourcePermissionsRequestDto(
                        name = '', 
                        allow_all_actions = True, 
                        actions = [
                            ''
                            ], 
                        objects = [
                            openapi_client.models.object_permissions_request_dto.ObjectPermissionsRequestDto(
                                uuid = '', 
                                name = '', 
                                allow = [
                                    ''
                                    ], 
                                deny = [
                                    ''
                                    ], )
                            ], )
                    ]
            )
        else:
            return RolePermissionsRequestDto(
                allow_all_resources = True,
        )
        """

    def testRolePermissionsRequestDto(self):
        """Test RolePermissionsRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
