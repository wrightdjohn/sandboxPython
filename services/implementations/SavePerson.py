class SavePersonRequest:
    def __init__(self,persons):
        self._persons = persons

    def get_persons(self):
        return self._persons


class SavePersonResponse:
    def __init__(self, persons):
        self._persons = persons

    def get_persons(self):
        return self._persons


class SavePersonService:
    def __init__(self, saver):
        self._saver = saver

    def execute_request(self,request):
        persons = self._saver.save_many(request.get_persons())

        return SavePersonResponse(persons)
