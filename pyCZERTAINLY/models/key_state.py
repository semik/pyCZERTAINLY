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


class KeyState(str, Enum):
    """
    Key State
    """

    """
    allowed enum values
    """
    PRE_MINUS_ACTIVE = 'pre-active'
    ACTIVE = 'active'
    DEACTIVATED = 'deactivated'
    COMPROMISED = 'compromised'
    DESTROYED = 'destroyed'
    DESTROYEDCOMPROMISED = 'destroyedCompromised'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of KeyState from a JSON string"""
        return cls(json.loads(json_str))


