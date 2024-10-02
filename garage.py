class Vehicle: 
  def __init__(self, main_color, capacity):
     self.main_color = main_color
     self.capacity = capacity
     
  def drive(self):
    print("car go vroom ")
    

     
class Porsche(Vehicle): 
    def __init__(self, fuel_cap, main_color, capacity):
      super().__init__(main_color, capacity)
      self.fuel_cap = fuel_cap
        
    def refuel(self):
      print("Porsche needs 93")
    
    def drive(self):
      print("posrche says brbrbrbr")
    


class Tesla(Vehicle):
    def __init__(self, battery, main_color, capacity):
      super().__init__(main_color, capacity)
      self.battery = battery
    
    def drive(self):
      print("Teslsa say shhhhhh")
    
    def super_charge(self):
      print("The Tesla gets to charge")
      
cayanne = Porsche("Test1", "test2", "test3")
modelWhy = Tesla("testla1", "testla2", "testla3")
modelWhy.drive()
cayanne.drive()

print(cayanne.fuel_cap, cayanne.main_color, cayanne.capacity)
print(modelWhy.battery, modelWhy.main_color, modelWhy.capacity)