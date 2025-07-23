import datetime
from datetime import datetime

class Bus:
    def __init__(self, bno, ac, cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno
    def get_ac(self):
        return self.ac
    def get_cap(self):
        return self.cap

    def display(self):
        print(f"1. Bus no: {self.get_bno()}")
        print(f"2. AC: {self.get_ac()}")
        print(f"3. Bus capacity: {self.get_cap()}")

class Booking:
    def __init__(self, name, bno, date):
        self.name = name
        self.bno = bno
        self.date = date

    def booking_info(self):
        print(f"Passenger Name: {self.name}")
        print(f"Bus No: {self.bno}")
        print(f"Date: {self.date}")

BUSES = [Bus(1, True, 2), Bus(2, False, 60), Bus(3, True, 55)]
print("Available buses")
for i in BUSES:
    i.display()
    print("---------------")

Bookings = []
while True:
    print('Press 1 to book ticket')
    print("Press 2 to view bookings")
    print("Press 3 to exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        name = input("Enter the passenger name: ")
        bno = input("Enter bus number: ")
        d = input("Enter the date (dd-mm-yyyy): ")
        try:
            date = datetime.strptime(d, "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format.")
            continue
        b = Booking(name, bno, date)
        Bookings.append(b)
        print("Booking successful!")
    elif ch == 2:
        if not Bookings:
            print("No booking so far")
        else:
            for i, booking in enumerate(Bookings, 1):
                print(f"Booking {i}:")
                booking.booking_info()
                print("---------------")
    elif ch == 3:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice.")