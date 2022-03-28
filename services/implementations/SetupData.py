

class SetupDataRequest:
    pass


class SetupDataResponse:
    pass


class SetupDataService():
    def __init__(self, setup_data):
        self._setup_data = setup_data

    def execute_request(self, req):
        self._setup_data.setup()
        return SetupDataResponse()

