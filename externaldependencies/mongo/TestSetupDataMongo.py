import unittest
import pymongo

from allsystemutilities.JsonMapper import JsonMapper
from externaldependencies.mongo.FinderPersonMongo import FinderPersonMongo
from externaldependencies.mongo.SaverPersonMongo import SaverPersonMongo
from externaldependencies.mongo.SetupDataMongo import SetupDataMongo
from services.StartupData import startupData
from services.implementations.RetrievePersons import PersonRetrieveCriteria


class TestSaverPersonMongo(unittest.TestCase):
    def setUp(self):
        self.mapper = JsonMapper()
        self.mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.finder = FinderPersonMongo(self.mongoClient, "mongotest", "people", self.mapper)
        self.saver = SaverPersonMongo(self.mongoClient, "mongotest", "people", self.mapper)
        self.person_list = startupData().person_list()
        self.setupData = SetupDataMongo(self.saver, self.person_list)

    def test_setup_then_check_data(self):
        self.setupData.setup()

        persons_list = self.finder.find_by(PersonRetrieveCriteria())

        for person in persons_list:
            assert person in self.person_list


