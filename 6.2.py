print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

class Hinhchunhat(object): 
   def __init__(self, dai, rong): 
      self.dai = dai
      self.rong = rong
############################### 
   def area(self): 
      return self.dai * self.rong
aHinhchunhat= Hinhchunhat(4, 5) 
print (aHinhchunhat.area())
