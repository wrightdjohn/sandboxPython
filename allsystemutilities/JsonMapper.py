import json

from services.Domain import ContactPointType
from services.Domain import Person
from services.Domain import Address
from services.Domain import ContactPoint
from services.implementations.RetrievePersons import PersonRetrieveCriteria


class JsonMapper:
    @staticmethod
    def map_request_args_to_criteria(args):
        criteria = PersonRetrieveCriteria()
        criteria.name_is_equal_to(args.get("nameIsEqualTo", default=None, type=str))
        criteria.name_starts_with(args.get("name_starts_with", default=None, type=str))
        criteria.name_ends_with(args.get("name_ends_with", default=None, type=str))
        criteria.name_contains(args.get("nameContains", default=None, type=str))
        criteria.employee_id_equal_to(args.get("employeeIdEqualTo", default=None, type=str))
        criteria.has_address_with_city(args.get("hasAddressWithCity", default=None, type=str))
        criteria.has_address_with_state(args.get("hasAddressWithState", default=None, type=str))
        criteria.has_address_with_postal_code(args.get("hasAddressWithPostalCode", default=None, type=str))
        criteria.has_address_with_country(args.get("hasAddressWithCountry", default=None, type=str))
        return criteria

    def map_person_from_json(self, json_str):
        body = json.loads(json_str)
        cp_list = self.map_contact_points_from_json(body["contactPoints"])
        address_list = self.map_addresses_from_json(body["addresses"])
        return Person(body["_id"], body["name"], body["employeeId"], cp_list, address_list)

    def map_persons_from_list_of_dict(self, dict_list):
        person_array = []
        for person_dict in dict_list:
            person_array.append(self.map_person_from_dict(person_dict))

        return person_array

    def map_person_from_dict(self, person_dict):
        address_list = [self.map_address_from_dict(address) for address in person_dict["addresses"]]
        cp_list = [self.map_contact_point_from_dict(cp) for cp in person_dict["contactPoints"]]
        return Person(str(person_dict["_id"]), person_dict["name"], person_dict["employeeId"], cp_list, address_list)

    def map_person_to_json(self, person):
        return json.dumps(self.map_person_to_dict(person), skipkeys=False, indent=4)

    def map_persons_to_json(self,persons):
        person_dict_list = [self.map_person_to_dict(person) for person in persons]
        return json.dumps({"personList":person_dict_list})

    def map_person_to_dict(self,person):
        address_array = []
        for address in person.addresses:
            address_array.append(self.map_address_to_dict(address))

        cp_array = []
        for contact_point in person.contact_points:
            cp_array.append(self.map_contact_point_dict(contact_point))

        if person.id is None:
            temp_dict = \
                {"name": person.name, "employeeId": person.employee_id,
                 "contactPoints": cp_array, "addresses": address_array}
        else:
            temp_dict = \
                {"_id": person.id, "name": person.name, "employeeId": person.employee_id,
                 "contactPoints": cp_array, "addresses": address_array}

        return temp_dict

    def map_contact_points_from_json(self, cp_json_array):
        result = []
        for cp_json in cp_json_array:
            result.append(self.map_contact_point_from_dict(cp_json))
        return result

    def map_contact_point_from_json(self, cp_json):
        return self.map_contact_point_from_dict(json.loads(cp_json))

    @staticmethod
    def map_contact_point_from_dict(cp_dict):
        return ContactPoint(ContactPointType(cp_dict["type"]), cp_dict["userName"], cp_dict["authenticated"])

    def map_contact_point_to_json(self, cp):
        return json.dumps(self.map_contact_point_dict(cp), indent=4)

    @staticmethod
    def map_contact_point_dict(cp):
        if cp.authenticated:
            return {"type": cp.type.value, "userName": cp.user_name, "authenticated": True}
        else:
            return {"type": cp.type.value, "userName": cp.user_name, "authenticated": False}

    def map_addresses_from_json(self, address_json_array):
        result = []
        for address_dict in address_json_array:
            result.append(self.map_address_from_dict(address_dict))
        return result

    def map_address_from_json(self, address_json):
        return self.map_address_from_dict(json.loads(address_json))

    @staticmethod
    def map_address_from_dict(address_dict):
        return Address(address_dict["addressee"],
                       address_dict["line1"], address_dict["line2"],
                       address_dict["city"], address_dict["state"], address_dict["postalCode"],
                       address_dict["country"])

    def map_address_to_json(self, address):
        return json.dumps(self.map_address_to_dict(address), indent=4)

    @staticmethod
    def map_address_to_dict(address):
        return {"addressee": address.addressee, "line1": address.line1, "line2": address.line2, "city": address.city,
                "state": address.state, "postalCode": address.postal_code, "country": address.country}
