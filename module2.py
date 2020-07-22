#Gestion de habitaciones

from Room import Room
from module1 import select_cruise
from sort_search import search_available
from Person import Person
from Client import Client
import file_management as fm
from math_operations import check_prime
from math_operations import abundant_num





def select_route(data_base):


  """
  Regresa el numero con de la ruta seleccionada

  """


  print('Rutas disponibles:')
  for i in range(len(data_base)):

    
    print(f'{i+1}\t',*data_base[i]["route"],sep = ' - ')

  while True:
    try:
      answer = int(input('Seleccione la ruta: '))

      if answer != 1 and answer != 2 and answer != 3 and answer != 4:
        raise Exception
      break

    except:

      print('Respuesta invalida. Intente nuevamente: ')

  return answer

def fill_rooms(data_base,letters,cruise_answer,r_type):

  """

  Regresa una lista con objetos tipo room

  cruise_answer representa el crucero seleccionado

  r_type representa el tipo de habitacion

  letters representa la letra del pasillo

  """
  rooms = []
  for r_letter in range(0,data_base[cruise_answer-1]["rooms"][r_type][0]):
    for r_number in range(1,data_base[cruise_answer-1]["rooms"][r_type][1]+1):
      if r_type == "simple":
        room = Room(letters[r_letter],r_number,data_base[cruise_answer-1]["capacity"][r_type],"Sencilla","Disponible",f"S{letters[r_letter]}{r_number}")
      elif r_type == "premium":
        room = Room(letters[r_letter],r_number,data_base[cruise_answer-1]["capacity"][r_type],"Premium","Disponible",f"P{letters[r_letter]}{r_number}")
      else: 
        room = Room(letters[r_letter],r_number,data_base[cruise_answer-1]["capacity"][r_type],"VIP","Disponible",f"V{letters[r_letter]}{r_number}")

      
      rooms.append(room)
  
  return rooms

def select_room_type(): 


  "Regresa el numero del tipo de habitacion seleccionada, y un string que contiene el nombre del tipo de habitacion"

  while True:

    try:
      
      #tipo de habitacion pedido
      r_type_answer = int(input('Tipos de habitaciones:\n1. Sencilla\n2. Premium\n3. VIP\nPor favor seleccione el tipo de habitación: '))
      if r_type_answer != 1 and r_type_answer != 2 and r_type_answer != 3:
        raise Exception 
      
      break
    except:

      print('Valor invalido. Intente nuevamente')
  
  if r_type_answer == 1:
      r_type_key = "simple"
  elif r_type_answer == 2:
    r_type_key = "premium"
  else:
    r_type_key = "vip"

  return r_type_answer,r_type_key


def show_floors(cruise,r_type_answer):

  """

  Muestra en pantalla las habitaciones del piso seleccionado

  """
  

  
  for habitacion in cruise[r_type_answer-1]:
    if habitacion.r_type == 'Sencilla':
      print(f'Pasillo: {habitacion.letter}\tNumero: {habitacion.number}\tCapacidad: {habitacion.capacity}\tTipo: {habitacion.r_type}\tPuede tener servicio a la habitación\t{habitacion.status}')
    elif habitacion.r_type == 'Premium':
      print(f'Pasillo: {habitacion.letter}\tNumero: {habitacion.number}\tCapacidad: {habitacion.capacity}\tTipo: {habitacion.r_type}\tPosee vista al mar\t{habitacion.status}')
    else:
      print(f'Pasillo: {habitacion.letter}\tNumero: {habitacion.number}\tCapacidad: {habitacion.capacity}\tTipo: {habitacion.r_type}\tPuede albergar fiestas privadas\t{habitacion.status}')



def floor_represent(data_base,cruise_answer):

  """

  Regresa una lista llena con listas que contienen los datos de habitaciones de cada piso

  answer representa el crucero seleccionado

  

  letters representa la letra del pasillo

  """


  letters=['A','B','C','D','E','F','G','H','I','J','K','L','M']
  floors = []
  
  
  simple_rooms = fill_rooms(data_base,letters,cruise_answer,"simple")
  premium_rooms = fill_rooms(data_base,letters,cruise_answer,"premium")
  vip_rooms = fill_rooms(data_base,letters,cruise_answer,"vip")

  
  floors.append(simple_rooms)
  floors.append(premium_rooms)
  floors.append(vip_rooms)
  

  
  return floors
  

