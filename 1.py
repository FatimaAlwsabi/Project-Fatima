class hospital:
    def __init__ (self, name, location, fees):
        self.name = name
        self.location =location
        self.fees = fees
    def print_data(self):
             print("__________________________________________" + "\n" +"hospital : " + self.name + "\n" + "location : " + self.location + "\n" + "fees : " + self.fees + "\n" + "__________________________________________")
hos1 = hospital('Al_toofeq','Behind the university building',"$16")

hos1.print_data()

#*****************************************************************************
print("If you want to register as a doctor enter the number 1 ")
print("If you want the eye department enter the number 2 ")
print("If you want the children section enter the number 3 ")
choice = input("enter the check number you want : ")


class Doctors:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree
    def doctor_data(self):
        name = input("what is your name : ")
        print("________choose from : bachelors or master or doctorate or professor________")
        degree = input("enter your degree : ")
        if degree == 'bachelors':
            print("acceptable\n@200")
        elif degree == 'master':
            print('acceptable at a good level\n@400')
        elif degree == 'doctorate':
            print("acceptable at a very good level\n@600")
        elif degree == 'professor':
            print("acceptable at an excellent level\n@800")
        else :
            print("sorry, you are not acceptable")
#doc1 = Doctors('', '')

#doc1.doctor_data()
#**********************************************************************************
class Department_Ophthalmology:
    def __init__ (self, name_patient, continuity):
        self.name_patient = name_patient
        self.continuity = continuity
    def Department_Ophthalmology_data(self):
        print("evening\nDr.Ramy\nNationality : Syrian\n--------------------------------------------------------------------------------")
        print("morning\nDr.suleiman\nNationality : Yemeni\n--------------------------------------------------------------------------------")
        name_patient = input("what is your name? ")
        continuity = input("enter the working time I want ( evening or morining ) : ")
        if continuity == "evening":
            print("evening\nDr.Ramy\nNationality : Syrian")
        elif continuity == "morning" :
            print("morning\nDr.suleiman : Yemeni")
        else:
            print("sorry, this is not valid")
       
#ophthalmology = Department_Ophthalmology('',  '')
 
#ophthalmology.Department_Ophthalmology_data()
#************************************************************************************************
class childern_section():
    def __init__ (self, name_patient, continuity):
        self.name_patient = name_patient
        self.continuity = continuity
    def Department_Ophthalmology_data(self):
        print("evening\nDr.Ramy\nNationality : Syrian\n--------------------------------------------------------------------------------")
        print("morning\nDr.suleiman\nNationality : Yemeni\n--------------------------------------------------------------------------------")
        name_patient = input("what is your name? ")
        continuity = input("enter the working time I want ( evening or morining ) : ")
        if continuity == "evening":
            print("evening\nDr.Ramy\nNationality : Syrian")
        elif continuity == "morning" :
            print("morning\nDr.suleiman : Yemeni")
        else:
            print("sorry, this is not valid")


    

if choice =="1":
    doc1 = Doctors('', '')
    doc1.doctor_data()
elif choice == "2":
    ophthalmology = Department_Ophthalmology('',  '')
    ophthalmology.Department_Ophthalmology_data()
elif choice == "3":
    ch = childern_section('', '')
else:
    print("KKKKKKK")
