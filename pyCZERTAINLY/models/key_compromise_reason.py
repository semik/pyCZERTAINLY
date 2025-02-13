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


class KeyCompromiseReason(str, Enum):
    """
    Reason for Compromise
    """

    """
    allowed enum values
    """
    DISCLOSURE = 'disclosure'
    MODIFICATION = 'modification'
    SUBSTITUTION = 'substitution'
    USE_OF_SENSITIVE_DATA = 'use_of_sensitive_data'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of KeyCompromiseReason from a JSON string"""
        return cls(json.loads(json_str))


