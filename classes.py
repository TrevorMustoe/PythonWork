class Pizza: 
  
  def __init__(self):
    self.size = 0
    self.style = ""
    self.crust_type = ""
    self.toppings = []
    
  def add_topping(self, toppings):
    self.toppings.append(toppings)
      
  def order_message(self):
    print(f'I would like a {self.size}, {self.style} pizza with {", ".join(self.toppings)} as toppings')
      
order = Pizza()
meatlovers = Pizza()
order.add_topping("new meat1") 
order.add_topping("new meat2") 
order.add_topping("new meat3") 
order.add_topping("new meat4") 
order.size = "200 inches"
meatlovers.size = "2345 inches"
order.style = "frozen"
order.crust_type = "None"
order.order_message()
meatlovers.order_message()