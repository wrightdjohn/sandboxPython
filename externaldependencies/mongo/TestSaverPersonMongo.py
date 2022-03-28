import unittest
import pymongo

from externaldependencies.mongo.FinderPersonMongo import FinderPersonMongo
from externaldependencies.mongo.SaverPersonMongo import SaverPersonMongo
from allsystemutilities.JsonMapper import JsonMapper
from services.Domain import Person, Address, ContactPoint, ContactPointType
from services.StartupData import startup_data


class TestSaverPersonMongo(unittest.TestCase):
    def setUp(self):
        self.mapper = JsonMapper()
        self.mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.finder = FinderPersonMongo(self.mongoClient, "mongotest", "people", self.mapper)
        self.saver = SaverPersonMongo(self.mongoClient, "mongotest", "people", self.mapper)

    def test_create_person(self):
        new_person = Person(None, "New Guy", "zz12345",
                            [ContactPoint(ContactPointType.EMAIL, "newguy@zoomzoom.com", True)],
                            [Address("New Guy", "111 Elwood Drive", "Apt 501", "Farport",
                                     "MO", "99999", "United States")]
                            )

        result_person = self.saver.save_one(new_person)
        saved_person = self.finder.find_by_id(result_person.id)
        assert saved_person == result_person

    def test_create_update_person(self):
        joe_black_in_memory = startup_data().joe_black
        joe_black_saved = self.finder.find_by_id(joe_black_in_memory.id)
        assert joe_black_in_memory == joe_black_saved
        joe_black_saved.name = "Josephine R. Black"
        self.saver.save_one(joe_black_saved)
        joe_black_saved2 = self.finder.find_by_id(joe_black_in_memory.id)
        assert joe_black_saved2 == joe_black_saved
        assert joe_black_saved2 != joe_black_in_memory
        self.saver.save_one(joe_black_in_memory)


if __name__ == '__main__':
    unittest.main()
