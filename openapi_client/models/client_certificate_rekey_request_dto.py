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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.certificate_request_format import CertificateRequestFormat
from openapi_client.models.request_attribute_dto import RequestAttributeDto
from typing import Optional, Set
from typing_extensions import Self

class ClientCertificateRekeyRequestDto(BaseModel):
    """
    ClientCertificateRekeyRequestDto
    """ # noqa: E501
    replace_in_locations: Optional[StrictBool] = Field(default=False, description="True to replace renewed certificate in the associated locations", alias="replaceInLocations")
    request: Optional[StrictStr] = Field(default=None, description="Certificate signing request encoded as Base64 string. If not provided, CSR attributes will be used")
    format: Optional[CertificateRequestFormat] = CertificateRequestFormat.PKCS10
    key_uuid: StrictStr = Field(description="Key UUID", alias="keyUuid")
    token_profile_uuid: StrictStr = Field(description="Token Profile UUID", alias="tokenProfileUuid")
    signature_attributes: Optional[List[RequestAttributeDto]] = Field(default=None, description="Signature Attributes. If not provided, existing attributes will be used to generate the new CSR", alias="signatureAttributes")
    __properties: ClassVar[List[str]] = ["replaceInLocations", "request", "format", "keyUuid", "tokenProfileUuid", "signatureAttributes"]

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
        """Create an instance of ClientCertificateRekeyRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in signature_attributes (list)
        _items = []
        if self.signature_attributes:
            for _item_signature_attributes in self.signature_attributes:
                if _item_signature_attributes:
                    _items.append(_item_signature_attributes.to_dict())
            _dict['signatureAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientCertificateRekeyRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "replaceInLocations": obj.get("replaceInLocations") if obj.get("replaceInLocations") is not None else False,
            "request": obj.get("request"),
            "format": obj.get("format") if obj.get("format") is not None else CertificateRequestFormat.PKCS10,
            "keyUuid": obj.get("keyUuid"),
            "tokenProfileUuid": obj.get("tokenProfileUuid"),
            "signatureAttributes": [RequestAttributeDto.from_dict(_item) for _item in obj["signatureAttributes"]] if obj.get("signatureAttributes") is not None else None
        })
        return _obj


