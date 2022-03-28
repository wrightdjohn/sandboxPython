
class BaseMongo:
    def __init__(self, mongoclient, database_name, collection_name, json_mapper):
        self._mongoclient = mongoclient
        self._database_name = database_name
        self._collection_name = collection_name
        self._json_mapper = json_mapper

    def get_collection(self):
        return self._mongoclient[self._database_name][self._collection_name]