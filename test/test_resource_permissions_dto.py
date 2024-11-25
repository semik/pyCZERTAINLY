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

from openapi_client.models.resource_permissions_dto import ResourcePermissionsDto

class TestResourcePermissionsDto(unittest.TestCase):
    """ResourcePermissionsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourcePermissionsDto:
        """Test ResourcePermissionsDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourcePermissionsDto`
        """
        model = ResourcePermissionsDto()
        if include_optional:
            return ResourcePermissionsDto(
                name = '',
                allow_all_actions = True,
                actions = [
                    ''
                    ],
                objects = [
                    openapi_client.models.object_permissions_dto.ObjectPermissionsDto(
                        uuid = '', 
                        name = '', 
                        allow = [
                            ''
                            ], 
                        deny = [
                            ''
                            ], )
                    ]
            )
        else:
            return ResourcePermissionsDto(
                name = '',
                allow_all_actions = True,
                actions = [
                    ''
                    ],
                objects = [
                    openapi_client.models.object_permissions_dto.ObjectPermissionsDto(
                        uuid = '', 
                        name = '', 
                        allow = [
                            ''
                            ], 
                        deny = [
                            ''
                            ], )
                    ],
        )
        """

    def testResourcePermissionsDto(self):
        """Test ResourcePermissionsDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
