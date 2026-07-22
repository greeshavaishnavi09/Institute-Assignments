class Employee:
    def __init__(self, id_number: int, salary: float):
        # Initialising private attributes
        self.__id = id_number
        self.__salary = salary

    # Getter for ID
    def get_id(self) -> int:
        return self.__id

    # Getter for Salary
    def get_salary(self) -> float:
        return self.__salary


# --- Execution and Observation ---

# 1. Create an Employee object
emp = Employee(101, 55000.0)

# 2. Try to access the private attribute directly
try:
    print(emp.__salary)
except AttributeError as error:
    print(f" Observed Error: {error}")

# 3. Access the private attribute using Name Mangling
print(f" Accessed via Name Mangling: {emp._Employee__salary}")
