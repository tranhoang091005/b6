print("TRẦN DANH HOÀNG")
print("MSSV:235752021610064")

class Nguoi(object):
    def getGender(self):
        return "Unknown"
class Nam(Nguoi):
    def getGender(self):
        return("Nam")
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
aNam = Nam()
aNu = Nu()

print(aNam.getGender())
print(aNu.getGender())
