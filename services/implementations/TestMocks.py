def quick_setup(database_name, collection_name):
    collection = CollectionMock(collection_name)
    database = DatabaseMock(database_name, collection)
    return ClientMock(database)


class ClientMock:
    def __init__(self, database):
        self.data = {database.name: database}

    def __getitem__(self, item):
        return self.data[item]


class DatabaseMock:
    def __init__(self, name, collection):
        self.name = name
        self.data = {collection.name: collection}

    def __getitem__(self, item):
        return self.data[item]


class CollectionMock:
    def __init__(self, name, delete_count=1, find_query={}, insert_value={}, insert_id=0, update_search={}, update_value={}):
        self.name = name
        self._delete_count = delete_count
        self._find_query = find_query
        self._insert_value = insert_value
        self._insert_id = insert_id
        self._update_search = update_search
        self._update_value = update_value
        self.events = []

    def delete_one(self, arg):
        self.events.append(("delete_one", arg))
        return DeleteResult(self._delete_count)

    def find(self, query):
        return self._find_query[query]

    def insert_one(self, insert_value):
        assert insert_value == self._insert_value
        return InsertResult(self._insert_id)

    def update_one(self, search, update_value):
        assert search == self._update_search
        assert update_value == self._update_value
        return UpdateResult

    @classmethod
    def build_delete(cls,database_name, collection_name, delete_cnt=1):
        collection = CollectionMock(collection_name, delete_count=delete_cnt)
        database = DatabaseMock(database_name, collection)
        return ClientMock(database)

    @classmethod
    def build_find(cls,database_name, collection_name, find_query={}):
        collection = CollectionMock(collection_name, find_query=find_query)
        database = DatabaseMock(database_name, collection)
        return ClientMock(database)

    @classmethod
    def build_insert_one(cls,database_name, collection_name, insert_value={}, insert_id=0):
        collection = CollectionMock(collection_name, insert_value=insert_value, insert_id=insert_id)
        database = DatabaseMock(database_name, collection)
        return ClientMock(database)

    @classmethod
    def build_update_one(cls,database_name, collection_name, update_search={}, update_value={}):
        collection = CollectionMock(collection_name, update_search=update_search, update_value=update_value)
        database = DatabaseMock(database_name, collection)
        return ClientMock(database)


class DeleteResult:
    def __init__(self, count):
        self._count = count

    def delete_count(self):
        return self._count


class UpdateResult:
    pass


class InsertResult:
    def __init__(self,insert_id):
        self.insert_id = insert_id