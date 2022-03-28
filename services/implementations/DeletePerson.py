class DeletePersonRequest:
    def __init__(self, person_id):
        self._person_id = person_id

    def get_person_id(self):
        return self._person_id


class DeletePersonResponse:
    pass;


class DeletePersonService:
    def __init__(self, deleter):
        self._deleter = deleter

    def execute_request(self, request):
        self._deleter.delete(request.get_person_id())
        return DeletePersonResponse()
