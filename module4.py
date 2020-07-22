#Gestion de restaurante
from Dish import Dish

from module1 import select_cruise
import file_management as fm
from sort_search import search_available
from Combo import Combo

def restaurant_operation():
  while True:
    try:
      operation_answer = input('Operaciones:\n1. Agregar productos al menu\n2. Eliminar productos del menu\n3. Modificar productos del menu\n4. Agregar combos al menu\n5. Eliminar combos del menu\n6. Buscar productos\n7. Vender productos del menu\nSeleccione la operacion a realizar: ')
      if operation_answer != '1' and operation_answer != '2' and operation_answer != '3' and operation_answer != '4' and operation_answer != '5' and operation_answer != '6' and operation_answer != '7':
        raise Exception
      break

    except:
      print('Valor invalido. Intente nuevamente')
  return operation_answer


def select_product(vector):

  print('Productos:')

  for i,item in enumerate(vector):
    print(f'{i+1}.\t{item.name}')

  while True:

    try:

      product_answer = int(input('\nIndique el producto / combo: '))
      if product_answer not in range(1,len(vector)+1):
        raise Exception
      break

    except:

      print('Valor invalido. Intente nuevamente')

  return product_answer


def add_dishes():


  """

  Funcion que permite agregar productos al menu

  """

  #Primero se valida si existe un archivo con los datos de platos en el menu, de ser asi se llena una lista con los datos guardados en el mismo, de lo contrario se crea la lista vacía
  dish_file = "restaurant_dishes.txt"
  count_dishes = fm.check_empty(dish_file)
  if count_dishes:
    dishes = []
  else:
    dishes = fm.fill_dishes(dish_file)
    

  continue_answer = '1'
  while continue_answer == '1':

    #Se recogen los datos del nuevo producto que se introducirá al menu
    while True:
      try:
        name = input('Introduzca el nombre del producto: ').title()
        price = float(input('Introduzca el precio del producto: '))
        classification_answer = input('Indique si el producto es (1 - Alimento / 2 - Bebida): ')
        if classification_answer != '1' and classification_answer != '2':
          raise Exception

        break

      except:

        print('Valor invalido. Intente nuevamente')

    if classification_answer == '1':
      classification = 'Alimento'
    else:
      classification = 'Bebida'

    #Si no hay archivos previamente guardados en el menu, se guardan los datos directamente
    if len(dishes) == 0: 
      

      price *= 1.16

      dish = Dish(name,price,classification)

      dishes.append(dish)
      fm.create_dishes_txt(dishes,dish_file)

      continue_answer = input('Presione 1 si desea continuar agregando productos: ')

    else:

      #Si hay archivos previamente guardados en el menu, se debe validar si el producto ya existe en el menu

      search_dish = search_available(dishes,0,name,6)

      if search_dish == "No encontrado":

        price *= 1.16

        dish = Dish(name,price,classification)

        dishes.append(dish)
        fm.create_dishes_txt(dishes,dish_file)
        continue_answer = input('Presione 1 si desea continuar agregando productos: ')

      else:

        print("Este plato ya se encuentra en la base de datos")
        continue_answer = input('Presione 1 si desea continuar agregando productos: ')


def delete_dish():

  """

  Funcion que permite eliminar productos del menu

  """

  #Primero se valida si existe un archivo con los datos de platos en el menu, de ser asi se llena una lista con los datos guardados en el mismo, de lo contrario se crea la lista vacía

  dish_file = "restaurant_dishes.txt"
  count_dishes = fm.check_empty(dish_file)
  if count_dishes:
    dishes = []
  else:
    dishes = fm.fill_dishes(dish_file)
    

  delete_answer = '1'

  while delete_answer == '1':

    # Si la lista de platos esta vacia, no se puede continuar con la operacion ya que no hay platos para eliminar
    if len(dishes) == 0:

      print('No hay platos en el menu')
      delete_answer = '0'

    else:
      product_answer = select_product(dishes)

      selected_dish = dishes[product_answer-1]

      dishes.remove(selected_dish)

      fm.create_dishes_txt(dishes,dish_file)

      delete_answer = input('Presione 1 si desea eliminar otro elemento: ')

