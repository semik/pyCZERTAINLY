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

from openapi_client.models.discovery_response_dto import DiscoveryResponseDto

class TestDiscoveryResponseDto(unittest.TestCase):
    """DiscoveryResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DiscoveryResponseDto:
        """Test DiscoveryResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DiscoveryResponseDto`
        """
        model = DiscoveryResponseDto()
        if include_optional:
            return DiscoveryResponseDto(
                discoveries = [
                    openapi_client.models.discovery_history_dto.DiscoveryHistoryDto(
                        uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                        name = 'Name', 
                        kind = 'IP-HostName', 
                        status = 'inProgress', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        total_certificates_discovered = 56, 
                        connector_uuid = '', 
                        connector_name = '', )
                    ],
                items_per_page = 56,
                page_number = 56,
                total_pages = 56,
                total_items = 56
            )
        else:
            return DiscoveryResponseDto(
                discoveries = [
                    openapi_client.models.discovery_history_dto.DiscoveryHistoryDto(
                        uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                        name = 'Name', 
                        kind = 'IP-HostName', 
                        status = 'inProgress', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        total_certificates_discovered = 56, 
                        connector_uuid = '', 
                        connector_name = '', )
                    ],
                items_per_page = 56,
                page_number = 56,
                total_pages = 56,
                total_items = 56,
        )
        """

    def testDiscoveryResponseDto(self):
        """Test DiscoveryResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
