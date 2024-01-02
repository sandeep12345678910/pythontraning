class Bike:
    def __init__(self,name:str,cc:int)-> None:
        self.name = name
        self.cc = cc


    def print_detail(self):
        print(f"Bike name {self.name}and cc is {self.cc}")
        
        
bike_1 = Bike(name = "Pulsar",cc = 200)
bike_1.print_detail()
bike_1.name = "R15"
print(bike_1.name)
