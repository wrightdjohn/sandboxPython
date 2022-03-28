from externaldependencies.mongo.BaseMongo import BaseMongo
from bson import ObjectId


class DeleterPersonMongo(BaseMongo):

    def delete(self, person_id):
        coll = self.get_collection()
        coll.delete_one({"_id": ObjectId(person_id)})