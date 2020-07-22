from Person import Person

class Client(Person):
  def __init__(self,name,dni,age,discapacity,r_type,room_id,payment,tour,restaurant):
    
    Person.__init__(self,name,dni,age,discapacity)
    self.r_type = r_type
    self.room_id = room_id
    self.payment = payment
    self.tour = tour
    self.restaurant = restaurant