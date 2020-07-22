#Venta de Tours
import file_management as fm
from module2 import input_people_quantity
from sort_search import search_available
from Tour import Tour

def select_tour():


  """
  Funcion que regresa el numero de Tour seleccionado
  """

  print('Tours disponibles:\n1. Tour en el puerto\n2. Degustacion de comida local\n3. Trotar por el pueblo/ciudad\n4. Visita a lugares historicos')
  

  while True:
    try:
      answer = int(input('Seleccione el tour: '))

      if answer != 1 and answer != 2 and answer != 3 and answer != 4:
        raise Exception
      break

    except:

      print('Respuesta invalida. Intente nuevamente: ')

  return answer

def tour_price(tour_answer,people_quantity):

  """
  Funcion que regresa el pago del tour seleccionado

  """

  if tour_answer == 1:
    base_price = 30
    limit = 4
    
    discount_person = 3
  elif tour_answer == 2:
    base_price = 100
    limit = 2
    
    discount_person = False
  elif tour_answer == 3:
    payment = 0
    return payment
  else:
    base_price = 40
    limit = 4
    
    discount_person = 3

  payment = 0

  
  if people_quantity <= limit:
    cont = 1

    while cont <= people_quantity:
      
      sum_payment = base_price

      if discount_person != False and cont >= discount_person:

        sum_payment = base_price*(1-0.1)
      
      payment += sum_payment
      cont += 1
      

    return payment

  else:

    print("Este Tour no se encuentra disponible para esta cantidad de personas")

def tour_time(tour_answer):
  if tour_answer == 1:
    time = "7 A.M"
  elif tour_answer == 2:
   time = "12 A.M"
  elif tour_answer == 3:
    time = "6 A.M"
  else:
    time = "10 A.M"

  return time

def tour_limit(tour_answer):

  if tour_answer == 1:
    limit = 10
  elif tour_answer == 2:
    limit = 100   
  elif tour_answer == 3:
    limit = False
  else:
    limit = 15

  return limit

def tour_bill(client,payment):

  bill = f"Nombre: {client.name}\nEdad: {client.age}\nCedula: {client.dni}\nHabitacion: {client.room_id}\nMonto a Pagar: {payment}\n "

  print(bill)

def sell_tours(cruise,cruise_answer):



  """

  Funcion que permite vender tours a los clientes hospedados en un respectivo crucero, ademas de almacenar los datos de dichas ventas

  """

  #Primero se valida si existe un archivo con los datos de tours comprados en el crucero, de ser asi se llena una lista con los datos guardados en el mismo, de lo contrario se crea la lista vacía

  tours_file = "tours_cruise"+str(cruise_answer)+".txt"
  count_tours = fm.check_empty(tours_file)
  if count_tours:
    tours = []
  else:
    tours = fm.fill_tours(tours_file)
    

  
  #Primero se valida si existe un archivo con los datos de clientes hospedados en el crucero, de ser asi se llena una lista con los datos guardados en el mismo, de lo contrario se crea la lista vacía
  clients_file = "clients_cruise"+str(cruise_answer)+".txt"
  count_clients = fm.check_empty(clients_file)
  if count_clients:
    clients = []
  else:
    clients = fm.fill_clients(clients_file)
    

  while True:
    
    try:
      dni = int(input('Por favor ingrese su dni:'))
      break
    except:
      print('Valor invalido. Intente nuevamente')

  #Se valida si la lista clientes no esta vacia, de estarlo se indica que no hay clientes hospedados en el crucero especificado

  if len(clients) != 0:

    #Se busca la cedula ingresada en la base de datos para validar si se encuentra registrado. De no estarlo no podrá comprar un tour

    search_dni = search_available(clients,0,dni,2)
     

    if search_dni != "No encontrado" and clients[search_dni].room_id != "Salió":
      tour_answer = select_tour()
      people_quantity = input_people_quantity()
      payment = tour_price(tour_answer,people_quantity)
      time = tour_time(tour_answer)
      limit = tour_limit(tour_answer)

      if len(tours) == 0:
        #Si payment es igual a none, significa que no se pudo comprar el tour ya que se exedio la cantidad de personas
        if payment != None:

          new_tour = Tour(dni,tour_answer,people_quantity,payment,time)
          #Se crea un archivo que contenga los datos del Tour comprado
          tours.append(new_tour)
          fm.create_tour_txt(tours,tours_file)

          #Se actualiza la base de datos de clientes indicando lo que pago en el tour
          clients[search_dni].tour = payment
          fm.create_client_txt(clients,clients_file)

          tour_bill(clients[search_dni],payment)

          print("Compra de tour exitosa")

          

      
        
      else:
        dni_tours = []
        search_dni_tours = search_available(tours,0,dni,2)

        
        first_tour_index = 0
        while first_tour_index < len(tours):
          
          
          found_tour_index = search_available(tours,first_tour_index,tour_answer,5)
          

          if found_tour_index != "No encontrado":
            dni_tours.append(found_tour_index)
            first_tour_index = found_tour_index
            first_tour_index += 1
            
          else:

            first_tour_index += 1
        print(dni_tours)
        if search_dni_tours != "No encontrado" and  tours[search_dni_tours].tour_id == tour_answer:
          print("No puede comprar el mismo tour varias veces")
        else:

          if payment != None:
            total_people = 0
            if len(dni_tours) != 0:
              for i in dni_tours:
                
                total_people += tours[i].people_quantity
            print(limit)
            print(total_people+people_quantity)

            #Se valida que no se exceda el cupo admitido de personas para el Tour
            if (total_people+people_quantity) > limit and limit != False:

              print(f"Lo sentimos, no hay cupos suficientes para {people_quantity} personas")

            else:
              new_tour = Tour(dni,tour_answer,people_quantity,payment,time)

              tours.append(new_tour)
              fm.create_tour_txt(tours,tours_file)

              clients[search_dni].tour += payment
              fm.create_client_txt(clients,clients_file)

              tour_bill(clients[search_dni],payment)

              print("Compra de tour exitosa")

              
    
    else:
      print("El numero de cedula ingresado no se encuentra en la base de datos")



  else:
    print("No hay clientes hospedados en este crucero")


def module3(cruise_answer,*cruise):

  cruise1,cruise2,cruise3,cruise4 = cruise

  if cruise_answer == 1:
    sell_tours(cruise1,cruise_answer)
  elif cruise_answer == 2:
    sell_tours(cruise2,cruise_answer)
  elif cruise_answer == 3:
    sell_tours(cruise3,cruise_answer)
  else:
    sell_tours(cruise4,cruise_answer)

