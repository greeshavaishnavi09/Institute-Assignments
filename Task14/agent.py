from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self,agent,agent_apikey):
        self.agent= agent
        self.__agent_apikey = agent_apikey

    def get_agent(self):
        return f"agent:{self.agent}"

    def get_agent_apikey(self):
            return f"agent_apikey:{self.__agent_apikey}"


    #abstractmethod :

    @abstractmethod
    def LLm_name(self):
         pass

    # instance methods
    def  agent_info(self):
         return f"agent:{self.agent} \n agent_apikey:{self.__agent_apikey}"
                 

# child class
class Flight_book(Agent):
     def __init__(self,agent,agent_api,agent_role):
        super().__init__(agent,agent_api)
        self._agent_role = agent_role

     def LLm_name(self):
          return "LLm _name : open ai LLm model"    

     def display_details(self):
        print("flight booking:")
        print(f"agent_role:{self._agent_role}")  
        print(self.agent_info())
        print(self.LLm_name())

# child2

class Hotel_agent(Agent):
     def __init__(self,agent,agent_api,role):
        super().__init__(agent,agent_api)
        self._role = role

     def LLm_name(self):
          return "LLm _name : Grok LLm model"    

     def display_details(self):
        print("Hotel booking:")
        print(f"role:{self._role}")  
        print(self.agent_info())
        print(self.LLm_name())        

flight = Flight_book("AI",3456789,"book the flight")
hotel = Hotel_agent("Grok",34567,"book the hotel")

print(flight.get_agent_apikey())
print(flight.agent_info())
print(flight.LLm_name())

print(hotel.get_agent_apikey())
print(hotel.agent_info())
print(hotel.LLm_name())
