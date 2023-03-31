import tkinter


class Patient:
    def __init__(self):
        self.__name = ""
        self.__address = ""
        self.__phone_no = ""
        self.__insurance = False
        self.__prescription = ""

    def set_personal_info(self):
        self.__name = input("Enter Name: ")
        self.__address = input("Enter Address: ")
        self.__phone_no = input("Enter Phone Number: ")
        x = input("Patient has insurance (y/n): ")
        if x == "Y" or x == "y":
            self.__insurance = True
        prescription = int(input("Enter 1 if patient has a prescription and 0 if they do not: "))
        if prescription == 1:
            left = input("Enter left eye prescription: ")
            right = input("Enter right eye prescription: ")
            self.__prescription = {"left": left, "right": right}
        else:
            self.__prescription = "N/A"

    def show_personal_info(self):
        print("Name:", self.__name)
        print("Address:", self.__address)
        print("Phone Number:", self.__phone_no)
        print("Insurance:", self.__insurance)
        print("Prescription:", self.__prescription)

    def get_patient_name(self):
        return self.__name

    def update_prescription(self):
        left = input("Enter left eye prescription: ")
        right = input("Enter right eye prescription")
        self.__prescription = {"left": left, "right": right}


class Appointments:
    def __init__(self):
        self.__appointment_date = {}
        self.__appointment_time = ""
        self.__dr_name = ""
        self.__patient_name = ""
        self.__cost = ""

    def set_appointment(self):
        self.__patient_name = input("Enter Patient's Name: ")
        year = input("Enter Year of Appointment: ")
        month = input("Enter Month of Appointment: ")
        day = input("Enter Day of Appointment: ")
        self.__appointment_time = input("Enter Time of Day: ")
        self.__appointment_date = {"year": year, "month": month, "day": day}
        self.__dr_name = input("Enter Doctor's Name: ")

    def show_appointment(self):
        print("Patient Name:", self.__patient_name)
        print("Doctor Name:", self.__dr_name)
        print("Appointment Scheduled for", self.__appointment_time, "on", self.__appointment_date["month"], "/",
              self.__appointment_date["day"], "/", self.__appointment_date["year"])

    def get_patient_name(self):
        return self.__patient_name

    def get_dr_name(self):
        return self.__dr_name

    def get_appointment_date(self):
        return self.__appointment_date


class Doctor:
    def __init__(self):
        self.__dr_name = ""
        self.__specialty = ""

    def add_new_dr(self):
        self.__dr_name = input("Enter doctor's name: ")
        self.__specialty = input("Enter doctor's specialty: ")

    def show_dr_info(self):
        print("Name:", self.__dr_name)
        print("Specialty:", self.__specialty)

    def get_dr_name(self):
        return self.__dr_name


class Billing:
    def __init__(self, name, payment, glasses, insurance, date):
        self.__payment_type = payment
        self.__cost = 100
        self.__glasses_price = glasses
        self.__insurance = insurance
        self.__patient_name = name
        if insurance == 1:
            self.__insurance = True
        if self.__insurance:
            self.__cost = self.__cost - 40
        self.__cost = self.__cost + self.__glasses_price
        self.__date = date

    def display_billing_info(self):
        print("Name: ", self.__patient_name)
        print("Payment Type: ", self.__payment_type)
        print("Glasses Total Cost: $", self.__glasses_price)
        print("Total Price: $", self.__cost)
        print("Appointment Date: ", self.__date)

    def get_patient_name(self):
        return self.__patient_name

    def get_date(self):
        return self.__date

    def get_glasses_price(self):
        return self.__glasses_price

    def get_total_cost(self):
        return self.__cost

    def print_total_cost(self):
        import Receipt as TC


class Glasses:
    def __init__(self):
        self.__patient_name = ""
        self.__lenses_price = ""
        self.__prescription = ""
        self.__date = ""

    def get_glasses_info(self):
        self.__patient_name = input("Enter Patient Name: ")
        left = input("Enter Left Eye Prescription: ")
        right = input("Enter Right Eye Prescription: ")
        self.__prescription = {"left": left, "right": right}
        self.__date = input("Enter Date in dd/mm/yyyy: ")
        self.__lenses_price = self.calculate_lenses(left, right)

    def calculate_lenses(self, left, right):
        Mild = False
        High = False
        Moderate = False
        Extreme = False
        lens_price = 0

        lens_avg = (abs(left) + abs(right)) / 2

        if lens_avg < 0.5:
            print("No prescription needed")
        elif 0.5 <= lens_avg < 3:
            Mild = True
        elif 3 <= lens_avg < 5:
            Moderate = True
        elif 5 <= lens_avg < 10:
            High = True
        elif lens_avg >= 10:
            Extreme = True
        else:
            print("No criteria for:", lens_avg)

        if Mild:
            lens_price = 50.00
        elif Moderate:
            lens_price = 75.00
        elif High:
            lens_price = 100.00
        elif Extreme:
            lens_price = 125.00

        return lens_price

    def display_glasses_info(self):
        print("Name: ", self.__patient_name)
        print("Price: $", self.__lenses_price)
        print("Prescription: ", self.__prescription)
        print("Date of Order: ", self.__date)

    def get_patient_name(self):
        return self.__patient_name

    def get_date(self):
        return self.__date

    def get_cost(self):
        return self.__lenses_price


class Frames:
    def __init__(self, color, shape, price):
        self.__frame_color = color
        self.__frame_shape = shape
        self.__frame_price = price

    def display_frame_info(self):
        print("Frame Color:", self.__frame_color)
        print("Frame Shape:", self.__frame_shape)
        print("Frame Price:", self.__frame_price)

    def get_price(self):
        return self.__frame_price


def show_frames():
    import Frame_shop as FR


# Frame Objects
f1 = Frames("Oval", "Blue", 50.99)
f2 = Frames("Circle", "Pink", 49.99)
f3 = Frames("Cat Eye", "Multi-Color", 64.99)
f4 = Frames("Oval", "Transparent", 50.99)
f5 = Frames("Rectangle", "Black", 54.99)
f6 = Frames("Square", "Brown", 34.99)