def client_register(clients):


  """
  Regresa un objeto de tipo Person, con los datos del cliente

  """

  while True:

    try:

      name = input('Por favor indique su nombre: ')
      dni = int(input('Por favor indique su numero de cedula: '))
      


      age = int(input('Por favor indique su edad: '))
      discapacity = input('Por favor indique si posee alguna discapacidad (1 - Si / 2 - No): ')
      if discapacity != "1" and discapacity != "2":
        raise Exception
      break
    except:

      print("Error en el ingreso de datos. Intente nuevamente")


  person = Person(name,dni,age,discapacity)

  return person

def input_people_quantity():

  "Regresa la cantidad de personas que quieren hospedarse"

  while True:

    try:
      
      
      people_quantity = int(input('Por favor ingrese la cantidad de personas a hospedarse/comprar tour: '))
      if people_quantity == 0:
        raise Exception
      break
    except:

      print('Valor invalido. Intente nuevamente')
  return people_quantity

def payment(client):
  
  """Calcula el pago al paciente dependiendo de las condiciones dadas

  Parametros:
      client (list): lista que contiene los datos del cliente

  Returns:
      pago (float): monto por pagar
  """
  
  
  pago_base = client.payment
  pago = pago_base
  if client.discapacity == "1":
    pago -= pago_base*(0.3)

  if check_prime(client.dni):
    pago -= pago_base*(0.1)
  if abundant_num(client.dni):
    pago -= pago_base*(0.15)
    
  return pago

def create_bill(new_clients,base_payment):

  """

  Imprime en pantalla la factura de el alquiler de la/las habitacion(es).

  Parametros:

  new_clients: lista con objetos de tipo Client

  base_payment: precio de la habitacion sin descuentos

  """
  total = 0
  print("\n")
  for client in new_clients:

    bill = f"Nombre: {client.name}\nEdad: {client.age}\nCedula: {client.dni}\nHabitacion: {client.room_id}\nPrecio: {base_payment}\nMonto a Pagar: {client.payment}\n "
    total += client.payment
    print(bill)

  tax = total*0.16
  total_iva = total + tax
  print(f'Total sin iva: {total}')
  print(f'Total: {total_iva} ')
  

