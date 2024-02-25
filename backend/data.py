from backend.bathroom import Bathroom
from backend.building import Building

class Data:
    def __init__(self):
        self.buildings = []
    
    def addBuilding(self, building: Building):
        self.buildings.append(building)
    
    def getBuildings(self):
        return self.buildings

    def getDummyData(self):
        # Populating Student Union Bathroom Data
        Union = Building("Student Union", 35.9097, -79.0483)
        third_floor = Bathroom("Third Floor", True, True, False, False, True, False, False)
        near_alpine = Bathroom("Across from Alpine", True, True, False, False, True, False, False)
        auditorium = Bathroom("Near Auditorium", True, True, False, False, True, False, False)
        bottom_floor = Bathroom("Bottom Floor", True, True, False, False, True, False, False)
        Union.addBathroom(third_floor)
        Union.addBathroom(near_alpine)
        Union.addBathroom(auditorium)
        Union.addBathroom(bottom_floor)

        # Populating Campus Y Bathroom Data
        CampusY = Building("Campus Y", 35.9114, -79.0512)
        meantime = Bathroom("Near Meantime", True, True, False, False, True, False, False)
        second_floor = Bathroom("Second Floor", True, True, False, False, True, False, False)
        CampusY.addBathroom(meantime)
        CampusY.addBathroom(second_floor)
        
        self.addBuilding(Union)
        self.addBuilding(CampusY)

        return self.buildings