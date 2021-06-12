def normal_dict():
  my_dict = {}

  for i in range(1,100+1):
    if i%3 != 0:
      my_dict[i] = i**3

  print(my_dict)

def dict_comprehension():
  
  # {key:value for value in iterable if condition}
  
  my_dict = {i: i**3 for i in range(1,100+1) if i%3 != 0}
  print(my_dict)

def reto():
  
  # Crear un diccionario cuyas llaves sean los primeros 1000 primeros numeros naturales con sus raices cuadradas como valores

  my_dict = {i: round(i**0.5,4) for i in range(1,1000+1)}
  print(my_dict)


if __name__ == '__main__':
  reto()