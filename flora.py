class Flora: #define class flora

    def __init__(self,name,areas,periods,climate,specialConditions): #set up initialization for function
        self.name = name
        self.areas = areas
        self.periods = periods
        self.climate = climate
        self.specialConditions = specialConditions
    
    #getters and setters if specific data in an object needs to be changed
    def get_name(self):
        return self.areas

    def set_name(self,value):
        self.name = value

    def set_areas(self, value):
        self.areas = value

    def get_areas(self):
        return self.areas

    def set_areas(self, value):
        self.areas = value

    def get_periods(self):
        return self.periods

    def set_periods(self, value):
        self.periods = value

    def get_climate(self):
        return self.climate

    def set_climate(self, value):
        self.climate = value

    def get_specialConditioins(self):
        return self.specialConditioins

    def set_specialConditioins(self, value):
        self.specialConditioins = value
