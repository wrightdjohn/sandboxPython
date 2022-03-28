from bson import ObjectId

from allsystemutilities.JsonMapper import JsonMapper
from externaldependencies.mongo.DeleterPersonMongo import DeleterPersonMongo
from externaldependencies.mongo.SaverPersonMongo import SaverPersonMongo
from services.StartupData import startupData, startup_data
from services.implementations.SavePerson import SavePersonService, SavePersonRequest
from services.implementations.TestMocks import CollectionMock


class TestSavePerson:

    def test_simple_save(self):
        joe_black = startup_data().joe_black
        mapper = JsonMapper()
        person_dict = mapper.map_person_to_dict(joe_black)
        person_dict.pop("_id")
        client_mock = CollectionMock.build_update_one("database_name","collection_name",
                                                      {"$eq": {"_id", ObjectId(joe_black.id)}},
                                                      {"$set": person_dict})
        saver = SaverPersonMongo(client_mock, "database_name", "collection_name", mapper)

        service = SavePersonService(saver)
        request = SavePersonRequest([joe_black])
        response = service.execute_request(request)
        assert response is not None
        assert response.get_persons() == [joe_black]

        collection = client_mock["database_name"]["collection_name"]
        command, query = collection.events[0]
        assert command == "update_one"
        assert query == {"_id": joe_black.id}
