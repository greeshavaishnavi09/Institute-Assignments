class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def display_all_details(self):
        print(f"length:{self.__length}") 
        print(f"width:{self.__width}") 

    # --- Setter and Getter for Length --
    def set_length(self, length):
        if length <= 0:
            print("length must be a positive number.")
        else:
            print("length is a poitive number")
           
        self.__length = length

    def get_length(self):
        return self.__length

    # --- Setter and Getter for Width ---
    def set_width(self, width):
        if width <= 0:
            print("Width must be a positive number.")
        else:
            print("width is a poitive number")    
        self.__width = width

    def get_width(self) -> float:
        return self.__width

    # --- Calculation Method ---
    def area(self):
        if self.__length*self.__width > 0:
            calculated_area = self.__length * self.__width
            print(f"area of a rectangle :{self.__length} * {self.__width}={calculated_area}")
            return calculated_area 
        else:
            print("No rectangle is formed")    
         
        
rec = Rectangle(4,3)
rec.set_length(3)
rec.set_width(5)
rec.area()
rec.display_all_details()
