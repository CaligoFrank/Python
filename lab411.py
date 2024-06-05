class Car:
    
    
    def __init__(self) -> None:
        self.model = 'none'
        self.year = 0
        self.color = 'none'
        
    def set_model(self, model):
        self.model = model
        
    def set_year(self, year):
        self.year = year
    
    def set_color(self, color):
        self.color = color
        
        
        
class DealerShip:
    def __init__(self) -> None:
        self.name = 'none'
        self.location = 'none'
        self.car_lot = []
        
    def set_name(self, name):
        self.name = name
    def set_location(self, location):
        self.location = location
        
    
    def add_car_to_lot(self, car : Car):
        self.car_lot.append(car)
                
    def cars_in_lot(self):
        return len(self.car_lot)




        
        
