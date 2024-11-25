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

from openapi_client.models.attribute_callback import AttributeCallback

class TestAttributeCallback(unittest.TestCase):
    """AttributeCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttributeCallback:
        """Test AttributeCallback
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttributeCallback`
        """
        model = AttributeCallback()
        if include_optional:
            return AttributeCallback(
                callback_context = '',
                callback_method = '',
                mappings = [
                    openapi_client.models.attribute_callback_mapping.AttributeCallbackMapping(
                        from = '', 
                        attribute_type = 'data', 
                        attribute_content_type = 'string', 
                        to = '', 
                        targets = [
                            'pathVariable'
                            ], 
                        value = openapi_client.models.value.value(), )
                    ]
            )
        else:
            return AttributeCallback(
                callback_context = '',
                callback_method = '',
                mappings = [
                    openapi_client.models.attribute_callback_mapping.AttributeCallbackMapping(
                        from = '', 
                        attribute_type = 'data', 
                        attribute_content_type = 'string', 
                        to = '', 
                        targets = [
                            'pathVariable'
                            ], 
                        value = openapi_client.models.value.value(), )
                    ],
        )
        """

    def testAttributeCallback(self):
        """Test AttributeCallback"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
