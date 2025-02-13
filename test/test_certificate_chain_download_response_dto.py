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

from pyCZERTAINLY.models.certificate_chain_download_response_dto import CertificateChainDownloadResponseDto

class TestCertificateChainDownloadResponseDto(unittest.TestCase):
    """CertificateChainDownloadResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificateChainDownloadResponseDto:
        """Test CertificateChainDownloadResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateChainDownloadResponseDto`
        """
        model = CertificateChainDownloadResponseDto()
        if include_optional:
            return CertificateChainDownloadResponseDto(
                format = 'raw',
                encoding = 'pem',
                content = '',
                complete_chain = True
            )
        else:
            return CertificateChainDownloadResponseDto(
                format = 'raw',
                encoding = 'pem',
                content = '',
                complete_chain = True,
        )
        """

    def testCertificateChainDownloadResponseDto(self):
        """Test CertificateChainDownloadResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
