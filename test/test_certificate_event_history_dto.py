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

from pyCZERTAINLY.models.certificate_event_history_dto import CertificateEventHistoryDto

class TestCertificateEventHistoryDto(unittest.TestCase):
    """CertificateEventHistoryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificateEventHistoryDto:
        """Test CertificateEventHistoryDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateEventHistoryDto`
        """
        model = CertificateEventHistoryDto()
        if include_optional:
            return CertificateEventHistoryDto(
                uuid = '',
                certificate_uuid = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                event = 'Issue Certificate',
                status = 'SUCCESS',
                message = '',
                additional_information = {
                    'key' : None
                    }
            )
        else:
            return CertificateEventHistoryDto(
                uuid = '',
                certificate_uuid = '',
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                event = 'Issue Certificate',
                status = 'SUCCESS',
                message = '',
        )
        """

    def testCertificateEventHistoryDto(self):
        """Test CertificateEventHistoryDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
