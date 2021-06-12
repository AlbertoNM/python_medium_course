def list():
  squares = []
  for i in range(1,100+1):
    if i%3 != 0:
      squares.append(i**2)

  print(squares)

def list_comprehensions():
  
  # [element for element in iterable if condition]
  
  squares = [i**2 for i in range(1,100+1) if i%3 != 0]
  print(squares)

def reto():
  
  # Crear, con un list comprehension, una lista de todos los multiplos de 4 que a la vez tambien son multiplos de 6 y de 9, hasta 5 digitos
  
  my_list = [i for i in range(1,99999) if i%36 == 0]
  print(my_list)


if __name__ == '__main__':
  reto()