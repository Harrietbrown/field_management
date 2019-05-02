from animal_manager import *

class Sheep(Animal):
    """A sheep"""
    #contructor
    def __init__(self, name):
        #call the parent call constructor with default values for sheep
        #growth rate = 1; food need = 3; water need = 5
        super().__init__(1,2,5,name)
        self._type = "sheep"

    #override grow method for subclass
    def grow(self,food,water):
        if food >= self._food_need and water >=self._water_need:
            if self._status == "baby":
                self._growth += self._growth_rate * 1.5
            elif self._status == "adolecant":
                self._growth += self._growth_rate * 1.25
            elif self._status == "adult":
                self._growth += self._growth_rate
            elif self._status == "old":
                self._growth += self._growth_rate * 2.
            else:
                self._growth += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update status
        self._update_status()

