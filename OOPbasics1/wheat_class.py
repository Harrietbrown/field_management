from crop_manager import *

class Wheat(Crop):
    """A wheat crop"""
    #contructor
    def __init__(self):
        #call the parent call constructor with default values for wheat
        #growth rate = 1; light need = 6; water need = 5
        super().__init__(1,6,5)
        self._type = "wheat"

    #override grow method for subclass
    def grow(self,light,water):
        if light >= self._light_need and water >=self._water_need:
            if self._status == "seedling":
                self._growth += self._growth_rate * 1.5
            elif self._status == "young":
                self._growth += self._growth_rate * 1.25
            elif self._status == "old":
                self._growth += self._growth_rate/2.
            else:
                self._growth += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update status
        self._update_status()

