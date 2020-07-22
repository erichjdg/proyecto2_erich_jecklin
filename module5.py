#Estadisticas

from module1 import select_cruise
import file_management as fm
from sort_search import search_available
from sort_search import sort_vector


def sell_average(data_base):

  """
  Funcion que calcula y muestra el promedio de gastos de un cliente en un crucero particular

  """

  cruise_answer = select_cruise(data_base)

  clients_file = "clients_cruise"+str(cruise_answer)+".txt"
  count_clients = fm.check_empty(clients_file)
  if count_clients:
    clients = []
  else:
    clients = fm.fill_clients(clients_file)
    print('Clientes lleno')
  if len(clients) == 0:

    print('No se encuentran clientes hospedados en este hotel')
    

  else:

    print(len(clients))
    payments = []
    lista = []
    for i in range(len(clients)):

      payment = clients[i].payment + clients[i].tour

      payments.append(payment)
      lista.append(i)
    
    average = sum(payments)/len(payments)

    print(f'El promedio de gasto de un cliente es de: {average}')

    

def percentage_tours(data_base):

  """
  Funcion que el porcentaje de clientes que no compran tours en un crucero en particular
  
  """

  
  cruise_answer =select_cruise(data_base)
  clients_file = "clients_cruise"+str(cruise_answer)+".txt"
  count_clients = fm.check_empty(clients_file)
  if count_clients:
    clients = []
  else:
    clients = fm.fill_clients(clients_file)
    print('Clientes lleno')

  tours_file = "tours_cruise"+str(cruise_answer)+".txt"
  count_tours = fm.check_empty(tours_file)
  if count_tours:
    tours = []
  else:
    tours = fm.fill_tours(tours_file)
    print('Clientes lleno')




  total_clients = len(clients)


  if len(clients) != 0:
    if len(tours) != 0:
      tour_clients = 0
      for i in range(len(clients)):

        found_client = search_available(tours,0,clients[i].dni,2)

        if found_client == "No encontrado":
          tour_clients += 1
      
      percentage = (tour_clients/total_clients)*100

      print(f'El porcentage de clientes que no compran tour en este crucero es de {percentage}%')
    else:
      percentage = 100
      print(f'El porcentage de clientes que no compran tour en este crucero es de {percentage}%')

  
  else:

    print('No hay clientes hospedados en este crucero')

    

def loyal_clients():

  """
  Funcion muestra los 3 clientes que mas dinero gastaron en los cruceros
  
  """

  total_clients = []
  
  payments = []
  cont = 0
  for cruise_answer in range(1,5):
    
    clients_file = "clients_cruise"+str(cruise_answer)+".txt"
    count_clients = fm.check_empty(clients_file)
    if count_clients:
      clients = []
    else:
      clients = fm.fill_clients(clients_file)
      


    if len(clients) != 0:

      for i in range(len(clients)):

        total_clients.append(clients[i])

        payment = clients[i].payment + clients[i].tour + clients[i].restaurant

        lista = []
         
        lista.append(cont)
        lista.append(payment)

        payments.append(lista)
        cont += 1

  if len(payments) != 0 and len(total_clients) != 0:

    
    payments = sort_vector(payments)

    

    cont = 0

    index = -1
    

    
    while cont < len(payments) and cont < 3 and index > -4:

      
      print(f'\t{total_clients[payments[index][0]].name}')

      cont += 1
      index -= 1
      

  else:

    print('No hay clientes hospedados')



      


  


def cruise_most_sells(data_base):

  """
  Funcion muestra los 3 cruceros que vendieron mas
  
  """

  
  
  payments = []
  cont = 0
  for cruise_answer in range(1,5):
    
    clients_file = "clients_cruise"+str(cruise_answer)+".txt"
    count_clients = fm.check_empty(clients_file)
    if count_clients:
      clients = []
    else:
      clients = fm.fill_clients(clients_file)
      

    if len(clients) != 0:
      amount_money = 0
      for i in range(len(clients)):

        

        amount_money += clients[i].payment

      lista = []
        
      lista.append(cruise_answer)
      lista.append(amount_money)

      payments.append(lista)
      cont += 1

  if len(payments) != 0:

    #print(payments)
    payments = sort_vector(payments)

   

    cont = 0

    
    index = -1

    

    while cont < len(payments) and cont < 3 and index > -4:

      
      print(f'\tCrucero: {data_base[payments[index][0]-1]["name"]}')
      

      cont += 1
      index -= 1
     

  else:

    print('No hay clientes hospedados')
  
    

def restaurants_most_sells():


  """
  Funcion muestra los 5 productos mas vendidos del restaurante
  
  """

  dish_file = "restaurant_dishes.txt"
  count_dishes = fm.check_empty(dish_file)
  if count_dishes:
    dishes = []
  else:
    dishes = fm.fill_dishes(dish_file)


  combo_file = "restaurant_combos.txt"
  count_combos = fm.check_empty(combo_file)
  if count_combos:
    combos = []
  else:
    combos = fm.fill_combos(combo_file)

  count_sells = fm.check_empty("sold_dishes.txt")

  if count_sells:

    print('Por el momento no hay productos vendidos')

  else:

    sells = []

    with open("sold_dishes.txt") as f:
      for line in f:
        sell = line[:-1]
        
        sells.append(sell)
    
    sells_quantities = []
    if len(dishes) != 0:
      for i in range(len(dishes)):
        

        product_quantity = sells.count(dishes[i].name)
        lista = []
        lista.append(dishes[i].name)
        lista.append(product_quantity)
        
        sells_quantities.append(lista)

    if len(combos) != 0:
      for i in range(len(combos)):
        

        product_quantity = sells.count(combos[i].name)
        lista = []
        lista.append(combos[i].name)
        lista.append(product_quantity)
        
        sells_quantities.append(lista)

        
        

        
        sells_quantities.append(lista)
      print(lista)
    if len(sells_quantities) != 0:

      sells_quantities = sort_vector(sells_quantities)
      #print(sells_quantities)
      cont = 0

    
      index = -1
      print('\nLos productos mas vendidos del restaurante son:\n')

      while cont < len(sells_quantities) and cont < 5 and index > -6:

        
        print(f'\t{sells_quantities[index][0]}')
        

        cont += 1
        index -= 1






  

  


def module5(data_base):

  

  while True:

    try:

      operation_answer = input('Ver:\n1. Promedio de gasto de un cliente en un crucero\n2. Porcentaje de clientes que no compran tour en un crucero\n3. Clientes de mayor fidelidad en una linea\n4. Crucero con mas ventas en tickets\n5. Productos mas vendidos del restaurante\nSeleccionar operacion: ')

      if operation_answer != '1' and operation_answer != '2' and operation_answer != '3' and operation_answer != '4' and operation_answer != '5':

        raise Exception
      break
    except:

      print('Valor Invalido. Intente nuevamente')


  if operation_answer == '1':

    sell_average(data_base)
  elif operation_answer == '2':

    percentage_tours(data_base)

  elif operation_answer == '3':

    loyal_clients()

  elif operation_answer == '4':

    cruise_most_sells(data_base)
  
  else:
    restaurants_most_sells()






  





