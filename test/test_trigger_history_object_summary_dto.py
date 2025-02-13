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

from pyCZERTAINLY.models.trigger_history_object_summary_dto import TriggerHistoryObjectSummaryDto

class TestTriggerHistoryObjectSummaryDto(unittest.TestCase):
    """TriggerHistoryObjectSummaryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TriggerHistoryObjectSummaryDto:
        """Test TriggerHistoryObjectSummaryDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TriggerHistoryObjectSummaryDto`
        """
        model = TriggerHistoryObjectSummaryDto()
        if include_optional:
            return TriggerHistoryObjectSummaryDto(
                object_uuid = '',
                reference_object_uuid = '',
                matched = True,
                ignored = True,
                triggers = [
                    pyCZERTAINLY.models.trigger_history_object_trigger_summary_dto.TriggerHistoryObjectTriggerSummaryDto(
                        trigger_uuid = '', 
                        trigger_name = '', 
                        triggered_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        records = [
                            pyCZERTAINLY.models.trigger_history_record_dto.TriggerHistoryRecordDto(
                                message = '', 
                                condition = pyCZERTAINLY.models.condition_dto.ConditionDto(
                                    uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                    name = 'Name', 
                                    description = '', 
                                    type = 'checkField', 
                                    resource = 'NONE', 
                                    items = [
                                        pyCZERTAINLY.models.condition_item_dto.ConditionItemDto(
                                            field_source = 'meta', 
                                            field_identifier = '', 
                                            operator = 'EQUALS', 
                                            value = pyCZERTAINLY.models.value.value(), )
                                        ], ), 
                                execution = pyCZERTAINLY.models.execution_dto.ExecutionDto(
                                    uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                    name = 'Name', 
                                    description = '', 
                                    type = 'setField', 
                                    resource = 'NONE', 
                                    items = [
                                        pyCZERTAINLY.models.execution_item_dto.ExecutionItemDto(
                                            field_source = 'meta', 
                                            field_identifier = '', 
                                            data = pyCZERTAINLY.models.data.data(), )
                                        ], ), )
                            ], )
                    ]
            )
        else:
            return TriggerHistoryObjectSummaryDto(
                matched = True,
                ignored = True,
                triggers = [
                    pyCZERTAINLY.models.trigger_history_object_trigger_summary_dto.TriggerHistoryObjectTriggerSummaryDto(
                        trigger_uuid = '', 
                        trigger_name = '', 
                        triggered_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        records = [
                            pyCZERTAINLY.models.trigger_history_record_dto.TriggerHistoryRecordDto(
                                message = '', 
                                condition = pyCZERTAINLY.models.condition_dto.ConditionDto(
                                    uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                    name = 'Name', 
                                    description = '', 
                                    type = 'checkField', 
                                    resource = 'NONE', 
                                    items = [
                                        pyCZERTAINLY.models.condition_item_dto.ConditionItemDto(
                                            field_source = 'meta', 
                                            field_identifier = '', 
                                            operator = 'EQUALS', 
                                            value = pyCZERTAINLY.models.value.value(), )
                                        ], ), 
                                execution = pyCZERTAINLY.models.execution_dto.ExecutionDto(
                                    uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                    name = 'Name', 
                                    description = '', 
                                    type = 'setField', 
                                    resource = 'NONE', 
                                    items = [
                                        pyCZERTAINLY.models.execution_item_dto.ExecutionItemDto(
                                            field_source = 'meta', 
                                            field_identifier = '', 
                                            data = pyCZERTAINLY.models.data.data(), )
                                        ], ), )
                            ], )
                    ],
        )
        """

    def testTriggerHistoryObjectSummaryDto(self):
        """Test TriggerHistoryObjectSummaryDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
