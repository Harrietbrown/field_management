from crop_manager import *

class Potato(Crop):
    """A potato crop"""
    #contructor
    def __init__(self):
        #call the parent call constructor with default values for potato
        #growth rate = 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Potato"

    #override grow method for subclass
    def grow(self,light,water):
        if light >= self._light_need and water >=self._water_need:
            if self._status == "seedling" and water >self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "young" and water >self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update status
        self._update_status()