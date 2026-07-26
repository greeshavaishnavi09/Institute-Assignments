class Agent1:
    def __init__(self, a1_name, a1_role, **kwargs):
        super().__init__(**kwargs)
        self.__a1_name = a1_name  
        self.__a1_role = a1_role

    def get_a1_name(self):
        return self.__a1_name

    def set_a1_name(self, name):
        self.__a1_name = name

    def get_a1_role(self):
        return self.__a1_role

    def set_a1_role(self, role):
        self.__a1_role = role


class Agent2:
    def __init__(self, a2_name, a2_role, **kwargs):
        super().__init__(**kwargs)
        self.__a2_name = a2_name  
        self.__a2_role = a2_role

    def get_a2_name(self):
        return self.__a2_name

    def set_a2_name(self, name):
        self.__a2_name = name

    def get_a2_role(self):
        return self.__a2_role

    def set_a2_role(self, role):
        self.__a2_role = role


class MCP(Agent1, Agent2):
    def __init__(self, a1_name, a1_role, a2_name, a2_role, API, **kwargs):
        super().__init__(
            a1_name=a1_name,
            a1_role=a1_role,
            a2_name=a2_name,
            a2_role=a2_role,
            **kwargs
        )
        self.__API = API  

    def get_API(self):
        return self.__API

    def set_API(self, api):
        if self.validate_api(api):  
            self.__API = api
        else:
            print("Invalid API format.")

    @staticmethod
    def validate_api(api_endpoint):
        return isinstance(api_endpoint, str) and len(api_endpoint) > 0


mcp = MCP("Vaishnavi", "Scanner", "Beta", "Analyzer", "v1/execute")

print("Agent 1 Name:", mcp.get_a1_name())


mcp.set_a1_name("New Alpha")
print("Updated Agent 1 Name:", mcp.get_a1_name())


print("Is valid API?", MCP.validate_api("v2/run"))
