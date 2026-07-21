# 24. Bus Reservation (Hard)
# Attributes
# bus_name
# total_seats
# booked_seats
# reserve(number)
# Reservation allowed only if booked_seats + number does not exceed total seats.
# After booking print Remaining seats.
#class method
class Bus_reservation:
    def __init__(self,bus_name,total_seats,booked_seats):
        self.bus_name=bus_name
        self.total_seats = total_seats
        self.booked_seats = booked_seats
    def display_details(self):
        print(f"Bus_namee: {self.bus_name}, Total_seats: {self.total_seats}, Booked_seats: {self.booked_seats }")    
    def reserve_number(self,number):
        # Check if the requested number of seats can fit in the remaining capacity
        if self.booked_seats + number <= self.total_seats:
            self.booked_seats += number
            remaining_seats = self.total_seats - self.booked_seats
            print(f"[Success] {number} seats reserved successfully.")
            print(f"Remaining seats: {remaining_seats}")
        else:
            print(f"[Error] Cannot reserve {number} seats. Only {self.total_seats - self.booked_seats} seats left.")
# class object(instance)
bus = Bus_reservation("Zingbus",20,3)
bus.display_details()
bus.reserve_number(5)
bus.reserve_number(16)         
