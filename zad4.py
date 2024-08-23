#Pętla for: Napisz skrypt, który wypisze liczby od 1 do 100.
# Dla liczb podzielnych przez 3 wyświetl "Fizz",
# dla liczb podzielnych przez 5 wyświetl "Buzz",
# a dla liczb podzielnych przez 3 i 5 jednocześnie wyświetl "FizzBuzz".

numbers=list(range(1,101))

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
