class Patient:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class InPatient(Patient):
    def __init__(self, name, age, room_number):
        super().__init__(name, age)
        self.room_number=room_number
        
    def display_room(self):
        print(f"{self.name} stays in Room number : {self.room_number}")

patient1=InPatient("Anjali", 52, 204)
print("Name: ",patient1.name)
print("Age : ",patient1.age)
patient1.display_room()