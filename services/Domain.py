from dataclasses import dataclass
from typing import List
from enum import Enum


class ContactPointType(str, Enum):
    PHONE = "PHONE"
    EMAIL = "EMAIL"
    FACEBOOK = "FACEBOOK"
    TWITTER = "TWITTER"
    LINKEDIN = "LINKEDIN"
    GITHUB = "GITHUB"


@dataclass
class Address():
    addressee: str
    line1: str
    line2: str
    city: str
    state: str
    postal_code: str
    country: str

@dataclass
class ContactPoint():
    type: ContactPointType
    user_name: str
    authenticated: bool

@dataclass
class Person():
    id: str
    name: str
    employee_id: str
    contact_points: List[ContactPoint]
    addresses: List[Address]

@dataclass
class PersonList():
    personList: List[Person]