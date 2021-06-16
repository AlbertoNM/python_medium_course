def divisors(num):
  divisors = [i for i in range(1, num+1) if num % i == 1]
  return divisors

def run():
  while True:
    try:
      num = int(input('Type a number: '))
      if num < 0:
        raise TypeError('Type a number greater than 0')
      print(divisors(num))
      break
    except ValueError:
      print('Invalid value')
    except TypeError as ve:
      print(ve)


if __name__ == '__main__':
  run()