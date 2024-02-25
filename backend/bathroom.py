class Bathroom:
      def __init__(self, name, pads, tampons, pad_running_low, tampon_running_low, free, pad_restock, tampon_restock):
        self.name = name
        self.pads = pads
        self.tampons = tampons
        self.pad_running_low = pad_running_low 
        self.tampon_running_low = tampon_running_low 
        self.free = free
        self.pad_restock = pad_restock
        self.tampon_restock = tampon_restock

      def getName(self):
        return self.name
      
      def getPad(self):
        return self.pads
      
      def getTampon(self):
        return self.tampons
      
      def padLow(self):
         return self.pad_running_low
      
      def tamponLow(self):
         return self.tampon_running_low
      
      def getisFree(self):
        return self.free
      
      def getPadRestock(self):
        return self.pad_restock
      
      def getTamponRestock(self):
        return self.tampon_restock