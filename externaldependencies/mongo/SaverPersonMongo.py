from bson import ObjectId

from externaldependencies.mongo.BaseMongo import BaseMongo


class SaverPersonMongo(BaseMongo):

    def save_one(self, person):
        person_dict = self._json_mapper.map_person_to_dict(person)
        if person.id is None:
            result = self.get_collection().insert_one(person_dict)
            person.id = str(result.inserted_id)
        else:
            person_dict.pop("_id")
            search_criteria = {"_id": {"$eq": ObjectId(person.id)}}
            update_query = {"$set": person_dict}
            self.get_collection().update_one(search_criteria,update_query)

        return person

    def save_many(self, persons):
        result = []
        for person in persons:
            result.append(self.save_one(person))

        return result
