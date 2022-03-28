from dataclasses import dataclass
from typing import List


class HealthCheckRequest():
    pass;


@dataclass
class HealthCheckResponse():
    all_healthy: bool
    error_messages: List[str]


class HealthCheckService():
    def __init__(self, health_checkers):
        self._health_checkers = health_checkers

    def execute_request(self,req):
        all_healthy = True
        error_messages = []
        for health_checker in self._health_checkers:
            error = health_checker.error_messages()
            if error is not None:
                all_healthy = False
                error_messages.append(error)

        return HealthCheckResponse(all_healthy,error_messages)
