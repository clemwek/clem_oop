class Car:
    def __init__(self, name):    
        self.name = name
 
    def drive(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
    def stop(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'
 
    def stop(self):
        return 'Sportscar breaking!'
 
class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'
 
    def stop(self):
        return 'Truck breaking!'
