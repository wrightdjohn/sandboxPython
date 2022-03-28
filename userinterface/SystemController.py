from flask import Response

from services.implementations.HeathCheck import HealthCheckRequest, HealthCheckResponse
from services.implementations.SetupData import SetupDataRequest, SetupDataResponse


class SystemController:
    def __init__(self, healthCheckService, setupDataService):
        self.healthCheckService = healthCheckService
        self.setupDataService = setupDataService

    def health_check(self):
        response = self.healthCheckService.execute_request(HealthCheckRequest())
        if response.all_healthy:
            return Response(status=200)
        else:
            return Response(status=500)

    def setup_data(self):
        self.setupDataService.execute_request(SetupDataRequest())
        return Response(status=200)
