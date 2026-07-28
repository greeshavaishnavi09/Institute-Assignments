class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.__name = name

    # Getter
    def get_name(self):
        return self.__name


class Employee(Person):
    def __init__(self, emp_id, **kwargs):
        super().__init__(**kwargs)
        self.__emp_id = emp_id

    # Getter
    def get_emp_id(self):
        return self.__emp_id


class Manager(Employee):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.__team_size = team_size

    # Getter
    def get_team_size(self):
        return self.__team_size


class HR:
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.__department = department

    # Getter
    def get_department(self):
        return self.__department


class TeamLead(Manager, HR):
    def __init__(self, name, emp_id, team_size, department, **kwargs):
        super().__init__(
            name=name,
            emp_id=emp_id,
            team_size=team_size,
            department=department,
            **kwargs
        )

    # Duck Typing Method
    def work(self):
        print(f"{self.get_name()} is managing the development team.")


# Independent Class
class Freelancer:
    def __init__(self, name):
        self.__name = name

    def work(self):
        print(f"{self.__name} is working on freelance projects.")


# Duck Typing Function
def do_work(obj):
    obj.work()

def display(obj):
    obj.work()    


# Objects
team = TeamLead(
    name="Vaishnavi",
    emp_id=101,
    team_size=8,
    department="Software"
)

free = Freelancer("Greesha")

display(free)
display(team)



