from externaldependencies.mongo.BaseMongo import BaseMongo

class SetupDataMongo(BaseMongo):
    def __init__(self, saver, person_list):
        self.saver = saver
        self.person_list = person_list

    def setup(self):
        collection = self.get_collection()
        collection.drop()

        self.saver.save_many(self.person_list)

