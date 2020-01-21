Fizzbuzz = []

for num in range(1, 101):
    if num % 5 == 0 and num % 3 == 0:
        print("Fizzbuzz: {}".format(num))
        Fizzbuzz.append(num)
    elif num % 3 == 0:
        print("Fizz: {}".format(num))
    elif num % 5 == 0:
        print("Buzz: {}".format(num))
    else:
        print("Num: {}".format(num))

print(Fizzbuzz)