def sell_room(cruise,data_base,cruise_answer,file_name):
  
  """
  Cruise: lista con informacion de las habitaciones del crucero, esta compuesta por listas por cada tipo de habitacion

  data_base: base de datos 

  cruise_answer: crucero seleccionado

  file_name: nombre del archivo de texto donde se almacenaran los datos de las habitaciones del respectivo crucero


  """
  
  r_type_answer,r_type_key = select_room_type()
  
  #Se busca si hay habitaciones del tipo seleccionado disponibles
  first_index = search_available(cruise[r_type_answer-1],0,"Disponible",1)
  
 


  
  #Primero se valida si existe un archivo con los datos de clientes hospedados en el crucero, de ser asi se llena una lista con los datos guardados en el mismo, de lo contrario se crea la lista vacía
  clients_file = "clients_cruise"+str(cruise_answer)+".txt"
  count_clients = fm.check_empty(clients_file)
  if count_clients:
    clients = []
  else:
    clients = fm.fill_clients(clients_file)
    print('Clientes lleno')
  #clients = []


  # Si no encontró habitacion disponible, significa que todas las habitaciones de ese tipo se encuentran ocupadas
  if first_index != "No encontrado":
    show_floors(cruise,r_type_answer)
    print("")
    
        
        
    people_quantity = input_people_quantity()
        
    #Habitaciones rentadas
    room_rented = 1

    #lista con las posiciones de habitaciones disponibles encotradas
    found_rooms = []
    
    found_rooms.append(first_index)
    #Si se desean hospedar mas personas de las que admite una habitacion, se debe aumentar el numero de habitaciones a rentar
    if people_quantity > (room_rented*data_base[cruise_answer-1]["capacity"][r_type_key]):
      while people_quantity > (room_rented*data_base[cruise_answer-1]["capacity"][r_type_key]) and first_index<len(cruise[r_type_answer-1]):

        room_rented +=1
        first_index += 1

        #Se busca si hay mas habitaciones del tipo seleccionado disponibles
        found_index = search_available(cruise[r_type_answer-1],first_index,"Disponible",1)
        if found_index != "No encontrado":
          found_rooms.append(found_index)
        
    # Si la cantidad de habitaciones disponibles encontradas no concuerda con la cantidad de habitaciones que se deben rentar para ocupar a todas las personas indicadas, no se podrá continuar con la operacion.
    if len(found_rooms) == room_rented:
      
      regist_count= 1
      index = 0
     
      new_clients = []
      print(found_rooms)

      #Se procede a realizar la toma de datos para la cantidad de personas que fue ingresada
      while regist_count <= people_quantity and index < (len(found_rooms)):
        print(f"Registro: {regist_count}")
        while True:
          try:

            person = client_register(clients)


            
            client = Client(person.name,person.dni,person.age,person.discapacity,r_type_key,r_type_key[0].upper()+cruise[r_type_answer-1][found_rooms[index]].letter + str(cruise[r_type_answer-1][found_rooms[index]].number),data_base[cruise_answer-1]["cost"][r_type_key],0,0)
            client.payment = payment(client)
            
            base_payment = data_base[cruise_answer-1]["cost"][r_type_key]
            

            if len(clients) != 0:
              
              #Se valida si la persona ya se encontraba registrada
              found = search_available(clients,0,client.dni,2)
              
              if found != "No encontrado":
                
                print("Este numero de cedula ya se encuentra en la base de datos.")
                raise Exception
              else:
                clients.append(client)
                new_clients.append(client)
                regist_confirm = 'Registro Exitoso'
                break
            else:
              clients.append(client)
              new_clients.append(client)
              regist_confirm = 'Registro Exitoso'
              break
          except:
            print("Error. El numero de cedula ya se encuentra en la base de datos")
        cruise[r_type_answer-1][found_rooms[index]].status = "Ocupada"
        
        
        index = regist_count//data_base[cruise_answer-1]["capacity"][r_type_key]
        regist_count +=1

      if regist_confirm == 'Registro Exitoso':  
        print(regist_confirm)
        print(found_rooms)
        #total = 0
        print("\n")

        create_bill(new_clients,base_payment)
        

        
        fm.create_cruise_txt(cruise,file_name)
        fm.append_client_txt(new_clients,clients_file)
        
    else:
      print(f'Lo sentimos, no tenemos suficietes habitaciones {r_type_key} disponibles')
  else:
        print(f'Lo sentimos, no tenemos habitaciones {r_type_key} disponibles')
  
  

  
  return cruise

def select_operation():
  while True:
    try:
      operation_answer = input('Operaciones:\n1. Ver habitaciones\n2. Rentar habitaciones\n3. Buscar habitaciones\n4. Dejar una habitacion\nSeleccione la operacion a realizar: ')
      if operation_answer != '1' and operation_answer != '2' and operation_answer != '3' and operation_answer != '4':
        raise Exception
      break

    except:
      print('Valor invalido. Intente nuevamente')
  return operation_answer
  

def search_room(cruise,cruise_answer,data_base):

  """
  Funcion que maneja los tipos de busqueda de habitacion que se desea realizar

  """

  clients_file = "clients_cruise"+str(cruise_answer)+".txt"
  count_clients = fm.check_empty(clients_file)
  if count_clients:
    clients = []
  else:
    clients = fm.fill_clients(clients_file)
    print('Clientes lleno')
  for i in range(len(clients)):
    print(clients[i].room_id)
  search_answer = "1"

  while search_answer == "1":

    if len(clients) == 0:
      msg = "No hay clientes hospedados en este crucero"
      print(msg)
      return msg
    #else:
    while True:
      try:
        search_filter = input("Filtros de busqueda:\n1. Tipo\n2. Capacidad\n3. Tipo + Pasillo + Número (ej. SA9)\nSeleccione filtro de busqueda: ")
        if search_filter != '1' and search_filter != '2' and search_filter != '3':
          raise Exception
        break
      except:
        print('Valor invalido. Intente nuevamente')
    if search_filter == '1':
      r_type_answer,r_type_key = select_room_type()
      show_floors(cruise,r_type_answer)
      search_answer = input("Presione 1 si desea realizar otra busqueda: ")
    elif search_filter == '2':
      search_answer = room_capacity_search(cruise)
      
    else: #si search_filter == 3
      search_answer = room_id_search(cruise,clients)

      
          
      
      

