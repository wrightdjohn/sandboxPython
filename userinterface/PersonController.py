from flask import request, Response
from allsystemutilities.JsonMapper import map_person_from_json
from allsystemutilities.JsonMapper import map_person_to_json
from allsystemutilities.JsonMapper import map_persons_to_json
from allsystemutilities.JsonMapper import map_request_args_to_criteria
from services.implementations.SavePerson import SavePersonRequest
from services.implementations.RetrievePersons import RetrievePersonsRequest
from services.implementations.DeletePerson import DeletePersonRequest


class PersonController:
    def __init__(self, personRetrieveService, personSaveService, personDeleteService):
        self.personRetrieveService = personRetrieveService
        self.personSaveService = personSaveService
        self.personDeleteService = personDeleteService

    @staticmethod
    def hello_world(self):  # put application's code here
        return 'Hello World!'

    def get_persons_by_id(self, id):
        req = RetrievePersonsRequest(person_id=id)
        response = self.personRetrieveService.execute_request(req)
        return Response(map_persons_to_json(response.get_persons()),200)

    def get_persons_by_criteria(self):
        criteria = map_request_args_to_criteria(request.args)
        req = RetrievePersonsRequest(person_criteria=criteria)
        response = self.personRetrieveService.execute_request(req)
        return Response(map_persons_to_json(response.get_persons()),200)

    def update_person(self):
        person = map_person_from_json(request.json)
        if person.id is None:
            raise Exception("You are trying to update a brand new person. Insert new persons")
        persons = [person]
        response = self.personSaveService.execute_request(SavePersonRequest(persons))
        return Response(map_person_to_json(response.get_persons()[0]),200)

    def insert_person(self):
        person = map_person_from_json(request.json)
        if person.id is not None:
            raise Exception("You are trying to insert an existing person. Update existing persons")
        persons = [person]
        response = self.personSaveService.execute_request(SavePersonRequest(persons))
        return Response(map_person_to_json(response.get_persons()[0]),201)

    def delete_person(self, id):
        if id is None:
            raise Exception("The id of the person be deleted is required")
        self.personDeleteService.execute_request(DeletePersonRequest(id))
        return Response(status=204)
