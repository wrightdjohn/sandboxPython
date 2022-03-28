from services.CriteriaElement import equal_to
from services.CriteriaElement import greater_than
from services.CriteriaElement import greater_than_or_equal
from services.CriteriaElement import less_than
from services.CriteriaElement import less_than_or_equal
from services.CriteriaElement import in_list
from services.CriteriaElement import starts_with
from services.CriteriaElement import ends_with
from services.CriteriaElement import contains


class RetrievePersonsRequest:
    def __init__(self, person_id=None, person_criteria=None):
        self._person_id = person_id
        self._person_criteria = person_criteria

    def get_person_id(self):
        return self._person_id

    def get_person_criteria(self):
        return self._person_criteria


class RetrievePersonsResponse:
    def __init__(self, persons):
        self._persons = persons

    def get_person_list(self):
        return self._persons


class RetrievePersonsService:
    def __init__(self, finder):
        self._finder = finder

    def execute_request(self, request):
        id = request.get_person_id()
        if id is None:
            criteria = request.get_person_criteria()
            persons = self._finder.find_by_criteria(criteria)
            return RetrievePersonsResponse(persons)
        else:
            person = self._finder.find_by_id(id)
            return RetrievePersonsResponse([person])


class PersonRetrieveCriteria:
    def __init__(self):
        self._elements=[]

    def is_empty(self):
        return len(self._elements) == 0

    def elements(self):
        return self._elements

    @staticmethod
    def not_empty(s):
        if s is None: return False
        if len(s.strip()) == 0: return False
        return True

    def common_filter(self, name, value, func):
        if self.not_empty(value):
            self._elements.append(func(name,value))

        return self

    def name_is_equal_to(self, name_value):
        self.common_filter("name",name_value,equal_to)

    def name_starts_with(self, name_value):
        self.common_filter("name",name_value,starts_with)

    def name_ends_with(self, name_value):
        self.common_filter("name",name_value,ends_with)

    def name_contains(self, name_value):
        self.common_filter("name",name_value,contains)

    def employee_id_equal_to(self, name_value):
        self.common_filter("employeeId",name_value,equal_to)

    def has_address_with_city(self, name_value):
        self.common_filter("addresses.city", name_value, equal_to)

    def has_address_with_state(self, name_value):
        self.common_filter("addresses.state", name_value, equal_to)

    def has_address_with_country(self, name_value):
        self.common_filter("addresses.country", name_value, equal_to)

    def has_address_with_postal_code(self, name_value):
        self.common_filter("addresses.postalCode", name_value, equal_to)