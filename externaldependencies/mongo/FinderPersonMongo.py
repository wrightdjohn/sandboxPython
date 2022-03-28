from bson import ObjectId

from externaldependencies.mongo.BaseMongo import BaseMongo
from services.CriteriaElement import CriteriaElementOperation


class FinderPersonMongo(BaseMongo):

    def find_by_id(self, person_id):
        coll = self.get_collection()
        obj_dict = coll.find_one(ObjectId(person_id))
        return self._json_mapper.map_person_from_dict(obj_dict)

    def find_by(self, criteria):
        coll = self.get_collection()
        query = self.convert_to_query(criteria)
        db_result = [doc for doc in coll.find(query)]
        return self._json_mapper.map_persons_from_list_of_dict(db_result)

    def convert_to_query(self,criteria):
        query = {}
        ce = criteria.elements()
        for element in ce:
            query_part = self.convert_element_query(element)
            query[query_part[0]] = query_part[1]

        return query

    @staticmethod
    def convert_element_query(element):
        if element.operation == CriteriaElementOperation.EQUAL_TO:
            return element.name, {"$eq": element.value}
        elif element.operation == CriteriaElementOperation.CONTAINS:
            return element.name, {"$regex": ".*"+element.value+".*"}
        elif element.operation == CriteriaElementOperation.STARTS_WITH:
            return element.name, {"$regex": "^" + element.value}
        elif element.operation == CriteriaElementOperation.ENDS_WITH:
            return element.name, {"$regex": ".*" + element.value}
        elif element.operation == CriteriaElementOperation.GREATER_THAN:
            return element.name, {"$ge": element.value}
        elif element.operation == CriteriaElementOperation.GREATER_THAN_OR_EQUAL:
            return element.name, {"$gte": element.value}
        elif element.operation == CriteriaElementOperation.LESS_THAN:
            return element.name, {"$le": element.value}
        elif element.operation == CriteriaElementOperation.LESS_THAN_OR_EQUAL:
            return element.name, {"$lte": element.value}
        elif element.operation == CriteriaElementOperation.IN_LIST:
            return element.name, {"$in": element.value}
        else:
            return element.name, element.value
