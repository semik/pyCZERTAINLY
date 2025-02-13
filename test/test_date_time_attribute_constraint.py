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

from pyCZERTAINLY.models.date_time_attribute_constraint import DateTimeAttributeConstraint

class TestDateTimeAttributeConstraint(unittest.TestCase):
    """DateTimeAttributeConstraint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DateTimeAttributeConstraint:
        """Test DateTimeAttributeConstraint
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DateTimeAttributeConstraint`
        """
        model = DateTimeAttributeConstraint()
        if include_optional:
            return DateTimeAttributeConstraint(
                description = '',
                error_message = '',
                type = 'regExp',
                data = pyCZERTAINLY.models.date_time_attribute_constraint_data.DateTimeAttributeConstraintData(
                    from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return DateTimeAttributeConstraint(
                type = 'regExp',
        )
        """

    def testDateTimeAttributeConstraint(self):
        """Test DateTimeAttributeConstraint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
