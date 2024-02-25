from backend.bathroom import Bathroom

class Building:
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long
        self.bathrooms = []
    
    def getName(self):
        return self.name
    
    def getBathrooms(self):
        return self.bathrooms
    
    def getLongitude(self):
        return self.long
    
    def getLatitude(self):
        return self.lat
    
    def addBathroom(self, bathroom: Bathroom): 
        self.bathrooms.append(bathroom)
    
    # mathod for getting responses from form
    # name is bathroom name
    # restock and running_low should be bool
    # item will be string: either 'pad' or 'tampon'
    def update(self, name, restock, running_low, item):
        for bathroom in self.bathrooms:
            if bathroom.getName() == name:
                if restock:
                    if item == "pad":
                        bathroom.pad_restock = True
                    elif item == "tampon":
                        bathroom.tampon_restock = True
                elif running_low:
                    if item == "pad":
                        bathroom.pad_running_low = True
                    elif item == "tampon":
                        bathroom.tampon_running_low = True