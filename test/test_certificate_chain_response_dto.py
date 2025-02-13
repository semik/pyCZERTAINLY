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

from pyCZERTAINLY.models.certificate_chain_response_dto import CertificateChainResponseDto

class TestCertificateChainResponseDto(unittest.TestCase):
    """CertificateChainResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificateChainResponseDto:
        """Test CertificateChainResponseDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateChainResponseDto`
        """
        model = CertificateChainResponseDto()
        if include_optional:
            return CertificateChainResponseDto(
                complete_chain = True,
                certificates = [
                    pyCZERTAINLY.models.certificate_detail_dto.CertificateDetailDto(
                        uuid = '', 
                        common_name = '', 
                        serial_number = '', 
                        issuer_common_name = '', 
                        issuer_dn = '', 
                        subject_dn = '', 
                        not_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        not_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        public_key_algorithm = '', 
                        signature_algorithm = '', 
                        key_size = 56, 
                        state = 'requested', 
                        validation_status = 'not_checked', 
                        ra_profile = pyCZERTAINLY.models.simplified_ra_profile_dto.SimplifiedRaProfileDto(
                            uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                            name = 'Name', 
                            enabled = True, 
                            authority_instance_uuid = '', ), 
                        fingerprint = '', 
                        groups = [
                            pyCZERTAINLY.models.group_dto.GroupDto(
                                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                name = 'Name', 
                                description = '', 
                                email = '', 
                                custom_attributes = [
                                    pyCZERTAINLY.models.response_attribute_dto.ResponseAttributeDto(
                                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                        name = 'Attribute', 
                                        label = 'Attribute Name', 
                                        type = 'data', 
                                        content_type = 'string', 
                                        content = [
                                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                                reference = '', 
                                                data = pyCZERTAINLY.models.data.data(), )
                                            ], )
                                    ], )
                            ], 
                        owner = '', 
                        owner_uuid = '', 
                        certificate_type = 'X.509', 
                        issuer_serial_number = '', 
                        compliance_status = 'not_checked', 
                        issuer_certificate_uuid = '', 
                        private_key_availability = True, 
                        trusted_ca = True, 
                        extended_key_usage = [
                            ''
                            ], 
                        key_usage = [
                            ''
                            ], 
                        subject_type = 'endEntity', 
                        metadata = [
                            pyCZERTAINLY.models.metadata_response_dto.MetadataResponseDto(
                                connector_uuid = '', 
                                connector_name = '', 
                                source_object_type = 'NONE', 
                                items = [
                                    pyCZERTAINLY.models.response_metadata_dto.ResponseMetadataDto(
                                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                        name = 'Attribute', 
                                        label = 'Attribute Name', 
                                        type = 'data', 
                                        content_type = 'string', 
                                        source_objects = [
                                            pyCZERTAINLY.models.name_and_uuid_dto.NameAndUuidDto(
                                                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                                name = 'Name', )
                                            ], )
                                    ], )
                            ], 
                        certificate_content = '', 
                        subject_alternative_names = {
                            'key' : None
                            }, 
                        locations = [
                            pyCZERTAINLY.models.location_dto.LocationDto(
                                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                name = 'Name', 
                                description = '', 
                                entity_instance_uuid = '', 
                                entity_instance_name = '', 
                                attributes = [
                                    pyCZERTAINLY.models.response_attribute_dto.ResponseAttributeDto(
                                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                        name = 'Attribute', 
                                        label = 'Attribute Name', 
                                        type = , 
                                        content_type = , )
                                    ], 
                                enabled = True, 
                                support_multiple_entries = True, 
                                support_key_management = True, 
                                certificates = [
                                    pyCZERTAINLY.models.certificate_in_location_dto.CertificateInLocationDto(
                                        certificate_uuid = '', 
                                        state = 'requested', 
                                        validation_status = 'not_checked', 
                                        common_name = '', 
                                        serial_number = '', 
                                        push_attributes = [
                                            
                                            ], 
                                        csr_attributes = [
                                            
                                            ], 
                                        with_key = True, )
                                    ], )
                            ], 
                        non_compliant_rules = [
                            pyCZERTAINLY.models.certificate_compliance_result_dto.CertificateComplianceResultDto(
                                connector_name = 'Provider1', 
                                rule_name = 'RuleName', 
                                rule_description = 'Description sample', 
                                status = 'nok', )
                            ], 
                        custom_attributes = [
                            
                            ], 
                        key = pyCZERTAINLY.models.key_dto.KeyDto(
                            uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                            name = 'Name', 
                            description = '', 
                            creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            token_profile_uuid = '', 
                            token_profile_name = '', 
                            token_instance_uuid = '', 
                            token_instance_name = '', 
                            owner = '', 
                            owner_uuid = '', 
                            items = [
                                pyCZERTAINLY.models.key_item_dto.KeyItemDto(
                                    uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                    name = 'Name', 
                                    description = '', 
                                    creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    key_wrapper_uuid = '', 
                                    token_profile_uuid = '', 
                                    token_profile_name = '', 
                                    token_instance_uuid = '', 
                                    token_instance_name = '', 
                                    owner = '', 
                                    owner_uuid = '', 
                                    associations = 56, 
                                    key_reference_uuid = '', 
                                    type = 'Secret', 
                                    key_algorithm = 'RSA', 
                                    format = 'Raw', 
                                    length = 56, 
                                    usage = [
                                        'sign'
                                        ], 
                                    enabled = True, 
                                    state = 'pre-active', )
                                ], 
                            associations = 56, ), 
                        certificate_request = pyCZERTAINLY.models.certificate_request_dto.CertificateRequestDto(
                            certificate_request_format = 'pkcs10', 
                            public_key_algorithm = '', 
                            signature_algorithm = '', 
                            content = '', 
                            common_name = '', 
                            subject_dn = '', 
                            signature_attributes = [
                                
                                ], ), 
                        source_certificate_uuid = '', 
                        issue_attributes = [
                            
                            ], 
                        revoke_attributes = [
                            
                            ], 
                        related_certificates = [
                            pyCZERTAINLY.models.certificate_dto.CertificateDto(
                                uuid = '', 
                                common_name = '', 
                                serial_number = '', 
                                issuer_common_name = '', 
                                issuer_dn = '', 
                                subject_dn = '', 
                                not_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                not_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                public_key_algorithm = '', 
                                signature_algorithm = '', 
                                key_size = 56, 
                                state = , 
                                validation_status = , 
                                fingerprint = '', 
                                owner = '', 
                                owner_uuid = '', 
                                issuer_serial_number = '', 
                                issuer_certificate_uuid = '', 
                                private_key_availability = True, 
                                trusted_ca = True, )
                            ], 
                        protocol_info = pyCZERTAINLY.models.certificate_protocol_dto.CertificateProtocolDto(
                            protocol = 'acme', 
                            protocol_profile_uuid = '', 
                            additional_protocol_uuid = '', ), )
                    ]
            )
        else:
            return CertificateChainResponseDto(
                complete_chain = True,
                certificates = [
                    pyCZERTAINLY.models.certificate_detail_dto.CertificateDetailDto(
                        uuid = '', 
                        common_name = '', 
                        serial_number = '', 
                        issuer_common_name = '', 
                        issuer_dn = '', 
                        subject_dn = '', 
                        not_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        not_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        public_key_algorithm = '', 
                        signature_algorithm = '', 
                        key_size = 56, 
                        state = 'requested', 
                        validation_status = 'not_checked', 
                        ra_profile = pyCZERTAINLY.models.simplified_ra_profile_dto.SimplifiedRaProfileDto(
                            uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                            name = 'Name', 
                            enabled = True, 
                            authority_instance_uuid = '', ), 
                        fingerprint = '', 
                        groups = [
                            pyCZERTAINLY.models.group_dto.GroupDto(
                                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                name = 'Name', 
                                description = '', 
                                email = '', 
                                custom_attributes = [
                                    pyCZERTAINLY.models.response_attribute_dto.ResponseAttributeDto(
                                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                        name = 'Attribute', 
                                        label = 'Attribute Name', 
                                        type = 'data', 
                                        content_type = 'string', 
                                        content = [
                                            pyCZERTAINLY.models.base_attribute_content_dto.BaseAttributeContentDto(
                                                reference = '', 
                                                data = pyCZERTAINLY.models.data.data(), )
                                            ], )
                                    ], )
                            ], 
                        owner = '', 
                        owner_uuid = '', 
                        certificate_type = 'X.509', 
                        issuer_serial_number = '', 
                        compliance_status = 'not_checked', 
                        issuer_certificate_uuid = '', 
                        private_key_availability = True, 
                        trusted_ca = True, 
                        extended_key_usage = [
                            ''
                            ], 
                        key_usage = [
                            ''
                            ], 
                        subject_type = 'endEntity', 
                        metadata = [
                            pyCZERTAINLY.models.metadata_response_dto.MetadataResponseDto(
                                connector_uuid = '', 
                                connector_name = '', 
                                source_object_type = 'NONE', 
                                items = [
                                    pyCZERTAINLY.models.response_metadata_dto.ResponseMetadataDto(
                                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                        name = 'Attribute', 
                                        label = 'Attribute Name', 
                                        type = 'data', 
                                        content_type = 'string', 
                                        source_objects = [
                                            pyCZERTAINLY.models.name_and_uuid_dto.NameAndUuidDto(
                                                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                                name = 'Name', )
                                            ], )
                                    ], )
                            ], 
                        certificate_content = '', 
                        subject_alternative_names = {
                            'key' : None
                            }, 
                        locations = [
                            pyCZERTAINLY.models.location_dto.LocationDto(
                                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                name = 'Name', 
                                description = '', 
                                entity_instance_uuid = '', 
                                entity_instance_name = '', 
                                attributes = [
                                    pyCZERTAINLY.models.response_attribute_dto.ResponseAttributeDto(
                                        uuid = '166b5cf52-63f2-11ec-90d6-0242ac120003', 
                                        name = 'Attribute', 
                                        label = 'Attribute Name', 
                                        type = , 
                                        content_type = , )
                                    ], 
                                enabled = True, 
                                support_multiple_entries = True, 
                                support_key_management = True, 
                                certificates = [
                                    pyCZERTAINLY.models.certificate_in_location_dto.CertificateInLocationDto(
                                        certificate_uuid = '', 
                                        state = 'requested', 
                                        validation_status = 'not_checked', 
                                        common_name = '', 
                                        serial_number = '', 
                                        push_attributes = [
                                            
                                            ], 
                                        csr_attributes = [
                                            
                                            ], 
                                        with_key = True, )
                                    ], )
                            ], 
                        non_compliant_rules = [
                            pyCZERTAINLY.models.certificate_compliance_result_dto.CertificateComplianceResultDto(
                                connector_name = 'Provider1', 
                                rule_name = 'RuleName', 
                                rule_description = 'Description sample', 
                                status = 'nok', )
                            ], 
                        custom_attributes = [
                            
                            ], 
                        key = pyCZERTAINLY.models.key_dto.KeyDto(
                            uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                            name = 'Name', 
                            description = '', 
                            creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            token_profile_uuid = '', 
                            token_profile_name = '', 
                            token_instance_uuid = '', 
                            token_instance_name = '', 
                            owner = '', 
                            owner_uuid = '', 
                            items = [
                                pyCZERTAINLY.models.key_item_dto.KeyItemDto(
                                    uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                                    name = 'Name', 
                                    description = '', 
                                    creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    key_wrapper_uuid = '', 
                                    token_profile_uuid = '', 
                                    token_profile_name = '', 
                                    token_instance_uuid = '', 
                                    token_instance_name = '', 
                                    owner = '', 
                                    owner_uuid = '', 
                                    associations = 56, 
                                    key_reference_uuid = '', 
                                    type = 'Secret', 
                                    key_algorithm = 'RSA', 
                                    format = 'Raw', 
                                    length = 56, 
                                    usage = [
                                        'sign'
                                        ], 
                                    enabled = True, 
                                    state = 'pre-active', )
                                ], 
                            associations = 56, ), 
                        certificate_request = pyCZERTAINLY.models.certificate_request_dto.CertificateRequestDto(
                            certificate_request_format = 'pkcs10', 
                            public_key_algorithm = '', 
                            signature_algorithm = '', 
                            content = '', 
                            common_name = '', 
                            subject_dn = '', 
                            signature_attributes = [
                                
                                ], ), 
                        source_certificate_uuid = '', 
                        issue_attributes = [
                            
                            ], 
                        revoke_attributes = [
                            
                            ], 
                        related_certificates = [
                            pyCZERTAINLY.models.certificate_dto.CertificateDto(
                                uuid = '', 
                                common_name = '', 
                                serial_number = '', 
                                issuer_common_name = '', 
                                issuer_dn = '', 
                                subject_dn = '', 
                                not_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                not_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                public_key_algorithm = '', 
                                signature_algorithm = '', 
                                key_size = 56, 
                                state = , 
                                validation_status = , 
                                fingerprint = '', 
                                owner = '', 
                                owner_uuid = '', 
                                issuer_serial_number = '', 
                                issuer_certificate_uuid = '', 
                                private_key_availability = True, 
                                trusted_ca = True, )
                            ], 
                        protocol_info = pyCZERTAINLY.models.certificate_protocol_dto.CertificateProtocolDto(
                            protocol = 'acme', 
                            protocol_profile_uuid = '', 
                            additional_protocol_uuid = '', ), )
                    ],
        )
        """

    def testCertificateChainResponseDto(self):
        """Test CertificateChainResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
