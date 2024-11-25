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

from openapi_client.models.date_time_attribute_constraint_data import DateTimeAttributeConstraintData

class TestDateTimeAttributeConstraintData(unittest.TestCase):
    """DateTimeAttributeConstraintData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DateTimeAttributeConstraintData:
        """Test DateTimeAttributeConstraintData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DateTimeAttributeConstraintData`
        """
        model = DateTimeAttributeConstraintData()
        if include_optional:
            return DateTimeAttributeConstraintData(
                var_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DateTimeAttributeConstraintData(
        )
        """

    def testDateTimeAttributeConstraintData(self):
        """Test DateTimeAttributeConstraintData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