def room_id_search(cruise,clients):

  """
  Funcion que muestra los clientes hospedados en una habitacion particular. Recibe como parametros la lista con los datos de las habitaciones del crucero y la lista con los datos de los clientes hospedados en el mismo
  """

  while True:
    try:
      room_id = input("Indique el Tipo + Pasillo + Número (ej. SA9):  ").upper()
      break
    except:
      print('Valor invalido. Intente nuevamente')
      
      
  r_type = 0  #Denota el indice del tipo de habitacion
  end_search = False

  #Mientras se de la condicion de que end search es Falso, se seguira repitiendo el ciclo. Tambien se valida de que r_type no supere el tamaño de la lista cruise 
  while r_type < len(cruise) and end_search == False:
    room_search = search_available(cruise[r_type],0,room_id,4)
    if room_search != "No encontrado":
      
      end_search = True
    r_type += 1
  if room_search != "No encontrado":
    if len(clients) != 0:
      first_index = search_available(clients,0,room_id,4)
      print(first_index)
      found_rooms = []
      found_rooms.append(first_index)
      if first_index != "No encontrado":
        
        end_search = False
        while end_search == False:
          first_index += 1
          if first_index < len(clients):
            
            found_index = search_available(clients,first_index,room_id,4)
            if found_index != "No encontrado":
              found_rooms.append(found_index)
              print(found_index)
            else:
              end_search = True
          else:
            end_search = True
          
          
        print("Clientes hospedados en esta habitacion:")
        for index in found_rooms:
          print(f"\t{clients[index].name}")
        print("")
        search_answer = input("Presione 1 si desea realizar otra busqueda: ")
      else:
        print("No hay clientes hospedados en esta habitacion")
        search_answer = input("Presione 1 si desea realizar otra busqueda: ")
      
  else:
    print("La habitacion ingresada no existe")
    search_answer = input("Presione 1 si desea realizar otra busqueda: ")
  return search_answer

def room_capacity_search(cruise):


  """
  Funcion que muestra las habitaciones con la capacidad de personas indicada
  """


  while True:
    try:
      room_capacity = int(input("Ingrese la capacidad de la habitacion que desea buscar: "))
      break
    except:
      print('Valor invalido. Intente nuevamente')
      
      
      
      
  r_type = 0
  end_search = False
  while r_type < len(cruise) and end_search == False:
    found_index = search_available(cruise[r_type],0,room_capacity,3)
    if found_index != "No encontrado":
      
      end_search = True
    r_type += 1
  if end_search == True:
    
    show_floors(cruise,r_type)
    print("\n")
    search_answer = input("Presione 1 si desea realizar otra busqueda")
  else: 
    print("No se encontró ninguna habitacion con esa capacidad")
    search_answer = input("Presione 1 si desea realizar otra busqueda: ")  
  return search_answer

