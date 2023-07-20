class Car:
    def __init__ (vehicle, Name,Model,Engine,Fuel,Colour,Cost,Segment,max_speed):

        vehicle.Name = Name
        vehicle.Model = Model
        vehicle.Engine = Engine
        vehicle.Fuel = Fuel
        vehicle.Colour = Colour
        vehicle.Cost = Cost
        vehicle.Segment = Segment
        vehicle.max_speed = max_speed

    def display_details(vehicle):
        print(f'Name: {vehicle.Name}')
        print(f'Model: {vehicle.Model}')
        print(f'Engine: {vehicle.Engine}')
        print(f'Fuel: {vehicle.Fuel}')
        print(f'Colour: {vehicle.Colour}')
        print(f'Cost: {vehicle.Cost}')
        print(f'Segment: {vehicle.Segment}')
        print(f'Speed: {vehicle.max_speed}km/h')

    def is_supercar(vehicle):
        if vehicle.max_speed > 400:
            print("its a super car")
        else:
            print(f"its a normal car with {vehicle.max_speed}km/h")

Venue = Car(Name="venue", Model=2021, Engine="BS6", Fuel="Deisel", Colour="White", Cost="14lacs", Segment="cross over", max_speed=180)
Venue.display_details()
Venue.is_supercar()
print("-"*100)

BMW = Car(Name="3series", Model=2020, Engine="BS6", Fuel="Deisel", Colour="Blue", Cost="40lacs", Segment="Sedan", max_speed=450)
BMW.display_details()
BMW.is_supercar()

