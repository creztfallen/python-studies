class Vehicle:
    
    def __init__(self, color, tires, brand, gas_tank):
        self.color = color
        self.tires = tires
        self.brand = brand
        self.gas_tank = gas_tank
        
    def fuel(self, liters):
        self.gas_tank += liters    
        
      