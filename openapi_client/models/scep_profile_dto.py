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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.simplified_ra_profile_dto import SimplifiedRaProfileDto
from typing import Optional, Set
from typing_extensions import Self

class ScepProfileDto(BaseModel):
    """
    ScepProfileDto
    """ # noqa: E501
    uuid: StrictStr = Field(description="Object identifier")
    name: StrictStr = Field(description="Object Name")
    enabled: StrictBool = Field(description="Enabled flag - true = enabled; false = disabled")
    description: Optional[StrictStr] = Field(default=None, description="SCEP Profile description")
    ra_profile: Optional[SimplifiedRaProfileDto] = Field(default=None, alias="raProfile")
    include_ca_certificate: StrictBool = Field(description="Include CA certificate in the SCEP response", alias="includeCaCertificate")
    include_ca_certificate_chain: StrictBool = Field(description="Include CA certificate chain in the SCEP response", alias="includeCaCertificateChain")
    renew_threshold: Optional[StrictInt] = Field(default=None, description="Renewal time threshold in days", alias="renewThreshold")
    scep_url: Optional[StrictStr] = Field(default=None, description="SCEP URL", alias="scepUrl")
    enable_intune: Optional[StrictBool] = Field(default=None, description="Status of Intune", alias="enableIntune")
    __properties: ClassVar[List[str]] = ["uuid", "name", "enabled", "description", "raProfile", "includeCaCertificate", "includeCaCertificateChain", "renewThreshold", "scepUrl", "enableIntune"]

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
        """Create an instance of ScepProfileDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScepProfileDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "enabled": obj.get("enabled"),
            "description": obj.get("description"),
            "raProfile": SimplifiedRaProfileDto.from_dict(obj["raProfile"]) if obj.get("raProfile") is not None else None,
            "includeCaCertificate": obj.get("includeCaCertificate"),
            "includeCaCertificateChain": obj.get("includeCaCertificateChain"),
            "renewThreshold": obj.get("renewThreshold"),
            "scepUrl": obj.get("scepUrl"),
            "enableIntune": obj.get("enableIntune")
        })
        return _obj


