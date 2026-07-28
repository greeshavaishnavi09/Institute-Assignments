class A:
    def __init__(self, a_name, **kwargs):
        super().__init__(**kwargs)
        self.__a_name = a_name

    # Getter
    def get_a_name(self):
        return self.__a_name

    # Setter
    def set_a_name(self, new_name):
        self.__a_name = new_name
        print("Updated A Name:", self.__a_name)

    def show_a(self):
        print("A Name :", self.__a_name)


class B(A):
    def __init__(self, b_id, **kwargs):
        super().__init__(**kwargs)
        self.__b_id = b_id

    # Getter
    def get_b_id(self):
        return self.__b_id

    # Setter
    def set_b_id(self, new_id):
        if new_id > 0:
            self.__b_id = new_id
            print("Updated B ID:", self.__b_id)
        else:
            print("Invalid ID")

    def show_b(self):
        print("B ID :", self.__b_id)


class C:
    def __init__(self, c_department, **kwargs):
        super().__init__(**kwargs)
        self.__c_department = c_department

    # Getter
    def get_c_department(self):
        return self.__c_department

    # Setter
    def set_c_department(self, new_department):
        self.__c_department = new_department
        print("Updated Department:", self.__c_department)

    def show_c(self):
        print("Department :", self.__c_department)


class D(B, C):
    def __init__(self, a_name, b_id, c_department, d_project, **kwargs):
        super().__init__(
            a_name=a_name,
            b_id=b_id,
            c_department=c_department,
            **kwargs
        )
        self.__d_project = d_project

    # Getter
    def get_d_project(self):
        return self.__d_project

    # Setter
    def set_d_project(self, new_project):
        if new_project > 0:
            self.__d_project = new_project
            print("Updated Project:", self.__d_project)
        else:
            print("Invalid Project")

    # Show Method
    def show(self):
        print("Hybrid Inheritance Example")
        print("A Name :", self.get_a_name())
        print("B ID :", self.get_b_id())
        print("Department :", self.get_c_department())
        print("Project :", self.get_d_project())


# Object
obj = D(
    a_name="Vaishnavi",
    b_id=101,
    c_department="Software",
    d_project=5
)

obj.show()