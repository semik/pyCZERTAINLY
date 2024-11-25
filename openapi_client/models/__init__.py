# coding: utf-8

# flake8: noqa
"""
    CZERTAINLY Core API

    REST API for CZERTAINLY Core

    The version of the OpenAPI document: 2.13.2-SNAPSHOT
    Contact: info@czertainly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.account_status import AccountStatus
from openapi_client.models.acme_account_list_response_dto import AcmeAccountListResponseDto
from openapi_client.models.acme_account_response_dto import AcmeAccountResponseDto
from openapi_client.models.acme_profile_dto import AcmeProfileDto
from openapi_client.models.acme_profile_edit_request_dto import AcmeProfileEditRequestDto
from openapi_client.models.acme_profile_list_dto import AcmeProfileListDto
from openapi_client.models.acme_profile_request_dto import AcmeProfileRequestDto
from openapi_client.models.action_detail_dto import ActionDetailDto
from openapi_client.models.action_dto import ActionDto
from openapi_client.models.action_request_dto import ActionRequestDto
from openapi_client.models.activate_acme_for_ra_profile_request_dto import ActivateAcmeForRaProfileRequestDto
from openapi_client.models.activate_cmp_for_ra_profile_request_dto import ActivateCmpForRaProfileRequestDto
from openapi_client.models.activate_scep_for_ra_profile_request_dto import ActivateScepForRaProfileRequestDto
from openapi_client.models.actor_record import ActorRecord
from openapi_client.models.actor_type import ActorType
from openapi_client.models.add_location_request_dto import AddLocationRequestDto
from openapi_client.models.add_ra_profile_request_dto import AddRaProfileRequestDto
from openapi_client.models.add_token_profile_request_dto import AddTokenProfileRequestDto
from openapi_client.models.add_user_request_dto import AddUserRequestDto
from openapi_client.models.approval_detail_dto import ApprovalDetailDto
from openapi_client.models.approval_detail_step_dto import ApprovalDetailStepDto
from openapi_client.models.approval_dto import ApprovalDto
from openapi_client.models.approval_profile_detail_dto import ApprovalProfileDetailDto
from openapi_client.models.approval_profile_dto import ApprovalProfileDto
from openapi_client.models.approval_profile_for_version_dto import ApprovalProfileForVersionDto
from openapi_client.models.approval_profile_request_dto import ApprovalProfileRequestDto
from openapi_client.models.approval_profile_response_dto import ApprovalProfileResponseDto
from openapi_client.models.approval_profile_update_request_dto import ApprovalProfileUpdateRequestDto
from openapi_client.models.approval_response_dto import ApprovalResponseDto
from openapi_client.models.approval_step_dto import ApprovalStepDto
from openapi_client.models.approval_step_recipient_dto import ApprovalStepRecipientDto
from openapi_client.models.approval_step_request_dto import ApprovalStepRequestDto
from openapi_client.models.approval_user_dto import ApprovalUserDto
from openapi_client.models.attribute_callback import AttributeCallback
from openapi_client.models.attribute_callback_mapping import AttributeCallbackMapping
from openapi_client.models.attribute_constraint_type import AttributeConstraintType
from openapi_client.models.attribute_content_type import AttributeContentType
from openapi_client.models.attribute_definition_dto import AttributeDefinitionDto
from openapi_client.models.attribute_mapping_dto import AttributeMappingDto
from openapi_client.models.attribute_type import AttributeType
from openapi_client.models.attribute_value_target import AttributeValueTarget
from openapi_client.models.audit_log_dto import AuditLogDto
from openapi_client.models.audit_log_response_dto import AuditLogResponseDto
from openapi_client.models.auth_method import AuthMethod
from openapi_client.models.auth_resource_dto import AuthResourceDto
from openapi_client.models.auth_type import AuthType
from openapi_client.models.authentication_service_exception_dto import AuthenticationServiceExceptionDto
from openapi_client.models.authority_instance_dto import AuthorityInstanceDto
from openapi_client.models.authority_instance_request_dto import AuthorityInstanceRequestDto
from openapi_client.models.authority_instance_update_request_dto import AuthorityInstanceUpdateRequestDto
from openapi_client.models.base_attribute_constraint import BaseAttributeConstraint
from openapi_client.models.base_attribute_content_dto import BaseAttributeContentDto
from openapi_client.models.base_attribute_dto import BaseAttributeDto
from openapi_client.models.boolean_attribute_content import BooleanAttributeContent
from openapi_client.models.bulk_action_message_dto import BulkActionMessageDto
from openapi_client.models.bulk_compromise_key_item_request_dto import BulkCompromiseKeyItemRequestDto
from openapi_client.models.bulk_compromise_key_request_dto import BulkCompromiseKeyRequestDto
from openapi_client.models.bulk_key_item_usage_request_dto import BulkKeyItemUsageRequestDto
from openapi_client.models.bulk_key_usage_request_dto import BulkKeyUsageRequestDto
from openapi_client.models.bulk_operation_response import BulkOperationResponse
from openapi_client.models.bulk_token_profile_key_usage_request_dto import BulkTokenProfileKeyUsageRequestDto
from openapi_client.models.certificate_chain_download_response_dto import CertificateChainDownloadResponseDto
from openapi_client.models.certificate_chain_response_dto import CertificateChainResponseDto
from openapi_client.models.certificate_compliance_check_dto import CertificateComplianceCheckDto
from openapi_client.models.certificate_compliance_result_dto import CertificateComplianceResultDto
from openapi_client.models.certificate_content_dto import CertificateContentDto
from openapi_client.models.certificate_detail_dto import CertificateDetailDto
from openapi_client.models.certificate_download_response_dto import CertificateDownloadResponseDto
from openapi_client.models.certificate_dto import CertificateDto
from openapi_client.models.certificate_event_history_dto import CertificateEventHistoryDto
from openapi_client.models.certificate_format import CertificateFormat
from openapi_client.models.certificate_format_encoding import CertificateFormatEncoding
from openapi_client.models.certificate_in_location_dto import CertificateInLocationDto
from openapi_client.models.certificate_protocol import CertificateProtocol
from openapi_client.models.certificate_protocol_dto import CertificateProtocolDto
from openapi_client.models.certificate_request_dto import CertificateRequestDto
from openapi_client.models.certificate_request_format import CertificateRequestFormat
from openapi_client.models.certificate_response_dto import CertificateResponseDto
from openapi_client.models.certificate_revocation_reason import CertificateRevocationReason
from openapi_client.models.certificate_state import CertificateState
from openapi_client.models.certificate_subject_type import CertificateSubjectType
from openapi_client.models.certificate_type import CertificateType
from openapi_client.models.certificate_update_objects_dto import CertificateUpdateObjectsDto
from openapi_client.models.certificate_validation_check import CertificateValidationCheck
from openapi_client.models.certificate_validation_check_dto import CertificateValidationCheckDto
from openapi_client.models.certificate_validation_result_dto import CertificateValidationResultDto
from openapi_client.models.certificate_validation_status import CertificateValidationStatus
from openapi_client.models.cipher_data_request_dto import CipherDataRequestDto
from openapi_client.models.cipher_request_data import CipherRequestData
from openapi_client.models.cipher_response_data import CipherResponseData
from openapi_client.models.client_certificate_data_response_dto import ClientCertificateDataResponseDto
from openapi_client.models.client_certificate_rekey_request_dto import ClientCertificateRekeyRequestDto
from openapi_client.models.client_certificate_renew_request_dto import ClientCertificateRenewRequestDto
from openapi_client.models.client_certificate_request_dto import ClientCertificateRequestDto
from openapi_client.models.client_certificate_revocation_dto import ClientCertificateRevocationDto
from openapi_client.models.client_certificate_sign_request_dto import ClientCertificateSignRequestDto
from openapi_client.models.cmp_profile_detail_dto import CmpProfileDetailDto
from openapi_client.models.cmp_profile_dto import CmpProfileDto
from openapi_client.models.cmp_profile_edit_request_dto import CmpProfileEditRequestDto
from openapi_client.models.cmp_profile_request_dto import CmpProfileRequestDto
from openapi_client.models.code_block_attribute_content import CodeBlockAttributeContent
from openapi_client.models.code_block_attribute_content_data import CodeBlockAttributeContentData
from openapi_client.models.compliance_connector_and_groups_dto import ComplianceConnectorAndGroupsDto
from openapi_client.models.compliance_connector_and_rules_dto import ComplianceConnectorAndRulesDto
from openapi_client.models.compliance_group_request_dto import ComplianceGroupRequestDto
from openapi_client.models.compliance_groups_dto import ComplianceGroupsDto
from openapi_client.models.compliance_groups_list_response_dto import ComplianceGroupsListResponseDto
from openapi_client.models.compliance_groups_response_dto import ComplianceGroupsResponseDto
from openapi_client.models.compliance_profile_dto import ComplianceProfileDto
from openapi_client.models.compliance_profile_request_dto import ComplianceProfileRequestDto
from openapi_client.models.compliance_profile_rule_dto import ComplianceProfileRuleDto
from openapi_client.models.compliance_profile_rules_request_dto import ComplianceProfileRulesRequestDto
from openapi_client.models.compliance_profiles_list_dto import ComplianceProfilesListDto
from openapi_client.models.compliance_provider_summary_dto import ComplianceProviderSummaryDto
from openapi_client.models.compliance_request_rules_dto import ComplianceRequestRulesDto
from openapi_client.models.compliance_rule_addition_request_dto import ComplianceRuleAdditionRequestDto
from openapi_client.models.compliance_rule_deletion_request_dto import ComplianceRuleDeletionRequestDto
from openapi_client.models.compliance_rule_status import ComplianceRuleStatus
from openapi_client.models.compliance_rules_dto import ComplianceRulesDto
from openapi_client.models.compliance_rules_list_response_dto import ComplianceRulesListResponseDto
from openapi_client.models.compliance_rules_response_dto import ComplianceRulesResponseDto
from openapi_client.models.compliance_status import ComplianceStatus
from openapi_client.models.compromise_key_request_dto import CompromiseKeyRequestDto
from openapi_client.models.condition_dto import ConditionDto
from openapi_client.models.condition_item_dto import ConditionItemDto
from openapi_client.models.condition_item_request_dto import ConditionItemRequestDto
from openapi_client.models.condition_request_dto import ConditionRequestDto
from openapi_client.models.condition_type import ConditionType
from openapi_client.models.connect_dto import ConnectDto
from openapi_client.models.connect_request_dto import ConnectRequestDto
from openapi_client.models.connector_dto import ConnectorDto
from openapi_client.models.connector_metadata_promotion_request_dto import ConnectorMetadataPromotionRequestDto
from openapi_client.models.connector_metadata_response_dto import ConnectorMetadataResponseDto
from openapi_client.models.connector_request_dto import ConnectorRequestDto
from openapi_client.models.connector_status import ConnectorStatus
from openapi_client.models.connector_update_request_dto import ConnectorUpdateRequestDto
from openapi_client.models.credential_attribute_content import CredentialAttributeContent
from openapi_client.models.credential_attribute_content_data import CredentialAttributeContentData
from openapi_client.models.credential_dto import CredentialDto
from openapi_client.models.credential_request_dto import CredentialRequestDto
from openapi_client.models.credential_update_request_dto import CredentialUpdateRequestDto
from openapi_client.models.cryptographic_key_response_dto import CryptographicKeyResponseDto
from openapi_client.models.custom_attribute import CustomAttribute
from openapi_client.models.custom_attribute_create_request_dto import CustomAttributeCreateRequestDto
from openapi_client.models.custom_attribute_definition_detail_dto import CustomAttributeDefinitionDetailDto
from openapi_client.models.custom_attribute_definition_dto import CustomAttributeDefinitionDto
from openapi_client.models.custom_attribute_properties import CustomAttributeProperties
from openapi_client.models.custom_attribute_update_request_dto import CustomAttributeUpdateRequestDto
from openapi_client.models.data_attribute import DataAttribute
from openapi_client.models.data_attribute_properties import DataAttributeProperties
from openapi_client.models.date_attribute_content import DateAttributeContent
from openapi_client.models.date_time_attribute_constraint import DateTimeAttributeConstraint
from openapi_client.models.date_time_attribute_constraint_data import DateTimeAttributeConstraintData
from openapi_client.models.date_time_attribute_content import DateTimeAttributeContent
from openapi_client.models.decrypt_data_response_dto import DecryptDataResponseDto
from openapi_client.models.discovery_certificate_dto import DiscoveryCertificateDto
from openapi_client.models.discovery_certificate_response_dto import DiscoveryCertificateResponseDto
from openapi_client.models.discovery_dto import DiscoveryDto
from openapi_client.models.discovery_history_detail_dto import DiscoveryHistoryDetailDto
from openapi_client.models.discovery_history_dto import DiscoveryHistoryDto
from openapi_client.models.discovery_response_dto import DiscoveryResponseDto
from openapi_client.models.discovery_status import DiscoveryStatus
from openapi_client.models.edit_key_request_dto import EditKeyRequestDto
from openapi_client.models.edit_location_request_dto import EditLocationRequestDto
from openapi_client.models.edit_ra_profile_request_dto import EditRaProfileRequestDto
from openapi_client.models.edit_token_profile_request_dto import EditTokenProfileRequestDto
from openapi_client.models.encrypt_data_response_dto import EncryptDataResponseDto
from openapi_client.models.endpoint_dto import EndpointDto
from openapi_client.models.entity_instance_dto import EntityInstanceDto
from openapi_client.models.entity_instance_request_dto import EntityInstanceRequestDto
from openapi_client.models.entity_instance_response_dto import EntityInstanceResponseDto
from openapi_client.models.entity_instance_update_request_dto import EntityInstanceUpdateRequestDto
from openapi_client.models.enum_item_dto import EnumItemDto
from openapi_client.models.error_message_dto import ErrorMessageDto
from openapi_client.models.execution_dto import ExecutionDto
from openapi_client.models.execution_item_dto import ExecutionItemDto
from openapi_client.models.execution_item_request_dto import ExecutionItemRequestDto
from openapi_client.models.execution_request_dto import ExecutionRequestDto
from openapi_client.models.execution_type import ExecutionType
from openapi_client.models.file_attribute_content import FileAttributeContent
from openapi_client.models.file_attribute_content_data import FileAttributeContentData
from openapi_client.models.filter_condition_operator import FilterConditionOperator
from openapi_client.models.filter_field_source import FilterFieldSource
from openapi_client.models.filter_field_type import FilterFieldType
from openapi_client.models.float_attribute_content import FloatAttributeContent
from openapi_client.models.function_group_code import FunctionGroupCode
from openapi_client.models.function_group_dto import FunctionGroupDto
from openapi_client.models.global_metadata_create_request_dto import GlobalMetadataCreateRequestDto
from openapi_client.models.global_metadata_definition_detail_dto import GlobalMetadataDefinitionDetailDto
from openapi_client.models.global_metadata_update_request_dto import GlobalMetadataUpdateRequestDto
from openapi_client.models.group_attribute import GroupAttribute
from openapi_client.models.group_dto import GroupDto
from openapi_client.models.group_request_dto import GroupRequestDto
from openapi_client.models.health_dto import HealthDto
from openapi_client.models.health_status import HealthStatus
from openapi_client.models.info_attribute import InfoAttribute
from openapi_client.models.info_attribute_properties import InfoAttributeProperties
from openapi_client.models.integer_attribute_content import IntegerAttributeContent
from openapi_client.models.issue_to_location_request_dto import IssueToLocationRequestDto
from openapi_client.models.key_algorithm import KeyAlgorithm
from openapi_client.models.key_association_dto import KeyAssociationDto
from openapi_client.models.key_compromise_reason import KeyCompromiseReason
from openapi_client.models.key_detail_dto import KeyDetailDto
from openapi_client.models.key_dto import KeyDto
from openapi_client.models.key_event_history_dto import KeyEventHistoryDto
from openapi_client.models.key_format import KeyFormat
from openapi_client.models.key_item_detail_dto import KeyItemDetailDto
from openapi_client.models.key_item_dto import KeyItemDto
from openapi_client.models.key_request_dto import KeyRequestDto
from openapi_client.models.key_request_type import KeyRequestType
from openapi_client.models.key_state import KeyState
from openapi_client.models.key_type import KeyType
from openapi_client.models.key_usage import KeyUsage
from openapi_client.models.location_dto import LocationDto
from openapi_client.models.locations_response_dto import LocationsResponseDto
from openapi_client.models.metadata_attribute import MetadataAttribute
from openapi_client.models.metadata_attribute_properties import MetadataAttributeProperties
from openapi_client.models.metadata_response_dto import MetadataResponseDto
from openapi_client.models.module import Module
from openapi_client.models.multiple_certificate_object_update_dto import MultipleCertificateObjectUpdateDto
from openapi_client.models.name_and_id_dto import NameAndIdDto
from openapi_client.models.name_and_uuid_dto import NameAndUuidDto
from openapi_client.models.notification_dto import NotificationDto
from openapi_client.models.notification_instance_dto import NotificationInstanceDto
from openapi_client.models.notification_instance_request_dto import NotificationInstanceRequestDto
from openapi_client.models.notification_instance_update_request_dto import NotificationInstanceUpdateRequestDto
from openapi_client.models.notification_request_dto import NotificationRequestDto
from openapi_client.models.notification_response_dto import NotificationResponseDto
from openapi_client.models.notification_settings_dto import NotificationSettingsDto
from openapi_client.models.object_attribute_content import ObjectAttributeContent
from openapi_client.models.object_permissions_dto import ObjectPermissionsDto
from openapi_client.models.object_permissions_request_dto import ObjectPermissionsRequestDto
from openapi_client.models.operation import Operation
from openapi_client.models.operation_result import OperationResult
from openapi_client.models.pagination_request_dto import PaginationRequestDto
from openapi_client.models.platform_enum import PlatformEnum
from openapi_client.models.platform_settings_dto import PlatformSettingsDto
from openapi_client.models.programming_language_enum import ProgrammingLanguageEnum
from openapi_client.models.protection_method import ProtectionMethod
from openapi_client.models.push_to_location_request_dto import PushToLocationRequestDto
from openapi_client.models.ra_profile_acme_detail_response_dto import RaProfileAcmeDetailResponseDto
from openapi_client.models.ra_profile_association_request_dto import RaProfileAssociationRequestDto
from openapi_client.models.ra_profile_cmp_detail_response_dto import RaProfileCmpDetailResponseDto
from openapi_client.models.ra_profile_dto import RaProfileDto
from openapi_client.models.ra_profile_scep_detail_response_dto import RaProfileScepDetailResponseDto
from openapi_client.models.random_data_request_dto import RandomDataRequestDto
from openapi_client.models.random_data_response_dto import RandomDataResponseDto
from openapi_client.models.range_attribute_constraint import RangeAttributeConstraint
from openapi_client.models.range_attribute_constraint_data import RangeAttributeConstraintData
from openapi_client.models.regexp_attribute_constraint import RegexpAttributeConstraint
from openapi_client.models.remove_certificate_dto import RemoveCertificateDto
from openapi_client.models.request_attribute_callback import RequestAttributeCallback
from openapi_client.models.request_attribute_dto import RequestAttributeDto
from openapi_client.models.resource import Resource
from openapi_client.models.resource_dto import ResourceDto
from openapi_client.models.resource_event_dto import ResourceEventDto
from openapi_client.models.resource_permissions_dto import ResourcePermissionsDto
from openapi_client.models.resource_permissions_request_dto import ResourcePermissionsRequestDto
from openapi_client.models.resource_record import ResourceRecord
from openapi_client.models.response_attribute_dto import ResponseAttributeDto
from openapi_client.models.response_metadata_dto import ResponseMetadataDto
from openapi_client.models.role_detail_dto import RoleDetailDto
from openapi_client.models.role_dto import RoleDto
from openapi_client.models.role_permissions_request_dto import RolePermissionsRequestDto
from openapi_client.models.role_request_dto import RoleRequestDto
from openapi_client.models.rule_detail_dto import RuleDetailDto
from openapi_client.models.rule_dto import RuleDto
from openapi_client.models.rule_request_dto import RuleRequestDto
from openapi_client.models.scep_profile_detail_dto import ScepProfileDetailDto
from openapi_client.models.scep_profile_dto import ScepProfileDto
from openapi_client.models.scep_profile_edit_request_dto import ScepProfileEditRequestDto
from openapi_client.models.scep_profile_request_dto import ScepProfileRequestDto
from openapi_client.models.schedule_discovery_dto import ScheduleDiscoveryDto
from openapi_client.models.scheduled_job_detail_dto import ScheduledJobDetailDto
from openapi_client.models.scheduled_job_dto import ScheduledJobDto
from openapi_client.models.scheduled_job_history_dto import ScheduledJobHistoryDto
from openapi_client.models.scheduled_job_history_response_dto import ScheduledJobHistoryResponseDto
from openapi_client.models.scheduled_jobs_response_dto import ScheduledJobsResponseDto
from openapi_client.models.scheduler_job_execution_status import SchedulerJobExecutionStatus
from openapi_client.models.search_field_data_by_group_dto import SearchFieldDataByGroupDto
from openapi_client.models.search_field_data_dto import SearchFieldDataDto
from openapi_client.models.search_filter_request_dto import SearchFilterRequestDto
from openapi_client.models.search_request_dto import SearchRequestDto
from openapi_client.models.secret_attribute_content import SecretAttributeContent
from openapi_client.models.secret_attribute_content_data import SecretAttributeContentData
from openapi_client.models.sign_data_request_dto import SignDataRequestDto
from openapi_client.models.sign_data_response_dto import SignDataResponseDto
from openapi_client.models.signature_request_data import SignatureRequestData
from openapi_client.models.signature_response_data import SignatureResponseData
from openapi_client.models.simplified_compliance_profile_dto import SimplifiedComplianceProfileDto
from openapi_client.models.simplified_ra_profile_dto import SimplifiedRaProfileDto
from openapi_client.models.source_record import SourceRecord
from openapi_client.models.statistics_dto import StatisticsDto
from openapi_client.models.string_attribute_content import StringAttributeContent
from openapi_client.models.subject_permissions_dto import SubjectPermissionsDto
from openapi_client.models.text_attribute_content import TextAttributeContent
from openapi_client.models.time_attribute_content import TimeAttributeContent
from openapi_client.models.token_instance_detail_dto import TokenInstanceDetailDto
from openapi_client.models.token_instance_dto import TokenInstanceDto
from openapi_client.models.token_instance_request_dto import TokenInstanceRequestDto
from openapi_client.models.token_instance_status import TokenInstanceStatus
from openapi_client.models.token_instance_status_component import TokenInstanceStatusComponent
from openapi_client.models.token_instance_status_detail_dto import TokenInstanceStatusDetailDto
from openapi_client.models.token_profile_detail_dto import TokenProfileDetailDto
from openapi_client.models.token_profile_dto import TokenProfileDto
from openapi_client.models.token_profile_key_usage_request_dto import TokenProfileKeyUsageRequestDto
from openapi_client.models.trigger_detail_dto import TriggerDetailDto
from openapi_client.models.trigger_dto import TriggerDto
from openapi_client.models.trigger_history_dto import TriggerHistoryDto
from openapi_client.models.trigger_history_object_summary_dto import TriggerHistoryObjectSummaryDto
from openapi_client.models.trigger_history_object_trigger_summary_dto import TriggerHistoryObjectTriggerSummaryDto
from openapi_client.models.trigger_history_record_dto import TriggerHistoryRecordDto
from openapi_client.models.trigger_history_summary_dto import TriggerHistorySummaryDto
from openapi_client.models.trigger_request_dto import TriggerRequestDto
from openapi_client.models.trigger_type import TriggerType
from openapi_client.models.update_action_request_dto import UpdateActionRequestDto
from openapi_client.models.update_condition_request_dto import UpdateConditionRequestDto
from openapi_client.models.update_execution_request_dto import UpdateExecutionRequestDto
from openapi_client.models.update_key_usage_request_dto import UpdateKeyUsageRequestDto
from openapi_client.models.update_rule_request_dto import UpdateRuleRequestDto
from openapi_client.models.update_scheduled_job import UpdateScheduledJob
from openapi_client.models.update_trigger_request_dto import UpdateTriggerRequestDto
from openapi_client.models.update_user_request_dto import UpdateUserRequestDto
from openapi_client.models.upload_certificate_request_dto import UploadCertificateRequestDto
from openapi_client.models.user_approval_dto import UserApprovalDto
from openapi_client.models.user_certificate_dto import UserCertificateDto
from openapi_client.models.user_detail_dto import UserDetailDto
from openapi_client.models.user_dto import UserDto
from openapi_client.models.user_identification_request_dto import UserIdentificationRequestDto
from openapi_client.models.utils_settings_dto import UtilsSettingsDto
from openapi_client.models.uuid_dto import UuidDto
from openapi_client.models.verification_response_data import VerificationResponseData
from openapi_client.models.verify_data_request_dto import VerifyDataRequestDto
from openapi_client.models.verify_data_response_dto import VerifyDataResponseDto
