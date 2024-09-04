# pole powierzchni koła = πr^2

import math

r = input("Podaj promień r: ")
r = float(r)  # Konwersja wpisanego ciągu znaków na liczbę zmiennoprzecinkową

promien = math.pi * r ** 2

print(f"Pole powierzchni koła o promieniu {r} wynosi {promien:.2f}")


#Funkcja input zawsze zwraca wartość typu str (ciąg znaków). W Pythonie nie można używać operatora potęgowania ** z typami str i int, co spowodowało błąd typu TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'. Twoje wejście r jest ciągiem znaków, a 2 jest liczbą całkowitą.