#Gestion de cruceros

import requests 

  
def api_cruise():

  #Regresa un diccionario con la base de datos de cruceros
  url = 'https://saman-caribbean.vercel.app/api/cruise-ships'
  request = requests.get(url) 

  
  # Se extrae la data en formato json

  data_base = request.json() 

  return data_base

def select_cruise(data_base):

  #El numero del crucero seleccionado

  print('Cruceros disponibles:')
  for i in range(len(data_base)):

    
    print(f'{i+1}\t{data_base[i]["name"]}')

  while True:
    try:
      answer = int(input('Seleccione el crucero: '))

      if answer != 1 and answer != 2 and answer != 3 and answer != 4:
        raise Exception
      break

    except:

      print('Respuesta invalida. Intente nuevamente: ')

  return answer

def room_quantity(data_base,answer,room_type):

  #Regresa cantidad de habitaciones de cada tipo que hay en un crucero

  quantity = data_base[answer-1]["rooms"][room_type][0]*data_base[answer-1]["rooms"][room_type][1]

  

  return quantity

def show_room(data_base,answer,simple_quantity,premium_quantity,vip_quantity):


  #Imprime en pantalla la informacion de una habitacion 

  print(f'Sencilla\tCosto: {data_base[answer-1]["cost"]["simple"]}\tCantidad: {simple_quantity}\tCapacidad: {data_base[answer-1]["capacity"]["simple"]} personas')
  print(f'Premium\t\tCosto: {data_base[answer-1]["cost"]["premium"]}\tCantidad: {premium_quantity}\tCapacidad: {data_base[answer-1]["capacity"]["premium"]} personas')
  print(f'VIP\t\t\tCosto: {data_base[answer-1]["cost"]["vip"]}\tCantidad: {vip_quantity}\t\tCapacidad: {data_base[answer-1]["capacity"]["vip"]} personas')


def show_cruise(data_base):

  
  """

  Imprime en pantalla los datos de las habitaciones del crucero seleccionado

  Recibe como parametro la base de datos con la informacion de los cruceros

  """
  
  
  answer = select_cruise(data_base)
  
  

  print(f'\nNombre: {data_base[answer-1]["name"]}')
  print(f'Ruta: ')
  print('\t',*data_base[answer-1]["route"],sep = ' - ')
  date = data_base[answer-1]["departure"]
  print(f'Fecha de salida: {date[0:10]}')
  print('Tipos de Habitaciones:')

  simple_quantity = room_quantity(data_base,answer,"simple")
  premium_quantity = room_quantity(data_base,answer,"premium")
  vip_quantity = room_quantity(data_base,answer,"vip")

  show_room(data_base,answer,simple_quantity,premium_quantity,vip_quantity)

  
 
  
  