# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from currency_exchange_fapi_client.models.access_expires_in import AccessExpiresIn
from currency_exchange_fapi_client.models.refresh_expires_in import RefreshExpiresIn
from typing import Optional, Set
from typing_extensions import Self

class TokenCreatedResponse(BaseModel):
    """
    TokenCreatedResponse
    """ # noqa: E501
    access_token: StrictStr
    token_type: StrictStr
    access_expires_in: AccessExpiresIn
    refresh_token: Optional[StrictStr] = None
    refresh_expires_in: Optional[RefreshExpiresIn]
    scope: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["access_token", "token_type", "access_expires_in", "refresh_token", "refresh_expires_in", "scope"]

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
        """Create an instance of TokenCreatedResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_expires_in
        if self.access_expires_in:
            _dict['access_expires_in'] = self.access_expires_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refresh_expires_in
        if self.refresh_expires_in:
            _dict['refresh_expires_in'] = self.refresh_expires_in.to_dict()
        # set to None if refresh_token (nullable) is None
        # and model_fields_set contains the field
        if self.refresh_token is None and "refresh_token" in self.model_fields_set:
            _dict['refresh_token'] = None

        # set to None if refresh_expires_in (nullable) is None
        # and model_fields_set contains the field
        if self.refresh_expires_in is None and "refresh_expires_in" in self.model_fields_set:
            _dict['refresh_expires_in'] = None

        # set to None if scope (nullable) is None
        # and model_fields_set contains the field
        if self.scope is None and "scope" in self.model_fields_set:
            _dict['scope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TokenCreatedResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_token": obj.get("access_token"),
            "token_type": obj.get("token_type"),
            "access_expires_in": AccessExpiresIn.from_dict(obj["access_expires_in"]) if obj.get("access_expires_in") is not None else None,
            "refresh_token": obj.get("refresh_token"),
            "refresh_expires_in": RefreshExpiresIn.from_dict(obj["refresh_expires_in"]) if obj.get("refresh_expires_in") is not None else None,
            "scope": obj.get("scope")
        })
        return _obj


