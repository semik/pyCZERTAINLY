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

from pyCZERTAINLY.models.notification_request_dto import NotificationRequestDto

class TestNotificationRequestDto(unittest.TestCase):
    """NotificationRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationRequestDto:
        """Test NotificationRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationRequestDto`
        """
        model = NotificationRequestDto()
        if include_optional:
            return NotificationRequestDto(
                items_per_page = 56,
                page_number = 56,
                unread = True
            )
        else:
            return NotificationRequestDto(
        )
        """

    def testNotificationRequestDto(self):
        """Test NotificationRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
