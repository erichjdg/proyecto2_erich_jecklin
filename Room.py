class Room: 

  def __init__(self,letter,number,capacity,r_type,status,room_id):
    self.letter = letter
    self.number = number
    self.capacity = capacity
    self.r_type = r_type
    self.status = status
    self.room_id = room_id


  # El status representa si la habitacion esta o no disponible. True significa disponible
