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
from openapi_client.models.response_attribute_dto import ResponseAttributeDto
from typing import Optional, Set
from typing_extensions import Self

class CredentialDto(BaseModel):
    """
    CredentialDto
    """ # noqa: E501
    uuid: StrictStr = Field(description="Object identifier")
    name: StrictStr = Field(description="Object Name")
    kind: StrictStr = Field(description="Credential Kind")
    attributes: List[ResponseAttributeDto] = Field(description="List of Credential Attributes")
    custom_attributes: Optional[List[ResponseAttributeDto]] = Field(default=None, description="List of Custom Attributes", alias="customAttributes")
    enabled: StrictBool = Field(description="Enabled flag - true = enabled; false = disabled")
    connector_uuid: StrictStr = Field(description="UUID of Credential provider Connector", alias="connectorUuid")
    connector_name: StrictStr = Field(description="Name of Credential provider Connector", alias="connectorName")
    __properties: ClassVar[List[str]] = ["uuid", "name", "kind", "attributes", "customAttributes", "enabled", "connectorUuid", "connectorName"]

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
        """Create an instance of CredentialDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item_attributes in self.attributes:
                if _item_attributes:
                    _items.append(_item_attributes.to_dict())
            _dict['attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_attributes (list)
        _items = []
        if self.custom_attributes:
            for _item_custom_attributes in self.custom_attributes:
                if _item_custom_attributes:
                    _items.append(_item_custom_attributes.to_dict())
            _dict['customAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CredentialDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "kind": obj.get("kind"),
            "attributes": [ResponseAttributeDto.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None,
            "customAttributes": [ResponseAttributeDto.from_dict(_item) for _item in obj["customAttributes"]] if obj.get("customAttributes") is not None else None,
            "enabled": obj.get("enabled"),
            "connectorUuid": obj.get("connectorUuid"),
            "connectorName": obj.get("connectorName")
        })
        return _obj


