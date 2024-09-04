#Napisz skrypt, który zapyta użytkownika o hasło.
# Program powinien pytać o hasło tak długo, aż użytkownik poda prawidłowe hasło ("python123").

password = input("Enter your password: ")

while password != "python123":
    print("Niepoprawne hasło")
    password = input("Enter your password: ")

print("Hasło poprawne")
