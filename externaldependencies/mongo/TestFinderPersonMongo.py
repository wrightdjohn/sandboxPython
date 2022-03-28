import unittest
import pymongo
from services.implementations.RetrievePersons import PersonRetrieveCriteria

from externaldependencies.mongo.FinderPersonMongo import FinderPersonMongo
from allsystemutilities.JsonMapper import JsonMapper


class TestFinderPersonMongo(unittest.TestCase):
    def setUp(self):
        self.mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.finder = FinderPersonMongo(self.mongoClient,"mongotest","people",JsonMapper())

    def test_find_by_id(self):
        joe_black = self.finder.find_by_id('6220fc388c70850875b5af0a')
        assert joe_black.name == "Joseph R. Black"

    def test_find_all(self):
        all_people = self.finder.find_by(PersonRetrieveCriteria())
        assert len(all_people) == 7

    def test_find_name_equals(self):
        criteria = PersonRetrieveCriteria()
        criteria.name_is_equal_to("Joseph R. Black")
        results = self.finder.find_by(criteria)
        assert len(results) == 1
        assert results[0].name == "Joseph R. Black"

    def test_find_name_contains(self):
        criteria = PersonRetrieveCriteria()
        criteria.name_contains("Black")
        results = self.finder.find_by(criteria)
        assert len(results) == 1
        assert results[0].name == "Joseph R. Black"

    def test_find_name_starts_with(self):
        criteria = PersonRetrieveCriteria()
        criteria.name_starts_with("Joseph")
        results = self.finder.find_by(criteria)
        assert len(results) == 1
        assert results[0].name == "Joseph R. Black"

    def test_find_name_ends_with(self):
        criteria = PersonRetrieveCriteria()
        criteria.name_ends_with("lack")
        results = self.finder.find_by(criteria)
        assert len(results) == 1
        assert results[0].name == "Joseph R. Black"

    def test_find_postal_code_less_than(self):
        criteria = PersonRetrieveCriteria()
        criteria.has_address_with_postal_code("55551")
        results = self.finder.find_by(criteria)
        assert len(results) == 4


if __name__ == '__main__':
    unittest.main()
