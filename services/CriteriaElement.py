from dataclasses import dataclass
from enum import Enum
from typing import Any


class CriteriaElementOperation(Enum):
    EQUAL_TO = "EQUAL_TO"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    IN_LIST = "IN_LIST"
    CONTAINS = "CONTAINS"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"


@dataclass
class CriteriaElement:
    name: str
    operation: CriteriaElementOperation
    value: Any


def equal_to(name,value):
    return CriteriaElement(name,CriteriaElementOperation.EQUAL_TO,value)


def greater_than(name,value):
    return CriteriaElement(name, CriteriaElementOperation.GREATER_THAN, value)


def greater_than_or_equal(name,value):
    return CriteriaElement(name, CriteriaElementOperation.GREATER_THAN_OR_EQUAL, value)


def less_than(name,value):
    return CriteriaElement(name, CriteriaElementOperation.LESS_THAN, value)


def less_than_or_equal(name,value):
    return CriteriaElement(name, CriteriaElementOperation.LESS_THAN_OR_EQUAL, value)


def in_list(name,value):
    return CriteriaElement(name, CriteriaElementOperation.IN_LIST, value)


def starts_with(name,value):
    return CriteriaElement(name,CriteriaElementOperation.STARTS_WITH,value)


def ends_with(name,value):
    return CriteriaElement(name,CriteriaElementOperation.ENDS_WITH,value)


def contains(name,value):
    return CriteriaElement(name, CriteriaElementOperation.CONTAINS, value)



