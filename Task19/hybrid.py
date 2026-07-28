class Person:
    def __init__(self,name,age,**kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__age = age


    # Getter Methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        if 18<= new_age <= 65:
            self.__age = new_age
            print(f"valid age:{self.__age}")
        else:
            print("not a valid age")    
        return self.__age
    def show(self):
        print("Person Details")
        print("Name :", self.__name)
        print("Age :", self.__age)

class Pilot(Person):
    def __init__(self,license,flight_hours,**kwargs):
        super().__init__(**kwargs)
        self.__license= license
        self.__flight_hours = flight_hours

        #getter
    def get_license(self):
            return self.__license     
    def get_flight_hours(self):
            return self.__flight_hours

    #setter
    def set_flight_hours(self,new_flight_hours):
        if new_flight_hours>0:
            self.__flight_hours = new_flight_hours
            print(f"Valid hours:{self.__flight_hours}")
        else:
             print("Not a valid hours")

class Engineer(Person):
    def __init__(self,fields,project,**kwargs):
        super().__init__(**kwargs)
        self.__fields= fields
        self.__project = project

     #getter
    def get_fields(self):
            return self.__fields     
    def get_project(self):
            return self.__project

    #setter
    def set_project(self,num):
        if num>0:
            self.__project = num
            print(f"Valid project:{self.__flight_project}")
        else:
             print("Not a valid project")

#Aerospace Engineer:

class Aerospace(Pilot,Engineer):
    def __init__(self,name,age,license,flight_hours,fields,project,r_mission,**kwargs):
        super().__init__(name=name,
                         age=age,
                         license=license,
                         flight_hours=flight_hours,
                         fields=fields,
                         project=project,
                         **kwargs
                        )
        self.rocket_mission = r_mission

    def get_r_mission(self):
        return self.rocket_mission  

    @staticmethod
    def valid_mission(mission):
         return 0 <mission<50
    #setter
    def set_rocket_mission(self,mission):
        if Aerospace.valid_mission(mission) :
            self.rocket_mission = mission
            return f"rocket_mission: {self.rocket_mission}"
        else:
             print("rocket mission must be between 0 and 50")


    def show(self):
        print("Person Details")
        print("Name :", self.get_name())
        print("age :", self.get_age())
        print("license :", self.get_license())
        print("flight_hours:", self.get_flight_hours())
        print("field:",self.get_fields())
        print("project :", self.get_project())
        print("r_mission :", self.get_r_mission())

Aero = Aerospace(name="Vaishnavi", age=34,license="fgjh", flight_hours=7,fields="sdgf",
                project= 9, r_mission=16)  
Aero.show()         

             
              