def leave_room(cruise,cruise_answer,data_base):




  
  clients_file = "clients_cruise"+str(cruise_answer)+".txt"
  count_clients = fm.check_empty(clients_file)
  if count_clients:
    clients = []
  else:
    clients = fm.fill_clients(clients_file)
    print('Clientes lleno')
  
  while True:
    
    try:
      dni = int(input('Por favor ingrese su dni:'))
      break
    except:
      print('Valor invalido. Intente nuevamente')
  if len(clients) != 0:    
    dni_index = search_available(clients,0,dni,2)
    if dni_index != "No encontrado":
      room_id = clients[dni_index].room_id
      clients[dni_index].room_id = "Salió"
      fm.create_client_txt(clients,clients_file)


      room_id_index = 0
      end_search = False
      found_rooms = []
      while end_search == False:
        
        if room_id_index < len(clients):
          
          found_index = search_available(clients,room_id_index,room_id,4)
          if found_index != "No encontrado":
            found_rooms.append(found_index)
            
          
        else:
          end_search = True
        room_id_index += 1
      print(len(found_rooms))
      if len(found_rooms) == 0:
        i = 0
        end_search = False
        while i < len(cruise) and end_search == False:
          room_index = search_available(cruise[i],0,room_id,4)
          if room_index != "No encontrado":
            cruise[i][room_index].status = "Disponible"
            end_search = True
          i += 1
        
        file_name = "rooms_cruise"+str(cruise_answer)+".txt"
        fm.create_cruise_txt(cruise,file_name)
      
      
    else:
      print("Este cliente no se encuentra en la base de datos")

  else:

    print("No hay clientes hospedados en este crucero")

  
  

#Las siguientes funciones manejan las operaciones de ver habitaciones, venta de habitaciones, busqueda de habitaciones y de dejar habitaciones respectivamente
  
def module2_operation1(data_base,*cruise):
  cruise_answer = select_cruise(data_base)
  cruise1,cruise2,cruise3,cruise4 = cruise
    
  r_type_answer,r_type_key = select_room_type()
  
  if cruise_answer == 1:
    show_floors(cruise1,r_type_answer)
  elif cruise_answer == 2:
    show_floors(cruise2,r_type_answer)
  elif cruise_answer == 3:
    show_floors(cruise3,r_type_answer)
  else:
    show_floors(cruise4,r_type_answer)
  

def module2_operation2(data_base,*cruise):

   
  cruise1,cruise2,cruise3,cruise4 = cruise
  
  
  while True:
    try:
      cruise_route = input("\nPor favor indique criterio de seleccion:\n1. Crucero\n2. Ruta\nSeleccione el criterio: ")
      if cruise_route != '1' and cruise_route != '2':
        raise Exception
      break

    except:
      print('Valor invalido. Intente nuevamente')
  if cruise_route == "1":
    cruise_answer = select_cruise(data_base)
  else:
    cruise_answer = select_route(data_base)
  if cruise_answer == 1:
    
    cruise1 = sell_room(cruise1,data_base,cruise_answer,"rooms_cruise1.txt")
    
  elif cruise_answer == 2:
    
    cruise2 = sell_room(cruise2,data_base,cruise_answer,"rooms_cruise2.txt")
    
  elif cruise_answer == 3:
    
    cruise3 = sell_room(cruise3,data_base,cruise_answer,"rooms_cruise3.txt")
    
  else:
    
    cruise4 = sell_room(cruise4,data_base,cruise_answer,"rooms_cruise4.txt")
    

  return cruise1,cruise2,cruise3,cruise4

def module2_operation3(data_base,*cruise):

  cruise1,cruise2,cruise3,cruise4 = cruise

  cruise_answer = select_cruise(data_base)
  if cruise_answer == 1:
    search_room(cruise1,cruise_answer,data_base)
  elif cruise_answer == 2:
    search_room(cruise2,cruise_answer,data_base)
  elif cruise_answer == 3:
    search_room(cruise3,cruise_answer,data_base)
  else:
    search_room(cruise4,cruise_answer,data_base)

def module2_operation4(data_base,*cruise):
  cruise_answer = select_cruise(data_base)
  cruise1,cruise2,cruise3,cruise4 = cruise
    
  
  
  if cruise_answer == 1:
    temp = leave_room(cruise1,cruise_answer,data_base)
    if temp != None:
      cruise1 = temp
  elif cruise_answer == 2:
    temp = leave_room(cruise2,cruise_answer,data_base)
    if temp != None:
      cruise2 = temp
  elif cruise_answer == 3:
    temp = leave_room(cruise3,cruise_answer,data_base)
    if temp != None:
      cruise3 = temp
  else:
    temp = leave_room(cruise4,cruise_answer,data_base)
    if temp != None:
      cruise4 = temp
  


    


  










  
  
  
  
  
 




  
  

  







  




  










