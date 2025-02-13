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


class CertificateValidationCheck(str, Enum):
    """
    Certificate validation check type
    """

    """
    allowed enum values
    """
    CERTIFICATE_CHAIN = 'certificate_chain'
    SIGNATURE = 'signature'
    CERTIFICATE_VALIDITY = 'certificate_validity'
    OCSP_VERIFICATION = 'ocsp_verification'
    CRL_VERIFICATION = 'crl_verification'
    BASIC_CONSTRAINTS = 'basic_constraints'
    KEY_USAGE = 'key_usage'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CertificateValidationCheck from a JSON string"""
        return cls(json.loads(json_str))


