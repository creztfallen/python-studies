from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, color, brand, gas_tank):
        super().__init__(color, 4 , brand, gas_tank)
        
    def fuel(self, liters):
        return super().fuel(liters)    