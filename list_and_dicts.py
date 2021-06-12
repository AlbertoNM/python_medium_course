def run():
  my_list = [1, 'Hello', True, 4.5]
  my_dict = {'firstname': 'Alberto', 'lastname': 'Narro'}

  super_list = [
    {'firstname': 'Alberto', 'lastname': 'Narro'},
    {'firstname': 'Esquites', 'lastname': 'xd'},
    {'firstname': 'Churls', 'lastname': 'noob'}
  ]

  super_dict = {
    'natural_nums': [1,2,3,4,5],
    'integer_nums': [-2,-1,0,1,2],
    'floating_nums': [1.1,1.2,1.3,1.4,1.5]
  }

  for key, value in super_dict.items():
    print(f'{key} - {value}')

  for values in super_list:
    for key, value in values.items():
      print(f'{key} - {value}')


if __name__ == '__main__':
  run()