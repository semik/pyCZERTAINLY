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

from pyCZERTAINLY.models.cmp_profile_detail_dto import CmpProfileDetailDto

class TestCmpProfileDetailDto(unittest.TestCase):
    """CmpProfileDetailDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CmpProfileDetailDto:
        """Test CmpProfileDetailDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CmpProfileDetailDto`
        """
        model = CmpProfileDetailDto()
        if include_optional:
            return CmpProfileDetailDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                enabled = True,
                variant = 'v2',
                description = 'Sample text description',
                ra_profile = pyCZERTAINLY.models.simplified_ra_profile_dto.SimplifiedRaProfileDto(
                    uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002', 
                    name = 'Name', 
                    enabled = True, 
                    authority_instance_uuid = '', ),
                cmp_url = 'https://your-domain.com/api/v1/protocols/cmp/cmpProfile',
                issue_certificate_attributes = [
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
                    ],
                revoke_certificate_attributes = [
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
                    ],
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
                    ],
                request_protection_method = 'sharedSecret',
                response_protection_method = 'sharedSecret',
                signing_certificate = pyCZERTAINLY.models.certificate_dto.CertificateDto(
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
                    trusted_ca = True, )
            )
        else:
            return CmpProfileDetailDto(
                uuid = '7b55ge1c-844f-11dc-a8a3-0242ac120002',
                name = 'Name',
                enabled = True,
                variant = 'v2',
                request_protection_method = 'sharedSecret',
                response_protection_method = 'sharedSecret',
        )
        """

    def testCmpProfileDetailDto(self):
        """Test CmpProfileDetailDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
