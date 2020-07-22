#from Room import Room 


def search_available(vector,first,search_input,search_type):
  
  """
  vector: lista compuesta de otras listas, estas a su vez compuestas de objetos
  r_type_answer: tipo de habitacion o lista de clientes
  first: indice donde se desea comenzar la busqueda
  search_input: elemento que se desea buscar
  search_type: tipo de busqueda, denota lo que se desea buscar



  """
  
  for i in range(first,len(vector)):
    
    if search_type == 1:
      if vector[i].status == search_input:
        found = i
        break
      else: 
        found = "No encontrado"
    if search_type == 2:
      if vector[i].dni == search_input:
        found = i
        break
      else: 
        found = "No encontrado"
    if search_type == 3:
      if vector[i].capacity == search_input:
        found = i
        break
      else: 
        found = "No encontrado"
    if search_type == 4:
      if vector[i].room_id == search_input:
        found = i
        break
      else: 
        found = "No encontrado"
    if search_type == 5:
      if vector[i].tour_id == search_input:
        found = i
        break
      else: 
        found = "No encontrado"
    if search_type == 6:
      if vector[i].name == search_input:
        found = i
        break
      else: 
        found = "No encontrado"

    
  return found

def sort_vector(vector):

  n = len(vector)

  for i in range(n):

    min_idx = i

    for j in range(i+1,n):

      if vector[min_idx][1] > vector[j][1]:

        min_idx = j

    vector[i],vector[min_idx] = vector[min_idx],vector[i]

  return vector



  