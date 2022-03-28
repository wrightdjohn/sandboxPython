from bson import ObjectId

from allsystemutilities.JsonMapper import JsonMapper
from externaldependencies.mongo.DeleterPersonMongo import DeleterPersonMongo
from services.implementations.DeletePerson import DeletePersonService, DeletePersonRequest
from services.implementations.TestMocks import CollectionMock


class TestDeletePerson:

    def test_simple_delete(self):
        mapper = JsonMapper()
        client_mock = CollectionMock.build_delete("database_name","collection_name")
        deleter = DeleterPersonMongo(client_mock, "database_name", "collection_name", mapper)

        service = DeletePersonService(deleter)
        request = DeletePersonRequest("6220fc388c70850875b5af0f")
        response = service.execute_request(request)
        assert response is not None

        collection = client_mock["database_name"]["collection_name"]
        command, query = collection.events[0]
        assert command == "delete_one"
        assert query == {"_id": ObjectId("6220fc388c70850875b5af0f")}


