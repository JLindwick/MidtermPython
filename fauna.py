class Fauna(): #define class flora
    def __init__(self,name,kingdom,phylum,order,family,genus,species): #set up initialization for function
        self.name = name
        self.kingdom = kingdom
        self.phylum = phylum
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species

    #getters and setters if specific data in an object needs to be changed

    def get_kingdom(self):
        return self.kingdom

    def set_kingdom(self, value):
        self.kingdom = value

    def get_phylum(self):
        return self.phylum

    def set_phylum(self, value):
        self.phylum = value

    def get_order(self):
        return self.order

    def set_order(self, value):
        self.order = value

    def get_family(self):
        return self.family

    def set_family(self, value):
        self.family = value

    def get_genus(self):
        return self.genus

    def set_genus(self, value):
        self.genus = value

    def get_species(self):
        return self.species

    def set_species(self, value):
        self.species = value