def modify_dish():

  """

  Funcion que permite modificar productos del menu

  """

  #Primero se valida si existe un archivo con los datos de platos en el menu, de ser asi se llena una lista con los datos guardados en el mismo, de lo contrario se crea la lista vacía

  dish_file = "restaurant_dishes.txt"
  count_dishes = fm.check_empty(dish_file)
  if count_dishes:
    dishes = []
  else:
    dishes = fm.fill_dishes(dish_file)
    
  continue_answer = '1'

  while continue_answer == '1':
    # Si la lista de platos esta vacia, no se puede continuar con la operacion ya que no hay platos para modificar
    if len(dishes) == 0:

      print('No hay platos en el menu')
      continue_answer = '0'

    else:
      
      product_answer = select_product(dishes)

      while True:

        try:
          atribute_answer = input('Atributos:\n1. Nombre\n2. Precio\n3.Clasificación\nSeleccione el atributo que desea modificar: ')

          if atribute_answer != '1' and atribute_answer != '2' and atribute_answer != '3':

            raise Exception

          if atribute_answer == '1':
            new_name = input('Introduzca el nuevo nombre del producto: ').title()
          elif atribute_answer == '2':
            
            new_price = float(input('Introduzca el nuevo precio del producto: '))
          else:
            clasification_answer = input('Indique la nueva clasificacion del producto (1 - Alimento / 2 - Bebida): ')
            if clasification_answer != '1' and clasification_answer != '2':
              raise Exception
          

          break

        except:

          print('Valor invalido. Intente nuevamente')

      if atribute_answer == '1':

        dishes[product_answer-1].name = new_name 
        fm.create_dishes_txt(dishes,dish_file)
        continue_answer = input('Presione 1 si desea modificar otro elemento: ')

      elif atribute_answer == '2':
        new_price *= 1.16
        dishes[product_answer-1].price = new_price
        fm.create_dishes_txt(dishes,dish_file)
        continue_answer = input('Presione 1 si desea modificar otro elemento: ')

      else:
        if clasification_answer == '1':
          clasification = 'Alimento'

          dishes[product_answer-1].clasification = clasification
          fm.create_dishes_txt(dishes,dish_file)
          continue_answer = input('Presione 1 si desea modificar otro elemento: ')
        else:
          clasification = 'Bebida'
        
          dishes[product_answer-1].clasification = clasification
          fm.create_dishes_txt(dishes,dish_file)
          continue_answer = input('Presione 1 si desea modificar otro elemento: ')

def create_combo():


  """

  Funcion que permite agregar combos al menu 

  """

  #Primero se valida si existe un archivo con los datos de platos en el menu, de ser asi se llena una lista con los datos guardados en el mismo, de lo contrario se crea la lista vacía

  dish_file = "restaurant_dishes.txt"
  count_dishes = fm.check_empty(dish_file)
  if count_dishes:
    dishes = []
  else:
    dishes = fm.fill_dishes(dish_file)

  #Primero se valida si existe un archivo con los datos de platos en el menu, de ser asi se llena una lista con los datos guardados en el mismo, de lo contrario se crea la lista vacía
  combo_file = "restaurant_combos.txt"
  count_combos = fm.check_empty(combo_file)
  if count_combos:
    combos = []
  else:
    combos = fm.fill_combos(combo_file)
  
  
  

  if len(dishes) == 0:

    print("No hay productos en el menu")
  else:
    
    more_dishes = '1'
    combo_products = ""
    count = 1
    
    while more_dishes == '1':
      print("Seleccione el producto que desea agregar al combo\n")
      dish_answer = select_product(dishes)
      combo_products += f"{dishes[dish_answer-1].name}\t"
      

      if count >= 2:
        
        more_dishes = input('\nPresione 1 si desea agregar mas productos al combo')
      count += 1
    
    while True:
      try:
        name = input('Introduzca el nombre del combo: ').title()

        price = float(input('Introduzca el precio del producto: '))
        

        break

      except:

        print('Valor invalido. Intente nuevamente')
    price *= 1.16

    

    combo = Combo(name,price,combo_products)
    combos.append(combo)
    fm.create_combos_txt(combos,combo_file)
    


    
