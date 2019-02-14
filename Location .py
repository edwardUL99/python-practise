class Location:
    def __init__(self,number,street,address1,address2):
        self.number = number
        self.street = street
        self.address1 = address1
        self.address2 = address2
    
    def fullAddress(self):
        print("\n%d %s" % (self.number, self.street))
        print("%s" % (self.address1))
        print ("%s" % (self.address2))
        
object = Location(27,"The Hawthorns", "Castletroy", "Limerick")
object.fullAddress()

object.number = str (object.number)

a = object.number + "," + " " + object.street + "," +" " + object.address1 + "," + " " + object.address2
locList = a
print("\n" + a)