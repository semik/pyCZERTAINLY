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


class Module(str, Enum):
    """
    Module of platform where log occurred
    """

    """
    allowed enum values
    """
    APPROVALS = 'approvals'
    AUTH = 'auth'
    CERTIFICATES = 'certificates'
    KEYS = 'keys'
    COMPLIANCE = 'compliance'
    CORE = 'core'
    DISCOVERY = 'discovery'
    ENTITIES = 'entities'
    PROTOCOLS = 'protocols'
    SCHEDULER = 'scheduler'
    WORKFLOWS = 'workflows'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Module from a JSON string"""
        return cls(json.loads(json_str))


