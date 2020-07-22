

"""

Las siguientes funciones son para realizar operaciones matematicas

"""


def check_prime(num):#,divisors=[],x=1):
  """
  Funcion que verifica si un numero es primo
  
  """
  divisors = []
  x = 1
  for x in range(num//2,0,-1):
    if num % x == 0:
      if x not in divisors:
        divisors.append(x)
        if x != (num//x):
          divisors.append(num//x)
  if len(divisors)==2:
      prime = True # 'Es primo'
  else:
    prime = False #'No es primo'
    
  return prime

def abundant_num(num):

  """
  Funcion que verifica si un numero es abundante
  
  """

  divs = [1]
  
  for x in range(num//2,0,-1):
    if num % x == 0:
      if x not in divs:
        divs.append(x)
        if x != (num//x):
          divs.append(num//x)
      #cont += num/x
  if sum(divs) > num:
    abundant = True #Es abundante
    
  else:
    abundant = False #Es abundante

  return abundant