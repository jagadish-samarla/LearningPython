number_input = int(input('enter any number: \n'))
divisors = [i for i in range(1, number_input) if (number_input % i) == 0]
#divisors = []
#for i in range(1, number_input):
 #   if i % number_input == 0:
  #      divisors.append(i)

print(f'{divisors} are divisors of {number_input}')