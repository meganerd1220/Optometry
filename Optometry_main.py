import OP_class as CD
patient_log = []
patient_count = 0
appointment_log = []
appointment_count = 0
billing_log = []
billing_count = 0
doctor_log = []
doctor_count = 0
glasses_log = []
glasses_count = 0
while 1:
    print("1. Schedule Appointment")
    print("2. Display Appointments")
    print("3. Access Patient Info")
    print("4. Billing")
    print("5. Create Glasses Order")
    print("6. Access Doctor Info")
    print("7. Exit Program")
    option = int(input("Enter Option: "))
    if option == 1:
        search = int(input("Enter 1 for Current Patient and 2 for New Patient: "))
        if search == 1:
            xappointment = "a" + str(appointment_count)
            xappointment = CD.Appointments()
            xappointment.set_appointment()
            appointment_count = appointment_count + 1
            appointment_log.append(xappointment)
        elif search == 2:
            xpatient = "p" + str(patient_count)
            xpatient = CD.Patient()
            xpatient.set_personal_info()
            patient_count = patient_count + 1
            xappointment = "a" + str(appointment_count)
            xappointment = CD.Appointments()
            xappointment.set_appointment()
            appointment_count = appointment_count + 1
            patient_log.append(xpatient)
            appointment_log.append(xappointment)

    elif option == 2:
        print("1. Display Appointments by Patient")
        print("2. Display Appointments by Doctor")
        print("3. Display Appointments by Day")
        print("4. Return to Main Menu")
        choice = int(input("Menu Option: "))
        if choice == 1:
            search = input("Enter Patient Name: ")
            for x in appointment_log:
                if search == x.get_patient_name():
                    x.show_appointment()
        elif choice == 2:
            search = input("Enter Doctor Name: ")
            for x in appointment_log:
                if search == x.get_dr_name():
                    x.show_appointment()
        elif choice == 3:
            year = input("Enter Year of Appointment: ")
            month = input("Enter Month of Appointment: ")
            day = input("Enter Day of Appointment: ")
            appointment = {"year": year, "month": month, "day": day}
            for x in appointment_log:
                if x.get_appointment_date() == appointment:
                    x.show_appointment()
        elif choice == 4:
            break
    elif option == 3:
        search = input("Enter Patient Name: ")
        while 1:
            print("1. Print Personal Information")
            print("2. Print Billing Information")
            print("3. Print Appointments")
            print("4. Print Glasses Info")
            print("5. Print All Information")
            print("6. Edit Personal Information")
            print("7. Update Prescription")
            print("8. Create New Patient")
            print("9. Return to Main Menu")
            choice = int(input("Enter Menu Option: "))
            if choice == 1:
                for x in patient_log:
                    if search == x.get_patient_name():
                        x.show_personal_info()
            elif choice == 2:
                for x in billing_log:
                    if search == x.get_patient_name():
                        x.display_billing_info()
            elif choice == 3:
                for x in appointment_log:
                    if search == x.get_patient_name():
                        x.show_appointment()
            elif choice == 4:
                for x in glasses_log:
                    if search == x.get_patient_name():
                        x.display_glasses_info()
            elif choice == 5:
                for x in patient_log:
                    if search == x.get_patient_name():
                        x.show_personal_info()
                for x in billing_log:
                    if search == x.get_patient_name():
                        x.display_billing_info()
                for x in appointment_log:
                    if search == x.get_patient_name():
                        x.show_appointment()
                for x in glasses_log:
                    if search == x.get_patient_name():
                        x.display_glasses_info()
            elif choice == 6:
                for x in patient_log:
                    if search == x.get_patient_name():
                        x.set_personal_info()
                        break
            elif choice == 7:
                for x in patient_log:
                    if search == x.get_patient_name():
                        x.update_prescription()
            elif choice == 8:
                xpatient = "p" + str(patient_count)
                xpatient = CD.Patient()
                xpatient.set_personal_info()
                patient_count = patient_count + 1
                patient_log.append(xpatient)
            elif choice == 9:
                break
    elif option == 4:
        xbilling = "b" + str(billing_count)
        patient_name = input("Enter Patient Name: ")
        payment_type = input("Enter Payment Type: ")
        if payment_type == "Card" or payment_type == "card":
            c_number = input("Enter Card Number: ")
            expiration = input("Enter Expiration Date")
            payment_type = {"type": "Card", "Card Number": c_number, "Expiration Date: ": expiration}
            date = input("Enter Date in dd/mm/yyyy: ")
            glasses_price = 0
            # for x in glasses_log:
            if patient_name == x.get_patient_name() or date == x.get_date():
                glasses_price = x.get_cost()
                reply = bool(int(input("Enter 1 if patient has insurance: ")))
                xbilling = CD.Billing(patient_name, payment_type, glasses_price, reply, date)
                billing_count = billing_count + 1
                billing_log.append(xbilling)
                xbilling.print_total_cost()
    elif option == 5:
        print("Shop for Frames")
        while 1:
            print("1. Display Frames")
            print("2. Add Frame to Cart")
            print("3. Back to Main Menu")
            frame_option = int(input("Enter option here: "))
            if frame_option == 1:
                print("Exit the popup window to continue the program")
                CD.show_frames()
            if frame_option == 2:
                print("Enter the corresponding number for the frames you want to purchase: ", end=" ")
                frame_no = int(input())
                if frame_no == 1:
                    CD.f1.get_price()
                if frame_no == 2:
                    CD.f2.get_price()
                if frame_no == 3:
                    CD.f3.get_price()
                if frame_no == 4:
                    CD.f4.get_price()
                if frame_no == 5:
                    CD.f5.get_price()
                if frame_no == 6:
                    CD.f6.get_price()
            if frame_option == 3:
                break
    elif option == 6:
        while 1:
            print("1. Add New Doctor")
            print("2. Search for Doctor")
            print("3. Update Doctor")
            print("4. Display Appointments by Doctor")
            print("5. Return to Main Menu")
            choice = int(input("Enter Menu Option: "))
            if choice == 1:
                xdoctor = "d"+str(doctor_count)
                xdoctor = CD.Doctor()
                xdoctor.add_new_dr()
                doctor_count += 1
                doctor_log.append(xdoctor)
            elif choice == 2:
                search = input("Enter Doctor Name: ")
                for x in doctor_log:
                    if search == x.get_dr_name():
                        x.show_dr_info()
            elif choice == 3:
                search = input("Enter Doctor Name: ")
                for x in doctor_log:
                    if search == x.get_dr_name():
                        x.show_dr_info()
            elif choice == 4:
                search = input("Enter Doctor Name: ")
                for x in appointment_log:
                    if search == x.get_dr_name():
                        x.show_appointment()
            elif choice == 5:
                break
    elif option == 7:
        break
