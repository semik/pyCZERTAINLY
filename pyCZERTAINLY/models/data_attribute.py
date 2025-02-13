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
from pyCZERTAINLY.models.attribute_callback import AttributeCallback
from pyCZERTAINLY.models.attribute_content_type import AttributeContentType
from pyCZERTAINLY.models.attribute_type import AttributeType
from pyCZERTAINLY.models.base_attribute_constraint import BaseAttributeConstraint
from pyCZERTAINLY.models.data_attribute_properties import DataAttributeProperties
from typing import Optional, Set
from typing_extensions import Self

class DataAttribute(BaseModel):
    """
    Data attribute allows to store and transfer dynamic data. Its content can be edited and send in requests to store.
    """ # noqa: E501
    uuid: StrictStr = Field(description="UUID of the Attribute for unique identification")
    name: StrictStr = Field(description="Name of the Attribute that is used for identification")
    description: Optional[StrictStr] = Field(default=None, description="Optional description of the Attribute, should contain helper text on what is expected")
    type: AttributeType
    content_type: AttributeContentType = Field(alias="contentType")
    properties: DataAttributeProperties
    constraints: Optional[List[BaseAttributeConstraint]] = Field(default=None, description="Optional regular expressions and constraints used for validating the Attribute content")
    attribute_callback: Optional[AttributeCallback] = Field(default=None, alias="attributeCallback")
    __properties: ClassVar[List[str]] = ["uuid", "name", "description", "type", "contentType", "properties", "constraints", "attributeCallback"]

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
        """Create an instance of DataAttribute from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in constraints (list)
        _items = []
        if self.constraints:
            for _item_constraints in self.constraints:
                if _item_constraints:
                    _items.append(_item_constraints.to_dict())
            _dict['constraints'] = _items
        # override the default output from pydantic by calling `to_dict()` of attribute_callback
        if self.attribute_callback:
            _dict['attributeCallback'] = self.attribute_callback.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "contentType": obj.get("contentType"),
            "properties": DataAttributeProperties.from_dict(obj["properties"]) if obj.get("properties") is not None else None,
            "constraints": [BaseAttributeConstraint.from_dict(_item) for _item in obj["constraints"]] if obj.get("constraints") is not None else None,
            "attributeCallback": AttributeCallback.from_dict(obj["attributeCallback"]) if obj.get("attributeCallback") is not None else None
        })
        return _obj


