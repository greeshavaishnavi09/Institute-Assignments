class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__age = age

    # Getter Methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter Method
    def set_age(self, new_age):
        if 18 <= new_age <= 65:
            self.__age = new_age
            print(f"Valid Age : {self.__age}")
        else:
            print("Not a valid age")

    def show(self):
        print("Person Details")
        print("Name :", self.__name)
        print("Age :", self.__age)


class Pilot(Person):
    def __init__(self, license, flight_hours, **kwargs):
        super().__init__(**kwargs)
        self.__license = license
        self.__flight_hours = flight_hours

    # Getter
    def get_license(self):
        return self.__license

    def get_flight_hours(self):
        return self.__flight_hours

    # Setter
    def set_flight_hours(self, new_flight_hours):
        if new_flight_hours > 0:
            self.__flight_hours = new_flight_hours
            print(f"Valid Flight Hours : {self.__flight_hours}")
        else:
            print("Invalid Flight Hours")


class Engineer(Person):
    def __init__(self, fields, project, **kwargs):
        super().__init__(**kwargs)
        self.__fields = fields
        self.__project = project

    # Getter
    def get_fields(self):
        return self.__fields

    def get_project(self):
        return self.__project

    # Setter
    def set_project(self, new_project):
        if new_project > 0:
            self.__project = new_project
            print(f"Valid Project : {self.__project}")
        else:
            print("Invalid Project")


class Aerospace(Pilot, Engineer):
    def __init__(self, name, age, license, flight_hours,
                 fields, project, r_mission):

        super().__init__(
            name=name,
            age=age,
            license=license,
            flight_hours=flight_hours,
            fields=fields,
            project=project
        )

        self.__rocket_mission = r_mission

    # Getter
    def get_r_mission(self):
        return self.__rocket_mission

    @staticmethod
    def valid_mission(mission):
        return 0 < mission < 50

    # Setter
    def set_rocket_mission(self, mission):
        if Aerospace.valid_mission(mission):
            self.__rocket_mission = mission
            print(f"Rocket Mission : {self.__rocket_mission}")
        else:
            print("Rocket mission must be between 0 and 50")

    def show(self):
        print("----- Aerospace Engineer -----")
        print("Name :", self.get_name())
        print("Age :", self.get_age())
        print("License :", self.get_license())
        print("Flight Hours :", self.get_flight_hours())
        print("Field :", self.get_fields())
        print("Projects :", self.get_project())
        print("Rocket Missions :", self.get_r_mission())


# Object
aero = Aerospace(
    name="Vaishnavi",
    age=34,
    license="IND-7865",
    flight_hours=2500,
    fields="Aerospace Engineering",
    project=8,
    r_mission=12
)

aero.show()