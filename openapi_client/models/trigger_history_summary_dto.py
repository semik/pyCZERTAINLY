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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_client.models.resource import Resource
from openapi_client.models.trigger_history_object_summary_dto import TriggerHistoryObjectSummaryDto
from typing import Optional, Set
from typing_extensions import Self

class TriggerHistorySummaryDto(BaseModel):
    """
    TriggerHistorySummaryDto
    """ # noqa: E501
    association_resource: Resource = Field(alias="associationResource")
    association_object_uuid: StrictStr = Field(description="UUID of the object associated with triggers.", alias="associationObjectUuid")
    objects_resource: Resource = Field(alias="objectsResource")
    objects_evaluated: StrictInt = Field(description="Number of objects evaluated.", alias="objectsEvaluated")
    objects_matched: StrictInt = Field(description="Number of objects matched at least by one trigger.", alias="objectsMatched")
    objects_ignored: StrictInt = Field(description="Number of objects matched by ignore triggers.", alias="objectsIgnored")
    objects: List[TriggerHistoryObjectSummaryDto] = Field(description="List of history of objects that triggers has been evaluated on.")
    __properties: ClassVar[List[str]] = ["associationResource", "associationObjectUuid", "objectsResource", "objectsEvaluated", "objectsMatched", "objectsIgnored", "objects"]

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
        """Create an instance of TriggerHistorySummaryDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TriggerHistorySummaryDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associationResource": obj.get("associationResource"),
            "associationObjectUuid": obj.get("associationObjectUuid"),
            "objectsResource": obj.get("objectsResource"),
            "objectsEvaluated": obj.get("objectsEvaluated"),
            "objectsMatched": obj.get("objectsMatched"),
            "objectsIgnored": obj.get("objectsIgnored"),
            "objects": [TriggerHistoryObjectSummaryDto.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None
        })
        return _obj


