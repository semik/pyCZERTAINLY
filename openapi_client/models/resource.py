# coding: utf-8

"""
    CZERTAINLY Core API

    REST API for CZERTAINLY Core

    The version of the OpenAPI document: 2.13.2-SNAPSHOT
    Contact: info@czertainly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Resource(str, Enum):
    """
    Type of the the trigger event source object
    """

    """
    allowed enum values
    """
    NONE = 'NONE'
    DASHBOARD = 'dashboard'
    SETTINGS = 'settings'
    AUDITLOGS = 'auditLogs'
    CREDENTIALS = 'credentials'
    CONNECTORS = 'connectors'
    ATTRIBUTES = 'attributes'
    JOBS = 'jobs'
    NOTIFICATIONINSTANCES = 'notificationInstances'
    USERS = 'users'
    ROLES = 'roles'
    ACMEACCOUNTS = 'acmeAccounts'
    ACMEPROFILES = 'acmeProfiles'
    SCEPPROFILES = 'scepProfiles'
    CMPPROFILES = 'cmpProfiles'
    AUTHORITIES = 'authorities'
    RAPROFILES = 'raProfiles'
    CERTIFICATES = 'certificates'
    CERTIFICATEREQUESTS = 'certificateRequests'
    GROUPS = 'groups'
    COMPLIANCEPROFILES = 'complianceProfiles'
    DISCOVERIES = 'discoveries'
    ENTITIES = 'entities'
    LOCATIONS = 'locations'
    TOKENPROFILES = 'tokenProfiles'
    TOKENS = 'tokens'
    KEYS = 'keys'
    APPROVALPROFILES = 'approvalProfiles'
    APPROVALS = 'approvals'
    RULES = 'rules'
    ACTIONS = 'actions'
    TRIGGERS = 'triggers'
    RESOURCES = 'resources'
    RESOURCEEVENTS = 'resourceEvents'
    SEARCHFILTERS = 'searchFilters'
    KEYITEMS = 'keyItems'
    PLATFORMENUMS = 'platformEnums'
    NOTIFICATIONS = 'notifications'
    CONDITIONS = 'conditions'
    EXECUTIONS = 'executions'
    COMPLIANCERULES = 'complianceRules'
    COMPLIANCEGROUPS = 'complianceGroups'
    CUSTOMATTRIBUTES = 'customAttributes'
    GLOBALMETADATA = 'globalMetadata'
    ACMEORDERS = 'acmeOrders'
    ACMEAUTHORIZATIONS = 'acmeAuthorizations'
    ACMECHALLENGES = 'acmeChallenges'
    CMPTRANSACTIONS = 'cmpTransactions'
    ENDENTITYPROFILE = 'endEntityProfile'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Resource from a JSON string"""
        return cls(json.loads(json_str))


