def read():
  with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
    numbers = [int(line) for line in f]
    print(numbers)

def write():
  names = ['Alberto', 'Rodrigo', 'Carlos', 'Kovin']
  with open('./archivos/names.txt', 'w', encoding='utf-8') as f:
    for name in names:
      f.write(f'{name}\n')

def run():
  write()


if __name__ == '__main__':
  run()