def delete_combo():

  """

  Funcion que permite eliminar combos del menu

  """


  combo_file = "restaurant_combos.txt"
  count_combos = fm.check_empty(combo_file)
  if count_combos:
    combos = []
  else:
    combos = fm.fill_combos(combo_file)

  delete_answer = '1'

  while delete_answer == '1':
    if len(combos) == 0:

      print('No hay platos en el menu')
      delete_answer = '0'

    else:
      product_answer = select_product(combos)

      selected_combo = combos[product_answer-1]

      combos.remove(selected_combo)

      fm.create_combos_txt(combos,combo_file)

      delete_answer = input('Presione 1 si desea eliminar otro elemento: ')

  
  
def search_menu():


  """
  Funcion que permite buscar combos en el menu

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
  search_continue = '1'

  while search_continue == '1':
    while True:

      try:
        
        search_type = input('Menu:\n1. Platos\n2. Combos\nIndique lo que desea buscar: ')
        if search_type != '1' and search_type != '2':
          raise Exception
        search_criteria = input('\nParametros de busqueda:\n1. Nombre\n2. Rango de precios\nSeleccione el parametro de busqueda que desea realizar: ')

        if search_criteria != '1' and search_criteria != '2':
          raise Exception

        break

      except:
        print('Valor invalido. Intente nuevamente')

    if search_criteria == '1':
      if search_type == '1':
        if len(dishes) == 0:
          print('No hay platos en el menu')
          search_continue = input('Presione 1 si desea realizar otra busqueda: ')
        else:
          while True:
            try:
              name = input('Ingrese el nombre del producto que desea buscar: ').title()
              break
            except:
              print('Valor Invalido. Intente nuevamente')
          name_index = search_available(dishes,0,name,6)

          if name_index == "No encontrado":
            print('El producto ingresado no se encuentra en el menu')
            search_continue = input('Presione 1 si desea realizar otra busqueda: ')
          else:
            print(f'\nProducto: {dishes[name_index].name}\nClasificación: {dishes[name_index].clasification}\nPrecio: {dishes[name_index].price}\n\n')
            search_continue = input('Presione 1 si desea realizar otra busqueda: ')
      else:
        if len(combos) == 0:
          print('No hay platos en el menu')
          search_continue = input('Presione 1 si desea realizar otra busqueda: ')
        else:
          while True:
            try:
              name = input('Ingrese el nombre del combo que desea buscar: ').title()
              break
            except:
              print('Valor Invalido. Intente nuevamente')
          name_index = search_available(dishes,0,name,6)

          if name_index == "No encontrado":
            print('El producto ingresado no se encuentra en el menu')
            search_continue = input('Presione 1 si desea realizar otra busqueda: ')
          else:
            print(f'\nProducto: {combos[name_index].name}\nProductos: {combos[name_index].products}\nPrecio: {combos[name_index].price}\n\n')
            search_continue = input('Presione 1 si desea realizar otra busqueda: ')
    else:
      while True:

        try:

          low = float(input('Por favor introduzca el limite inferior del rango de precios: '))
          high = float(input('Por favor introduzca el limite superior del rango de precios: '))
          break
        except:

          print('Valor invalido. Intente nuevamente')


      if search_type == '1':
        if len(dishes) != 0:
          cont = 0
          for i in range(len(dishes)):

            if dishes[i].price >= low and dishes[i].price <= high:

              print(f'\nProducto: {dishes[i].name}\nClasificación: {dishes[i].clasification}\nPrecio: {dishes[i].price}\n\n')
              cont +=1

          if cont == 0:
            print('No se encontraron productos en ese rango de precios')
            search_continue = input('Presione 1 si desea realizar otra busqueda: ')
          else:
            search_continue = input('Presione 1 si desea realizar otra busqueda: ')
        else:

          print('No hay platos en el menu')
          search_continue = input('Presione 1 si desea realizar otra busqueda: ')

      else:
        if len(combos) != 0:
          cont = 0
          for i in range(len(combos)):

            if combos[i].price >= low and combos[i].price <= high:

              print(f'\nProducto: {combos[i].name}\nClasificación: {combos[i].products}\nPrecio: {combos[i].price}\n\n')
              cont +=1

          if cont == 0:
            print('No se encontraron combos en ese rango de precios')
            search_continue = input('Presione 1 si desea realizar otra busqueda: ')
          else:
            search_continue = input('Presione 1 si desea realizar otra busqueda: ')

        else:

          print('No hay combos en el menu')
          search_continue = input('Presione 1 si desea realizar otra busqueda: ')

def sell_products(data_base): 


  """

  Funcion que permite vender productos del menu, y almacenar los datos de la venta en los clientes y almacenar productos vendidos

  """

  cruise_answer = select_cruise(data_base)
  clients_file = "clients_cruise"+str(cruise_answer)+".txt"
  count_clients = fm.check_empty(clients_file)
  if count_clients:
    clients = []
  else:
    clients = fm.fill_clients(clients_file)
    print('Clientes lleno')

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


  while True:
    
    try:
      dni = int(input('Por favor ingrese su dni:'))
      break
    except:
      print('Valor invalido. Intente nuevamente')

  if len(clients) == 0:
    print('No se encuentran clientes hospedados en este crucero')
  else:
    search_dni = search_available(clients,0,dni,2)
    if search_dni == "No encontrado":
      print('El numero de cedula ingresado no se encuentra en la base de datos')
    else:

      if clients[search_dni].room_id == "Salió":
        print('El numero de cedula ingresado no se encuentra en la base de datos')
      else:
        while True:

          try:
            
            search_type = input('Menu:\n1. Platos\n2. Combos\nIndique lo que desea buscar: ')
            if search_type != '1' and search_type != '2':
              raise Exception
            
            break

          except:
            print('Valor invalido. Intente nuevamente')
        if search_type == '1':

          if len(dishes) != 0:

            product_answer = select_product(dishes)
            payment = dishes[product_answer-1].price
            #Se actualiza el dato del cliente para denotar que hizo una compra en el restaurante
            clients[search_dni].restaurant += payment

            #Se crea un archivo que almacene los productos vendidos
            fm.create_client_txt(clients,clients_file)

            with open("sold_dishes.txt",'a') as f:

              f.write(f'{dishes[product_answer-1].name}\n')

            bill = f"Nombre: {clients[search_dni].name}\nEdad: {clients[search_dni].age}\nCedula: {clients[search_dni].dni}\nHabitacion: {clients[search_dni].room_id}\nMonto a Pagar: {payment}\nProducto: {dishes[product_answer-1].name} "
            print(bill)
          else:
            print('No hay platos en el menu')

        else:

          if len(combos):

            product_answer = select_product(combos)
            payment = combos[product_answer-1].price
            #Se actualiza el dato del cliente para denotar que hizo una compra en el restaurante
            clients[search_dni].restaurant += payment

            #Se crea un archivo que almacene los productos vendidos
            fm.create_client_txt(clients,clients_file)

            with open("sold_dishes.txt",'a') as f:

              f.write(f'combos[product_answer-1].name\n')

            bill = f"Nombre: {clients[search_dni].name}\nEdad: {clients[search_dni].age}\nCedula: {clients[search_dni].dni}\nHabitacion: {clients[search_dni].room_id}\nMonto a Pagar: {payment}\nProducto: {combos[product_answer-1].name} "
            print(bill)

          print('No se encuentran combos en el menu')

        







def module4(data_base):

  operation_answer = restaurant_operation()

  

  if operation_answer == '1':
    add_dishes()

  elif operation_answer == '2':
    delete_dish()

  elif operation_answer == '3':

    modify_dish()

  elif operation_answer == '4':

    create_combo()

  elif operation_answer == '5':

    delete_combo()

  elif operation_answer == '6':

    search_menu()
  else:

    sell_products(data_base)














 