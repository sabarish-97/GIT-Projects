import sys
print(sys.path)
from modules.contact import Contact, ProfessionalContact, PersonalContact

contact = Contact("Rohit", 7443585129)    
Professional = ProfessionalContact("Rohit", "878384994094", "ceo", "Fireaway", "rohit10959@gmail.com")
personal = PersonalContact("sabarish", "6785940040", "may 4", "sbarosk@gmail.com")    

contact.displayinfo()
Professional.displayinfo()
personal.displayinfo()

personal.update_phone_number("9876543210")
personal.displayinfo()