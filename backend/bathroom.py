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
    return self.pad_running_low
  
  def getTampon(self):
    return self.tampon_running_low
  
  def getisFree(self):
    return self.free
  
  def getPadRestock(self):
    return self.pad_restock
  
  def getTamponRestock(self):
    return self.tampon_restock
  
  # def has(self):
  #   if self.tampons and self.pads:
  #     return "both"
  #   elif self.tampons and not self.pads:
  #     return "tampons"
  #   elif self.pads and not self.tampons:
  #     return "pads"