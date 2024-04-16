class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def displayinfo(self):
        print(f"Name: {self.name}") 
        print(f"Phone number: {self.phone_number}")    



class ProfessionalContact(Contact):
    def __init__(self, name, phone_number, job_title, company, professional_email):
        super().__init__(name, phone_number)
        self.job_title = job_title
        self.company = company
        self.professsional_email = professional_email

    def displayinfo(self):
        super().displayinfo()
        print(f"Job Title: {self.job_title}")
        print(f"Company: {self.company}")
        print(f"Professional Email: {self.professsional_email}")  

class PersonalContact(Contact):
    def __init__(self, name, phone_number, birthday, personal_email):
        super().__init__(name, phone_number)
        self.birthday = birthday
        self.personal_email = personal_email

    def displayinfo (self):
        super().displayinfo()
        print(f"Birthday: {self.birthday}")
        print(f"Personal Email: {self.personal_email}")

contact = Contact("Rohit", 7443585129)    
Professional = ProfessionalContact("Rohit", "878384994094", "ceo", "Fireaway", "rohit10959@gmail.com")
personal = PersonalContact("sabarish", "6785940040", "may 4", "sbarosk@gmail.com")    

contact.displayinfo()
Professional.displayinfo()
personal.displayinfo()

personal.update_phone_number("9876543210")
personal.displayinfo()