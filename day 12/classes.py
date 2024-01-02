class student:
     s_id = 1
     name ="Ram"
     address = "kathmandu"
     phone_number = '9812435677'


     def print_details(self):
          print("ID:",self.s_id)
          print("Name : ", self.name)
          print("Address",self.address)
          print("phone number:", self.phone_number)

student1 = student()
student1.print_details()

