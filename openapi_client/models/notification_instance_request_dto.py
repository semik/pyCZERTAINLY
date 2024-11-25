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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.attribute_mapping_dto import AttributeMappingDto
from openapi_client.models.request_attribute_dto import RequestAttributeDto
from typing import Optional, Set
from typing_extensions import Self

class NotificationInstanceRequestDto(BaseModel):
    """
    NotificationInstanceRequestDto
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Notification instance description")
    attributes: List[RequestAttributeDto] = Field(description="List of Notification instance Attributes")
    attribute_mappings: Optional[List[AttributeMappingDto]] = Field(default=None, description="List of attribute mappings between mapping attributes and (recipient) custom attributes", alias="attributeMappings")
    name: StrictStr = Field(description="Notification instance name")
    connector_uuid: StrictStr = Field(description="UUID of Notification provider", alias="connectorUuid")
    kind: StrictStr = Field(description="Notification instance Kind")
    __properties: ClassVar[List[str]] = ["description", "attributes", "attributeMappings", "name", "connectorUuid", "kind"]

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
        """Create an instance of NotificationInstanceRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_mappings (list)
        _items = []
        if self.attribute_mappings:
            for _item_attribute_mappings in self.attribute_mappings:
                if _item_attribute_mappings:
                    _items.append(_item_attribute_mappings.to_dict())
            _dict['attributeMappings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationInstanceRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "attributes": [RequestAttributeDto.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None,
            "attributeMappings": [AttributeMappingDto.from_dict(_item) for _item in obj["attributeMappings"]] if obj.get("attributeMappings") is not None else None,
            "name": obj.get("name"),
            "connectorUuid": obj.get("connectorUuid"),
            "kind": obj.get("kind")
        })
        return _obj


