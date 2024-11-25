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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.certificate_dto import CertificateDto
from openapi_client.models.protection_method import ProtectionMethod
from openapi_client.models.response_attribute_dto import ResponseAttributeDto
from openapi_client.models.simplified_ra_profile_dto import SimplifiedRaProfileDto
from typing import Optional, Set
from typing_extensions import Self

class CmpProfileDetailDto(BaseModel):
    """
    CmpProfileDetailDto
    """ # noqa: E501
    uuid: StrictStr = Field(description="Object identifier")
    name: StrictStr = Field(description="Object Name")
    enabled: StrictBool = Field(description="Enabled flag - true = enabled; false = disabled")
    variant: StrictStr = Field(description="Variant of the CMP Profile")
    description: Optional[StrictStr] = Field(default=None, description="CMP Profile description")
    ra_profile: Optional[SimplifiedRaProfileDto] = Field(default=None, alias="raProfile")
    cmp_url: Optional[StrictStr] = Field(default=None, description="CMP URL", alias="cmpUrl")
    issue_certificate_attributes: Optional[List[ResponseAttributeDto]] = Field(default=None, description="List of Attributes to issue a Certificate for the associated RA Profile", alias="issueCertificateAttributes")
    revoke_certificate_attributes: Optional[List[ResponseAttributeDto]] = Field(default=None, description="List of Attributes to revoke a Certificate for the associated RA Profile", alias="revokeCertificateAttributes")
    custom_attributes: Optional[List[ResponseAttributeDto]] = Field(default=None, description="List of Custom Attributes for CMP Profile", alias="customAttributes")
    request_protection_method: ProtectionMethod = Field(alias="requestProtectionMethod")
    response_protection_method: ProtectionMethod = Field(alias="responseProtectionMethod")
    signing_certificate: Optional[CertificateDto] = Field(default=None, alias="signingCertificate")
    __properties: ClassVar[List[str]] = ["uuid", "name", "enabled", "variant", "description", "raProfile", "cmpUrl", "issueCertificateAttributes", "revokeCertificateAttributes", "customAttributes", "requestProtectionMethod", "responseProtectionMethod", "signingCertificate"]

    @field_validator('variant')
    def variant_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['v2', 'v2_3gpp', 'v3']):
            raise ValueError("must be one of enum values ('v2', 'v2_3gpp', 'v3')")
        return value

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
        """Create an instance of CmpProfileDetailDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in issue_certificate_attributes (list)
        _items = []
        if self.issue_certificate_attributes:
            for _item_issue_certificate_attributes in self.issue_certificate_attributes:
                if _item_issue_certificate_attributes:
                    _items.append(_item_issue_certificate_attributes.to_dict())
            _dict['issueCertificateAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in revoke_certificate_attributes (list)
        _items = []
        if self.revoke_certificate_attributes:
            for _item_revoke_certificate_attributes in self.revoke_certificate_attributes:
                if _item_revoke_certificate_attributes:
                    _items.append(_item_revoke_certificate_attributes.to_dict())
            _dict['revokeCertificateAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_attributes (list)
        _items = []
        if self.custom_attributes:
            for _item_custom_attributes in self.custom_attributes:
                if _item_custom_attributes:
                    _items.append(_item_custom_attributes.to_dict())
            _dict['customAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of signing_certificate
        if self.signing_certificate:
            _dict['signingCertificate'] = self.signing_certificate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CmpProfileDetailDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "enabled": obj.get("enabled"),
            "variant": obj.get("variant"),
            "description": obj.get("description"),
            "raProfile": SimplifiedRaProfileDto.from_dict(obj["raProfile"]) if obj.get("raProfile") is not None else None,
            "cmpUrl": obj.get("cmpUrl"),
            "issueCertificateAttributes": [ResponseAttributeDto.from_dict(_item) for _item in obj["issueCertificateAttributes"]] if obj.get("issueCertificateAttributes") is not None else None,
            "revokeCertificateAttributes": [ResponseAttributeDto.from_dict(_item) for _item in obj["revokeCertificateAttributes"]] if obj.get("revokeCertificateAttributes") is not None else None,
            "customAttributes": [ResponseAttributeDto.from_dict(_item) for _item in obj["customAttributes"]] if obj.get("customAttributes") is not None else None,
            "requestProtectionMethod": obj.get("requestProtectionMethod"),
            "responseProtectionMethod": obj.get("responseProtectionMethod"),
            "signingCertificate": CertificateDto.from_dict(obj["signingCertificate"]) if obj.get("signingCertificate") is not None else None
        })
        return _obj


