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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pyCZERTAINLY.models.certificate_state import CertificateState
from pyCZERTAINLY.models.certificate_type import CertificateType
from pyCZERTAINLY.models.certificate_validation_status import CertificateValidationStatus
from pyCZERTAINLY.models.compliance_status import ComplianceStatus
from pyCZERTAINLY.models.group_dto import GroupDto
from pyCZERTAINLY.models.simplified_ra_profile_dto import SimplifiedRaProfileDto
from typing import Optional, Set
from typing_extensions import Self

class CertificateDto(BaseModel):
    """
    CA Certificate for the SCEP Profile
    """ # noqa: E501
    uuid: StrictStr = Field(description="UUID of the Certificate")
    common_name: StrictStr = Field(description="Certificate common name", alias="commonName")
    serial_number: Optional[StrictStr] = Field(default=None, description="Certificate serial number", alias="serialNumber")
    issuer_common_name: Optional[StrictStr] = Field(default=None, description="Certificate issuer common name", alias="issuerCommonName")
    issuer_dn: Optional[StrictStr] = Field(default=None, description="Issuer DN of the Certificate", alias="issuerDn")
    subject_dn: StrictStr = Field(description="Subject DN of the Certificate", alias="subjectDn")
    not_before: Optional[datetime] = Field(default=None, description="Certificate validity start date", alias="notBefore")
    not_after: Optional[datetime] = Field(default=None, description="Certificate expiration date", alias="notAfter")
    public_key_algorithm: StrictStr = Field(description="Public key algorithm", alias="publicKeyAlgorithm")
    signature_algorithm: StrictStr = Field(description="Certificate signature algorithm", alias="signatureAlgorithm")
    key_size: StrictInt = Field(description="Certificate key size", alias="keySize")
    state: CertificateState
    validation_status: CertificateValidationStatus = Field(alias="validationStatus")
    ra_profile: Optional[SimplifiedRaProfileDto] = Field(default=None, alias="raProfile")
    fingerprint: Optional[StrictStr] = Field(default=None, description="SHA256 fingerprint of the Certificate")
    groups: Optional[List[GroupDto]] = Field(default=None, description="Groups associated to the Certificate")
    owner: Optional[StrictStr] = Field(default=None, description="Certificate Owner")
    owner_uuid: Optional[StrictStr] = Field(default=None, description="Certificate Owner UUID", alias="ownerUuid")
    certificate_type: Optional[CertificateType] = Field(default=None, alias="certificateType")
    issuer_serial_number: Optional[StrictStr] = Field(default=None, description="Serial number of the issuer", alias="issuerSerialNumber")
    compliance_status: Optional[ComplianceStatus] = Field(default=None, alias="complianceStatus")
    issuer_certificate_uuid: Optional[StrictStr] = Field(default=None, description="UUID of the issuer certificate", alias="issuerCertificateUuid")
    private_key_availability: StrictBool = Field(description="Private Key Availability", alias="privateKeyAvailability")
    trusted_ca: StrictBool = Field(description="Indicator whether CA is marked as trusted, set to null if certificate is not CA", alias="trustedCa")
    __properties: ClassVar[List[str]] = ["uuid", "commonName", "serialNumber", "issuerCommonName", "issuerDn", "subjectDn", "notBefore", "notAfter", "publicKeyAlgorithm", "signatureAlgorithm", "keySize", "state", "validationStatus", "raProfile", "fingerprint", "groups", "owner", "ownerUuid", "certificateType", "issuerSerialNumber", "complianceStatus", "issuerCertificateUuid", "privateKeyAvailability", "trustedCa"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CertificateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ra_profile
        if self.ra_profile:
            _dict['raProfile'] = self.ra_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CertificateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "commonName": obj.get("commonName"),
            "serialNumber": obj.get("serialNumber"),
            "issuerCommonName": obj.get("issuerCommonName"),
            "issuerDn": obj.get("issuerDn"),
            "subjectDn": obj.get("subjectDn"),
            "notBefore": obj.get("notBefore"),
            "notAfter": obj.get("notAfter"),
            "publicKeyAlgorithm": obj.get("publicKeyAlgorithm"),
            "signatureAlgorithm": obj.get("signatureAlgorithm"),
            "keySize": obj.get("keySize"),
            "state": obj.get("state"),
            "validationStatus": obj.get("validationStatus"),
            "raProfile": SimplifiedRaProfileDto.from_dict(obj["raProfile"]) if obj.get("raProfile") is not None else None,
            "fingerprint": obj.get("fingerprint"),
            "groups": [GroupDto.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "owner": obj.get("owner"),
            "ownerUuid": obj.get("ownerUuid"),
            "certificateType": obj.get("certificateType"),
            "issuerSerialNumber": obj.get("issuerSerialNumber"),
            "complianceStatus": obj.get("complianceStatus"),
            "issuerCertificateUuid": obj.get("issuerCertificateUuid"),
            "privateKeyAvailability": obj.get("privateKeyAvailability"),
            "trustedCa": obj.get("trustedCa")
        })
        return _obj


