import module1
import module2
import module3
import module4
import module5
import file_management as fm

def main():

  
  
  data_base = module1.api_cruise()

  count_cruise1 = fm.check_empty("rooms_cruise1.txt")
  count_cruise2 = fm.check_empty("rooms_cruise2.txt")
  count_cruise3 = fm.check_empty("rooms_cruise3.txt")
  count_cruise4 = fm.check_empty("rooms_cruise4.txt")

  if count_cruise1:
    cruise1 = module2.floor_represent(data_base,1)
    fm.create_cruise_txt(cruise1,"rooms_cruise1.txt")
  else:
    cruise1 = fm.fill_cruise("rooms_cruise1.txt")
    
  if count_cruise2:
    cruise2 = module2.floor_represent(data_base,2)
    fm.create_cruise_txt(cruise2,"rooms_cruise2.txt")
  else:
    cruise2 = fm.fill_cruise("rooms_cruise2.txt")
    
  if count_cruise3:
    cruise3 = module2.floor_represent(data_base,3)
    fm.create_cruise_txt(cruise3,"rooms_cruise3.txt")
  else:
    cruise3 = fm.fill_cruise("rooms_cruise3.txt")
    
  if count_cruise4:
    cruise4 = module2.floor_represent(data_base,4)
    fm.create_cruise_txt(cruise4,"rooms_cruise4.txt")
  else:
    cruise4 = fm.fill_cruise("rooms_cruise4.txt")
    
  

  answer_continue = '1'
  while answer_continue == '1':
    while True:
      try:
        answer = int(input('Bienvenido a Saman Caribbean.\n1\tConsultar Cruceros\n2\tGestion de habitaciones\n3\tVenta de Tours\n4\tGestion de restaurante\n5\tVer estadisticas\nSeleccione la operación que desea realizar: '))

        if answer != 1 and answer != 2 and answer != 3 and answer != 4 and answer != 5:
          raise Exception
        break

      except:

        print('Respuesta invalida. Intente nuevamente: ')
    

    if answer == 1:
      print('')
      module1.show_cruise(data_base)
    elif answer == 2:
      print('')
  
      operation_answer = module2.select_operation()
      if operation_answer == "1":
        module2.module2_operation1(data_base,cruise1,cruise2,cruise3,cruise4)
      elif operation_answer == '2':
      
        cruise1,cruise2,cruise3,cruise4 = module2.module2_operation2(data_base,cruise1,cruise2,cruise3,cruise4)
      elif operation_answer == '3':
        module2.module2_operation3(data_base,cruise1,cruise2,cruise3,cruise4)
      else:
        module2.module2_operation4(data_base,cruise1,cruise2,cruise3,cruise4)
    
    elif answer == 3:
      cruise_answer = module1.select_cruise(data_base)
      module3.module3(cruise_answer,cruise1,cruise2,cruise3,cruise4)

    elif answer == 4:

      module4.module4(data_base)

    else:

      module5.module5(data_base)
      



    
    answer_continue = input('\nPresione 1 si desea realizar otra operación: ')
    print('\n\n\n')
    
    
    print('\n\n\n')
  
if __name__ == '__main__':
  main()
  
  
  
  