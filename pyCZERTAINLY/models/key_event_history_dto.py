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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class KeyEventHistoryDto(BaseModel):
    """
    KeyEventHistoryDto
    """ # noqa: E501
    uuid: StrictStr = Field(description="UUID of the event")
    key_uuid: StrictStr = Field(description="UUID of the Key", alias="keyUuid")
    created: datetime = Field(description="Event creation time")
    created_by: StrictStr = Field(description="Created By", alias="createdBy")
    event: StrictStr = Field(description="Event type")
    status: StrictStr = Field(description="Event result")
    message: StrictStr = Field(description="Event message")
    additional_information: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, description="Additional information for the event", alias="additionalInformation")
    __properties: ClassVar[List[str]] = ["uuid", "keyUuid", "created", "createdBy", "event", "status", "message", "additionalInformation"]

    @field_validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Create Key', 'Compromised Key', 'Destroy Key', 'Update Key Usages', 'Sign Data', 'Verify Data', 'Encrypt Data', 'Decrypt Data', 'Enable Key', 'Disable Key']):
            raise ValueError("must be one of enum values ('Create Key', 'Compromised Key', 'Destroy Key', 'Update Key Usages', 'Sign Data', 'Verify Data', 'Encrypt Data', 'Decrypt Data', 'Enable Key', 'Disable Key')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SUCCESS', 'FAILED']):
            raise ValueError("must be one of enum values ('SUCCESS', 'FAILED')")
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
        """Create an instance of KeyEventHistoryDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeyEventHistoryDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "keyUuid": obj.get("keyUuid"),
            "created": obj.get("created"),
            "createdBy": obj.get("createdBy"),
            "event": obj.get("event"),
            "status": obj.get("status"),
            "message": obj.get("message"),
            "additionalInformation": obj.get("additionalInformation")
        })
        return _obj


