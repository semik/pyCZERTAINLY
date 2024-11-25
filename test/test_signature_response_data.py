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

from pyCZERTAINLY.models.signature_response_data import SignatureResponseData

class TestSignatureResponseData(unittest.TestCase):
    """SignatureResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignatureResponseData:
        """Test SignatureResponseData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignatureResponseData`
        """
        model = SignatureResponseData()
        if include_optional:
            return SignatureResponseData(
                data = '',
                identifier = 'customId',
                details = pyCZERTAINLY.models.details.details()
            )
        else:
            return SignatureResponseData(
                data = '',
        )
        """

    def testSignatureResponseData(self):
        """Test SignatureResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
