import unittest
import pymongo

from externaldependencies.mongo.FinderPersonMongo import FinderPersonMongo
from externaldependencies.mongo.SaverPersonMongo import SaverPersonMongo
from externaldependencies.mongo.DeleterPersonMongo import DeleterPersonMongo
from allsystemutilities.JsonMapper import JsonMapper
from services.Domain import Person, Address, ContactPoint, ContactPointType


class TestDeleterPersonMongo(unittest.TestCase):
    def setUp(self):
        self.mapper = JsonMapper()
        self.mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.finder = FinderPersonMongo(self.mongoClient, "mongotest", "people", self.mapper)
        self.saver = SaverPersonMongo(self.mongoClient, "mongotest", "people", self.mapper)
        self.deleter = DeleterPersonMongo(self.mongoClient, "mongotest", "people", self.mapper)

    def test_create_and_delete_person(self):
        new_person = Person(None,"Delete Me Guy","zz12345",
                            [ContactPoint(ContactPointType.EMAIL, "newguy@zoomzoom.com", True)],
                            [Address("New Guy", "111 Elwood Drive", "Apt 501", "Farport",
                                     "MO", "99999", "United States")]
                            )

        result_person = self.saver.save_one(new_person)
        saved_person = self.finder.find_by_id(result_person.id)
        assert saved_person == result_person
        self.deleter.delete(saved_person.id)


if __name__ == '__main__':
    unittest.main()
