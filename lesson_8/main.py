from vehicle import Vehicle
from car import Car

truck = Vehicle('blue', 6, 'scania',  10)

# print(truck)
# print(type(truck))

print(truck.color, truck.tires, truck.brand, truck.gas_tank)

car = Car('green', 'ford', 8)
print(car.color, car.tires, car.brand, car.gas_tank)

car.fuel(6)
print(car.color, car.tires, car.brand, car.gas_tank)
