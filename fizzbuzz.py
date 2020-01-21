Fizzbuzz = []
num_3 = []
num_5 = []
num_none = []

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("Fizzbuzz: {}".format(num))
        Fizzbuzz.append(num)
    elif num % 3 == 0:
        print("Fizz: {}".format(num))
        num_3.append(num)
    elif num % 5 == 0:
        print("Buzz: {}".format(num))
        num_5.append(num)
    else:
        print("Num: {}".format(num))
        num_none.append(num)


print(Fizzbuzz , Fizzbuzz)
print('3: ', num_3)
print('5: ', num_5)
print('none: ', num_none)
