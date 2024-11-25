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
from typing import Optional, Set
from typing_extensions import Self

class DataAttributeProperties(BaseModel):
    """
    Properties of the Attributes
    """ # noqa: E501
    label: StrictStr = Field(description="Friendly name of the the Attribute")
    visible: StrictBool = Field(description="Boolean determining if the Attribute is visible and can be displayed, otherwise it should be hidden to the user.")
    group: Optional[StrictStr] = Field(default=None, description="Group of the Attribute, used for the logical grouping of the Attribute")
    required: StrictBool = Field(description="Boolean determining if the Attribute is required. If true, the Attribute must be provided.")
    read_only: StrictBool = Field(description="Boolean determining if the Attribute is read only. If true, the Attribute content cannot be changed.", alias="readOnly")
    list: StrictBool = Field(description="Boolean determining if the Attribute contains list of values in the content")
    multi_select: StrictBool = Field(description="Boolean determining if the Attribute can have multiple values", alias="multiSelect")
    __properties: ClassVar[List[str]] = ["label", "visible", "group", "required", "readOnly", "list", "multiSelect"]

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
        """Create an instance of DataAttributeProperties from a JSON string"""
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
        """Create an instance of DataAttributeProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "label": obj.get("label"),
            "visible": obj.get("visible") if obj.get("visible") is not None else True,
            "group": obj.get("group"),
            "required": obj.get("required") if obj.get("required") is not None else False,
            "readOnly": obj.get("readOnly") if obj.get("readOnly") is not None else False,
            "list": obj.get("list") if obj.get("list") is not None else False,
            "multiSelect": obj.get("multiSelect") if obj.get("multiSelect") is not None else False
        })
        return _obj


