from Room import Room
from Client import Client
from Tour import Tour
from Dish import Dish
from Combo import Combo

"""

Las siguientes funciones son para la creacion y lectura de archivos

"""

def check_empty(file_name):
#Regresa True si el archivo esta vacio o no existe

  
  try:

    count = 0
    with open(file_name) as f:
      for line in f:
        count += 1
    if count == 0:
      
      return True
    else:
      return False
  except:
    return True


def fill_clients(file_name):
  clients = []

  with open(file_name) as f:
    for line in f:
      cliente = line[:-1].split(',')
      client = Client(cliente[0],int(cliente[1]),int(cliente[2]),cliente[3],cliente[4],cliente[5],float(cliente[6]),float(cliente[7]),float(cliente[8]))
      clients.append(client)
    return clients

def fill_cruise(file_name):

  floors = []
  simple_rooms = []
  premium_rooms = []
  vip_rooms = []

  with open(file_name) as f:
    for line in f:
      habitacion = line[:-1].split(',')
      room = Room(habitacion[0],int(habitacion[1]),int(habitacion[2]),habitacion[3],habitacion[4],f"{habitacion[5]}")
      if room.r_type == "Sencilla":
        simple_rooms.append(room)
      elif room.r_type == "Premium":
        premium_rooms.append(room)
      else:
        vip_rooms.append(room)
  floors.append(simple_rooms)
  floors.append(premium_rooms)
  floors.append(vip_rooms)

  return floors



  

def create_cruise_txt(cruise,file_name):
  with open(file_name,'w') as f:
    for floor in cruise:
      for room in floor:
        f.write(f'{room.letter},{room.number},{room.capacity},{room.r_type},{room.status},{room.room_id}\n') 

  


def append_client_txt(clients,file_name):
  with open(file_name,'a') as f:
    for client in clients:
      
      f.write(f'{client.name},{client.dni},{client.age},{client.discapacity},{client.r_type},{client.room_id},{client.payment},{client.tour},{client.restaurant}\n') 

  

def create_client_txt(clients,file_name):
  with open(file_name,'w') as f:
    for client in clients:
      
      f.write(f'{client.name},{client.dni},{client.age},{client.discapacity},{client.r_type},{client.room_id},{client.payment},{client.tour},{client.restaurant}\n') 

  

def append_tour_txt(tours,file_name):
  with open(file_name,'a') as f:
    for tour in tours:
      #dni,tour_id,people_quantity,payment,time
      f.write(f'{tour.dni},{tour.tour_id},{tour.people_quantity},{tour.payment},{tour.time}\n') 

  

def create_tour_txt(tours,file_name):
  with open(file_name,'w') as f:
    for tour in tours:
      #dni,tour_id,people_quantity,payment,time
      f.write(f'{tour.dni},{tour.tour_id},{tour.people_quantity},{tour.payment},{tour.time}\n') 

  print(f'Archivo {file_name} creado')

def fill_tours(file_name):
  tours = []

  with open(file_name) as f:
    for line in f:
      tour = line[:-1].split(',')
      new_tour = Tour(int(tour[0]),int(tour[1]),int(tour[2]),float(tour[3]),tour[4])
      tours.append(new_tour)
    return tours



def create_dishes_txt(dishes,file_name):
  with open(file_name,'w') as f:
    for dish in dishes:
      
      f.write(f'{dish.name},{dish.price},{dish.clasification}\n') 

  

def fill_dishes(file_name):
  dishes = []

  with open(file_name) as f:
    for line in f:
      dish = line[:-1].split(',')
      new_dish = Dish(dish[0],float(dish[1]),dish[2])
      dishes.append(new_dish)
    return dishes

def create_combos_txt(combos,file_name):
  with open(file_name,'w') as f:
    for combo in combos:
      
      f.write(f'{combo.name},{combo.price},{combo.products}\n') 

  

def fill_combos(file_name):
  combos = []

  with open(file_name) as f:
    for line in f:
      combo = line[:-1].split(',')
      new_combo = Combo(combo[0],float(combo[1]),combo[2])
      combos.append(new_combo)
    return combos


