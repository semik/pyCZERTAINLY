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
from pyCZERTAINLY.models.action_detail_dto import ActionDetailDto
from pyCZERTAINLY.models.resource import Resource
from pyCZERTAINLY.models.rule_detail_dto import RuleDetailDto
from pyCZERTAINLY.models.trigger_type import TriggerType
from typing import Optional, Set
from typing_extensions import Self

class TriggerDetailDto(BaseModel):
    """
    TriggerDetailDto
    """ # noqa: E501
    uuid: StrictStr = Field(description="Object identifier")
    name: StrictStr = Field(description="Object Name")
    description: Optional[StrictStr] = Field(default=None, description="Description of the trigger")
    type: TriggerType
    resource: Resource
    ignore_trigger: StrictBool = Field(description="Flag if to ignore object when trigger rules are matched and do not perform any actions and stop evaluating other triggers. Based on context could have other implications to object processing. If ignore is set, trigger does not have any actions.", alias="ignoreTrigger")
    event: Optional[StrictStr] = Field(default=None, description="Event that should fire trigger")
    event_resource: Optional[Resource] = Field(default=None, alias="eventResource")
    rules: List[RuleDetailDto] = Field(description="List of Rules in the Rule Trigger")
    actions: List[ActionDetailDto] = Field(description="List of Action Groups in the Rule Trigger")
    __properties: ClassVar[List[str]] = ["uuid", "name", "description", "type", "resource", "ignoreTrigger", "event", "eventResource", "rules", "actions"]

    @field_validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['discoveryFinished']):
            raise ValueError("must be one of enum values ('discoveryFinished')")
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
        """Create an instance of TriggerDetailDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item_rules in self.rules:
                if _item_rules:
                    _items.append(_item_rules.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item_actions in self.actions:
                if _item_actions:
                    _items.append(_item_actions.to_dict())
            _dict['actions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TriggerDetailDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "resource": obj.get("resource"),
            "ignoreTrigger": obj.get("ignoreTrigger"),
            "event": obj.get("event"),
            "eventResource": obj.get("eventResource"),
            "rules": [RuleDetailDto.from_dict(_item) for _item in obj["rules"]] if obj.get("rules") is not None else None,
            "actions": [ActionDetailDto.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None
        })
        return _obj


