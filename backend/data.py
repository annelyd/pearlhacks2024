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
        Union = Building("Student Union", 35.9102, -79.0476)
        third_floor = Bathroom("Third Floor", True, True, False, False, True, False, False)
        near_alpine = Bathroom("Across from Alpine", True, False, False, False, True, False, True)
        auditorium = Bathroom("Near Auditorium", True, True, False, True, True, False, False)
        bottom_floor = Bathroom("Bottom Floor", False, True, False, False, True, False, False)
        Union.addBathroom(third_floor)
        Union.addBathroom(near_alpine)
        Union.addBathroom(auditorium)
        Union.addBathroom(bottom_floor)
        self.addBuilding(Union)

        # Populating Campus Y Bathroom Data
        CampusY = Building("Campus Y", 35.9114, -79.0512)
        meantime = Bathroom("Near Meantime", False, False, False, False, True, True, True)
        second_floor = Bathroom("Second Floor", True, True, False, False, True, False, False)
        CampusY.addBathroom(meantime)
        CampusY.addBathroom(second_floor)
        self.addBuilding(CampusY)

        # Populating Davis Library Bathroom Data
        # DavisLibrary = Building("Davis Library", 35.911048, -79.048055)
        # first_floor = Bathroom("First Floor", False, False, False, True, True, True, False)
        # DavisLibrary.addBathroom(first_floor)
        # self.addBuilding(DavisLibrary)

        return self.buildings