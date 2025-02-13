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

from pyCZERTAINLY.models.connect_dto import ConnectDto

class TestConnectDto(unittest.TestCase):
    """ConnectDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConnectDto:
        """Test ConnectDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectDto`
        """
        model = ConnectDto()
        if include_optional:
            return ConnectDto(
                function_group = pyCZERTAINLY.models.function_group_dto.FunctionGroupDto(
                    function_group_code = 'credentialProvider', 
                    kinds = ["SoftKeyStore","Basic","ApiKey"], 
                    end_points = [
                        pyCZERTAINLY.models.endpoint_dto.EndpointDto(
                            uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                            name = 'Name', 
                            context = '/v1', 
                            method = 'POST', 
                            required = True, )
                        ], 
                    uuid = '204a57f6-2ed3-45b6-bf09-af8b8c900e33', 
                    name = '', )
            )
        else:
            return ConnectDto(
                function_group = pyCZERTAINLY.models.function_group_dto.FunctionGroupDto(
                    function_group_code = 'credentialProvider', 
                    kinds = ["SoftKeyStore","Basic","ApiKey"], 
                    end_points = [
                        pyCZERTAINLY.models.endpoint_dto.EndpointDto(
                            uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                            name = 'Name', 
                            context = '/v1', 
                            method = 'POST', 
                            required = True, )
                        ], 
                    uuid = '204a57f6-2ed3-45b6-bf09-af8b8c900e33', 
                    name = '', ),
        )
        """

    def testConnectDto(self):
        """Test ConnectDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
