import unittest
from allsystemutilities.JsonMapper import JsonMapper
from services.Domain import ContactPointType
from services.StartupData import startup_data
import json


class TestJsonMapper(unittest.TestCase):
    def setUp(self):
        self.json_mapper = JsonMapper()
        self.startup_data = startup_data()
        self.joe_black = self.startup_data.joe_black
        self.jim_borman = self.startup_data.jim_borman
        self.jessica_wilde = self.startup_data.jessica_wilde
        self.virginia_otoole = self.startup_data.virginia_o_toole
        self.martin_lake = self.startup_data.martin_lake
        self.preeta_smith = self.startup_data.preeta_smith

    @staticmethod
    def assert_address_dict(json_dict):
        assert json_dict["addressee"] == "Joe Black"
        assert json_dict["line1"] == "716 Elm Street"
        assert json_dict["line2"] == "Apt 201"
        assert json_dict["city"] == "Monroeville"
        assert json_dict["state"] == "Va"
        assert json_dict["postalCode"] == "55551"
        assert json_dict["country"] == "United States"

    @staticmethod
    def assert_contact_point_dict(json_dict):
        assert json_dict["type"] == "PHONE"
        assert json_dict["userName"] == "616-555-1212"
        assert json_dict["authenticated"] == "true"

    @staticmethod
    def assert_address(address):
        assert address.addressee == "Joe Black"
        assert address.line1 == "716 Elm Street"
        assert address.line2 == "Apt 201"
        assert address.city == "Monroeville"
        assert address.state == "Va"
        assert address.postal_code == "55551"
        assert address.country == "United States"

    @staticmethod
    def assert_contact_point(contact_point):
        assert contact_point.type == ContactPointType.PHONE
        assert contact_point.user_name == "616-555-1212"
        assert contact_point.authenticated

    def test_map_contact_point_to_json(self):
        cp = self.joe_black.contact_points[0]
        json_str = self.json_mapper.map_contact_point_to_json(cp)
        print(json_str)
        self.assert_contact_point_dict(json.loads(json_str))

    def test_map_address_to_json(self):
        address = self.joe_black.addresses[0]
        json_str = self.json_mapper.map_address_to_json(address)
        print(json_str)
        json_dict = json.loads(json_str)

        self.assert_address_dict(json_dict)

    def test_map_person_to_json(self):
        person = self.joe_black
        json_str = self.json_mapper.map_person_to_json(person)
        print(json_str)
        json_dict = json.loads(json_str)

        assert json_dict["_id"] == "6220f65C8f03315fb10b327c"
        assert json_dict["name"] == "Joseph R. Black"
        assert json_dict["employeeId"] == "x121212"

        assert len(json_dict["contactPoints"]) == 1
        cp_sub_dict = json_dict["contactPoints"][0]
        self.assert_contact_point_dict(cp_sub_dict)

        assert len(json_dict["addresses"]) == 1
        address_sub_dict = json_dict["addresses"][0]
        self.assert_address_dict(address_sub_dict)

    def test_map_contact_point_from_json(self):
        json_str = \
            """
                {
                "type": "PHONE",
                "userName": "616-555-1212",
                "authenticated": "true"
                }
            """

        contact_point = self.json_mapper.map_contact_point_from_json(json_str)
        self.assert_contact_point(contact_point)

    def test_map_address_from_json(self):
        json_str = \
            """
            {
                "addressee": "Joe Black",
                "line1": "716 Elm Street",
                "line2": "Apt 201",
                "city": "Monroeville",
                "state": "Va",
                "postalCode": "55551",
                "country": "United States"
            }
            """

        address = self.json_mapper.map_address_from_json(json_str)
        self.assert_address(address)

    def test_map_person_from_json(self):
        json_str = \
            """
            {
                "_id": "6220f65C8f03315fb10b327c",
                "name": "Joseph R. Black",
                "employeeId": "x121212",
                "contactPoints": [
                    {
                        "type": "PHONE",
                        "userName": "616-555-1212",
                        "authenticated": "true"
                    }
                ],
                "addresses": [
                    {
                        "addressee": "Joe Black",
                        "line1": "716 Elm Street",
                        "line2": "Apt 201",
                        "city": "Monroeville",
                        "state": "Va",
                        "postalCode": "55551",
                        "country": "United States"
                    }
                ]
            }
            """

        person = self.json_mapper.map_person_from_json(json_str)

        assert person.id == "6220f65C8f03315fb10b327c"
        assert person.name == "Joseph R. Black"
        assert person.employee_id == "x121212"
        assert len(person.contact_points) == 1
        contact_point = person.contact_points[0]
        self.assert_contact_point(contact_point)
        assert len(person.addresses) == 1
        address = person.addresses[0]
        self.assert_address(address)

    def test_roundtrip_with_multiple_contacts_addresses(self):
        expected = self.preeta_smith
        json_str = self.json_mapper.map_person_to_json(expected)
        actual = self.json_mapper.map_person_from_json(json_str)

        assert actual.id == expected.id
        assert actual.name == expected.name
        assert actual.employee_id == expected.employee_id
        assert len(actual.addresses) == len(expected.addresses)
        for index in range(len(actual.addresses)):
            assert actual.addresses[index].addressee == expected.addresses[index].addressee
            assert actual.addresses[index].line1 == expected.addresses[index].line1
            assert actual.addresses[index].line2 == expected.addresses[index].line2
            assert actual.addresses[index].city == expected.addresses[index].city
            assert actual.addresses[index].state == expected.addresses[index].state
            assert actual.addresses[index].postal_code == expected.addresses[index].postal_code
            assert actual.addresses[index].country == expected.addresses[index].country

        assert len(actual.contact_points) == len(expected.contact_points)
        for index in range(len(actual.contact_points)):
            assert actual.contact_points[index].type == expected.contact_points[index].type
            assert actual.contact_points[index].user_name == expected.contact_points[index].user_name
            assert actual.contact_points[index].authenticated == expected.contact_points[index].authenticated


if __name__ == '__main__':
    unittest.main()
